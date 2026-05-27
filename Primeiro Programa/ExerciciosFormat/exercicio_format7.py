'''uma imobiliaria para aos corretores um salario base de 1.500,00. alem disso, uma comissao de R$ 200,00
por cada imovel vendido e 5% do valor de cada venda. construa um programa que solicite o nome do corretor, 
a quantidade de imoveis vendidos e o valor total de suas vendas. ao fim, o programa deve calcular e escrever
o salario final do corretor de imoveis.'''

salario_base = 1500.00 
comissao = 200

corretor = input("digite o nome do corredor: ")
print("seu salario é: ", salario_base)
vendas = int(input("Digite a quantidade de vendas: "))
total_vendas = float(input("informe o valor total de vendas R$: "))

sal_final = salario_base + ( comissao * vendas) + (total_vendas * 0.05)

print(f"Salario final do corretor {corretor}  é de R$: {sal_final:.2f}")