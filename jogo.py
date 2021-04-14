from random import randint


class Jogo:

    def verificar_vencedor_rodada(self, valor_carta_jogador, valor_carta_computador):

        if (valor_carta_jogador == 1 and valor_carta_computador == 1) or \
                (valor_carta_jogador == 2 and valor_carta_computador == 2) or \
                (valor_carta_jogador == 3 and valor_carta_computador == 3):
            print("\nEmpate na rodada!\n")
            return 3
        elif (valor_carta_jogador == 1 and valor_carta_computador == 2) or \
                (valor_carta_jogador == 2 and valor_carta_computador == 3) or \
                (valor_carta_jogador == 3 and valor_carta_computador == 1):
            print("\nVocê perdeu a rodada!\n")
            return 2
        else:
            print("\nVocê venceu a rodada!\n")
            return 1

    def gera_carta_automaticamente(self):
        carta = randint(1, 3)
        return carta

    def verifica_vencedor_jogo(self, contador_jogador, nome_jogador, contador_oponente, nome_oponente, round):

        print(f"{nome_jogador}: {contador_jogador} x {nome_oponente}: {contador_oponente}\n")

        if contador_jogador == 2:
            print(f"{nome_jogador} Venceu o jogo.\n")
            return True
        elif contador_oponente == 2:
            print(f"{nome_oponente} Venceu o jogo.\n")
            return True
        elif round == 3:
            if contador_jogador > contador_oponente:
                print(f"{nome_jogador} Venceu o jogo.\n")
                return True
            elif contador_jogador < contador_oponente:
                print(f"{nome_oponente} Venceu o jogo.\n")
                return True
            else:
                print(f"{contador_jogador} a {contador_oponente}. Jogo empatou!\n")
                return True
        return False
