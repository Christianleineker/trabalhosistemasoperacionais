import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Entrada de dados
        System.out.print("Digite o número de frames: ");
        int frames = sc.nextInt();
        sc.nextLine(); // Limpa o buffer

        System.out.print("Digite a sequência de páginas (ex: 70120304 ou 7 0 1 2 0 3 0 4): ");
        String input = sc.nextLine();

        // Conversão da sequência em lista de inteiros
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

        // Execução do algoritmo LRU
        Resultado lru = runLRU(frames, refs);

        // Exibição dos resultados
        System.out.println("\n--- RESULTADOS (LRU) ---");
        System.out.printf("Faltas de página: %d%n", lru.faltas);
        System.out.printf("Taxa de faltas: %.2f%%%n", lru.taxa);

        sc.close();
    }

    // Classe para armazenar os resultados
    static class Resultado {
        int faltas;
        double taxa;

        Resultado(int f, double t) {
            faltas = f;
            taxa = t;
        }
    }

    /**
     * Implementação do algoritmo LRU (Least Recently Used)
     * Utiliza LinkedHashMap com acesso ordenado (accessOrder = true).
     */
    static Resultado runLRU(int frames, List<Integer> refs) {
        LinkedHashMap<Integer, Boolean> cache = new LinkedHashMap<>(frames, 0.75f, true);
        int faltas = 0;

        for (int p : refs) {
            // Se a página não está na memória, ocorre uma falta
            if (!cache.containsKey(p)) {
                faltas++;
                // Se o cache está cheio, remove a página menos recentemente usada
                if (cache.size() == frames) {
                    Integer chaveRemover = cache.keySet().iterator().next();
                    cache.remove(chaveRemover);
                }
            }
            // Marca a página como recentemente acessada
            cache.put(p, true);
        }

        double taxa = refs.isEmpty() ? 0.0 : (faltas * 100.0 / refs.size());
        return new Resultado(faltas, taxa);
    }
}
