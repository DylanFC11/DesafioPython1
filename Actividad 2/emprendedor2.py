


P = int(input("Precio de suscripcion solo con numeros enteros: "))
Un = int(input("Numero de usuarios normales solo con numeros enteros: "))
Up = int(input("Numero de usuarios premium solo con numeros enteros: "))
Gt = int(input("Gastos totales solo con numeros enteros: "))
Utilidades = P * (Un + Up) - Gt

print(f"Utilidades del Proyecto: {Utilidades}")