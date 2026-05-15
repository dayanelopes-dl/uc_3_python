import random
print("### SISTEMA DE SORTEIO ###")
print("-"*30)

nomes = []
while True:
    nome = input("Digite um Nome: ")
    nomes.append(nome)  #coloca na lista
    
    op = input("Deseja continuar[S][N]? ")
    if op.upper() == "N":  #upper entende maiusculo e minusculo
        break
print(nomes)
print("-"*30)

random.shuffle(nomes)   #muda posiçoes(embaralha dados)
#print(f"Lista Embaralhada: {nomes} ") #se nao quiser aparecer, so nao fazer o (print) da lista embaralhada.
sorteio = random.choice(nomes) #choice sorteia um (dado)
print(f"nome do sortudo é: {sorteio}")
print("-"*30)
while True:
    sorteio_2 = input("Realizar outro sorteio? s/n: ")
    if sorteio_2 == "s":
        nomes.remove(sorteio)
        print(nomes)
        sorteio = random.choice(nomes)
        prin(f"o nome sortudo é: {sorteio}")
    else:
        print("Fim do sorteio")
        break