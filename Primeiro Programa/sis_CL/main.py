#Uma tupla com os perfis permitidos no sistema
perfis_permitidos = ("Aluno", "Professor", "Tecnico")

tipos_problemas = ("Internet", "Computador", "Progetor","Teclado", "Mouse")

#Lista armazena os usuarios cadastrados
usuarios = []

chamados = []

#Função para salvar os dados do usuario em arquivo txt
def salvar_usuario_arquivo(usuario):
    
    #Tenta abrir e gravar no arquivo
    try:
        
        #Abre o arquivo
        arquivo = open('C:/Users/vboxuser/Documents/cadastro_usuario.txt', 'a', encoding='utf-8')
        
        #Escreve os dados do usuario no arquivo txt separando por ponto e virgula
        arquivo.write(
            usuario["nome"] + ";" +
            usuario["login"] + ";" +
            usuario["senha"] + ";" +
            usuario["perfil"] + "\n"
        )
        
        #Fecha o arquivo
        arquivo.close()
    
    #Mostra o erro de gravação no arquivo    
    except:
        
        #Mostra a mensagem de erro de gravação
        print("Erro ao salvar os dados do usuário no arquivo.")
    
    #Sempre vai executar
    finally:
        
        #Mostra a mensagem de sucesso
        print("Dados salvo com sucesso.")

#Função para fazer Login
def fazer_login():
    
    #Solicita os dados do Login
    login = input("Informe o Login: ")
    
    #Solicita os dados da Senha
    senha = input("Informe a Senha: ")
    
    #Percorre a lista de usuarios
    for usuario in usuarios:
        
        #Verifica se o login e a senha estão corretos
        if usuario['login'] == login and usuario['senha'] == senha:
            
            #Mostra mensagem de boas vindas
            print("Login Realizado com Sucesso")
            
            #Retorna o usuario logado
            return usuario
    
    #Mostra a mensagem caso não encontre o usuario
    print("Login ou Senha incorreta!!!")

    return None
#para registrar chamado
def registrar_chamado(usuario_logado):
    
    #cria dicionario 
    chamado = {}

    chamado['usuario'] = usuario_logado['nome']

    print("Tipo de Problemas")
    for problema in tipos_problemas:
        print("-", problema)
    chamado["problema"] = input("Digite o tipo do problema: ")

    if chamado['problema'] not in tipos_problemas:
        
        print("tipos de problema invalido")

        return

    chamado['descricao'] = input("Descreva o problema: ")

    chamado["status"] = "Aberto"

    chamados.append(chamado)

    salvar_chamado_usuario(chamado)

def salvar_chamado_usuario(chamado):
   
    try:

        arquivo_chamado = open('C:/Users/vboxuser/Documents/chamados.txt', 'w', encoding='utf-8')
        
        arquivo_chamado.write(
            chamado['usuario'] + ";" +
            chamado['problema'] + ";" +
            chamado['descricao'] + ";" +
            chamado['status'] + "\n"
        )

        arquivo_chamado.close()
    
    except:
        print("erro ao salvar chamado")
        

    finally:
        print("chamados salvo com sucesso")
    

def carregar_chamado():
     try:
    # abre o arquivo txt no modo leitura
        arquivo_lista = open("C:/Users/vboxuser/Documents/chamados.txt", 'r' , encoding='utf-8')

      # ele percorre cada linha dentro arquivo txt
        for lista in arquivo_lista:

            lista = lista.strip()

           # verifica se a linha nao esta vazia
            if lista != '':
             
             # separa os dados usando ponto e virgula
                dados = lista.split(";")
            #cria um dicionario
                chamado = {
                    "usuario": dados[0],
                    "problema": dados[1],
                    "descricao": dados[2],
                    "status": dados[3]
                }

                #adiciona o usaurio dentro da lista de usuario
                chamados.append(chamado)

        #fecho o arquivo pos a leitura
        arquivo_lista.close()

     except FileNotFoundError:
        print("O arquivo não foi criado ainda")

        #sempre ira executar
     finally:
        #mensagem para mostra o carregamento do usuario
        print("chamado carregado com sucesso!")


    
#Uma função para cadastrar novos usuários
def cadastrar_usuario():
    
    #Criar um dicionário vazio para o usuário
    usuario = {}
    
    #Solicita o nome do usuario
    usuario['nome'] = input("Digite o nome completo: ")
    
    #Solicita o login do usuário
    usuario['login'] = input("Digite o login: ")
    
    #Solicita a senha do usuário
    usuario['senha'] = input("Digite a senha: ")
    
    #Mostra os perfis do sistema
    print("\nPerfis disponiveis")
    
    #Percorre a tupla dos perfis permitidos
    for perfil in perfis_permitidos:
        
        #Mostra cada perfil
        print("-", perfil)
        
    #Solicita o perfil do usuario
    usuario['perfil'] = input("Digite o perfil: ")
    
    #Verifica se o perfil informado pelo usuario exite
    if usuario['perfil'] not in perfis_permitidos:
        
        #Mostra a mensagem de erro
        print("Perfil inválido")
        
        #Encerra a função cadastrar
        return
    
    #Percorre a lista de usuarios cadastrados
    for i in usuarios:
        
        #Verifica se o login já existe
        if i['login'] == usuario['login']:
            
            #Mostra a mensagem de erro
            print("Esse login já existe.")
            
            #Encerra a função
            return
    
    #Adiciona o usuario na lista
    usuarios.append(usuario)
    
    salvar_usuario_arquivo(usuario)
    
    #Mostra mensagem de sucesso
    print("Usuário cadastrado com sucesso!")

 # função é resposavel por carregar os usuarios do arquivo txt
def carregar_usuario():
    #try para tentar abrir o arquivo txt
    try:
    # abre o arquivo txt no modo leitura
        arquivo = open("C:/Users/vboxuser/Documents/cadastro_usuario.txt", 'r' , encoding='utf-8')

      # ele percorre cada linha dentro arquivo txt
        for linha in arquivo:

            linha = linha.strip()

           # verifica se a linha nao esta vazia
            if linha != '':
             
             # separa os dados usando ponto e virgula
                dados = linha.split(";")
            #cria um dicionario
                usuario = {
                    "nome": dados[0],
                    "login": dados[1],
                    "senha": dados[2],
                    "perfil": dados[3]
                }

                #adiciona o usaurio dentro da lista de usuario
                usuarios.append(usuario)

        #fecho o arquivo pos a leitura
        arquivo.close()

    #caso op arquivo ainda nao exist, isso aqui vai funcionar
    except FileNotFoundError:
        print("O arquivo não foi criado ainda")

        #sempre ira executar
    finally:
        #mensagem para mostra o carregamento do usuario
        print("usuario carregado com sucesso!")



#Função para mostrar o menu após o login
def menu_sistema(usuario_logado):
    
    #Repetição do menu
    while True:
        #Mostra o menu do sistema
        print("\n===== Menu Sistema =====")
        print("1 - Registrar chamado")
        print("2 - Listar chamados")
        print("3 - Sair")
        
        #Tentar ler a opção do usuário
        try:
            
            #Solicita a opção e converte para numero inteiro
            opcao = int(input("Escolha uma opção: "))
        
        #Caso o usuário digite uma string
        except ValueError:
            
            #Mostra mensagem de erro
            print("Erro! Digite apenas números.")
            
            #Continuar o loop
            continue
        
        #Sempre vai executar
        finally:
            
            #Mostra mensagem que a opção deu certo
            print("Opção processada com sucesso.")
        
        
        if opcao == 1:
            
            registrar_chamado(usuario_logado)
            
        elif opcao == 2:
        
            if len(chamados) == 0:
                print("nenhum chamado")
            else:

                for chamado in chamados:
                    print(chamado['usuario'] ,'-', chamado['problema'], '-', chamado['descricao'], '-', chamado['status'])
        
        #Se escolher a 3, sai da conta
        elif opcao == 3:
        
            #Mostra mensagem
            print("Saindo da conta")
            
            #Interrompe o while
            break
        
        #Casp escolha uma opção inválida
        else:
            
            #Mostra mensagem de erro
            print("Opção inválida!")



#Função Principal do Programa
def menu_principal():
    
    #Estrutura de repetição do menu
    while True:
        
        #Mostrando o menu
        print("\n===== SISTEMA DE CHAMADOS ESCOLAR =====")
        print("1 - Cadastrar Usuários")
        print("2 - Fazer Login")
        print("3 - Listar usuários cadastrados")
        print("4 - Sair")
        
        #Tentar ler a opção do usuário
        try:
            
            #Solicita a opção e converte para numero inteiro
            opcao = int(input("Escolha uma opção: "))
        
        #Caso o usuário digite uma string
        except ValueError:
            
            #Mostra mensagem de erro
            print("Erro! Digite apenas números.")
            
            #Continuar o loop
            continue
        
        #Sempre vai executar
        finally:
            
            #Mostra mensagem que a opção deu certo
            print("Opção processada com sucesso.")
        
        #Verifica se a variavel opção é igual a 1
        if opcao == 1:
            
            #Chama a função cadastrar usuario
            cadastrar_usuario()
            
        #Verifica se a variavel opção é igual a 2
        elif opcao == 2:
            
            usuario_logado = fazer_login()

            if usuario_logado != None:

                menu_sistema(usuario_logado)
            
        #Verifica se a variavel opção é igual a 3
        elif opcao == 3:
            if len(usuarios) == 0:
             print("nenhum usuario cadastrado")

            else:

                for usuario in usuarios:
                    print(usuario['nome'],'-', usuario['login'],'-', usuario['perfil'])
                
            
        #Verifica se a variavel opção é igual a 4
        elif opcao == 4:
            
            #Mostra mensagem de encerramento
            print("Sistema encerrado.")
            
            #Para o while do menu principal
            break
        
        #Caso digite uma opção inexistente
        else:
            
            #Mostra a mensagem de erro
            print("Opção inválida!!!")


carregar_chamado()

carregar_usuario()  

menu_principal()