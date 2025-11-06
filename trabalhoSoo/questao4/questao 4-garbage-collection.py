import gc
import sys

# Parte 1 - Classe que simula objetos pesados na memória

class Objeto:
    def __init__(self, nome):
        self.nome = nome
        # Cria um "array" grande para simular uso de memória
        self.dados = [0] * 10**6  
        self.ref = None  # atributo para criar referências circulares
        print(f"Objeto '{self.nome}' criado.")

    def __del__(self):
        # Este método é chamado quando o objeto é coletado pelo Garbage Collector
        print(f"Objeto '{self.nome}' destruído.")

# Parte 2 - Cenário 1: Coleta automática por contagem de referência

print("\n=== CENÁRIO 1: Coleta automática por contagem de referência ===")

obj1 = Objeto("A")
print(f"Contagem de referência (antes de deletar): {sys.getrefcount(obj1)}")

# Removendo referência
obj1 = None  # quando não há mais referências, o objeto é coletado automaticamente

# Forçamos uma coleta para garantir que o __del__ foi chamado
gc.collect()

# Parte 3 - Cenário 2: Referências circulares

print("\n=== CENÁRIO 2: Referências circulares ===")

obj2 = Objeto("B")
obj3 = Objeto("C")

# Criamos uma referência circular
obj2.ref = obj3
obj3.ref = obj2

print("Objetos B e C agora possuem referências circulares.")
print(f"Refcount de obj2: {sys.getrefcount(obj2)}")
print(f"Refcount de obj3: {sys.getrefcount(obj3)}")

# Removemos as referências principais
obj2 = None
obj3 = None

# Neste ponto, os objetos ainda não são destruídos automaticamente,
# pois o contador de referência nunca chega a zero (referem-se entre si).
print("Referências removidas, mas os objetos ainda estão vivos devido à referência circular.")

# Forçamos a coleta manualmente
print("Forçando coleta de lixo com gc.collect()...")
coletados = gc.collect()
print(f"Número de objetos coletados: {coletados}")

# Parte 4 - Cenário 3: Estatísticas e coleta geracional

print("\n=== CENÁRIO 3: Estatísticas e coleta geracional ===")

# Ativa a coleta automática se estiver desativada
gc.enable()

# Cria vários objetos para gerar atividade no GC
objetos = [Objeto(f"obj{i}") for i in range(5)]

# Removendo todas as referências
objetos = None

# Força o coletor a rodar
gc.collect()

# Exibe estatísticas do coletor de lixo
print("\n--- Estatísticas do Garbage Collector (geracional) ---")
stats = gc.get_stats()
for i, gen in enumerate(stats):
    print(f"Geração {i}: {gen}")

# Parte 5 - Explicação teórica
print("""
EXPLICAÇÃO:
- A coleta por contagem de referências destrói objetos assim que o contador chega a zero.
- Já a coleta geracional é usada para lidar com referências circulares e otimizar o desempenho.
- O Python separa os objetos em 3 gerações (0, 1, 2). Objetos que "sobrevivem" a coletas
  são promovidos para gerações mais altas, pois provavelmente vivem mais tempo.
- O módulo gc permite observar, forçar e ajustar esse comportamento.
""")
