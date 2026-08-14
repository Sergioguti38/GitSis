cuantos = int(input("Cuantosw usuaarios va a crear?"))

usuarios = []

for i in range(cuantos):
    nombre = input("inserte el nombre del usuario: ")
    usuarios.append(nombre)

print(usuarios)