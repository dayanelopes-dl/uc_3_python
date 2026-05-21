def soma (a, b):
    soma = a + b
    return

def subtracao (a, b):
    subtracao = a - b 
    return subtracao

def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

def divisao(a, b):
    divisao = a / b
    return divisao

def menu():
    
    print("Calculadora")
    print(" 1 - Soma ")
    print(" 2 - Subtração ")
    print(" 3 - Multiplicação")
    print(" 4 - Divisão")
    try:
         op = int(input("Informe a operação: "))
         a = float(input("Informe o 1º numero: "))
         b = float(input("Informe o 2º Numero: "))
         if op == 1:
          print(soma(a, b))
         elif op == 2:
          print(subtracao(a, b))
         elif op == 3:
          print(multiplicacao(a, b))
         elif op == 4:
          print(divisao(a, b))
         else:
          print("Opção incorreta!!!")
    except:
     print("dados incorretos. apenas valores numericos!")
    finally:
      print("finalizado")
menu()