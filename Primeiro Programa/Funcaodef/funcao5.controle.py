# controle de hospede
# cadastro de hospede - nome - idade - cpf - tipo de quarto - quantidade de diarias
# reserva de quartos
# quantidade de diarias
# valor da hospedagem
# disponibilidade de quartos
# quarto/ valor - standard - 120 - luxo - 250 - premium - 400
# quantidade de diarias - situação  do quarto - ate R$ 500 - economico - R$501 ate 1500 - intermediario - acima 1500 - premium

hospede = {}


def cadastrar_hospede():
    try:

        hospede["nome"] = input("Informe o nome do hospede: ")
        hospede["idade"] = int(input("informe a idade: "))
        hospede["Cpf"] = input("Informe o CPF: ")
        hospede["tipo de quarto"] = input("Informe o tipo de quarto: ")
        hospede["quantidade de diarias"] = int(
            input("Informe a quantidade de diarias: "))
        return hospede
    except ValueError:
        print("Erro: por favor, insira valores válidos.")
        return None


def calcular_valor_hospedagem(hospede):
    tipo_quarto = hospede["tipo de quarto"].lower()
    quantidade_diarias = hospede["quantidade de diarias"]

    if tipo_quarto == "standard":
        valor_diaria = 120
    elif tipo_quarto == "luxo":
        valor_diaria = 250
    elif tipo_quarto == "premium":
        valor_diaria = 400
    else:
        print("Tipo de quarto inválido.")
        return None

    valor_total = valor_diaria * quantidade_diarias
    return valor_total


def verificar_situacao_quarto(valor_total):
    if valor_total <= 500:
        return "Econômico"
    elif 501 <= valor_total <= 1500:
        return "Intermediário"
    else:
        return "Premium"


def menu():
    print("Bem-vindo ao sistema de controle de hóspedes!")
    print("1. Cadastrar hóspede")
    print("2. Ver quartos disponíveis")
    print("3. Sair")
    while True:
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            hospede = cadastrar_hospede()
            if hospede:
                valor_total = calcular_valor_hospedagem(hospede)
                if valor_total is not None:
                    situacao_quarto = verificar_situacao_quarto(valor_total)
                    print(f"Valor total da hospedagem: R$ {valor_total:.2f}")
                    print(f"Situação do quarto: {situacao_quarto}")
        elif opcao == "2":
            print("Quartos disponíveis: Standard, Luxo, Premium")
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    menu()
