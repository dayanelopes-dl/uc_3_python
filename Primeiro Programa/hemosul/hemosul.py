# sistema de triagem da Hemosul

# inicio
doadores = []


def cadastro():
    try:
        while True:
            documento = int(
                input("Possui documento oficial com foto? (1 -s / 2- n): "))
            if documento == 2:
                print(
                    "não pode doar: É obrigatório apresentar documento oficial com foto.")
                break

            peso = float(input("Digite o seu peso (kg): "))
            if peso < 51:
                print("não pode doar: Peso mínimo 51kg")
                break

            idade = int(input("Digite a sua idade (anos): "))
            if idade < 16 or idade > 69:
                print("não pode doar: A idade deve estar entre 16 e 69 anos.")
                break

            elif idade in [16, 17]:

                if input("Está acompanhado e autorizado pelo responsável legal? ( s/n): ").lower() != 's':
                    print(
                        "não pode doar: Menores de 16 e 17 anos precisam de acompanhamento e autorização.")
                    break

            if input("Está em boas condições de saúde (sem gripe ou infecção)? (s/n): ").lower() != 's':
                print("nao pode doar: Deve estar em boas condições de saúde.")
                break

            if input("Está devidamente descansado e alimentado? (s/n): ").lower() != 's':
                print("nao pode doar: Deve estar descansado e alimentado.")
                break
            else:
                menu()
                break

    except ValueError:
        print("erro. apenas documento, peso e idade apenas valores numericos")


def Triagem(cadastro):
    try:
        hepatite = input("Já teve Hepatite apos 11 anos (s/n): ")
        doencas = input("Doença de Chagas,Cancer, Sifilis ou HIV? (s/n): ")
        drogas = input("Já fez uso de drogas injetaveis ou ilicitas?(s/n): ")

        if doencas == "sim" and drogas == "sim" and hepatite == "sim":
            print("Não pode doar sangue")
    except ValueError:
        print("erro, digite apenas sim ou nao!")


# parte do menu


def apsvacinacao():
    vacinas = ("anterrábica = 1 ano,\n antitetânica / Gripe (Influenza) / Hepatite A e B / HPV = 48hrs,\n rubéola/sarampo / Varicela / BCG / Febre amarela / Dengue / Monkeypox = 1 mes, \nCovid-19 -Pfizer = 7 dias\n")
    op1 = int(input("vc tomou vacina recentimente? (em 1 ano) (1 - S/ 2 - N): "))
    if op1 == "1":
        print(f"se for algumas dessas abaixo:{vacinas}")
    else:
        print("podera doar normalmente!")


# recomendaçoes
def recomendacoes():
    print("----Recomendações!----")
    print("- Não engerir bebidas por 12 hrs ate o horario da doação")
    print("- não fumar por 2 hrs ")
    print("- esteja bem alimentado\n (evite alimentos gordurosos no dia anterior à doação!)")
    print("- igerir bastante água!\n (3 copos de água antes da doação)")
    print("- caso obtenha crianças (menores 12 anos),estejam acompanhados de um outro responsavel.")


def menu():
    try:

            print("Bem Vindo ao HEMOSUL")
            print("-"*30)
            print("Critérios  basicos para doação de sangue ")
            print("1 -  cadastro inicial ")
            print("2 - triagem só apos cadastro inicial")
            print("3 - Aguardar após vacinação ")
            print("4 - Recomendação ")
            print(" 5 - sair")
            op = int(input("Escolha uma opção que deseja:"))
            if op == 1:
                doadores = cadastro()
            elif op == 2:
                doadores = Triagem()
            elif op == 3:
                doadores = apsvacinacao()
            elif op == 4:
                doadores = recomendacoes()
            elif op == 5:
                print("encerrando programa")
        
            
    except ValueError:
        print("erro. apenas numeros")
    finally:
        ("fim do programa")

menu()
