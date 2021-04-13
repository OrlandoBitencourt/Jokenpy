import cartas
import jogadores
import jogo


cartas = [cartas.Cartas("Pedra",1), cartas.Cartas("Papel",2), cartas.Cartas("Tesoura",3)]

print("\nJokenpy\n")

computador = jogadores.Jogadores("Computador")

jogador = jogadores.Jogadores(input("Informe seu nome: "))
print(f"\nSeja bem-vindo: {jogador.nome}!\n")


while True:

    jogo_iniciado = jogo.Jogo()

    print(f"Você recebeu 3 cartas.")
    for carta in cartas:
        print(f"{carta.valor} - {carta.nome}")

    carta_escolhida = jogador.escolher_carta()

    for carta in cartas:
        carta.printa_carta_escolhida(jogador.nome, carta_escolhida)

    valor_carta_computador = jogo_iniciado.gera_carta_automaticamente()

    for carta in cartas:
        carta.printa_carta_escolhida(computador.nome, valor_carta_computador)

    rodada = jogo_iniciado.verificar_vencedor(carta_escolhida, valor_carta_computador)
