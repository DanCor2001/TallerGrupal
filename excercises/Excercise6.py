from functions.functions import Functions
class Exercise6:
    def __init__(self):
        while True:
            Exercise6.main_list(self)
            text=""
            for i,x in enumerate(self.selectlist):
                if i==0:text+=f"¡Ejercicio 6!\n\n{i+1}. {x[0]}\n"
                elif i==len(self.selectlist)-1:text+=f"{i+1}. {x[0]}"
                else:text+=f"{i+1}. {x[0]}\n"
            select1=Functions.filter("int",text,1,len(self.selectlist))
            self.selectlist[select1-1][1]()
            if select1==len(self.selectlist):
                break
    def main_list(self):
        self.selectlist=[["Hacer Exponencial",lambda: Exercise6.exponential()],
                       ["Hacer Raíz Cuadrada",lambda: Exercise6.square_root()],
                       ["Atrás",lambda: Functions.clean_console()]]
    def exponential ():
        num3=float(0)
        num1=Functions.filter("int","Número base:",1,float("inf"))
        num2=Functions.filter("int","Número exponencial:",1,float("inf"))
        num3=num1**num2
        print(f"La ecuación es la siguiente:\n {num1} ^ {num2} = {num3}\n")
    def square_root ():
        num2=float(0)
        num1=Functions.filter("int","Número base:",1,float("inf"))
        num2=num1**(1/2)
        print(f"La ecuación es la siguiente:\n  ²v{num1} = {num2:.1f}\n")