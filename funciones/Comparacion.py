"""cargo=input("Ingrese su cargo: ").upper()
if (cargo=="ADMINISTRATIVO" or cargo=="TESORERIA"):
    print("Usted tiene un aumento de un 25%")
else:
    print("Siga su camino, aqui no hay ningun aumento")"""

cargo=input("Ingrese su cargo: ").upper()
sueldo=int(input("Ingrese su sueldo: "))
if (cargo=="ADMINISTRADOR") & (sueldo>30000):
    print("Tiene un aumento del 25%")
else:
    print("Usted no tiene aumentos")
