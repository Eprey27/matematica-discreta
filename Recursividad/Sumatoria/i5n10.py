import math

def sumatoria(n):
    total = 0
    for i in range(5, n - 10 + 1):
        total += math.log2(i) / (i**2 + 1)
    return total

n = 20  # Puedes cambiar este valor para cualquier n
result = sumatoria(n)

print(f"El resultado de la sumatoria para n = {n} es: {result}")
