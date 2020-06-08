#Estrategia divide y venceras

"""
21 10 12 0 34 15    seleccionamos pibote ||La eficiencia depende del pibote que escojas
P  i           d    i->izquierdo d->derecho

15 10 12 0 34 21
p   i       d

15 10 12 0 34 21
P      i d

0 10 12 15 34 21    en teoria deberia estar asi, pero no podemos tener un crece
P     d i           asi que dividimos en dos grupos

0 10 12     15 34 21 
p  i  d     p   i  d

"""
def quicksort(lista):
    quicksort_2(lista,0,len(lista)-1)


def quicksort_2(lista, inicio, fin):
    if inicio < fin:

        pivote = particion(lista, inicio, fin)

        quicksort_2(lista, inicio, pivote-1)
        quicksort_2(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    pivote = lista[inicio]
    #print("Valor del pivote {}".format(pivote))
    izquierda = inicio+1
    derecha = fin
    #print("Indice izquierdo {} e indice derecho {}".format(izquierda, derecha))

    bandera = False             #las banderas nos indican si ya terminamos
    while not bandera:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while derecha >= izquierda and lista[derecha] >= pivote:
            derecha = derecha -1
        if derecha < izquierda:
            bandera = True
        else: 
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp

    #print(lista)

    temp = lista [inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp
    return derecha

lista=[21, 10, 12, 0, 11, 9, 24, 20, 14, 1]
#print(lista)
#quicksort(lista)
#print("LISTA ORDENADA {}".format(lista))
