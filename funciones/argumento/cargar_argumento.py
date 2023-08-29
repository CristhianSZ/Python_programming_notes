def contar_ceros(*args):
    contador=0
    op="si"
    while op=="si":
        args=int(input("Ingrese un numero: "))
        if args==0:
            contador+= 1
        else:
            pass
        op=input("Desea ingresar otro numero (si/no): ")
    return contador
print("La cantidad de ceros es: ",contar_ceros())
contar_ceros()