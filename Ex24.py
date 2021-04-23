Num = float(input("Ingrese su Numero: "))
while Num > 0:
    if Num % 2 == 0:
        print("Es un par positivo")
    elif Num % 2 == 1:
        print("Es un impar positivo")
while Num < 0:
    if Num % 2 == 0:
        print("Es un par negativo")
    elif Num % 2 == 1:
        print("Es un impar negativo")