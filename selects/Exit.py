from functions.functions import Functions
class Exit:
    def __init__(self):
        while True:
            Exit.exit_list(self)
            text=""
            for i,x in enumerate(self.exitlist):
                if i==0:text+=f"¿Desea Salir?\n\n{i+1}. {x[0]}\n"
                elif i==len(self.exitlist)-1:text+=f"{i+1}. {x[0]}"
                else:text+=f"{i+1}. {x[0]}\n"
            select1=Functions.filter("int",text,1,len(self.exitlist))
            self.exitlist[select1-1][1]()
            if select1==len(self.exitlist):break
    def exit_list(self):
        self.exitlist=[["Sí",lambda: Functions.close_console()],
                       ["No",lambda: Functions.clean_console()]]