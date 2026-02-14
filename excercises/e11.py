class AhorroPersonal:
    
    def __init__(self, saldoInicial):
        self.saldoInicial = saldoInicial
    
    def agregarInteres(self, tasa):
  
        interes = self.saldoInicial * (tasa / 100)
        self.saldoInicial += interes
        return self.saldoInicial
    
    def previsionAnual(self, tasa):

        return self.saldoInicial * (1 + tasa / 100)
    def funcion():
        saldo = float(input("ingrese el saldo inicial: "))
        
        tasa = float(input("ingrrese la tasa de interes (%): "))

        ahorro = AhorroPersonal (saldo)
        
        print("   RESULTADOS   ")
        print("saldo despues de agregar interes: ", ahorro.agregarInteres (tasa) )
        print("prevision anual: ", ahorro.previsionAnual (tasa))
