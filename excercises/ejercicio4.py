from functions.functions import Functions
class EstadisticaSimple:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
 
    def calcularPromedio():
        num1=Functions.filter("float","Nota 1:",0,5)
        num2=Functions.filter("float","Nota 2:",0,5)
        num3=Functions.filter("float","Nota 3:",0,5)
        promedio= (num1 + num2 + num3)/3
        print(f"El promedio es: {promedio}") 

    