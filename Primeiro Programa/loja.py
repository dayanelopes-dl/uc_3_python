
print("sistema de km percorrido")
print("-" * 20)

quantidade = int(input(" qual a quantidade km percorrido: "))

if quantidade > 1000:
    print("viagem longa")
elif quantidade >= 300 and quantidade <= 1000:
    print("viagem media")
else:
    print("viagem curta")

print("-"*20)
    
carga = input(" carga fragil, s / n?\n ")
if carga == "s":
    print("transporte especial")
else:
    print("sem transporte especial")