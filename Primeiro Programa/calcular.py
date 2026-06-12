def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero."
    return num1 / num2

def menu():
    print("Escolha a operação:")
    print("1. Subtração")
    print("2. Multiplicação")
    print("3. Divisão")
    print("0. Sair")

while True:
   try:
    menu()

    escolha = input("Digite sua escolha: ")

    if escolha == '0':
        print("Programa encerrado.")
        break
    elif escolha in ['1', '2', '3']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        

        if escolha == '1':
            resultado = subtracao(num1, num2)
            print(f"Resultado da subtração: {resultado}")
        elif escolha == '2':
            resultado = multiplicacao(num1, num2)
            print(f"Resultado da multiplicação: {resultado}")
        elif escolha == '3':
            resultado = divisao(num1, num2)
            print(f"Resultado da divisão: {resultado}")
        else:
         print("Escolha inválida. Por favor, tente novamente.")
        
   except ValueError:
       print("digite apenas numeros")