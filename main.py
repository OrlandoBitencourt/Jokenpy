import cartas
import jogadores
import jogo
import validadores


cartas = [cartas.Cartas("Pedra", 1), cartas.Cartas("Papel", 2), cartas.Cartas("Tesoura", 3)]

print("\nJokenpy\n")

computador = jogadores.Jogadores("Computador")

jogador = jogadores.Jogadores(input("Informe seu nome: "))
print(f"\nSeja bem-vindo: {jogador.nome}!\n")

while True:
    contador_round_jogador1 = 0
    contador_round_jogador2 = 0
    sair_menu = "s"

    for round in range(1, 4):
        print(f"Round: {round}\n")

        jogo_iniciado = jogo.Jogo()

        print(f"Você recebeu 3 cartas.")
        for carta in cartas:
            print(f"{carta.valor} - {carta.nome}")

        carta_escolhida = jogador.escolher_carta()

        for carta in cartas:
            if carta_escolhida == carta.valor:
                carta.printar_carta_escolhida(jogador.nome)

        valor_carta_computador = jogo_iniciado.gera_carta_automaticamente()

        for carta in cartas:
            if valor_carta_computador == carta.valor:
                carta.printar_carta_escolhida(computador.nome)

        vencedor = jogo_iniciado.verificar_vencedor_rodada(carta_escolhida, valor_carta_computador)

        if vencedor == 1:
            contador_round_jogador1 = validadores.valida_rodada(contador_round_jogador1)
        elif vencedor == 2:
            contador_round_jogador2 = validadores.valida_rodada(contador_round_jogador2)

        ganhou = jogo_iniciado.verifica_vencedor_jogo(contador_round_jogador1, jogador.nome,
                                                      contador_round_jogador2, computador.nome,
                                                      round)

        if ganhou:
            sair_menu = input("Jogar novamente? N para sair: ")
            round = 1

    if sair_menu == "n" or sair_menu == "N":
        break
