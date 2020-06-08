import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random 
from time import time
from ejercicio5 import inserSort
from ejercicio6 import  quicksort

datos = [ii*100 for ii in range(1,21)]

tiempo_is = []
tiempo_qs = []

for ii in datos:
    lista_is = random.sample(range(0, 10000000), ii)
    lista_qs = lista_is.copy()

    t0 = time()
    inserSort(lista_is)
    tiempo_is.append(round(time()-t0,6)) #lista de tiempos que vamos a obtener

    t0 = time()
    quicksort(lista_qs)
    tiempo_qs.append(round(time()-t0,6))

print("Tiempos parciales de ejecución en insertsort {} [s]".format(tiempo_is))
print("Tiempos parciales de ejecución en quicksort {} [s]".format(tiempo_qs))

fig, ax = plt.subplots()
ax.plot(datos, tiempo_is, label="inser sort", marker= "*", color="r")
ax.plot(datos, tiempo_qs, label="quick sort", marker= "*", color="b")

ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)


plt.title("Tiempos de ejecucion [s] inser sort vs quicksort")
plt.show()
    
