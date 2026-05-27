try:  # tente executar esse codigo
    numero = int(input("Digite um numero: "))

    print(numero)

except:  # Execute esse codigo
    print("Voce digitou um valor invalido")

finally:  # faz mais sentido para banco de dados, fim do bloco
    print("vou sempre executar!")
    # utilizado apenas para o usuario
