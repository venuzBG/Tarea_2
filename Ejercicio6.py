# Ejercicio 3: Determinar cuántos términos se requieren para error < 1e-6

def serie(x, tol=1e-6):
    rhs = (1 + 2*x) / (1 + x + x**2)
    S = 0
    k = 1
    while True:
        num = 2**(k-1) * x**(2**(k-1) - 1) - 2**k * x**(2**k - 1)
        den = 1 - x**(2**(k-1)) + x**(2**k)
        S += num / den
        if abs(S - rhs) < tol:
            break
        k += 1
    return k, S, rhs

# Ejemplo
n, S, rhs = serie(0.25)
print(f"Se requieren {n} términos.")
print(f"Suma parcial = {S}, Valor real = {rhs}")