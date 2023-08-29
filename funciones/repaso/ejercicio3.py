def cero_seguidos():
    numeros = []
    while True:
        entrada = input("Ingrese un número (ingrese 'fin' para terminar): ")
        if entrada == 'fin':
            break
        num = int(entrada)
        numeros.append(num)
    for i in range(len(numeros)-1):
        if numeros[i] == 0 and numeros[i+1] == 0:
            return True
    return False
resultado=cero_seguidos()
print(resultado)