pessoas = []

for i in range(5):
    nome = input(f"nome da pessoa {i+1}: ")
    idade = int(input(f"idade de {nome}: "))
    pessoas.append([nome, idade])

menor = 0 
for i in range(len(pessoas)):
    if pessoas[i][1] < pessoas[menor][1]: # compara a idade da pessoa atual com a idade da pessoa mais nova encontrada até agora
        menor = i

for pessoa in pessoas:
    print(pessoa)
print(f"A pessoa mais nova é {pessoas[menor][0]}")