#Volver a jugar?
op="si"
while (op =="si"):


    # Lista inicial
    palitos=[ "-", "—" , "---" , "----" ]
    # mezclar palitos
    from random import shuffle
    def mezclar(lista):
        shuffle(lista)
        return(lista)
    # pedirle intento
    def probar_suerte():
        intento=""
        while intento not in ["1","2","3","4"]:
            intento=input("Ingrese un numero contenido entre el 1 y el 4: ")
        return int(intento)
    # comprobar intento
    def chequear_intento(lista,intento):
        if lista[intento-1]=="-":
            print("Debes hacer la prenda")
        else:
            print("Te salvaste")
        print("te ha tocado",lista[intento-1])

    palitos_mezclado=mezclar(palitos)
    seleccion=probar_suerte()
    chequear_intento(palitos_mezclado,seleccion)

    op=input("Jugar de nuevo(si/no)?")