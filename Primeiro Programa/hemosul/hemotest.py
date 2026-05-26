vacinas = {"anterrábica",
"antitetânica",
"Gripe (Influenza)",
"Hepatite A e B",
"HPV",
"rubéola",
"sarampo",
"Varicela",
"BCG",
"Febre amarela",
"Dengue",
"Monkeypox",
"Covid",
"Pfizer"}

for x in vacinas:
    op=input(f"Você teve {x}(s/n)").upper()

    if op == "S":
        print ("aguarde o intervalo recomendado!")
        break
    else:
        print("podera doar normalmente!")
        break