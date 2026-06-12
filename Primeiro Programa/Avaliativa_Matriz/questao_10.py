#10. Uma escola deseja armazenar as notas de 3 alunos em 4 bimestres. 
#Utilize uma matriz para armazenar as notas e exiba:  Todas as notas, Média de cada aluno,Situação (Aprovado ou Reprovado) 
#Considere média mínima 7

notas = []


for i in range(3):
    linha = []
    print(f"Aluno {i + 1}")
    
    for j in range(4):
        msg = f'Nota do {j+1}º bimestre: '
        linha.append(float(input(msg)))
        notas.append(linha)

for i in range(3):
    print(f"Aluno {i + 1}")
    print("Notas:", notas[i])
    
    media = sum(notas[i]) / 4

    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")