num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

print("MENU")
print("1. MEDIA PONDERADA, comdos 2 números")
print("2. Quadrado da soma dos 2 Numeros")
print("3. cubo do menor numero")

op = int(input("escolha uma opção: "))

if op < 1 or op > 3:
    print("Opcao INVALIDA!")
    exit() 
elif op == 1: 
    media = (num1 * 2) + (num2 * 3) /5
    print(f"\n Media ponderada calculada: {media:.2f}")
elif op == 2:
    quadrado = (num1 + num2) **2
    print("f\n O quadrado da soma dos numeros: {quadrado:.2f}")
else:
    if num1 < num2:
       cubo = num1 **3
       print(f"\n{num1:.2f} é o menor e o seu cubo é: {cubo:.2f}")
    else:
     cubo = num2 **3
     print(f"\n {num2:2f} é o menor numero e o seu cubo é {cubo:.2f}")
        
    
    