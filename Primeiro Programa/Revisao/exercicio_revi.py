
distancia = float(input("Informe a distancia: "))
urgente = int(input("Sua entrega é urgente? 1 - SIM, 0 - NÃO: "))

if urgente == 1:
    print("prioritaria")
elif distancia > 300:
    print("Entrega longa")
else:
    print("Entrega Padrão")
