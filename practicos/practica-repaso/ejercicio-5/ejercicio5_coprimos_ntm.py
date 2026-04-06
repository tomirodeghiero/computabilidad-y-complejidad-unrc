from __future__ import annotations

from math import gcd


def ntm_coprimos_por_bezout(m: int, n: int) -> bool:
    """
    Simula una MT no deterministica que decide si m y n son coprimos.

    Idea NTM:
    - Acepta si existe un par (x, y) tal que: m*x + n*y = 1.
    - Por Bezout, esto ocurre sii gcd(m, n) = 1.

    Para que sea decidor (todas las ramas halten), acotamos la busqueda a:
    x, y in [-B, B], con B = max(m, n).
    Esa cota es suficiente para encontrar algun testigo cuando gcd(m, n) = 1.
    """

    if m <= 0 or n <= 0:
        raise ValueError("m y n deben ser enteros positivos")

    b = max(m, n)

    # "Ramas no deterministicas": elegir x e y en el rango acotado.
    for x in range(-b, b + 1):
        for y in range(-b, b + 1):
            if m * x + n * y == 1:
                # Existe rama de aceptacion.
                return True

    # Ninguna rama acepto -> rechazo.
    return False


def demo() -> None:
    casos = [
        (8, 15),   # coprimos
        (12, 18),  # no coprimos
        (35, 64),  # coprimos
        (21, 14),  # no coprimos
        (17, 31),  # coprimos
    ]

    for m, n in casos:
        acepta_ntm = ntm_coprimos_por_bezout(m, n)
        esperado = gcd(m, n) == 1
        print(
            f"m={m:>2}, n={n:>2} -> coprimos? {acepta_ntm} "
            f"(esperado: {esperado})"
        )


if __name__ == "__main__":
    demo()
