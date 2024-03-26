


P = int(input("Precio de suscripcion solo con numeros enteros: "))
U = int(input("Numero de usuarios solo con numeros enteros: "))
Gt = int(input("Gastos totales solo con numeros enteros: "))
Utilidades = P * U - Gt
Uanterior =int(input("Utilidades del año anterior solo con numeros enteros: "))

print(f"Utilidades del Proyecto: {Utilidades}")
print(f"Razon entre utilidades actuales y año anterior: {Utilidades/Uanterior:.2f} ")
