class Particao:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.processo = None

    def esta_livre(self):
        return self.processo is None


class GerenciadorMemoria:
    def __init__(self):
        self.particoes = [
            Particao("P1", 100),
            Particao("P2", 150),
            Particao("P3", 200),
            Particao("P4", 250),
            Particao("P5", 300)
        ]
        self.fragmentacao_total = 0

    def alocar_processo(self, nome, tamanho, nome_particao):
        particao = next((p for p in self.particoes if p.nome.lower() == nome_particao.lower()), None)
        if not particao:
            print(f"Erro: partição {nome_particao} não existe.")
            return
        if not particao.esta_livre():
            print(f"Erro: a partição {particao.nome} já está ocupada.")
            return
        if tamanho > particao.tamanho:
            print(f"Erro: o processo {nome} ({tamanho} unidades) não cabe na partição {particao.nome} ({particao.tamanho} unidades).")
            return
        particao.processo = {"nome": nome, "tamanho": tamanho}
        fragmentacao = particao.tamanho - tamanho
        self.fragmentacao_total += fragmentacao
        print(f"Processo {nome} alocado na {particao.nome} ({particao.tamanho} unidades).")
        print(f"Fragmentação interna: {fragmentacao} unidades.")

    def liberar_processo(self, nome):
        for particao in self.particoes:
            if particao.processo and particao.processo["nome"].lower() == nome.lower():
                print(f"Processo {nome} liberado da {particao.nome}.")
                particao.processo = None
                return
        print(f"Erro: processo {nome} não encontrado.")

    def exibir_memoria(self):
        print("\nEstado atual da memória:")
        for particao in self.particoes:
            if particao.esta_livre():
                print(f"{particao.nome} ({particao.tamanho} unidades): LIVRE")
            else:
                p = particao.processo
                print(f"{particao.nome} ({particao.tamanho} unidades): {p['nome']} ({p['tamanho']} unidades)")
        print(f"Fragmentação interna total: {self.fragmentacao_total} unidades.\n")


def main():
    memoria = GerenciadorMemoria()
    print("Gerenciador de Memória Iniciado.")
    print("Comandos: alocar <nome> <tamanho> <partição> | liberar <nome> | exibir | sair")

    while True:
        comando = input(">>> ").strip().split()

        if not comando:
            continue

        acao = comando[0].lower()

        if acao == "alocar" and len(comando) == 4:
            nome = comando[1]
            try:
                tamanho = int(comando[2])
                nome_particao = comando[3]
                memoria.alocar_processo(nome, tamanho, nome_particao)
            except ValueError:
                print("Erro: tamanho deve ser um número inteiro.")
        elif acao == "liberar" and len(comando) == 2:
            nome = comando[1]
            memoria.liberar_processo(nome)
        elif acao == "exibir":
            memoria.exibir_memoria()
        elif acao == "sair":
            print("Encerrando o gerenciador de memória.")
            break
        else:
            print("Comando inválido. Use: alocar <nome> <tamanho> <partição> | liberar <nome> | exibir | sair")


if __name__ == "__main__":
    main()
