def factoriales(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoriales(n-1)

# Pruebas
print(factoriales(0))  # Debería imprimir 1
print(factoriales(1))  # Debería imprimir 1
print(factoriales(5))  # Debería imprimir 120 (5! = 5 * 4 * 3 * 2 * 1)
print(factoriales(10)) # Debería imprimir 3628800 (10! = 10 * 9 * 8 * ... * 1)