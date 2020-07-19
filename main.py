from time import time
from ListaRandomica import lista_randomica
from LinearSearch import linear_search
from BinarySearch import binary_search


def demonstracao(lista:list, nome_algoritmo:str, algoritmo, item_procurado:int, builtin=False):
    print('Começando a busca através do método ' + nome_algoritmo + '...')
    tempo = time()
    try:
        posicao = algoritmo(lista, 0, len(lista), item_procurado) if not builtin else lista.index(item_procurado)
    except ValueError:
        posicao = -1
    tempo = time() - tempo
    print(f'Item localizado na {posicao + 1}ª posição.') if posicao >= 0 else print('Item não localizado.')
    print(f'Tempo gasto: {tempo:.5f} segundos\n')


if __name__ == '__main__':
    # lista = [8, 10, 1, 4, 2, 5, 9, 7, 6, 3]
    lista = lista_randomica(10001, 10001, True)

    print('Lista:', lista, '\n')

    demonstracao(sorted(lista[:]), 'built-in index', None, 10001, True)
    demonstracao(sorted(lista[:]), 'linear search', linear_search, 10001)
    demonstracao(sorted(lista[:]), 'binary search', binary_search, 10001)