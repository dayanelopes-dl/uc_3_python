try:  #tente executar esse codigo
     numero = int(input("Digite um numero: "))

     print(numero)

except: # Execute esse codigo
    print("Voce digitou um valor invalido")

finally:   #faz mais sentido para banco de dados
    print("vou sempre executar!")