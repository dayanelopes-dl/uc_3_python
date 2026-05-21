
print("-" *20)
print("Informe  os dados para calclular a prioridade de Entrega ")
print("Resposta 1 para SIM ou 2 para NÃO:")
urgente =int(input(" a ENTREGA É URGENTE: "))
distancia = float(input(" A ENTREGA É LONGA DISTANCIA? DIGITE O VALOR DA DISTANCIA:"))

if urgente == 1:
    print("então a entrega é prioritaria")
elif distancia > 300:
    print("Distancia longa")
else:
    print("entrega padrao")
    



