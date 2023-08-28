op = "si"
suma = 0
while(op=="si"):
    n=int(input("Ingrese un numero: "))
    suma+=n
    print("¿Desea seguir?")
    op=input().lower()
print("La suma de los numeros ingresedos es: ",suma)