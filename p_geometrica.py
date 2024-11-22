# Función que calcula el término n-ésimo de una progresión geométrica
def termino_enesimo_pg(a1: float, n: int, r: float) -> float:
    return a1 * (r ** (n - 1))

if __name__ == "__main__":

    primer_termino: float = float(input("Introduce el primer término (a1): ")) 
    indice_termino: int = int(input("Introduce el número de término (n): "))  
    razon_comun: float = float(input("Introduce la razón común (r): ")) 

    resultado: float = termino_enesimo_pg(primer_termino, indice_termino, razon_comun)

    print(f"El término {indice_termino}-ésimo de la progresión geométrica es: {resultado}")
