
numero_secreto = 42
total_tentativas = 10
total_pontos = 0 
pontos_perdidos = 10
inicio_pontos = 100

print("Jodo de Adivinhe o numero")
print("Qual é o numero secreto?")
print("Escolha o nivel de dificuldade")
print("(1) 10 tentativas (2) 5 tentativas (3) 3 tentativas")
nivel = int(input("Defina o nivel: "))
if (nivel == 1):
    total_tentativas = 10
elif (nivel == 2):
    total_tentativas = 5
else:
    total_tentativas = 3

for tentativa in range (1, total_tentativas + 1):
    print("Tentativa {} de {}" .format(tentativa, total_tentativas))
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

    pontos_perdidos = abs(chute - numero_secreto)
    if pontos_perdidos > 1:
        total_pontos = total_pontos + pontos_perdidos
    print("Voce tem {} pontos" .format(total_pontos))
    print("voce tem total de {} pontos" .format(inicio_pontos - total_pontos))



print("Fim de Jogo")