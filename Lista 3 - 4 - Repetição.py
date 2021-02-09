n = int(input("Digite um número inteiro: "))

ant = n % 10
n = n // 10
aux = 0

while n > 0:
    atual = n % 10
    if atual == ant:
        aux += 1
        break
    n = n // 10
    ant = atual
        
if aux == 0:
    print("não")
else:
    print("sim")
    
