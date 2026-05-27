'''Construa um programa para calcular a área de convivência
de uma escola cujo formato é circular. Para isso, o usuário deve
informar o valor do raio.'''

from math import pi
raio = float(input("Digite o raio da área: "))
area = pi * raio ** 2 # mesmo que area = pi * pow(raio, 2)
print(f"Área = {area:.2f}.")