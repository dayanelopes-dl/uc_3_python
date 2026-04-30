# LOJA DE ROUPAS DE CAMISAS

camisa = 12.50
quantidade = int(input("Digite Quantas camisas voce deseja? "))
valorfinal = camisa * quantidade
if quantidade <= 5:
    valordesconto = valorfinal * 0.03 
    valorfinal = valorfinal - valordesconto                  
elif quantidade <= 10:
    valordesconto = valorfinal * 0.05
    alorfinal = valorfinal - valordesconto    
else:
    valordesconto = valorfinal * 0.07
    valorfinal = valorfinal - valordesconto
    
    

print(f"Valor final: R$  {valordesconto:.2f}")
   