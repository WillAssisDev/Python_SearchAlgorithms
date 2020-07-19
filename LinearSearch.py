def linear_search(lista:list, inicio:int, fim:int, item_procurado:int):
    for indice in range(inicio, fim):
        if lista[indice] == item_procurado:
            return indice
    return -1
