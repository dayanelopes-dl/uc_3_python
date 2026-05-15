# 2(USUARIO) CADASTRAR NOME , IDADE, SEXO , SERIE, (ALUNO)
# O PROFESSOR CADASTRA 4 NOTAS PRA ESSE ALUNO.
#LISTA NO FINAL A NOTA DE CADA ALUNO. lança 4 nota
#TIRAr MEDIA
# CADASTRAR DISCIPLINA 

alunos = []
print("## Cadastro de Aluno ##")
print("-"*30)

#cADASTRO
while True:
    
alunos.append(input("nome: "))
alunos.append(input("Idade: "))
alunos.append(input("Sexo: "))
alunos.append(input("Serie: "))
disciplina = input("Disciplina: ")

print(""*30)

nota1 = float(input("Informe 1ª nota: "))
nota2 = float(input("Informe 2ª nota: "))
nota3 = float(input("Informe 3ª nota: "))
nota4 = float(input("Informe 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print("-"*30)

alunos = [nome, idade , sexo, serie]
dip = [disciplina]
notas = [nota1, nota2, nota3, nota4]
print(f"aluno:{nome}\nidade:{idade}\nsexo:{sexo}\nserie:{serie}")
print(f"disciplina:{disciplina}")
print(f"notas:{notas}")
print(f"a media é:{media}")
