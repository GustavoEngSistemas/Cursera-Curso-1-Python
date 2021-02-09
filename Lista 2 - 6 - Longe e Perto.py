x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

distancia = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

if distancia >= 10:
    print("longe")
else:
    print("perto")

