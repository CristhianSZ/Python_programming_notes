nombre=""
TotalVentasMes=0
nombre=input("Ingrese su nombre: ")
TotalVentasMes=float(input("Ingrese el monto del total de ventas realizadas en el mes: "))
Comision=TotalVentasMes*0.13
print(nombre, "su comision es: ", Comision);
##Detalle para que figure con 2 decimales: round
print(nombre, "su comision es: ", round(Comision,3));
print(nombre, "su comision es: ", round(Comision));


