import matplotlib.pyplot as plt

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(start, end):
    return [fibonacci(i) for i in range(start, end+1)]

# Calcula la serie de Fibonacci del 5º al 10º término
series = fibonacci_series(4, 9)

# Representación gráfica
plt.figure(figsize=(10, 6))
plt.plot(series, 'o-', label='Fibonacci Series')
plt.title('Fibonacci Series')
plt.xlabel('Index')
plt.ylabel('Value')
plt.xticks(range(len(series)), range(4, 9 + 1))  # Ajusta las etiquetas del eje x para que muestren el rango correcto
plt.legend()
plt.grid(True)
plt.show()
