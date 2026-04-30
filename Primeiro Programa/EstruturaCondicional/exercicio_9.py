print("operaçao de divisao")

while True:
    n1 = int(input("Informe o 1º numero: "))
    n2 = int(input("Informe o 2º numero: "))

    if n2 == 0:
        print("Divisor não pode ser 0")
        break

    print(f"{n1} / {n2} = {(n1/n2):.2f}")

print("Fim da operação")
