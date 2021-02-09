
def verifica_primo(n):
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
        i +=1

    if divisores == 2:
        return 1
    else:
        return 0

def maior_primo(x):
    maior = 0
    while x >= 2:
        if verifica_primo(x) and x > maior:
            maior = x
        x -= 1

    return maior
