"""
Dar cambio con cierto numero de monedas
una vez probado el candidato, no lo volvemos
 a usar

solucion con algoritmo greedy o voraz
"""
def cambio(cantidad,monedas):
    resultado= []
    while cantidad>0:
        if cantidad >= monedas[0]:
            num = cantidad // monedas[0]
            cantidad = cantidad - (num*monedas[0])
            resultado.append([monedas[0], num])
        monedas = monedas[1:]
    return resultado

if __name__ =="__main__":
    print(cambio(1000, [20,10,5,2,1]))
    print(cambio(20, [20,10,5,2,1]))
    print(cambio(30, [20,10,5,2,1]))
    print(cambio(98, [5,20,1,50]))
    #la solucion que arroja no es la cantidad eficiente

