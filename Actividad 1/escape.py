from math import sqrt


r = float(input("Ingrese el radio en kilometros sin unidad de medida:"))
g = float(input("ingrese la constante gravedad sin unidad de medida: "))
Ve = sqrt(2 * g * (r*1000))

print(f"La velocidad de escape es: {Ve} m/s")
