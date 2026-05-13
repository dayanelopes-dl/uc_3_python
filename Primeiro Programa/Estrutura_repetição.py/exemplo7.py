mulheres = 0
homens_ac18 = 18

#while True: # while = enquanto for verdaeiro ele nao para.
for res in range (5):
    idade = int(input("Informe sua idade: "))
    if idade < 0:
        break
    sexo = input("M - Masculino F - Feminino: ")
    if sexo == "F" or sexo == "f":
        mulheres = mulheres + 1
    elif sexo == "M" or sexo == "m":
        if idade >= 18:
            homens_ac18 = homens_ac18 + 1
print(f"Total de Mulheres: {mulheres}")
print(f"Total de Homens: {homens_ac18}")



