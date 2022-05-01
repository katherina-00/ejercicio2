import csv
import menu
from ViajeroFrecuente import ViajeroFrecuente

if __name__=="__main__":

    viajeros = []

    with open("viajeros.csv","r") as file:
        reader=csv.reader(file,delimiter=",")
        for fila in reader:
            viajeros.append(ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3], int(fila[4])))

    numViajero=int(input("Ingrese numero de viajero: "))
    op=menu.muestraMenu()

    while op!=4:

        if op==1:
            ViajeroFrecuente.muestraMillas(viajeros[numViajero-1])

        elif op==2:
            aux=int(input("Ingrese cantidad de millas a acumular: "))
            ViajeroFrecuente.acumulaMillas(viajeros[numViajero-1],aux)

        elif op==3:
            cant=int(input("Ingrese cantidad de millas a canjear: "))
            ViajeroFrecuente.canjearMillas(viajeros[numViajero-1],cant)

        op=menu.muestraMenu()
