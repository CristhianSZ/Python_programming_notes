def devolver_distintos(r1,r2,r3):
    suma=r1+r2+r3
    vector=[r1,r2,r3]
    if (suma > 15):
       return print("La suma es mayor a 15 por ello el mayor es: ",max(vector))
    elif (suma<10):
        min(vector)
        return print("La suma es menor a 10 por ello el menor es: ",min(vector))
    else:
        vector.sort() #Ordena los numeros de menor a mayor
        return vector[1]
print(devolver_distintos(4,9,2))

