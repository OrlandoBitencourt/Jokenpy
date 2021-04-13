from random import randint

class Jogo:

    def verificar_vencedor_rodada(self, valor_carta_jogador, valor_carta_computador):

        if (valor_carta_jogador == 1 and valor_carta_computador == 1) or (valor_carta_jogador == 2 and valor_carta_computador == 2) or (valor_carta_jogador == 3 and valor_carta_computador == 3):
            print("\nEmpate na rodada!\n")
            return 3
        elif (valor_carta_jogador == 1 and valor_carta_computador == 2) or (valor_carta_jogador == 2 and valor_carta_computador == 3) or (valor_carta_jogador == 3 and valor_carta_computador == 1):
            print("\nVocê perdeu a rodada!\n")
            return 2
        else:
            print("\nVocê venceu a rodada!\n")
            return 1


    def gera_carta_automaticamente(self):

        carta = randint(1, 3)

        return carta


    def verifica_vencedor_jogo(self, contador_jogador, nome_jogador):

        if contador_jogador == 2:
            print(f"{nome_jogador.nome} Venceu o jogo.")
            return True

        return False