def é_primo(n):
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
            if(divisores > 2):
                break
        i +=1

    if divisores == 2:
        return 1
    else:
        return 0

def n_primos(n):
    quant = 0
    i = 2
    while i <= n:
        if é_primo(i):
            quant += 1
        i += 1
    return quant
        
    
