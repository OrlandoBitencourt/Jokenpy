class Jogadores:

    nome = ""

    def __init__(self, nome):
        self.nome = nome
        print(f"\nSeja bem-vindo: {self.nome}!\n")


    def escolher_carta(self):
        carta_escolhida = 0

        while True:
            try:
                carta_escolhida = int(input("Informe o numero representante da carta escolhida: "))
            except:
                pass

            validar_campo = self.valida_carta_escolhida(carta_escolhida)

            if validar_campo == True:
                break

        if carta_escolhida == 1:
            print(f"\n{self.nome} escolheu: 1 - Pedra")
        elif carta_escolhida == 2:
            print(f"\n{self.nome} escolheu: 2 - Papel")
        elif carta_escolhida == 3:
            print(f"\n{self.nome} escolheu: 3 - Tesoura")

        return carta_escolhida


    def valida_carta_escolhida(self, carta_escolhida):

            if carta_escolhida > 0 and carta_escolhida <= 3:
                return True

            else:
                print("\nDigite uma opção válida!\n")
                return False
