# for é um looping 
#for x in range (1, 10, 2):
    #print(x)

numero_secreto = 42
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

    

print("Fim de Jogo")