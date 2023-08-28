op = "SI"
suma = 0
while(op=="SI"):
    n=int(input("Ingrese un numero: "))
    suma+=n
    print("¿Desea seguir?")
    op=input().upper()
print("La suma de los numeros ingresedos es: ",suma)

