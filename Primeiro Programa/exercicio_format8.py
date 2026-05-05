copo1 = "laranja"
copo2 = "acerola"

print("Antes da troca")
print(f"Copo 1 tem {copo1}")
print(f"Copo 2 tem {copo2}")

#copo3 = copo1 
#copo1 = copo2
#copo2 = copo3 

copo1, copo2 = copo2, copo1 

print("\nDepois da troca")
print(f"Copo 1 tem {copo1}")
print(f"Copo2 tem {copo2}")
