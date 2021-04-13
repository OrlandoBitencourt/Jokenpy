class Jogo:

    def verificar_vencedor(self, valor_carta_jogador, valor_carta_computador):

        if (valor_carta_jogador == 1 and valor_carta_computador == 1) or (valor_carta_jogador == 2 and valor_carta_computador == 2) or (valor_carta_jogador == 3 and valor_carta_computador == 3):
            print("\nEmpate!\n")
            return 3
        elif (valor_carta_jogador == 1 and valor_carta_computador == 2) or (valor_carta_jogador == 2 and valor_carta_computador == 3) or (valor_carta_jogador == 3 and valor_carta_computador == 1):
            print("\nVocê perdeu!\n")
            return 2
        else:
            print("\nVocê venceu!\n")
            return 1
