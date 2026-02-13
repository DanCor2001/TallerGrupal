from functions.functions import Functions
from selects.Exit import Exit
class Exercise6:
    def __init__(self,num1):
        self.num1=num1
    def Operation(self):
        self.num1
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
        print(f"La ecuación es la siguiente:\n  ²v{num1} = {num2}\n")