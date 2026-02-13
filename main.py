from functions.functions import Functions
from excercises.TercerEjercicio import ConversorTemperatura
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
        self.mainlist=[["Primer Ejercicio",lambda: print("1")],
                       ["Segundo Ejercicio",lambda: print("2")],
                       ["Tercer Ejercicio",lambda: ConversorTemperatura.funcion()],
                       ["Cuarto Ejercicio",lambda: print("4")],
                       ["Quinto Ejercicio",lambda: print("5")],
                       ["Sexto Ejercicio",lambda: print("6")],
                       ["Séptimo Ejercicio",lambda: print("7")],
                       ["Octavo Ejercicio",lambda: print("8")],
                       ["Noveno Ejercicio",lambda: print("9")],
                       ["Decimo Ejercicio",lambda: print("10")],
                       ["Décimo Primer Ejercicio",lambda: print("11")],
                       ["Décimo Segundo Ejercicio",lambda: print("12")],
                       ["Décimo Tercer Ejercicio",lambda: print("13")],
                       ["Décimo Cuarto Ejercicio",lambda: print("14")],
                       ["Décimo Quinto Ejercicio",lambda: print("15")],
                       ["Salir",lambda: Exit()]]
Main()