"""
Se ingresa el nombre de la persona se le explica el juego
Se le explica intentos
Ingresa numeros
si el numeros es mayuor al aleartoreo se indica la cercania
si acierta se indica el intento de acierto
y el quinto intento indica la ultima oportunidad
y los aciertos deben ser personalizados
"""
from random import randint
aleatorio=randint(1,100)
intento=7
ContIntentos=0
c=0
print("Quiere jugar")
op=input()
print("Ingrese su nombre")
nombre=input().upper()
print("Hola",nombre,"actualmente existe un numero secreto y lo adivinaras, tienes ",intento," intentos y el numero esta entre 0 y 100")
while (intento>0)and(op=="si"):
    if (intento==1):
        print("Su ultimo intento!!!")
    num=int(input("Ingrese su numero: "))
    ContIntentos+=1
    if(num>aleatorio):
        print("El numero es menor")
        intento-=1
    elif(num<aleatorio):
        print("El numero es mayor")
        intento -= 1
    else:
        print("Acertaste",nombre,"adiviniste el numero es: ",aleatorio)
        print("En el intento: ",ContIntentos)
        c=1
        break
if (c==0):
    print(nombre,"tus intentos se acabaron, mejor suerte para la proxima")
    print("El numero secreo era: ",aleatorio)