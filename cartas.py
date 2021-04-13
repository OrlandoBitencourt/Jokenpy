

class Cartas:

    nome: ""
    valor: 0

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return (f"{self.valor} - {self.nome}")

    def printa_carta_escolhida(self, nome_jogador, valor_carta):
        if valor_carta == self.valor:
            print(f"{nome_jogador} escolheu: {self.valor} - {self.nome}")


