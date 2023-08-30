from random import *
def lanzar_dados():
    d1=randint(1,6)
    d2=randint(1,6)
    return d1,d2
    #return random.randint(1,6),random.randint(1,6)
def evaluar_jugada(dado1,dado2):

    suma = dado1 + dado2
    if suma<=6:
        return "La suma de los dados es: ",suma,"es muy bajo"
    elif suma>6 and suma<10:
        return "La suma de los dados es: ",suma,"casi ganas"
    else:
        return "La suma de los dados es: ", suma, "ganaste"
resultado=lanzar_dados()
print(resultado)
suma_dados=evaluar_jugada(resultado[0],resultado[1])
print(suma_dados)

