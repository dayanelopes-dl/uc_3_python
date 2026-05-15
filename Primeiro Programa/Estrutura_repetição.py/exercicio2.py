'''CONSTRUA UM ALGORITIMO QUE RECEBA O NOME E O PREÇO DE 5 MEDICAMENTOS DE UMA
DROGARIA.
O PROGRMA DEVE INFORMAR O NOME E O PREÇO DO MEDICAMENTO MAIS BARATO,
BEM COMO A MEDIA ARITIMETICA DOS PREÇOS INFORMADOS '''


   
media_preco = 0
   
medicamento = input("informe o medicamento: ") 
preco = float(input("informe o preço: "))
nome_medicamento = medicamento
menor_preco = preco
media_preco = media_preco + preco
   
   
   
for b in range (4):
    medicamento = input("Informe o nome do medicamento: ")
    preco = float(input("Informe o preço: "))
    
    if preco < menor_preco:
        menor_preco = preco
        nome_medicamento = medicamento
        media_preco = media_preco + preco
        
media = media_preco / 5
print(f"O {nome_medicamento} é o medicamento mais barato, custa R${menor_preco}")
print(f"media dos preços é: {media}")    