from factorial import factorial
# Función para calcular la combinación C(n, r)
def combinacion(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))

n: int = int(input("Introduce el valor de n: "))
r: int = int(input("Introduce el valor de r: "))

resultado: int = combinacion(n, r)

print(f"La combinación de {n} elementos tomados de {r} en {r} es: {resultado}")
