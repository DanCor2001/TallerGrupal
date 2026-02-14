class CalculadoraTriangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
                            
    def calcularArea(self):
        resultado = (self.base * self.altura)/2
        return resultado
    def funcion ():
        print("\nCalcula area de triangulo\n")
        base1 = float(input("por favor escriba la base del triangulo: "))
        altura1 = float(input("por favor escriba la altura del triangulo: "))

        triangulo1 = CalculadoraTriangulo(base1, altura1)

        print("el area 1 es: ",triangulo1.calcularArea())
        
    