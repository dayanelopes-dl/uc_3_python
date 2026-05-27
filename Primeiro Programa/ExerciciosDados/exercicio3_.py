
print("Informe seu Salario e o seu Cargo com opçoes Abaixo:")
salario = float(input("Informe seu Salario: R$"))

print("-#" * 20)
print("Opções de Cargo a Abaixo:")
print("1. Programador de Sistemas")
print("2. Analista de Sistemas")
print("3. Analista de Bancos de Dados")
print("-#" * 20)
cargo = float(input("Informe seu cargo conforme o numeros listados:"))


if cargo < 1 or cargo > 3: 
    print("cargo invalido")
    exit()
elif cargo == 1:
 salario = salario * 0.30 + salario
 print(f"o novo salario é: R$ {salario:.2f}")
elif cargo == 2:
    salario = salario * 0.20 + salario
    print(f" o seu novo salario é: R$ {salario:.2f}")
else:
    cargo == 3
    salario = salario * 0.15 + salario
    print(f"seu novo salario é: R$ {salario:.2f}")
        

