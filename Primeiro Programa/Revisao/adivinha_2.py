numero_secreto = 42
chute = int(input('Digite um numero: '))

if (chute == numero_secreto):
    print('Voce acertou o Numero!')
elif (chute > numero_secreto):
    print(" Voce errou! O numero que voce digitou é MAIOR")
else:
    print(" Voce errou! O numero que voce digitou é MENOR")