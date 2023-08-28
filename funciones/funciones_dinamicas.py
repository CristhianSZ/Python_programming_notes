vector=[]
for i in range(5):
    n= int(input("Ingrese un numero: "))
    vector.append(n)
def buscar_3_cifras(vector):
    for i in vector:
        if i in range(100,1000):
            return True
        else:
            pass
    return False
resultado=buscar_3_cifras(vector)
print(resultado)
