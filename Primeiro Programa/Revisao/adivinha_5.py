numero_secreto = 42
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    print("Tentativa {} de {}" .format(rodada, total_tentativas))
    chute = int(input('Digite um numero: '))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    if (acertou):
        print('Voce acertou o Numero!')
        break
    elif (maior):
        print(" Voce errou! O numero que voce digitou é MAIOR")
    else:
        print(" Voce errou! O numero que voce digitou é MENOR")

    rodada = rodada  + 1

print("Fim de Jogo")