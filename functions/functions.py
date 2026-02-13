import os
import time
class Functions():
    def clean_console():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    def close_console():
        print("Saliendo del programa...")
        time.sleep(1)
        os._exit(0)
    def filter(kind,prompt,min_value,max_value):
        exception=""
        end="\nIngrese:\n"
        while True:
            try:
                if kind == "int":
                    entry = int(input(f"{prompt}\n{exception}{end}"))
                elif kind == "float":
                    entry = float(input(f"{prompt}\n{exception}{end}"))
                elif kind == "str":
                    entry = input(f"{prompt}\n{exception}{end}")
                    Functions.clean_console()
                    return entry
                if min_value<=entry<=max_value:
                    Functions.clean_console()
                    return entry
                else:
                    if min_value == float("-inf"):
                        exception=f"\n\033[91mFuera de rango:\nSolo valores menores o iguales a {max_value}.\033[0m"
                        Functions.clean_console()
                    elif max_value == float("inf"):
                        exception=f"\n\033[91mFuera de rango:\nSolo valores mayores o iguales a {min_value}.\033[0m"
                        Functions.clean_console()
                    elif min_value == max_value:
                        exception=f"\n\033[91mFuera de rango:\nSolo puede ingresar el valor {min_value}.\033[0m"
                        Functions.clean_console()
                    else:
                        exception=f"\n\033[91mFuera de rango:\nSolo valores entre {min_value} y {max_value}.\033[0m"
                        Functions.clean_console()
            except ValueError:
                if kind == "int":
                    exception=f"\n\033[91mNo es un número entero.\033[0m"
                    Functions.clean_console()
                elif kind == "float":
                    exception=f"\n\033[91mNo es un número real.\033[0m"
                    Functions.clean_console()