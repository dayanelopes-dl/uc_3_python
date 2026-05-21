def v_primo (n): #parametro(n) , (v_primo=> nome função)
    test = 1

    for i in range(2, n): #(2) é inicio, (n)fim.
       if n % i == 0:
        test = test + 1

    if test != 1:
        print(" não é primo")
    else:
        print(" é primo")
    
#num = 13
#print(v_primo(num)) 
v_primo(7)     # numero do parametro