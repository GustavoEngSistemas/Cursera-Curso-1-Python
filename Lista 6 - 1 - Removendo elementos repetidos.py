def remove_repetidos(lista):
    lista_limpa = []
    for elemento in lista:
        if elemento not in lista_limpa:
            lista_limpa.append(elemento)
            
    return sorted(lista_limpa)
