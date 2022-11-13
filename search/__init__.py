def binary_search(lista, item, inicio=0, fim=None, copy=True):
    if copy:
        lista = lista.copy()

    if fim is None:
        fim = len(lista)-1

    if inicio <= fim:
        m = (inicio + fim)//2
        if lista[m] == item:
            return m
        if item < lista[m]:
            return binary_search(lista, item, inicio, m-1, copy=False)
        else:
            return binary_search(lista, item, m+1, fim, copy=False)
    return None


def sequential_search(lista,item):
    lista = lista.copy()
    for i in lista:
        if i == item:
            return lista.index(i)
    return None