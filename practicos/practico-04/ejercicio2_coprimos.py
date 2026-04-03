import random
import time


def gcd_euclides(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def gcd_stein(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b = b - a

    return a << shift


def son_coprimos_euclides(a: int, b: int) -> bool:
    return gcd_euclides(a, b) == 1


def son_coprimos_stein(a: int, b: int) -> bool:
    return gcd_stein(a, b) == 1


def generar_pares(bits: int, cantidad: int, rng: random.Random) -> list[tuple[int, int]]:
    minimo = 1 << (bits - 1)
    maximo = (1 << bits) - 1
    pares = []
    for _ in range(cantidad):
        a = rng.randint(minimo, maximo)
        b = rng.randint(minimo, maximo)
        pares.append((a, b))
    return pares


def benchmark(bits_list=(8, 16, 32, 64), muestras=200, seed=2026):
    rng = random.Random(seed)
    filas = []

    for bits in bits_list:
        pares = generar_pares(bits, muestras, rng)

        t0 = time.perf_counter()
        resultados_e = [son_coprimos_euclides(a, b) for a, b in pares]
        t1 = time.perf_counter()

        resultados_s = [son_coprimos_stein(a, b) for a, b in pares]
        t2 = time.perf_counter()

        if resultados_e != resultados_s:
            raise RuntimeError(f"Desacuerdo entre algoritmos para {bits} bits.")

        coprimos = sum(resultados_e)
        filas.append(
            {
                "bits": bits,
                "muestras": muestras,
                "coprimos": coprimos,
                "euclides_ms": (t1 - t0) * 1000,
                "stein_ms": (t2 - t1) * 1000,
            }
        )

    return filas


def imprimir_tabla(filas):
    print(
        f"{'bits':>6} {'muestras':>10} {'coprimos':>10} {'euclides(ms)':>14} {'stein(ms)':>12}"
    )
    print("-" * 60)
    for f in filas:
        print(
            f"{f['bits']:>6} {f['muestras']:>10} {f['coprimos']:>10} "
            f"{f['euclides_ms']:>14.3f} {f['stein_ms']:>12.3f}"
        )


if __name__ == "__main__":
    filas = benchmark()
    imprimir_tabla(filas)
