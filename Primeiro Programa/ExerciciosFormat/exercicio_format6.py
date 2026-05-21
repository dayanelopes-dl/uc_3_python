'''Implante um programa que converta o valor de uma velocidade 
media em km/h para m/s.
Para isso, o usuario deve informar o valor da velocidade media. sabe - se que  o fator utilizado para 
essa conversao é 3,6'''

vel_km= float(input("Informe o valor da velocidade media (km/h): "))
vel_m = vel_km /3.6
print(f"{vel_km:.2f} km/h equivalente a {vel_m:.2f}")
