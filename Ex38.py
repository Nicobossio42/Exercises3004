Num1 = int(input("Ingrese el primer numero: "))
Num2 = int(input("Ingrese el segundo numero: "))
Num3 = int(input("Ingrese el tercer numero: "))

if Num1 > Num2 > Num3:
    print("Los numeros estan disminuyendo")
elif Num1 < Num2 < Num3:
    print("Los numeros estan aumentando")
elif Num1 < Num3 > Num2:
    print("Los numeros no hacen nada")