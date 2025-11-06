import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o número de frames: ");
        int frames = sc.nextInt();
        sc.nextLine();
        System.out.print("Digite a sequência (ex: 70120304 ou 7 0 1 2 0 3 0 4): ");
        String input = sc.nextLine();

        // Lista de referências
        List<Integer> refs = new ArrayList<>();
        if (input.contains(" ")) {
            for (String s : input.split(" ")) {
                if (!s.isEmpty()) refs.add(Integer.parseInt(s));
            }
        } else {
            for (char c : input.toCharArray()) {
                if (Character.isDigit(c)) refs.add(Character.getNumericValue(c));
            }
        }

        Resultado fifo = runFIFO(frames, refs);
        Resultado lru = runLRU(frames, refs);

        System.out.println("\n--- RESULTADOS ---");
        System.out.printf("FIFO -> Faltas: %d | Taxa: %.2f%%%n", fifo.faltas, fifo.taxa);
        System.out.printf("LRU -> Faltas: %d | Taxa: %.2f%%%n", lru.faltas, lru.taxa);

        System.out.println("\nAnálise comparativa:");
        if (fifo.faltas < lru.faltas)
            System.out.println("O algoritmo FIFO foi mais eficiente (menos faltas de página).");
        else if (lru.faltas < fifo.faltas)
            System.out.println("O algoritmo LRU foi mais eficiente (menos faltas de página).");
        else
            System.out.println("Ambos apresentaram o mesmo número de faltas.");
        
        sc.close();
    }

    // Classe para retorno de resultados
    static class Resultado {
        int faltas;
        double taxa;
        Resultado(int f, double t) { faltas = f; taxa = t; }
    }

    static Resultado runFIFO(int frames, List<Integer> refs) {
        Queue<Integer> fifo = new LinkedList<>();
        Set<Integer> paginas = new HashSet<>();
        int faltas = 0;

        for (int p : refs) {
            if (!paginas.contains(p)) {
                faltas++;
                if (paginas.size() == frames) {
                    int removida = fifo.poll();
                    paginas.remove(removida);
                }
                paginas.add(p);
                fifo.add(p);
            }
        }
        double taxa = refs.isEmpty() ? 0.0 : (faltas * 100.0 / refs.size());
        return new Resultado(faltas, taxa);
    }

    static Resultado runLRU(int frames, List<Integer> refs) {
        LinkedHashMap<Integer, Boolean> cache = new LinkedHashMap<>(frames, 0.75f, true);
        int faltas = 0;

        for (int p : refs) {
            if (!cache.containsKey(p)) {
                faltas++;
                if (cache.size() == frames) {
                    Integer chaveRemover = cache.keySet().iterator().next();
                    cache.remove(chaveRemover);
                }
            }
            cache.put(p, true);
        }
        double taxa = refs.isEmpty() ? 0.0 : (faltas * 100.0 / refs.size());
        return new Resultado(faltas, taxa);
    }
}
