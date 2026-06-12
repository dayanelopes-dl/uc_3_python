dados_alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    # Validação: Se o aluno já existir, exibe a mensagem e para a função
    if aluno_existe(nome):
        print(f"Erro! O aluno '{nome}' já está cadastrado. Cadastre um novo aluno.")
        return

    try:
        idade = int(input("Digite a idade: "))
        turma = input("Digite a turma: ")
    except ValueError:
        print("Erro! Idade apenas números!")
        return 
        
    # Estrutura da matriz pura: [Nome, Nota1, Nota2, Nota3, Nota4, Média]
    dados_alunos.append([nome, 0.0, 0.0, 0.0, 0.0, 0.0])
    print(f"Aluno {nome} cadastrado com sucesso!")


def aluno_existe(nome):
    # Percorre todas as linhas da matriz usando range e len
    for i in range(len(dados_alunos)):
        # Se o nome digitado for igual ao nome cadastrado na coluna 0 (ignorando maiúsculas/minúsculas)
        if dados_alunos[i][0].lower() == nome.lower():
            return True
    return False


def lancar_notas():
    try:
        if not dados_alunos:
            print("Nenhum aluno cadastrado ainda.")
            return
            
        print("Lista de Alunos:")
        for i in range(len(dados_alunos)):
            print(f"[{i}] - {dados_alunos[i][0]}")
            
        escolha = int(input("Digite o número do aluno para lançar as notas: "))

        if 0 <= escolha < len(dados_alunos):
            # Captura as colunas de notas atuais (índices 1 a 4)
            notas_atuais = dados_alunos[escolha][1:5]
            
            # VALIDAÇÃO: Se a soma das notas for maior que 0, significa que as notas já existem
            if sum(notas_atuais) > 0:
                print(f"Erro! As notas para o aluno {dados_alunos[escolha][0]} já foram cadastradas.")
                return # Interrompe a função e volta direto para o menu
                
            print(f"Lançando notas para {dados_alunos[escolha][0]}")
            
            for j in range(4):
                dados_alunos[escolha][1 + j] = float(input(f"Digite a {j+1}ª nota: "))
                
            notas = dados_alunos[escolha][1:5]
            media = sum(notas) / 4

            dados_alunos[escolha][5] = media 
            print("Notas lançadas e médias calculadas com sucesso!")
        
        else:
            print("Aluno inválido.")
     
    except ValueError:
        print("Erro. Apenas valores numéricos são aceitos.")
    return



def situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def consultar_aluno():
    if not dados_alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    print("---CONSULTAR ALUNO---")
    for i in range(len(dados_alunos)):
        print(f"[{i}] - {dados_alunos[i][0]}")

    escolha = int(input("Digite o número do aluno para consultar: "))

    if 0 <= escolha < len(dados_alunos):
        aluno = dados_alunos[escolha]
        print(f"\nAluno: {aluno[0]}")
        print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}, {aluno[4]}")
        print(f"Média Final: {aluno[5]:.2f}")
    else:
        print("Aluno inválido.")

def relatorio_geral():
    if not dados_alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    print("\n--- RELATÓRIO GERAL DOS ALUNOS ---")
    
   
    total_alunos = len(dados_alunos)
    soma_medias = 0.0
    qtd_aprovados = 0
    qtd_recuperacao = 0
    qtd_reprovados = 0
    
   
    nome_melhor = dados_alunos[0][0]
    maior_media = dados_alunos[0][5]
    
    nome_pior = dados_alunos[0][0]
    menor_media = dados_alunos[0][5]

  
    print("-"*40)
    
    for i in range(total_alunos):
        aluno = dados_alunos[i]
        nome = aluno[0]
        media = aluno[5]
        situacao_aluno = situacao(media)
        
        # 1. Mostra o início da linha com o Nome do Aluno
        print(f"Aluno:{nome} / Notas: ", end="")
        
        # 2. Varre as colunas de notas (índices 1, 2, 3 e 4) na mesma linha
        for j in range(1, 5):
            print(f"[{aluno[j]:.1f}] ", end="")
            
        # 3. Mostra a coluna da Média e a Situação no final da linha
        print(f"/ Média: [{media:.2f}] / Situação: {situacao_aluno}")

        
        # Somatório para a média da turma
        soma_medias += media
        
        # Contagem da situação utilizando a sua função
        if situacao_aluno == "Aprovado":
            qtd_aprovados += 1
        elif situacao_aluno == "Recuperação":
            qtd_recuperacao += 1
        else:
            qtd_reprovados += 1
            
        # Verificação do melhor aluno
        if media > maior_media:
            maior_media = media
            nome_melhor = nome
            
        # Verificação do pior aluno
        if media < menor_media:
            menor_media = media
            nome_pior = nome

    # Cálculos finais
    media_turma = soma_medias / total_alunos

   
    print("-"*40)
    print(f"Quantidade total de alunos: {total_alunos}")
    print(f"Média geral da turma: {media_turma:.2f}")
    print(f"Melhor aluno: {nome_melhor} (Média: {maior_media:.2f})")
    print(f"Pior aluno: {nome_pior} (Média: {menor_media:.2f})")
    print("-" * 40)
    print(f"Alunos Aprovados: {qtd_aprovados}")
    print(f"Alunos em Recuperação: {qtd_recuperacao}")
    print(f"Alunos Reprovados: {qtd_reprovados}")
    print("-"*40)

def salvar_dados():
    if not dados_alunos:
        print("Não há dados para salvar.")
        return

    # Abre o arquivo para escrita. O ';' criará a divisão perfeita de colunas
    with open("C:/Users/Day Lopes/Documents/alunos.txt", "a", encoding="utf-8") as arquivo:
        # Cabeçalho para identificar as colunas (Opcional, remova se o exercício não pedir)
        arquivo.write("Nome;Nota 1;Nota 2;Nota 3;Nota 4;Média\n")
        
        for i in range(len(dados_alunos)):
            aluno = dados_alunos[i]
            
            # Mapeia as variáveis direto das colunas da matriz do aluno
            nome = aluno[0]
            n1 = aluno[1]
            n2 = aluno[2]
            n3 = aluno[3]
            n4 = aluno[4]
            media = aluno[5]
            
            # Monta a linha separando cada coluna por ponto e vírgula
            linha = f"{nome};{n1};{n2};{n3};{n4};{media:.2f}\n"
            
            # Escreve a linha gerada no arquivo texto
            arquivo.write(linha)
            
    print("Dados salvos em 'alunos.txt' com as notas organizadas em colunas!")


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