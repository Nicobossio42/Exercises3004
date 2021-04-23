Num1 = int(input("Ingrese el primer numero: "))
Num2 = int(input("Ingrese el segundo numero: "))
Num3 = int(input("Ingrese el tercer numero: "))

if Num1 > Num2:
    print("El numero mayor es: ", Num1)
elif Num2 > Num1:
    print("El numero mayor es: ", Num2)

if Num3 > Num1:
    print("El numero mayor es: ", Num3)
elif Num3 > Num2:
    print("El numero mayor es:", Num3)