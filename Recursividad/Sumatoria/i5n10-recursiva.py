import math

def sumatoria(n, i=5):
    # Caso base: cuando i > n-10, la sumatoria termina.
    if i > n - 10:
        return 0
    
    # Calcula el término actual.
    term = math.log2(i) / (i**2 + 1)
    
    # Devuelve el término actual sumado a la sumatoria de los términos restantes.
    return term + sumatoria(n, i + 1)

n = 20  # Puedes cambiar este valor para cualquier n
result = sumatoria(n)

print(f"El resultado de la sumatoria para n = {n} es: {result}")
