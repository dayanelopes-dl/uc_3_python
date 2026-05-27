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
    
    print("-" * 30)   

    
    disciplinas = []

    qtd = int(input("Quantas disciplinas deseja cadastrar? "))

    for y in range(qtd):
        print(f"Disciplina {y + 1} ")

        nome_disciplina = input("Nome da disciplina: ")

        notas = []

        for n in range(4):
            nota = float(input(f"Digite a {n + 1}ª nota: "))
            notas.append(nota)

        media = sum(notas) / 4
        print(f"A média da disciplina {nome_disciplina} é: {media:.2f}")

        disciplinas.append({
            "disciplina": nome_disciplina,
            "media": media
        })

    alunos.append({
        "nome": aluno,
        "idade": idade, 
        "sexo": sexo,
        "serie": serie,
        "disciplinas": disciplinas
    })
    
    print("-" * 30)

               
print("relatório de alunos cadastrados:")
print("-" * 30)

for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Sexo: {aluno['sexo']}")
    print(f"Série: {aluno['serie']}")

    print("Disciplinas:")

    for disciplina in aluno["disciplinas"]:
        print(f"  - {disciplina['disciplina']}: Média = {disciplina['media']:.2f}")
    print("-" * 30)
        