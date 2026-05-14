"""CRIE UM PROGRAMA NO QUAL O USUARIO INFORME 2 NUMEROS INTEIROS: AE B.
PARA QUE O PROGRAMA CONTINUE SUA EXECUÇÃO, VERIFIQUE SE A < B.
SE SIM, CALCULE A SOMA DOS NUMEROS INTEIROS NO INTERVALO [A,B].
CASO CONTRARIO, INFORME UMA MENSAGEM DE ERRO."""

a = int(input("Informe um numero: "))
b = int(input("Informe outro numero: "))

if a < b: 
    soma = 0
    for x in range(a, b  + 1):   #esta formula so funcio se a <(menor) que b, se for maior não funciona.
        soma = soma + x
    print(f"Soma dos inteiros no intervalos de {a} e {b} é: {soma}")
else:
    print("Erro. a deve ser menor que B.")