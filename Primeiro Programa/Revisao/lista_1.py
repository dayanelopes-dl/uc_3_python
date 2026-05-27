meses = ['jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez']



while True:
    num = int(input("Digite um numero: "))

    if 1 <= num <= 12:
        mes_escolhido = meses[num - 1]
        
        num_invertido = mes_escolhido[::-1]

        print("O mes escolhido é: {}" .format(len(mes_escolhido)))
        print("de tras para frente: {}" .format(num_invertido))
    else:
        print("Numero invalido, tente novamente")
    





