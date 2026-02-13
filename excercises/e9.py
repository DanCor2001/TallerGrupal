class convertidormedidas:
    def __init__(self, metros):
        self.metros = metros
    
    def centimetros (self):
        return self.metros *100
    
    def kilometros(self):
        return self.metros / 1000
    def funcion():
        metros = float(input("ingrese los metros a convertir: " ))

        convertidor = convertidormedidas (metros)

        print("  RESULTADOS  ")
        print("En centimetros:", convertidor.centimetros())
        print("En kilometros:", convertidor.kilometros())