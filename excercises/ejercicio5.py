from functions.functions import Functions
class CalculadoraIVA:
    def __init__(self,base1):
        self.base1=base1
    def iva(self):
        print(f"Con un precio base de: ${self.base1}.\n"
              f"Y de un IVA del 21%, el precio final es: ${(self.base1+(self.base1*0.21)):.1f}.\n")
    def funcion():
        base1=Functions.filter("float","Precio base.",1,float("inf"))
        obj1=CalculadoraIVA(base1)
        obj1.iva()