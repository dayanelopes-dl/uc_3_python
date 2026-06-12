print("## Cadastro de Aluno ##")
print("-"*30)

alunos = []
disciplinas = []
notas = []
while True:
    nome = input("Nome do aluno (ou sair para parar): ").strip()
    if nome.lower() == "sair":
        break
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")              
    serie = input("Série: ")
    alunos.append((nome, idade, sexo, serie))
    print("-"*30)
    
    while True:
        nome_disciplina = input("Informe o nome da disciplina: ")
        
        notas_disciplina = []
        for i in range(4):
            nota = float(input(f"Informe a nota {i+1} da disciplina {nome_disciplina}: "))
            notas_disciplina.append(nota) 
            print("-"*30)
        media = sum(notas_disciplina) / 4
        print(f"A média da disciplina {nome_disciplina} é: {media:.2f}")
        disciplinas.append(nome_disciplina)

        opcao = input("Deseja cadastrar outra disciplina?[S][N]? ")
        if opcao.upper() == "N":
            break   
        print("-"*30)
        opcao2 = input("Deseja cadastrar outro aluno?[S][N]? ")   
        if opcao2.upper() == "N":
            break

        print([alunos, disciplinas, notas, media])
        
        
