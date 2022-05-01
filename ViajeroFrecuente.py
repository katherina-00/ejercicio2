class ViajeroFrecuente:
    __numViajero=0
    __dni=0
    __nombre=""
    __apellido=""
    __millas_acum: int=0

    def __init__(self,numViajero,dni,nombre,apellido,millas_acum):
        self.__numViajero=numViajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum

    def muestraMillas(self):
        print(self.__millas_acum)

    def acumulaMillas(self, aux):
        self.__millas_acum+=aux
        print("La cantidad de millas es: {} ".format(self.__millas_acum))

    def canjearMillas(self,cant):

        if cant<=self.__millas_acum:
            self.__millas_acum-=cant
            print("La cantidad de millas restantes son: {}".format(self.__millas_acum))
        else: print("La cantidad de millas a canjear excede la cantidad existente")
