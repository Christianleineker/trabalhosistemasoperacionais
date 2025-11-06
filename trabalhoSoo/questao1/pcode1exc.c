#include <stdio.h>
#include <stdlib.h>  

int main() {
    // PARTE 1: ARRAY ESTÁTICO COM 5 INTEIROS
    int arrayE[5];  // Alocação estática
    for (int i = 0; i < 5; i++) {
        arrayE[i] = i + 1; // Preenche com valores de 1 a 5
    }

    // PARTE 2: ARRAY DINÂMICO COM 10 INTEIROS
    int *arrayD;  // Ponteiro para o array dinâmico
    arrayD = (int *)malloc(10 * sizeof(int)); // Aloca memória para 10 inteiros com malloc

    // Verifica se a alocação foi bem-sucedida
    if (arrayD == NULL) {
        printf("Erro: falha na alocação de memória!\n");
        return 1; // Encerra o programa
    }

    // PARTE 3: PREENCHER O ARRAY DINÂMICO COM VALORES DE 10 A 19
    for (int i = 0; i < 10; i++) {
        arrayD[i] = 10 + i;
    }

    // PARTE 4: EXIBIR VALORES E ENDEREÇOS 
    printf("ARRAY ESTÁTICO\n");
    for (int i = 0; i < 5; i++) {
        printf("arrayE[%d] = %d | Endereco: %p\n", i, arrayE[i], &arrayE[i]);
    }

    printf("\nARRAY DINÂMICO\n");
    for (int i = 0; i < 10; i++) {
        printf("arrayD[%d] = %d | Endereco: %p\n", i, arrayD[i], &arrayD[i]);
    }

    // PARTE 5: DIFERENÇA ENTRE ENDEREÇOS 
    printf("\nEndereco inicial do array estatico: %p\n", (void *)arrayE);
    printf("Endereco inicial do array dinâmico: %p\n", (void *)arrayD);

    // Calcula a diferença entre os endereços (em bytes)
    long diferenca = (char *)arrayD - (char *)arrayE;
    printf("Diferenca entre os enderecos: %ld bytes\n", diferenca);

    //  PARTE 6: LIBERAR MEMÓRIA 
    free(arrayD);
    printf("\nMemória dinâmica liberada com sucesso.\n");

    return 0;
}