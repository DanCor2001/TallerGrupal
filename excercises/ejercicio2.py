import math
class CalculadoraAreaCuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

    def calcularPerimetro(self):
        return self.lado * 4

    def prueba():
        while True:
            entrada = input("Ingrese el lado del cuadrado (escriba 'salir' para terminar): ")

            if entrada.lower().replace(" ", "") == "salir":
                print("Programa finalizado")
                break

            try:
                lado = float(entrada)
                cuadrado = CalculadoraAreaCuadrado(lado)

                print("area cuadrado:", cuadrado.calcularArea())
                print("Perimetro cuadrado:", cuadrado.calcularPerimetro())

            except ValueError:
                print("Entrada invalida, ingrese un numero o salir")