def quicksort(lista, inicio=0, fim=None, copia=True):

    def _partition(lista, inicio, fim):
        pivo = lista[fim]
        barra_verde = inicio

        for barra_vermelha in range(inicio, fim): 

            if lista[barra_vermelha] <= pivo:
                lista[barra_vermelha], lista[barra_verde] = lista[barra_verde], lista[barra_vermelha] 
                barra_verde = barra_verde + 1
                
        lista[barra_verde], lista[fim] = lista[fim], lista[barra_verde]
        return barra_verde

    if copia:
        lista = lista.copy() 
    
    if fim is None:
        fim = len(lista)-1

    if inicio < fim:
        p = _partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1, copia=False)
        quicksort(lista, p+1, fim, copia=False)
    
    if copia:
        return lista


def bubble_sort(lista):
    lista = lista.copy()
    size = len(lista)
    for j in range(size-1):
        for i in range(size-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


def selection_sort(lista):
    lista = lista.copy()
    size = len(lista)
    for j in range(size-1):
        min_index = j
        for i in range(j, size):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    return lista