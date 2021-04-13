from random import randint

class Jogo:

    def verificar_vencedor(self, valor_carta_jogador):

        valor_carta_ai = randint(0, 3)

        self.printa_carta_escolhida("Computador", valor_carta_ai)

        if (valor_carta_jogador == 1 and valor_carta_ai == 1) or (valor_carta_jogador == 2 and valor_carta_ai == 2) or (valor_carta_jogador == 3 and valor_carta_ai == 3):
            print("\nEmpate!\n")
            return 3
        elif (valor_carta_jogador == 1 and valor_carta_ai == 2) or (valor_carta_jogador == 2 and valor_carta_ai == 3) or (valor_carta_jogador == 3 and valor_carta_ai == 1):
            print("\nVocê perdeu!\n")
            return 2
        else:
            print("\nVocê venceu!\n")
            return 1

    def printa_carta_escolhida(self, nome, carta):
        if carta == 1:
            print(f"{nome} escolheu: 1 - Pedra")
        elif carta == 2:
            print(f"{nome} escolheu: 2 - Papel")
        elif carta == 3:
            print(f"{nome} escolheu: 3 - Tesoura")