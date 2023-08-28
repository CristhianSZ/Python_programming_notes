nombre = ["ana","Yoan","Pedro","Antonio","Umberto"]
c=0
for i in range (5):
    if (nombre[i].startswith("Z")):
        print("Se encontro un nombre que comienza con 'A': ",nombre[i])
        c=1
        break

if (c==0):
        print("No hay nombre con esa eleccion de busqueda.")

print("Fin del programa")

pass  # funciona para pasar la decision muy utilizado en este caso