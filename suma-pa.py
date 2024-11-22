from p_aritmetica import termino_enesimo_pa
# Función que calcula la suma de los primeros n términos de una progresión aritmética
def suma_pa(a1: float, n: int, d: float) -> float:

    a_n = termino_enesimo_pa(a1, n, d)

    suma = (n / 2) * (a1 + a_n)
    return suma

if __name__ == "__main__":

  primer_termino: float = float(input("Introduce el primer término (a1): "))
  numero_terminos: int = int(input("Introduce el número de términos (n): "))
  diferencia_comun: float = float(input("Introduce la diferencia común (d): "))

  resultado: float = suma_pa(primer_termino, numero_terminos, diferencia_comun)

  print(f"La suma de los primeros {numero_terminos} términos de la progresión aritmética es: {resultado}")
