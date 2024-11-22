from p_geometrica import termino_enesimo_pg
# Función que calcula la suma de los primeros n términos de una progresión geométrica
def suma_pg(a1: float, n: int, r: float) -> float:
    suma = 0
    
    for i in range(n):
        print(i)
        suma += termino_enesimo_pg(a1, (i+1) ,r) 
    
    return suma

if __name__ == "__main__":

  primer_termino: float = float(input("Introduce el primer término (a1): ")) 
  numero_terminos: int = int(input("Introduce el número de términos (n): "))
  razon_comun: float = float(input("Introduce la razón común (r): "))

  resultado: float = suma_pg(primer_termino, numero_terminos, razon_comun)

  print(f"La suma de los primeros {numero_terminos} términos de la progresión geométrica es: {resultado}")
