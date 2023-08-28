from random import randint
aleatorio=randint(1,100)
print(aleatorio)
cantidadIntentos=5
c=0
numeroIntento=0

print("Que comience el juego:)")
print("Ingresa tu nombre")
nombre= input()
print("Hola",nombre,"actualmente existe un numero secreto y tu como buen jugador que se desempeña en su accionar lo adivinaras o de lo contrario ya sabras")
print("Bien",nombre,"ingresa un numero de tu predileccion")
for i in range(5):
    if cantidadIntentos>0:
        num=int(input())
        cantidadIntentos-=1
        numeroIntento+=1
        if (num==aleatorio):
            print(nombre,"acertaste, el numero secreto era ", aleatorio)
            c=1
            break
        else:
            if(num<aleatorio):
                print(nombre,"el numero es mas grande")
            else:
                print(nombre,"el numero es mas pequeño")
if(c==o):
    print("Se terminaron los intentos ")

