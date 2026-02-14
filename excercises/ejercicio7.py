class CalculadoraDescuentos:
    def __init__(self, precio, porcentaje):
        self.precio = precio
        self.porcentaje = porcentaje
        
    def montoDescuento(self):
        descuento = self.precio * (self.porcentaje/ 100)
        return descuento
    
    def descuentoFinal(self):
        return self.precio - self.montoDescuento()
    def funcion ():
        precio = float(input("Ingrese el precio del producto: "))
        porcentaje = float(input("Ingrese el porcenjate del descuento: "))   

        calculadora = CalculadoraDescuentos(precio, porcentaje)

        print("Monto del descuento:", calculadora.montoDescuento())
        print("Monto del precio final:", calculadora.descuentoFinal())
