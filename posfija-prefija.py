operacion=(input("Ingrese la operacion que desea evaluar: "))
if operacion[0] in "+ - * /":
    print("La operacion es prefija ")
    print("\nEvaluando... ")
    prefija=True
    posfija=False
else:
    print("La operacion es posfija")
    print("\nEvaluando... ")
    posfija=True
    prefija=False


if prefija == True and posfija== False:
    Pila=[]
    for dato in operacion[::-1]:
        if dato.isdigit():
            Pila.append(int(dato))
        else:
            
            operador1 = Pila.pop()
            operador2 = Pila.pop()

            if dato == "+":
                Pila.append(operador1 + operador2)
            elif dato == "-":
                Pila.append(operador1-operador2)
            elif dato == "*":
                Pila.append(operador1*operador2)
            elif dato == "/":
                Pila.append(operador1/operador2)
    resultado=Pila.pop()
    print("\nEl resultado de la opearcion es ", resultado)
            

elif posfija == True and prefija ==False:
    Pila=[]
    for dato in operacion:
        if dato.isdigit():
            Pila.append(int(dato))
        else:
            
            operador2 = Pila.pop()
            operador1 = Pila.pop()

            if dato == "+":
                Pila.append(operador1 + operador2)
            elif dato == "-":
                Pila.append(operador1-operador2)
            elif dato == "*":
                Pila.append(operador1*operador2)
            elif dato == "/":
                Pila.append(operador1/operador2)
    resultado=Pila.pop()
    print("\nEl resultado de la opearcion es ", resultado)