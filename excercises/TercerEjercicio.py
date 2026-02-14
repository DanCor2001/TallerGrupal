from functions.functions import Functions
class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = int(celsius)

    def aFahrenheit(self):
        return (self.celsius * 9/5) + 32

    def aKelvin(self):
        return self.celsius + 273.15

    def ejecutar(self):
        print(f"{self.celsius}°C son {self.aFahrenheit()}°F")
        print(f"{self.celsius}°C son {self.aKelvin()}K")

    def funcion():
        num1=Functions.filter("float","Temperatura en centigrados:",float("-inf"),float("inf"))
        temperatura = ConversorTemperatura(num1)
        temperatura.ejecutar()

