def numeros_persona(nombre,*args):
    suma=sum(args)
    return (nombre,'la suma de tus numeros es:',suma)
print(numeros_persona("Pedro",8,9,15))