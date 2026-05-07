''' ELABORE UM ALGORITIMO PARA DIAGNOSTICAR GRIPE COMUM
USE AS SEGUINTES FATORES:
SINTOMAS -> FEBRE MODERADA, NARIZ ENTUPIDO, DOR DE GARGANTA,
TOSSE, DURAÇÃO DOS SINTOMAS -> MENOR QUE 7 DIAS, MAIOR QUE 7 DIAS
CLASSIFICAÇÃO: PROVAVEL DE GRIPECOMUM OU SINTOMAS ATIPICOS, INVESTIGAR
OUTRAS CONDIÇOES'''

print(" ###Sistema de Pre- diagnostico###")
print("Informe seu sintomas com opçoes abaixo com S/N")

nariz_entupido = input(" esta com nariz entupido? (s/n): ")
febre_moderada = input(" esta com febre? (s/n): ")
dor_na_garganta = input("esta com dor de garganta? (s/n): ")
tosse = input(" esta com tossse? (s/n): ")

duracao = int(input(" Há quantos dias esta sentindo esses sintomas?"))

tem_sintomas = (nariz_entupido == 's' or dor_na_garganta == 's' or
tosse == 's' or febre_moderada == 's') 

if tem_sintomas and duracao < 7:
    print("\n Classificação: PROVAVEL GRIPE COMUM ou Sintomas Atipicos")
    
    
else:
    print("\n Classificação:nao gripado")
    exit()
