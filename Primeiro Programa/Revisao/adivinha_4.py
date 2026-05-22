# Equanto acontecer alguma coisa = faça ( While)

# x = 5

# while(x > 1): # ele nao vai imprimir 1 por que 1 nao é maior que 1
# print(x)
# x = x - 1

numero_secreto = 42
total_tentativas = 3

while (total_tentativas > 0):
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

    total_tentativas = total_tentativas - 1
