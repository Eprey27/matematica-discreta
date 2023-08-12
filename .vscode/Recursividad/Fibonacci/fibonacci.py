def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(start, end):
    return [fibonacci(i) for i in range(start, end+1)]

# Ejemplo: para obtener los números de Fibonacci del 5º al 10º término
print(fibonacci_series(4, 9))
