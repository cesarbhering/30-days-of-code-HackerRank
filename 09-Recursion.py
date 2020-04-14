def factorial(n):
    resultado = (n*(n-1))
    n -= 2
    while n >= 1:
        resultado = resultado*n
        n -= 1
    return resultado