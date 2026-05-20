def cadastrar_aluno():
    aluno = {} #Dicionario

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["sexo"] = input("Digite o sexo do aluno: ")
    aluno["serie"] = input("Digite a serie do aluno: ")
    
    aluno["disciplina"] = []

    qtd_disciplina = int(input("Quantas disciplinas deseja cadastrar ? "))

    for i in range(qtd_disciplina):
        disciplina = cadastrar_disciplina(i)
        aluno["disciplina"].append(disciplina)

    return aluno

def cadastrar_disciplina(i):
    disciplina ={}

    disciplina["Nome"] = input(f"Digite o nome da {i + 1} disciplina: ")
    disciplina["notas"] = []

    for i in range(4):
        nota = float(input(f"Digite a {i + 1} nota: "))
        disciplina ["notas"].append(nota)

    disciplina["media"] = calcular_media(disciplina["notas"])

    return disciplina

def calcular_media(notas):
    
    media = sum(notas) / len(notas)
    return media

def menu():
    alunos = []
    while True:
        print("______MENU______")
        print(" 1 - Cadastrar Aluno")
        print(" 2 - mostrar relatório")
        print(" 3 - Sair")
        op = int(input("escolha uma opção: "))
        
        if op == 1:
             aluno = cadastrar_aluno()
             alunos.append(aluno)
             
        elif op == 2:
            mostrar_relatorio(alunos)
          
        elif op == 3:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

def mostrar_relatorio(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!!!")
    else:
        print("Relatório")

        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Sexo: {aluno['sexo']}")
            print(f"Série: {aluno['serie']}")

            print("Disciplinas:")

            for disciplina in aluno["disciplina"]:
                print(f"Disciplina: {disciplina['Nome']}")
                print(f"Notas: {disciplina['notas']}")
                print(f"Média: {disciplina['media']}")
menu()

        
