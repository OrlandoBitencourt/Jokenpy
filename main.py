import cartas
import jogadores
import jogo

carta_pedra = cartas.Cartas("Pedra",1)
carta_papel = cartas.Cartas("Papel",2)
carta_tesoura = cartas.Cartas("Tesoura",3)

print("\nJokenpy\n")

jogador = jogadores.Jogadores(input("Informe seu nome: "))

while True:

    print(f"Você recebeu 3 cartas.\n {carta_pedra}\n {carta_papel}\n {carta_tesoura}\n")

    carta_escolhida = jogador.escolher_carta()

    rodada_atual = jogo.Jogo()

    rodada = rodada_atual.verificar_vencedor(carta_escolhida)
