# Función que calcula el término n-ésimo de una progresión aritmética
def termino_enesimo_pa(a1: float, n: int, d: float) -> float:
    return a1 + (n - 1) * d

if __name__ == "__main__":
  
    primer_termino: float = float(input("Introduce el primer término (a1): ")) 
    indice_termino: int = int(input("Introduce el número de término (n): "))
    diferencia_comun: float = float(input("Introduce la diferencia común (d): "))

    resultado: float = termino_enesimo_pa(primer_termino, indice_termino, diferencia_comun)

    print(f"El término {indice_termino}-ésimo de la progresión aritmética es: {resultado}")
