print("Bienvenidos a la plataforma:)")
Usuario = str("Nicolas")
Contraseña = str("Hola")
Acceso = Usuario + Contraseña

user = str(input("Ingrese su usuario: "))
password = str(input("Ingrese su contraseña: "))

Acces = user + password

if Acces != Acceso:
    print("Acceso denegado")
else:
    print("Acceso concedido")