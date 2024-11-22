from factorial import factorial
# Función para calcular la variación V(n, r)
def variacion(n: int, r: int) -> int:
    return factorial(n) // factorial(n - r)

n: int = int(input("Introduce el valor de n: "))
r: int = int(input("Introduce el valor de r: "))

resultado: int = variacion(n, r)

print(f"La variación de {n} elementos tomados de {r} en {r} es: {resultado}")
