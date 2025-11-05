# Ejercicio 2: Determinar n mínimo para error < tolerancia
from math import pi

def n_para_tolerancia(tol):
    n = 1
    while 4 / (2 * n + 1) > tol:
        n += 1
    return n

print("Para error < 1e-3: n =", n_para_tolerancia(1e-3))
print("Para error < 1e-10: n =", n_para_tolerancia(1e-5))
