
# ax² + bx + c = 0 EQUAÇÃO DE 2° GRAU
# B**2 , POW(B,2)
from math import sqrt

a = int(input("INFORME O VALOR DE a:"))
b = int(input("INFORME O VALOR DE b:"))
c = int(input("INFORME O VALOR DE c:"))

#calculo do DELTA
delta = b**2 - 4 * a * c

if delta < 0:
    print("não existem raizes.")
elif delta == 0:
 x = -b / (2 * a)
 print(f"x1 = x2 = {x:.2f}")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)  
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f" As raizes reais de x1 são: {x1:.2f}")
    print(f" As raizes reais de x2 são: {x2:.2f}")