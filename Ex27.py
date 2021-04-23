x = float(input("Ingrese su primera nota: "))
while x > 5:
    print("EL resultado es incorrecto, vuelva a ingresar: ")
    x = float(input("Ingrese su primera nota: "))

y = float(input("Ingrese su segunda nota: "))
while y > 5:
    print("EL resultado es incorrecto, vuelva a ingresar: ")
    y = float(input("Ingrese su segunda nota: "))

m = float(input("Ingrese su tercera nota: "))
while m > 5:
    print("EL resultado es incorrecto, vuelva a ingresar: ")
    m = float(input("Ingrese su tercera nota: "))

z = float(input("Ingrese su cuarta nota: "))
while z > 5:
    print("EL resultado es incorrecto, vuelva a ingresar: ")
    z = float(input("Ingrese su cuarta nota: "))

n = float(input("Ingrese su quinta nota: "))
while n > 5:
    print("EL resultado es incorrecto, vuelva a ingresar: ")
    n = float(input("Ingrese su quinta nota: "))

Acum = (x * 0.15 + y * 0.20 + m * 0.15 + z * 0.40 + n * 0.20 / 5)
print("Su nota final es: ", Acum)

if Acum < 2.0:
    print("No puede habilitar")
elif Acum < 3.0:
    print("Reprobo el semestre")

if Acum > 3.0:
    print("Aprobo el semestre")

if Acum > 4.5:
    print("Mil felicitaciones, Aprobo de la mejor manera")