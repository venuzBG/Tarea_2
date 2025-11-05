# Ejercicio 3: Determinar n mínimo para |error| < 1e-3 usando Machin
def machin_error(n):
    from math import pi
    def arctan_series(x, n):
        return sum(((-1)**(k+1)) * (x**(2*k-1)) / (2*k-1) for k in range(1, n+1))
    pi_aprox = 4 * (4 * arctan_series(1/5, n) - arctan_series(1/239, n))
    return abs(pi - pi_aprox)

for n in range(1, 6):
    print(f"n={n}, error={machin_error(n):.2e}")

