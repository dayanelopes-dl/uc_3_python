import random
n = [2, 4, 7, 1, 3, 5, 6]
n.sort() #ordenação crescente
print(n)
#n.sort(reverse=True)
n.reverse()#ordenação decrescente
print(n)

copia =list(n)
print(n)
print(copia)

n.clear() #limpa lista
print(n)
