import validadores


class Jogadores:

    nome = ""

    def __init__(self, nome):
        self.nome = nome

    def escolher_carta(self):
        carta_escolhida = 0

        while True:
            try:
                carta_escolhida = int(input("Informe o numero representante da carta escolhida: "))
            except:
                pass

            validar_campo = validadores.valida_carta_escolhida(carta_escolhida)

            if validar_campo == True:
                break

        return carta_escolhida



