def cero_seguidos(*args):
    contador=0
    for lado in args:
        if contador+1==len(args):
            return False
        elif(args[contador]==0) and (args[contador+1]==0):
            return True
        else:
            contador+=1
    return False
print(cero_seguidos(0,6,1,0,9,3,5,0,0))