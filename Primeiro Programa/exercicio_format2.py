'''Construa um programa que receba do usuário a variação do
deslocamento de um objeto (em metros) e a variação do tempo
percorrido (em segundo). Ao fim, o programa deve calcular a
velocidade média, em m/s, do objeto. Vm = delta S / delta T'''

delta_s = float(input("Digite o deslocamento (em metros): "))
delta_t = float(input("Digite o tempo (em segundos): "))
velocidade = delta_s / delta_t
print(f"Vm = {velocidade:.2f} m/s")