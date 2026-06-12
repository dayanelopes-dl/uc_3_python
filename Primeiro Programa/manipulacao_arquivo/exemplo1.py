abrindo_arquivo = open('C:/Users/vboxuser/Documents/primeiro_arquivo.txt','w') #aqui criei um arquivo 

abrindo_arquivo.write('numeros pares de 1 a 100\n') 
for i in range(1, 101):
    if i % 2 ==0:
        abrindo_arquivo.write(f'{i}\n')

abrindo_arquivo.close() # aqui fechei um arquivo 

abertura = open('C:/Users/vboxuser/Documents/primeiro_arquivo.txt','r') # modo leitura
print(abertura.readlines())
abertura.close()