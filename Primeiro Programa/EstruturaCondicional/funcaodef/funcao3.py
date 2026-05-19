dados = [] # lista vazia
disciplinas = []

def cadastrar_aluno(): 
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    sexo = input("informe o sexo do aluno: ")
    dados.append([nome, idade , sexo])
    print("Aluno cadastrado com sucesso!")

def cadastrar_disciplina():
    disciplinas = input("Informe o nome da disciplina: ")
    ch = int(input("Informe a carga horario: "))
    disciplinas.append([disciplinas, ch])
    print("Disciplina Cadastrada com sucesso!")

while True:
    print("---Sistema Academico---")
    print(" 1 - cadastrar aluno")
    print(" 2 - cadastar disciplina")
    op = int(input("Informe o que deseja:"))

    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_disciplina()
    else:
        print("Saindo do sistema")



 