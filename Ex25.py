Valor = int(input("Ingrese el valor dado: "))



Iva = Valor * 0.19
Descuento = Valor + Iva * 0.05
SinDescuento = Valor + Iva

if Valor > 150000:
    print("Su valor mas el descuento es: ", Descuento)

elif Valor < 150000:
    Valor * Iva
    print("Su valor es: ", SinDescuento)