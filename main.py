import cartas
import jogadores
import jogo
import validadores

cartas = [cartas.Cartas("Pedra",1), cartas.Cartas("Papel",2), cartas.Cartas("Tesoura",3)]

print("\nJokenpy\n")

computador = jogadores.Jogadores("Computador")

jogador = jogadores.Jogadores(input("Informe seu nome: "))
print(f"\nSeja bem-vindo: {jogador.nome}!\n")

while True:

    for round in range(2):

        contador_round_jogador1 = 0
        contador_round_jogador2 = 0

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

        vencedor = jogo_iniciado.verificar_vencedor_rodada(carta_escolhida, valor_carta_computador)

        if vencedor == 1:

            contador_round_jogador1 = validadores.valida_rodada(contador_round_jogador1)
            ganhou = jogo_iniciado.verifica_vencedor_jogo(contador_round_jogador1,jogador.nome)

        elif vencedor == 2:

            contador_round_jogador2 = validadores.valida_rodada(contador_round_jogador2)
            ganhou = jogo_iniciado.verifica_vencedor_jogo(contador_round_jogador1, jogador.nome)

        if ganhou:

            sair_menu = input("Jogar novamente? N para sair: ")

            if sair_menu == "n" or sair_menu == "N":
                break