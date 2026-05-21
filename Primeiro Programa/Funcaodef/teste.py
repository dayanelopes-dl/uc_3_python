hospede = {}


def cadastrar_hospede():
    try:
        hospede["nome"] = input("Informe o nome do hóspede: ")
        hospede["idade"] = int(input("Informe a idade: "))
        hospede["cpf"] = input("Informe o CPF (11 dígitos): ")
    
        

        print("Tipos de quarto:")
        print("1 - Standard R$120")
        print("2 - Luxo R$250")
        print("3 - Premium R$400")
        
        opcao_quarto = input("Escolha o tipo de quarto: ")

        tipos = {
            "1": "standard",
            "2": "luxo",
            "3": "premium"
        }

        if opcao_quarto not in tipos:
            print("Opção inválida.")
            return

        hospede["tipo de quarto"] = tipos[opcao_quarto]

        hospede["quantidade de diarias"] = int(
            input("Informe a quantidade de diárias: ")
        )

        return hospede

    except ValueError:
        print("Erro: por favor, insira valores válidos.")
        return



def calcular_valor_hospedagem(hospede):
    valores = {
        "standard": 120,
        "luxo": 250,
        "premium": 400
    }

    tipo_quarto = hospede["tipo de quarto"]
    quantidade_diarias = hospede["quantidade de diarias"]

    valor_total = valores[tipo_quarto] * quantidade_diarias
    return valor_total


def verificar_situacao_quarto(valor_total):
    if valor_total <= 500:
        return "Econômico"
    elif valor_total <= 1500:
        return "Intermediário"
    else:
        return "Premium"




def menu():
    print(" SISTEMA DE CONTROLE DE HÓSPEDES ")
    print("-" * 30)

    while True:
        print("MENU")
        print("1 - Cadastrar hóspede")
        print("2 - Ver quartos disponíveis")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            hospede = cadastrar_hospede()

            if hospede:
                valor_total = calcular_valor_hospedagem(hospede)
                situacao = verificar_situacao_quarto(valor_total)
                print("-"*30)

                print(" DADOS DA HOSPEDAGEM ")
                print(f"Nome: {hospede['nome']}")
                print(f"Quarto: {hospede['tipo de quarto'].title()}")
                print(f"Diárias: {hospede['quantidade de diarias']}")
                print(f"Valor total: R$ {valor_total:.2f}")
                print(f"Categoria: {situacao}")
                print("-"*30)

        elif opcao == "2":
            print("-"*30)
            print("Quartos disponíveis:")
            print("1 - Standard - R$ 120")
            print("2 - Luxo - R$ 250")
            print("3 - Premium - R$ 400")
            print("-"*30)

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")



menu()