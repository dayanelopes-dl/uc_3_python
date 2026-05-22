# Operaçoes com bool

a = [ 1,2, 3]
b = [1, 2, 3]

print( a == b) # True
c = a
# o (IS) compara endereçamento na memoria
print(a is b) # false aqui nao esta , por que nao esta atribuindo a nada
print(a is c) #True por que esta atribuindo 

# o id pra descobrir o numero de identificação na memoria
print(id(a))
print(id(b))
print(id(c))