def valida_carta_escolhida(carta_escolhida):
    if carta_escolhida > 0 and carta_escolhida <= 3:
        return True
    else:
        print("\nDigite uma opção válida!\n")
        return False

def valida_rodada(rodada):
    rodada += 1
    return rodada

