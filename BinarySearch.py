def binary_search(lista:list, inicio:int, fim:int, item_procurado:int):
    if inicio >= fim:
        return -1
    else:
        posicao_meio = (inicio + fim) // 2
        if item_procurado == lista[posicao_meio]:
                return posicao_meio
        elif item_procurado < lista[posicao_meio]:
            return binary_search(lista, inicio, posicao_meio - 1, item_procurado)
        else:
            return binary_search(lista, posicao_meio + 1, fim, item_procurado)
