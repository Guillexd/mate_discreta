# Función recursiva para calcular el factorial de un número
def factorial(n: int) -> int:
    # Caso base: si n es 0, el factorial es 1
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":

  numero: int = int(input("Introduce un número para calcular su factorial: "))

  resultado: int = factorial(numero)

  print(f"El factorial de {numero} es: {resultado}")
