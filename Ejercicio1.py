# Ejercicio 1: sumas con aritmética de 3 dígitos
def round3(x):
    """Redondea a tres cifras significativas."""
    return float(f"{x:.3g}")

# (a) Suma de 1/i^2
# (b) Suma de 1/i^3

s1, s2 = 0.0, 0.0
# ascendente
for i in range(1, 11):
    s1 = round3(s1 + round3(1 / i**2))
# descendente
for i in range(10, 0, -1):
    s2 = round3(s2 + round3(1 / i**2))

print("Ascendente =", s1)
print("Descendente =", s2)
