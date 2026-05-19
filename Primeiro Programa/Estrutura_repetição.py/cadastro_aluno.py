print("CADASTRO DE ALUNOS")
print("-" * 30)
alunos = []

qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))   

for x in range(qtd_alunos):
    print(f"Aluno {x + 1}")

    aluno = input("Nome do aluno: ")
    idade = int(input("Idade: "))           
    sexo = input("Sexo: ")
    serie = input("Série: ")
    alunos.append({"nome": aluno, "idade": idade, "sexo": sexo, "serie": serie}) 
    print("-" * 30)   

    
    disciplinas = []

    qtd = int(input("Quantas disciplinas deseja cadastrar? "))

    for x in range(qtd):
        print(f"Disciplina {x + 1} ")

        nome_disciplina = input("Nome da disciplina: ")

        notas = []

        for n in range(4):
            nota = float(input(f"Digite a {n + 1}ª nota: "))
            notas.append(nota)

        media = sum(notas) / 4
        print(f"A média da disciplina {nome_disciplina} é: {media:.2f}")
        disciplinas.append({"disciplina": nome_disciplina, "media": media})   
        print("-" * 30)
        
               


print("relatório de alunos cadastrados:")
print("-" * 30)
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Sexo: {aluno['sexo']}, Série: {aluno['serie']}")
    for disciplina in disciplinas:
        print(f"Disciplina: {disciplina['disciplina']}, Média: {disciplina['media']:.2f}") 
        