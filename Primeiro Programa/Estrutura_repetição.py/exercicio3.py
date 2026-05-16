# 2(USUARIO) CADASTRAR NOME , IDADE, SEXO , SERIE, (ALUNO)
# O PROFESSOR CADASTRA 4 NOTAS PRA ESSE ALUNO.
#LISTA NO FINAL A NOTA DE CADA ALUNO. lança 4 nota
#TIRAr MEDIA
# CADASTRAR DISCIPLINA 

alunos = []
medias = []

print("## Cadastro de Aluno ##")
print("-"*30)

#cADASTRO

while True:
    aluno = input("aluno: ")
    alunos.append(aluno)
    idade = int(input("idade:"))
    alunos.append(idade)
    sexo = input("sexo: ")
    alunos.append(sexo)
    serie = input("serie: ")
    alunos.append(serie)
    disciplinas = input("disciplina:") 
    alunos.append(disciplinas)
    nota1 = float(input("Informe 1ª nota: "))
    alunos.append(nota1)
    nota2 = float(input("Informe 2ª nota: "))
    alunos.append(nota2)
    nota3 = float(input("Informe 3ª nota: "))
    alunos.append(nota3)
    nota4 = float(input("Informe 4ª nota: "))
    alunos.append(nota4)
    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)
    print("-"*30)

    opcao = input("Deseja continuar[S][N]? ")
    if opcao.upper() == "N":
        break

print(f"Alunos cadastrados: {alunos[0:8]}")
print(f" Média dos alunos: {medias [0:1]}")
print("-"*30)

#alunos = [nome, idade , sexo, serie]
#dip = [disciplina]
#notas = [nota1, nota2, nota3, nota4]
#print(f"aluno:{nome}\nidade:{idade}\nsexo:{sexo}\nserie:{serie}")
#print(f"disciplina:{disciplina}")
#print(f"notas:{notas}")
#print(f"a media é:{media}")
