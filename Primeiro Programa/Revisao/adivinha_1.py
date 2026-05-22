numero_secreto = 42
chute = int(input('Digite um numero: '))

if (chute == numero_secreto):
    print('Voce acertou o Numero!')
else:
    if (chute > numero_secreto):
        print("Voce errou! o seu chute foi maior que o numero secreto.")
    else:
         print("voce errou ! o seu chute foi menor qu eo numero secreto")
