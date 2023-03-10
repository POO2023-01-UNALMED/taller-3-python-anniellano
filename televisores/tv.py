class TV:
    #Atributo de clase
    _numTV = 0

    #Constructores
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        TV._numTV +=1
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control= None

    #Retorna el total de los tv
    def getNumTV(self):
        return self._numTV
    
    #cambiar estado
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    

    #cambiar canales
    def canalUp(self):
        if TV.getEstado(self):
            if (self._canal >=1 and self._canal <120):
                self._canal+=1

    def canalDown(self):
        if TV.getEstado(self):
            if (self._canal >1 and self._canal <=120):
                self._canal-=1
    

    def volumenUp(self):
        if TV.getEstado(self):
            if (self._volumen >=0 and self._volumen <7):
                self._volumen+=1

    def volumenDown(self):
        if TV.getEstado(self):
            if (self._volumen >0 and self._volumen <=7):
                self._volumen-=1
    

    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if TV.getEstado(self):
            if (self._canal >=1 and self._canal <=120):
                self._canal=canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if TV.getEstado(self):
            if volumen >= 0 and volumen <=7:
                self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def setNumTV(self,n):
        TV._numTV = n