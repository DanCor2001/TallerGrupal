import math
class GeometriaCirculo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def prueba():
        while True:
            entrada = input("Ingrese el radio del circulo (escriba 'salir' para terminar): ")

            if entrada.lower().replace(" ", "") == "salir":
                print("Programa finalizado")
                break

            try:
                radio = float(entrada)
                circulo = GeometriaCirculo(radio)

                print("area circulo:", circulo.area())
                print("Perimetro circulo:", circulo.circunferencia())

            except ValueError:
                print("Entrada invalida, ingrese un numero o salir")
