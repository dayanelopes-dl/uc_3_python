x = int(input("Informe um numero: "))

if x % 2 == 0:
    quadrado = x **2 
    print(f"{x} é par e o seu quadrado é: {quadrado}.")
else:
    cubo = x **3
    print(f"{x} é impar e o seu cubo é: {cubo}")