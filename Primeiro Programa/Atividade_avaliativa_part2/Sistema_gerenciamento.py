#Desenvolvimento um sistema de gerenciamento Escolar contendo as seguintes funcionalidades:

alunos = []

matriz = [[alunos]] #matriz


def cadastrar_aluno():
    nome = input("Nome do aluno: ")

    for a in alunos:
        if a["nome"].lower() == nome.lower():
            print("Aluno já cadastrado!")
            return

    aluno = {
        "nome": nome,
        "idade": int(input("Idade: ")),
        "turma": input("Turma: "),
        "notas": []
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
    
def lancar_notas():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():

            print(f"Aluno encontrado: {aluno['nome']}")

            notas_aluno = []

            for i in range(4):
                while True:
                    try:
                        nota = float(input(f"{i+1}ª nota: "))
                        if 0 <= nota <= 10:
                            break
                        else:
                            print("Digite uma nota entre 0 e 10.")
                    except ValueError:
                        print("Digite um número válido.")

                notas_aluno.append(nota)

           
            print("Notas lançadas com sucesso!")
            return

    print("Aluno não encontrado.")


def calcular_media_indice(i):
    if len(notas[i]) == 0:
        return 0
    return sum(notas[i]) / len(notas[i])

def situacao_indice(i):
    media = calcular_media_indice(i)

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def consultar_aluno():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(f"\nNome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Turma: {aluno['turma']}")
            if aluno["notas"]:
                print("Notas:", aluno["notas"])
                print("Média:", calcular_media(aluno))
                print("Situação:", situacao(aluno))
            else:
                print("Nenhuma nota lançada.")
            return
    print("Aluno não encontrado.")

def relatorio_geral():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    melhor_aluno = None
    pior_aluno = None
    melhor_media = -1
    pior_media = 11

    for aluno in alunos:
        media = calcular_media(aluno)
        soma_medias += media

        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1

        if media > melhor_media:
            melhor_media = media
            melhor_aluno = aluno["nome"]

        if media < pior_media:
            pior_media = media
            pior_aluno = aluno["nome"]

    media_turma = soma_medias / len(alunos)
    total_alunos = len(alunos)

    print("--- RELATÓRIO GERAL ---")
    print("total de Alunos: ", total_alunos)
    print("Média da turma:", media_turma)
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)
    print("Melhor aluno:", melhor_aluno, "-", melhor_media)
    print("Pior aluno:", pior_aluno, "-", pior_media)


def salvar_dados():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado para salvar.")
        return

    try:
        with open('C:/Users/vboxuser/Documents/alunos_cadastrados.txt', 'a', encoding='utf-8') as arquivo:
            for aluno in alunos:
                arquivo.write(
                    aluno["nome"] + ";" +
                    str(aluno["idade"]) + ";" +
                    aluno["turma"] + ";" +
                    str(aluno["notas"]) + ";" +
                    str(calcular_media(aluno)) + ";" +
                    situacao(aluno) + "\n"
                )
    except:
        print("Erro ao salvar os alunos.")
    else:
        print("Todos os alunos foram salvos com sucesso!")

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
print(matriz)
menu_principal()