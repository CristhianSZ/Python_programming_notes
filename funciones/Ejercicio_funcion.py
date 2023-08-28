"""Ejercicio 1
Declara una funcion llamada saludar, que cada vez que sea llamada imprima en pantalla hola mundo """
"""
EJercicio 2
dEclara una funcion llamada bienvenido que tome como argumento el nombre de una persona y que cada vez que sea llamada la funcion 
imprima en pantalla "!Bienvenido nombre de la persona"
"""
"""
Ejercicio 3
Declara una funcion llamada cuadrado que tome como argumento un numero
 cualquiera y que cada vez que sea llamada imprima en pantalla el cuadrado de dicho numero 
"""
"""
Ejercicio1
def saludar():
    print("Hola mundo")
saludar()"""

"""Ejercicio 2"""
"""def Bienvenido(nombre_persona):
    print("¡Bienvenido! "+ nombre_persona+"!")
Bienvenido("Lucas")"""
"""Ejercicio 3"""
def cuadrado(numero):
    calculo=numero**2
    print("El cuadrado de ",numero,"es",calculo)
cuadrado(int(input("Ingrese un numero: ")))