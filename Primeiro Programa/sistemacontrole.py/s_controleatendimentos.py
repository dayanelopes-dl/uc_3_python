tipo_atendimento = ("Consulta", "Exame", "Retorno")
tipo_de_pagamento = ("Dinheiro", "Pix", "Cartão")

pacientes = []
atendimentos = []

def cadastrar_paciente():
            paciente = {}
            paciente["nome"] = input("Digite o nome do paciente: ")
            paciente["idade"] = int(input("Digite a idade do paciente: "))

            print("Tipos de atendimento:")
            print("1 - Consulta R$300")
            print("2 - Exame R$200")
            print("3 - Retorno R$70")

            try:
                while True:
                    opcao = int(input("Escolha o tipo de atendimento: "))
                    if opcao == 1:
                        paciente["tipo_atendimento"] = "Consulta"
                        break
                    elif opcao == 2:
                        paciente["tipo_atendimento"] = "Exame"
                        break
                    elif opcao == 3:
                        paciente["tipo_atendimento"] = "Retorno"
                        break
                    else:
                        print("Opção inválida.")
                        break
            except ValueError:
             print("Erro! Digite apenas números.")
             return

            paciente["quantidade_atendimento"] = int(input("Digite a quantidade de atendimentos: "))
            if paciente["quantidade_atendimento"] <= 0:
                print("Quantidade inválida. Tente novamente.")
                return
                print("Tipo de atendimento inválido. Tente novamente.")
                return

            paciente["forma_pagamento"] = input("Digite a forma de pagamento (Dinheiro, Pix, Cartão): ")
            if paciente["forma_pagamento"] not in tipo_de_pagamento:
                print("Forma de pagamento inválida. Tente novamente.")
                return
                print("Forma de pagamento registrada com sucesso!")
                return paciente["forma_pagamento"]


               
            print("Paciente cadastrado com sucesso!")
            continuar = input("Deseja cadastrar outro paciente? (s/n): ")
            if continuar.lower() != 's':
                return pacientes
            else:
                return menu()
                
            pacientes.append(paciente)

            salvar_paciente_arquivo(paciente)

def calcular_valor_atendimento():
    valor_cobrado = {
        "Consulta": 300,
        "Exame": 200,
        "Retorno": 70
    }
    tipos_atendimento = paciente["tipo_atendimento"]
    quantidade_atendimento = paciente["quantidade_atendimento"]
    valor_total = valor_cobrado[tipos_atendimento] * quantidade_atendimento
    return valor_total

def salvar_paciente_arquivo(paciente):
    try:
            arquivo = open('C:/Users/vboxuser/Documents/paciente_cadastrado.txt', 'w', encoding='utf-8')
            arquivo.write(
                    paciente["nome"] + ";" +
                    paciente["idade"] + ";" +
                    paciente["tipo_atendimento"] + ";" +
                    str(paciente["quantidade_atendimento"]) + ";" +
                    paciente["forma_pagamento"] + "\n"
                )
            arquivo.close()

    except:
        print("Erro ao salvar o paciente no arquivo.")

    finally:
        print("Paciente concluído.")

def carregar_paciente_arquivo():
    try:
        arquivo = open('C:/Users/vboxuser/Documents/paciente_cadastrado.txt', 'r', encoding='utf-8')
        for lista in arquivo:
            
            lista = lista.strip()
            if lista != '':
                dados = lista.split(";")
                paciente = {
                    "nome": dados[0],
                    "idade": dados[1],
                    "tipo_atendimento": dados[2],
                    "quantidade_atendimento":(dados[3]),
                    "forma_pagamento": dados[4]
                }
                pacientes.append(paciente)

        arquivo.close()

    except FileNotFoundError:
        print("Arquivo não foi encontrado ainda")
    finally:
        print("Carregamento de pacientes concluído.")


def mostrar_relatorio(pacientes):
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado!!!")
    else:
        print("Relatório")

        for paciente in pacientes:
            print(f"Nome: {paciente["nome"]}")
            print(f"Idade: {paciente["idade"]}")
            print(f"Tipo de Atendimento: {paciente["tipo_atendimento"]}")
            print(f"Quantidade de Atendimentos: {paciente["quantidade_atendimento"]}")
            print(f"Forma de Pagamento: {paciente["forma_pagamento"]}")

def menu():
    while True:
        print("______MENU______")
        print(" 1 - Cadastrar Paciente")
        print(" 2 - mostrar relatório final ")
        print(" 3 - Sair")
        op = int(input("escolha uma opção: "))

        if op == 1:
            paciente = cadastrar_paciente()
            pacientes.append(paciente)

        elif op == 2:
            mostrar_relatorio(pacientes)

        elif op == 3:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

carregar_paciente_arquivo() 
menu()