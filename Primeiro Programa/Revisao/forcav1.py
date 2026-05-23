print("-" * 20)
print('*'*5, 'bem vindo ao Jogo da forca', '*'*5)
print("-" * 20)

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False

while (not acertou and not enforcou):
    chute = input("Digite uma letra:\n ")
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):

                # print("Encontrei a letra {} na posição {}".format(letra, posicao))
                letras_acertadas[posicao] = letra

            posicao = posicao + 1
    else:
        erros = erros + 1

    enforcou = erros == 5
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print("Parabens, voce ganhou!!!")
else:
    print("Voce perdeu!!!")

print("Fim de jogo")
