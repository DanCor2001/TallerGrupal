class CalculadoraBasica:

    def sumar(num1, num2):
        return num1 + num2

    def restar(num1, num2):
        return num1 - num2
    def funcion():
        print("1. Sumar")
        print("2. Restar")
        while True:
            opcion = input("sumar (1) o restar (2) salir (3): ")
            match opcion:
                case "1":
                    num1 = float(input("primer numero: ")) 
                    num2 = float(input("segundo numero: "))
                    print("Resultado de la suma:", CalculadoraBasica.sumar(num1, num2))

                case "2":
                    num1 = float(input("primer numero: "))
                    num2 = float(input("segundo numero: "))
                    print("Resultado de la resta:", CalculadoraBasica.restar(num1, num2))
                case "3":
                    print("baysssss")
                    break