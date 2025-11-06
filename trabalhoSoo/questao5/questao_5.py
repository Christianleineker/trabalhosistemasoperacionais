"""
Autor: Arthur de Souza Alves
Autor: Murilo da Cruz de Lima
Disciplina: Sistemas Operacionais
---------------------------------
Descrição:
    Este programa compara o tempo de execução entre dois tipos de alocação de memória:
    - Alocação na PILHA (variáveis locais criadas dentro de funções)
    - Alocação no HEAP (objetos criados dinamicamente durante a execução)

Objetivo:
    Medir e comparar o tempo médio gasto para:
    1. Criar e destruir 1.000.000 de variáveis locais (pilha)
    2. Alocar e desalocar 1.000.000 de objetos dinâmicos (heap)
    3. Exibir a diferença percentual de desempenho entre os dois tipos de alocação

Ferramentas utilizadas:
    - Linguagem: Python
    - Biblioteca: time (para medir tempo)
    - Biblioteca: gc (para controle manual do coletor de lixo)
"""

import time
import gc

# Quantidade de iterações e repetições
N = 1_000_000
REPETICOES = 5


def alocacao_pilha():
    """Simula alocação na pilha (variáveis locais criadas e destruídas rapidamente)."""
    for i in range(N):
        x = i
        x += 1


def alocacao_heap():
    """Simula alocação no heap (objetos criados e destruídos dinamicamente)."""
    for i in range(N):
        obj = [i]
        del obj
    gc.collect()  # força a coleta de lixo após as alocações


def medir_tempo(funcao):
    """Mede o tempo de execução de uma função."""
    inicio = time.time()
    funcao()
    fim = time.time()
    return fim - inicio


if __name__ == "__main__":
    tempos_pilha = []
    tempos_heap = []
    mais_rapido_heap = 0
    mais_lento_heap = 0

    print("\n=== TESTE DE DESEMPENHO DE ALOCAÇÃO ===")
    print(f"Executando {REPETICOES} repetições com {N:,} iterações cada...\n")

    for i in range(REPETICOES):
        # Mede o tempo da pilha e do heap em cada repetição
        tempo_p = medir_tempo(alocacao_pilha)
        tempo_h = medir_tempo(alocacao_heap)

        tempos_pilha.append(tempo_p)
        tempos_heap.append(tempo_h)

        # Compara os dois resultados
        if tempo_h < tempo_p:
            mais_rapido_heap += 1
            situacao = "Heap foi mais rápido"
        else:
            mais_lento_heap += 1
            situacao = "Heap foi mais lento"

        print(f"Repetição {i + 1}: Pilha = {tempo_p:.6f}s | Heap = {tempo_h:.6f}s → {situacao}")

    # Calcula médias
    media_pilha = sum(tempos_pilha) / REPETICOES
    media_heap = sum(tempos_heap) / REPETICOES
    diferenca = ((media_heap - media_pilha) / media_pilha) * 100

    # Exibe resultados finais
    print("\n" + "=" * 40)
    print("=== RESULTADOS FINAIS ===")
    print("=" * 40)
    print(f"Média (Pilha): {media_pilha:.6f} s")
    print(f"Média (Heap):  {media_heap:.6f} s")
    print(f"O Heap foi aproximadamente {diferenca:.2f}% mais lento que a Pilha, em média.")
    print(f"\n→ O Heap foi mais rápido {mais_rapido_heap} vez(es).")
    print(f"→ O Heap foi mais lento  {mais_lento_heap} vez(es).")

    print("\n" + "=" * 40)
    print("=== Discussão dos Resultados ===")
    print("=" * 40)
    print("""

          
Espera-se que o tempo de alocação no HEAP seja significativamente maior do que o da PILHA.

Variações possíveis:
- O desempenho pode variar dependendo do sistema operacional, carga da CPU e da política do coletor de lixo.
- Em execuções sucessivas, o coletor de lixo pode ser mais ou menos ativo, alterando levemente os tempos.

Conclusão:
A alocação na pilha é mais eficiente para variáveis temporárias e simples, enquanto o heap é mais
flexível, mas possui maior custo computacional devido ao gerenciamento dinâmico de memória.
""")


# ------------------------------------------------------------
# Analogia simples:
# A pilha funciona como uma pilha de pratos — o último que entra é o primeiro a sair.
# O heap é como uma gaveta cheia de talheres misturados: é preciso procurar o que quer usar.
# Por isso, a pilha é mais rápida, e o heap é mais flexível, porém mais lento.
# ------------------------------------------------------------
