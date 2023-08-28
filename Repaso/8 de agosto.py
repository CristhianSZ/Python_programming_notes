"""
Escribir un numero y si es el acertado que lo enuncie y 5 intentos
Si el numero que se elegio es menor o mayor al selecto debe de indicarse entre intentos
y decir cuantos intentos hubo y en cual se acerto

Se ingresa el nombre de la persona se le explica el juego
Se le explica intentos
Ingresa numeros
si el numeros es mayuor al aleartoreo se indica la cercania
si acierta se indica el intento de acierto
y el quinto intento indica la ultima oportunidad
y los aciertos deben ser personalizados
"""
from random import randint
aleatorio=randint(1,50)
contIntentos=5
print("Esto es una trampa para probar el juego, el numero secreto es: ",aleatorio)
c=0
intentos=0
print("Comencemos el juego tiene 5 intentos")
for i in range(5):
    if (contIntentos>0):
        num = int(input("Adivine un numero entre el 1 y el 50 incluidos: "))
        contIntentos-=1
        intentos+=1
        print("Cantidad de intentos restantes: ", contIntentos)
        if (num == aleatorio):
            print("Acerto en su eleccion, el numero secreto es: ",aleatorio)
            c=1
            break
        else:
            if (num<aleatorio):
                print("El numero secreto es mas grande")
            else:
                print("El numero secreto tiene un valor mas pequeño")
if(c==0):
    print("Se terminaron sus intentos, el numero secreto era: ",aleatorio)
print("Usted acerto en el intento numero: ",intentos)

print("Final del programa")
