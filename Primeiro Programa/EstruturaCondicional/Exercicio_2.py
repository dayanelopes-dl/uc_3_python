# Arvore de decisão
print("## PROGRAMA DE EMPRESTIMO ##\n")
print("Responda: 0 - NÃO e 1 - SIM\n")

negativado = int(input("Voce possui nome negativado? "))

if negativado == 1:
    print("não pode realizar emprestimo")
else:
    clt = int(input("Possui Carteira Assinada? "))
    if clt == 0:
        print("não pode realizar emprestimo")
    else:
        casa = int(input("possui casa propria? "))
    if casa == 0:
        print("Não pode realizar emprestimo")
    else:
        print("conceder Emprestimo")
