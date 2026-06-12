
dados_alunos = []

def cadastrar_aluno():
    nome = input("digite o nome do aluno: ")
    idade = int(input("digite a idade: "))
    turma = input("digite a turma: ")

    dados_alunos.append([nome,idade, turma, 0.0, 0.0, 0.0, 0.0, 0.0,])
    print(f"Aluno {nome} cadastrado com sucesso!")

def lancar_notas():
    if not dados_alunos:
        print(f"nenhum aluno cadastrado ainda")
        return
    print("Lista de Alunos: ")
    for i in range(len(dados_alunos)):
        aluno = dados_alunos[i]
        print(f"[{i}] - {aluno[0]}")

    escolha = int(input("digite o numero do aluno para lançar as notas: "))

    if 0 <= escolha < len(dados_alunos):
        print(f"Lançando notas para {dados_alunos[escolha][0]}")

        for j in range(1, 5):
            dados_alunos[escolha][j] = float(input(f"Digite {j}ª nota: "))

        notas = dados_alunos[escolha][1:5]
        media = sum(notas) / 4
        dados_alunos[escolha][5] = media #salva media na coluna 5
        print("Notas lançadas e média calculada com sucesso!")
    else:
        print("Aluno Invalido.")

def situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def consultar_aluno():
   
    if len(dados_alunos) == dados_alunos[nome]:
        print("Nenhum aluno cadastrado.")
        return
    nome_pesquisa = input("Digite o nome do aluno que deseja consultar: ")
   

    for i in range(len(dados_alunos)):
        if dados_alunos[i] == nome_pesquisa:
            print(f"nome: {nome_encontrado}")
    print("Aluno não encontrado.")





def menu_principal():
    while True:
        print("--- SISTEMA DE GERENCIAMENTO ESCOLAR ---")
        print("1 - Cadastrar Aluno")
        print("2 - Lançar Notas")
        print("3 - Consultar Aluno")
        print("4 - Relatório Geral")
        print("5 - Salvar Dados")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            lancar_notas()
        elif opcao == 3:
            consultar_aluno()
        elif opcao == 4:
            relatorio_geral()
        elif opcao == 5:
            salvar_dados()
        elif opcao == 6:
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

menu_principal()

