largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = j = 0

while i < altura:
    while j < largura:
        if i == 0 or i == altura-1 or j == 0 or j == largura -1:
            print("#", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
    j = 0