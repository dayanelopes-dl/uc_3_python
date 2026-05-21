#palavra = "PARALELEPIPEDO" #(1)
#print(palavra[3:7]) #intervalo em Lista ([]) <- posição
#print(palavra[2:5:10])

#frutas = ["Laranja", "Maça", "Goiaba","Pera"]   #lista em [] contagem em 0 <- posição (2)
#frutas = frutas + ["Uva","Abacaxi","Morango","Banana","Kiwi"]
#imprimi varias entre (numero e : vai ate o ultimo numero)
#print(frutas)

#frutas[7] = "Banana da Terra" #substituição de itens por posição
#frutas.remove("Uva")
#print(len(frutas)) #LEN serve para Contar os itens na lista...
#print(frutas[3:6]) 
#print(frutas)

numeros = [1, 2, 3, 4, 5] #listas (3)
#print(numeros)
#numeros[1] = numeros[3] + numeros[2]
print(numeros)
numeros.append(6) #adiciona apenas um valor só (APPEND)
print(numeros)
numeros.extend(["Laranja","Maça","Uva"]) #adiciona 1 ou mais valores (EXTEND)
print(numeros)
numeros.insert(2, "casa") #informando a posição conseguimos adiciona a informação , adicona apenas um item. especifica
print(numeros)
numeros.remove("Laranja")
print(numeros) 
numeros.pop(5)  #consegue remover pelos indice
print(numeros)