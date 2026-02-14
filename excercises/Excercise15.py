from functions.functions import Functions
class Exercise15:
    def __init__(self,num1):
        self.num1=num1
    def operation(self):
        flag1=False
        if self.num1%2==0: flag1=True 
        if flag1: print(f"El {self.num1} es un número par.\n")
        else: print(f"El {self.num1} es un número impar.\n")
    def show():
        while True:
            list=Exercise15.main_list()
            text=""
            for i,x in enumerate(list):
                if i==0:text+=f"¡Ejercicio 15!\n\n{i+1}. {x[0]}\n"
                elif i==len(list)-1:text+=f"{i+1}. {x[0]}"
                else:text+=f"{i+1}. {x[0]}\n"
            select1=Functions.filter("int",text,1,len(list))
            list[select1-1][1]()
            if select1==len(list):
                break
    def main_list():
        selectlist=[["Comprobar Impart",lambda: Exercise15.doit()],
                    ["Atrás",lambda: Functions.clean_console()]]
        return selectlist
    def doit():
        num1=Functions.filter("int","Número base:",1,float("inf"))
        obj1=Exercise15(num1)
        obj1.operation()