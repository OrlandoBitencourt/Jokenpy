from random import randint

class Jogo:

    def verificar_vencedor(self, valor_carta_jogador):

        valor_carta_ai = randint(0, 3)

        if valor_carta_ai == 1:
            print("Computador escolheu: 1 - Pedra\n")
        elif valor_carta_ai == 2:
            print("Computador escolheu: 2 - Papel\n")
        elif valor_carta_ai == 3:
            print("Computador escolheu: 3 - Tesoura\n")

        if (valor_carta_jogador == 1 and valor_carta_ai == 1) or (valor_carta_jogador == 2 and valor_carta_ai == 2) or (valor_carta_jogador == 3 and valor_carta_ai == 3):
            print("Empate!\n")
            return 3
        elif (valor_carta_jogador == 1 and valor_carta_ai == 2) or (valor_carta_jogador == 2 and valor_carta_ai == 3) or (valor_carta_jogador == 3 and valor_carta_ai == 1):
            print("Você perdeu!\n")
            return 2
        else:
            print("Você venceu!\n")
            return 1
