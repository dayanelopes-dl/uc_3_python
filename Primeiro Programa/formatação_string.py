'''Quando trabalhamos com strings, é bastante comum querermos formatá-las e, para isso, Python oferece
diversas maneiras, tais como os marcadores de posição %, o
método format() e a classe Template.'''

from datetime import datetime #Biblioteca de tempo
ano_atual = datetime.now().year #Metodo para obter o ano atual
clube = "CORINTHIANS"
campeonato_mundial = 1
ano_fundacao = 1910
print(f"{clube} possui {campeonato_mundial} títulos mundiais." f" São {ano_atual - ano_fundacao} anos de existência.")

print(f"Matricula: {1003:06d}") #:06d diz “Exiba um número inteiro com 6 dígitos. Se ele possuir menos de 6 dígitos,
#preencha com zeros à esquerda até deixá-lo com 6 dígitos.”

print(f"Valor de pi é: {3.14159265352384626433}.")
'''Observe que o valor informado possui 20 casas decimais, no entanto, ao executar esse comando, Python fará o
truncamento para 16 casas decimais. E se você desejasse trabalhar, realmente, com a precisão de 20 casas decimais? Como
faria? Bastaria informar que deseja utilizar um valor com ponto
flutuante e a quantidade de casas decimais.'''
print(f"Valor de pi é: {3.14159265352384626433:.20f}.")