#uma tupla com os perfis de usuario permitidos no sistema
perfis_permitidos = ("aluno", "professor", "tecnico")

#lista armazenar os usuarios cadastrados no sistema
usuarios = []

#função responsável por salvar os usuarios cadastrados em um arquivo de texto
def salvar_usuario_arquivo(usuario): #via parametro recebe o usuario a ser salvo

    #tenta abrir e gravar no arquivo de texto
    try:

        #abre o arquivo de texto para escrita
        arquivo = open('C:/Users/vboxuser/Documents/cadastrado_usuario.txt', 'a', encoding='utf-8')

        #escreve os dados do usuario no arquivo de texto, separando cada campo por ponto e virgula
        arquivo.write(
            usuario["nome"] + ";" +
            usuario["login"] + ";" +
            usuario["senha"] + ";" +
            usuario["perfil"] + "\n"
        )

        arquivo.close() #fecha o arquivo de texto

    except:

        #mostra mensagem de erro de gravacao do usuario no arquivo de texto
        print("Erro ao salvar o usuario no arquivo de texto")
    finally:

        #mostra mensagem de usuario salvo com sucesso no arquivo de texto
        print("Usuario salvo com sucesso")  

def fazer_login():
    #solicitar o login do usuario
    login = input("Digite o login: ")

    #solicitar a senha do usuario
    senha = input("Digite a senha: ")

    #percorrer a lista de usuarios cadastrados para verificar se o login e senha estão corretos
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            print("Login realizado com sucesso")
            return usuario

    #mostrar mensagem de erro caso o login ou senha estejam incorretos
    print("Login ou senha incorretos")

#uma função para cadastrar novos usuarios 
def cadastrar_usuario():


    #criar um dicionário vazio para armazenar os dados do usuario
    usuario = {}

    #solicitar o nome completo do usuario e armazenar no dicionário
    usuario["nome"] = input("Digite o nome completo: ")
    usuario['login'] = input("Digite o login: ")
    usuario['senha'] = input("Digite a senha: ")
    
    #mostrar os perfis disponíveis no sistema
    print("\nPerfis disponíveis: ")

    #percorrer a tupla de perfis permitidos e mostrar cada um deles
    for perfil in perfis_permitidos:
        print("-",  perfil)

    #solicitar o perfil do usuario 
    usuario["perfil"] = input("Digite o perfil do usuario: ")

    #verificar se o perfil digitado pelo usuario existe
    if usuario['perfil'] not in perfis_permitidos:

        #mostrar mensagem de erro
        print("Perfil inválido")

        #encerrar a função cadastrar
        return
    #percorre a lista de usuarios cadastrados para verificar se o login já existe
    for i in usuarios:   
    
     if i['login'] == usuario['login']:
        print("Login já existe")
        return
    usuarios.append(usuario)

    salvar_usuario_arquivo(usuario)
    print("Usuario cadastrado com sucesso")

def menu_sistema():
    
        while True:
            print("\n ===== Menu Sistema =====")
            print(" 1 - Registrar chamado")
            print(" 2 - Listat chamados")
            print("3 - sair")
        try:   
            opcao = input("escolha uma opção: ")
        except ValueError:
            #mostra mensagem de erro 
            print("Opção inválida. Por favor, digite um número.")

            #continuar o loop 
            continue
        #sempre executa essa parte do código, independente de ter ocorrido um erro ou não
        finally:
            #mostra mensagem de opção processada com sucesso
            print("Opção processada com sucesso.")


            if opcao == 1:
             print("opçao 1")
            elif opcao == 2:
                print("opção 2")
            elif opcap == 3:
                print("saindo da conta")
                break
            else:
                print("opção invalida")
   

#Função Principal do PROGRAMA
def menu_principal():

    while True:
        # mostrando o menu
        print("===== SISTEMA DE CHAMADOS ESCOLAR")
        print("1 - Cadastrar Usuarios")
        print("2 - Fazer login")
        print("3 - Listar usuarios cadastrados")
        print("4 - Sair")

        try:
            #Solicita a opção e converte para numero inteiro
            op = int(input("escolha uma opção: "))
        except ValueError:
            #mostra mensagem de erro 
            print("Opção inválida. Por favor, digite um número.")

            #continuar o loop 
            continue
        #sempre executa essa parte do código, independente de ter ocorrido um erro ou não
        finally:
            #mostra mensagem de opção processada com sucesso
            print("Opção processada com sucesso.")

        #Verifica se variavel oção é igual a 1 

        if op == 1:
            cadastrar_usuario()
        #verifica se variavel oção é igual a 2

        elif op == 2:

            usuario_logado = fazer_login()
            
        #verifica se variavel oção é igual a 3

        elif op == 3:
            print("opção 3")
        #mostra a mensagem de encerramento do sistema e para o while do menu
        elif op == 4:
            print("sistema encerrado")
            #para o while do menu
            break
        else:
            print("opção invalida")

menu_principal()


