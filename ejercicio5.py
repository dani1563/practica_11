#Estrategia incremental
#Algoritmo de ordenacion por inserción 

"""
21 10 12 0 34 15 numeros a ordenar
Parte ordenada
Partimos de la idea de que ya está ordenado el primero 

21                  10 12 34 15  10<21 SI
10 21               12 0 33 15   12<10 NO 12<21 SI
10 12 21            0 34 15
0 10 12 21          34 15
0 10 12 21 34       15
0 10 12 15 21 34
"""
def inserSort(lista):
    for index in range(1, len(lista)): #(n-1)
        actual = lista[index]
        posicion = index
        #print("Valor a ordenar {}".format(actual))
        while posicion>0 and lista[posicion-1]>actual: #(n^2)
            lista[posicion] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
        #print(lista)
        #print()
    return lista

lista= [21,10,12,0,34,15]
#print(lista)
#inserSort(lista)
#print(lista)

"""
ordenamiento por fuerza bruta, burbuja
divide y venceras, merge
quicksort- divide el problema en dos, aprte los datos y mueve los que se encuentran
en la posicion incorrecta respecto al pibote
"""