KmPrice = 5000
DiasEstar = int(input("Inrtroduzca el numeroo de dias que se quedara: "))
KmRecor = int(input("Ingrese el numero de km que va a recorrer: "))
PrecioBol = KmPrice * DiasEstar * KmRecor

if DiasEstar > 7 and KmRecor > 1000:
    PrecioBol * 0.15
else:
    PrecioBol

print("El precio  de su boleto es: ", PrecioBol)