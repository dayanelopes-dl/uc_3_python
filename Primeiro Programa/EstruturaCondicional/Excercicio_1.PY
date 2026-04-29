#estrutura IF e ELSE
nota1 = float(input("digite a 1º nota: "))
nota2 = float(input("digite a 2º nota: "))
media = (nota1 + nota2) / 2

if media >= 60:   #SEMPRE EM IF E ELSE E ELIF NO FINAL( : )
    print("APROVADO")
elif media >= 30 and media <= 59:
    print("EXAME FINAL")
else:
    print("REPROVADO")   
