import java.util.*;

/**
 * Implementação do algoritmo de substituição de páginas FIFO (First-In, First-Out).
 * O programa simula o gerenciamento de memória, exibindo page hits e page faults
 * com estatísticas detalhadas ao final da execução.
 */
public class FIFOPageReplacement {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada de dados
        int numFrames = solicitarNumero(scanner, "Digite o número de frames: ");
        List<Integer> referencias = solicitarReferencias(scanner);

        // Execução da simulação
        SimuladorFIFO simulador = new SimuladorFIFO(numFrames, referencias);
        simulador.executar();
        simulador.exibirEstatisticas();

        scanner.close();
    }

    /**
     * Solicita ao usuário o número de frames.
     */
    private static int solicitarNumero(Scanner scanner, String mensagem) {
        System.out.print(mensagem);
        while (!scanner.hasNextInt()) {
            System.out.print("Valor inválido! Digite um número inteiro: ");
            scanner.next();
        }
        return scanner.nextInt();
    }

    /**
     * Solicita e converte a sequência de referências em uma lista de inteiros.
     */
    private static List<Integer> solicitarReferencias(Scanner scanner) {
        System.out.print("Digite a sequência de referências (ex: 7 0 1 2 0 3 0 3 2): ");
        scanner.nextLine(); // limpa o buffer

        List<Integer> referencias = new ArrayList<>();
        for (String valor : scanner.nextLine().trim().split("\\s+")) {
            try {
                referencias.add(Integer.parseInt(valor));
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido ignorado: " + valor);
            }
        }
        return referencias;
    }
}

/**
 * Classe responsável por simular o algoritmo FIFO.
 */
class SimuladorFIFO {

    private final int numFrames;
    private final List<Integer> referencias;
    private final Queue<Integer> memoria;
    private int pageFaults;

    // Códigos ANSI para colorir o terminal
    private static final String RESET = "\u001B[0m";
    private static final String RED = "\u001B[31m";
    private static final String GREEN = "\u001B[32m";
    private static final String YELLOW = "\u001B[33m";

    public SimuladorFIFO(int numFrames, List<Integer> referencias) {
        this.numFrames = numFrames;
        this.referencias = referencias;
        this.memoria = new LinkedList<>();
        this.pageFaults = 0;
    }

    /**
     * Executa a simulação do algoritmo FIFO e exibe o passo a passo.
     */
    public void executar() {
        System.out.println("\n--- SIMULAÇÃO DO ALGORITMO FIFO ---");
        System.out.printf("%-15s %-25s %-25s %-15s%n", "Referência", "Frames", "Evento", "Total Faults");
        System.out.println("=".repeat(90));

        for (int ref : referencias) {
            if (memoria.contains(ref)) {
                exibirStatus(ref, "Page Hit", GREEN);
            } else {
                processarPageFault(ref);
            }
        }
    }

    /**
     * Trata um page fault, substituindo páginas se necessário.
     */
    private void processarPageFault(int ref) {
        if (memoria.size() < numFrames) {
            memoria.add(ref);
            pageFaults++;
            exibirStatus(ref, "Page Fault (novo)", RED);
        } else {
            int removida = memoria.poll();
            memoria.add(ref);
            pageFaults++;
            exibirStatus(ref, "Page Fault (substituiu " + removida + ")", YELLOW);
        }
    }

    /**
     * Exibe o status atual da simulação em formato tabular e colorido.
     */
    private void exibirStatus(int referencia, String evento, String cor) {
        System.out.printf("%-15d %-25s %s%-25s%s %-15d%n",
                referencia, memoria, cor, evento, RESET, pageFaults);
    }

    /**
     * Exibe o resumo final da simulação.
     */
    public void exibirEstatisticas() {
        double taxaFaltas = (double) pageFaults / referencias.size();
        System.out.println("\n--- ESTATÍSTICAS FINAIS ---");
        System.out.println("Total de referências: " + referencias.size());
        System.out.println("Total de faltas de página: " + pageFaults);
        System.out.printf("Taxa de faltas de página: %.2f%%%n", taxaFaltas * 100);
    }
}
