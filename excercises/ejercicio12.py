class calcularIMC:

    def __init__(self, peso,altura):
        self.peso = peso
        self.altura = altura

    def obtenerIndice(self):
        if self.altura <=0 :    
            return "altura invalida"
        return self.peso / (self.altura * self.altura)
    
    def categoria (self):
        imc = self.obtenerIndice()

        if imc < 18.5 :
            return "bajo peso"
        if imc >= 18.5 and imc < 25 :
            return "peso normal"
        if imc >= 25 and imc < 30:
            return "sobrepeso"
        else:
            return "obesidad"


print("calcular imc")

peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura m : "))



persona = calcularIMC(peso, altura)

imc = persona.obtenerIndice()
categoria = persona.categoria()
if isinstance(imc, str):
    print(imc)
else:
    print(f"IMC: {imc:.2f}")
    print(f"Categoría: {categoria}")