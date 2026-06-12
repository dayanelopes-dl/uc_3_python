import random
print("### SISTEMA DE SORTEIO ###")
print("-"*30)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
while True:
    numero = int(input("Digite 15 numeros entre 1 e 25: "))
    if numero in numeros:
        numeros.remove(numero)      
    else:
        print("Número inválido ou já digitado. Tente novamente.")                   
    if len(numeros) == 10:
        break
print("Números digitados:", numeros)
print("-"*30)
random.shuffle(numeros)   #muda posiçoes(embaralha dados)
sorteio = random.choice(numeros) #choice sorteia um (dado)
print(f"O número sorteado é: {sorteio}")
print("-"*30)
