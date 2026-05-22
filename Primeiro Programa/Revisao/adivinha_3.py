numero_secreto = 42
chute = int(input('Digite um numero: '))

acertou = chute == numero_secreto
maior = chute > numero_secreto


if (acertou):
    print('Voce acertou o Numero!')
elif (maior):
    print(" Voce errou! O numero que voce digitou é MAIOR")
else:
    print(" Voce errou! O numero que voce digitou é MENOR")
