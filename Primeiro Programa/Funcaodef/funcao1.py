def somatoria (*argumento):   # BLOCO SOMATORIA
    soma = 0
    for i in argumento:
        soma += i
    return soma
print(somatoria(1,2,3,4,5))