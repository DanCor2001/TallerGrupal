class CalculadoraVelocidad:
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def calcularVelocidadMedia(self):
        if self.tiempo <= 0:
            print("El tiempo debe ser mayor que 0")
            return 0
        velocidad = self.distancia / self.tiempo
        return velocidad
    def funcion():
        distancia = float(input("Ingrese la distancia (en km): "))
        tiempo = float(input("Ingrese el tiempo (en horas): "))

        calculadora = CalculadoraVelocidad(distancia, tiempo)
        velocidad_media = calculadora.calcularVelocidadMedia()

        print("La velocidad media es:", velocidad_media, "km/h")
