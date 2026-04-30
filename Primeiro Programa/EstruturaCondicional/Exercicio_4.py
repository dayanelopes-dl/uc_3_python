num1 = int(input("Digite o 1º Numero: "))
num2 = int(input("Digite o 2º Numero: "))
num3 = int(input("Digite o 3º Numero: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Tem numeros iguais digitado")
    exit()  # Encerra o programa
if num1 > num2 and num1 > num3:
    print("O numero Maior é: ", num1)
if num2 > num1 and num2 > num3:
    print("O numero Maior é: ", num2)
if num3 > num1 and num3 > num2:
    print("O numero Maior é: ", num3)

    # EXERCICIO DE LOGICA
    # PARA DESCOBRIR O NUMERO MAIOR
