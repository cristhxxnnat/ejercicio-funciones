# Función para calcular el promedio
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# Entrada de datos
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

# Llamada a la función
resultado = calcular_promedio(n1, n2, n3)

print("El promedio es:", resultado)