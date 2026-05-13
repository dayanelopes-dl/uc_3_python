pares = 0
impares = 0

for cont in range(5):  #dentro for ele repete em range(intervalos) no caso (5), range limita
    numeros =int(input("Digite um numero:\n"))
    if numeros % 2 == 0:
        pares = pares + 1
else:
        impares = impares + 1
        
print(f"Quantidade de numeros pares digitados é: {pares}")
print(f"Quantidade de numeros impares digitados é: {impares}")