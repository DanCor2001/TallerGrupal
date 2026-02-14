#Finalizado
from functions.functions import Functions
from excercises.ejercicio1 import CalculadoraBasica
from excercises.ejercicio2 import CalculadoraAreaCuadrado
from excercises.ejercicio8 import GeometriaCirculo
from excercises.TercerEjercicio import ConversorTemperatura
from excercises.ejercicio4 import EstadisticaSimple
from excercises.Excercise6 import Exercise6
from excercises.Excercise15 import Exercise15
from excercises.ejercicio7 import CalculadoraDescuentos
from excercises.e9 import convertidormedidas
from excercises.e11 import AhorroPersonal
from excercises.ejercicio10 import CalculadoraTriangulo
from excercises.ejercicio13 import RepartidorGastos
from excercises.ejercicio12 import calcularIMC
from excercises.ejercicio14 import CalculadoraVelocidad
from excercises.ejercicio5 import CalculadoraIVA
from selects.Exit import Exit
class Main:
    def __init__(self):
        while True:
            Main.main_list(self)
            text=""
            for i,x in enumerate(self.mainlist):
                if i==0:text+=f"¡Ejercicios!\n\n{i+1}. {x[0]}\n"
                elif i==len(self.mainlist)-1:text+=f"{i+1}. {x[0]}"
                else:text+=f"{i+1}. {x[0]}\n"
            select1=Functions.filter("int",text,1,len(self.mainlist))
            self.mainlist[select1-1][1]()
    def main_list(self):
        self.mainlist=[["Primer Ejercicio",lambda: CalculadoraBasica.funcion()],
                       ["Segundo Ejercicio",lambda: CalculadoraAreaCuadrado.prueba()],
                       ["Tercer Ejercicio",lambda: ConversorTemperatura.funcion()],
                       ["Cuarto Ejercicio",lambda: EstadisticaSimple.calcularPromedio()],
                       ["Quinto Ejercicio",lambda: CalculadoraIVA.funcion()],
                       ["Sexto Ejercicio",lambda: Exercise6()],
                       ["Séptimo Ejercicio",lambda: CalculadoraDescuentos.funcion()],
                       ["Octavo Ejercicio",lambda: GeometriaCirculo.prueba()],
                       ["Noveno Ejercicio",lambda: convertidormedidas.funcion()],
                       ["Decimo Ejercicio",lambda: CalculadoraTriangulo.funcion()],
                       ["Décimo Primer Ejercicio",lambda: AhorroPersonal.funcion()],
                       ["Décimo Segundo Ejercicio",lambda: calcularIMC.funcion()],
                       ["Décimo Tercer Ejercicio",lambda: RepartidorGastos.funcion()],
                       ["Décimo Cuarto Ejercicio",lambda: CalculadoraVelocidad.funcion()],
                       ["Décimo Quinto Ejercicio",lambda: Exercise15.show()],
                       ["Salir",lambda: Exit()]]
Main()