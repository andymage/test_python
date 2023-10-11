from sympy import fibonacci

# Límite para la secuencia de Fibonacci (1,000,000)
limite = 1000000

# Generar la secuencia de Fibonacci hasta el límite
secuencia_fibonacci = []
n = 0
while fibonacci(n) <= limite:
    secuencia_fibonacci .append(fibonacci(n))
    n += 1

# Mostrar la secuencia de Fibonacci
print("La secuencia de Fibonacci hasta", limite, "es: ")
print(secuencia_fibonacci)
