print("## Cadastro de Aluno ##")
print("-"*30)

alunos = []


while True:

   alunos = {
    "nome": input("aluno: "),
    "idade": int(input("idade:")),
    "sexo": input("sexo: "),
    "serie": input("serie: "),
    "diciplina" : []
   }
   break
    
while True: 
    nome_disciplina = input("Disciplina: ")
    if nome_disciplina.upper() ==  0:
        break

    notas = []
    for x in range(1, 5):
        nota = float(input(f"Informe a {x}ª nota: "))
        notas.append(nota)
    media = sum(notas) / 4
    print(f"A média da disciplina {nome_disciplina} é: {media:.2f}")

    print("-"*30)

    opcao = input("Deseja cadastrar outra disciplina?[S][N]? ")
    if opcao.upper() == "N":
        break

print("-"*30)
print(" Relatorio de Alunos cadastrados")
print("-"*30)
print(f"Aluno: {alunos['nome']}") 
print(f"Idade: {alunos['idade']}")
print(f"Sexo: {alunos['sexo']}")
print(f"Série: {alunos['serie']}")  
print(f"Disciplina: {nome_disciplina}")
print(f"Notas: {notas}")    
print(f"Média: {media:.2f}")