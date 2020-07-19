from random import randint

def lista_randomica(quantidade: int, tamanho_maximo: int = 1000, exclusivos: bool = False):
    if exclusivos:
        lista = []
        for n in range(0, quantidade):
            numero = randint(0, tamanho_maximo)
            while numero in lista:
                numero = randint(0, tamanho_maximo)
            lista.append(numero)
    else:
        lista = [randint(0, tamanho_maximo) for n in range(0, quantidade + 1)]
    return lista