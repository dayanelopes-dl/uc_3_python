# cadastro de produto
# nome do produto - categoria - quantidade de estoque - preço
# relatorio
# categoria - quantidade - preço - situação do estoque - situaçao do estoque( quantidade > 10 é BOM)
# ( > 5  < 10 = medio - < 5 = baixo)

def cadastrar_produto():
    try:
        produto = {}

        produto["nome"] = input("Informe o nome do produto: ")
        produto["categoria"] = input("Informe a categoria: ")
        produto["quantidade"] = int(input("Informe a quantidade de ESTOQUE: "))
        produto["preco"] = float(input("Informe o preço: "))
        return produto

    except ValueError:
        print("erro. qauantidade e preco devem ser numericos")

    finally:
        print("produto finalizado")


def menu():
    produtos = []

    while True:
        print("______MENU______")
        print(" 1 - Cadastrar produto")
        print(" 2 - mostrar relatório")
        print(" 3 - Sair")
        op = int(input("escolha uma opção: "))

        if op == 1:
            produto = cadastrar_produto()
            produtos.append(produto)

        elif op == 2:
            mostrar_relatorio(produtos)

        elif op == 3:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")


def mostrar_relatorio(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado")
    else:
        print("RELATORIO")
    for produto in produtos:
        print(f"Produto: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")

        if produto["quantidade"] > 10:
            print(f"Situação do estoque: 'BOM' ")
            print("-"*30)
        elif produto["quantidade"] > 5:
            print(f"Sitação do estoque: 'MEDIO' ")
            print("-"*30)
        else:
            print(f"Situacao do estoque: 'BAIXO' ")
            print("-"*30)

    return mostrar_relatorio


menu()
