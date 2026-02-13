class RepartidorGastos:
    def __init__(self, totalFactura, numeroPersonas):
        self.totalFactura = totalFactura
        self.numeroPersonas = numeroPersonas
                            
    def divisionEquitativa(self):
        resultado = self.totalFactura / self.numeroPersonas
        return resultado
    def funcion ():
        print("\nDivide en partes iguales los pagos\n")
        tot = float(input("por favor escriba el total de la factura: "))
        per= int(input("por favor escriba numero de personas: "))

        pago1 = RepartidorGastos(tot, per)

        print("el total es: ",pago1.divisionEquitativa())