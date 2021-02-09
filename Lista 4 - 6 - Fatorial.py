while True:
    n = int(input("Digite um valor: "))
    if n < 0:
        exit() 
    fat = 1
    print(f"{n}! = ", end=" ")
    while n >= 1:
        fat *= n
        if n != 1:
            print(n, end=" x ")
        else:
            print(n, end = " ")
        n -= 1
    print(f"= {fat}")
    