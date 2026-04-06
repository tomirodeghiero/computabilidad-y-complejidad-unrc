# Ejercicio 5

## Enunciado

Disenar una MT no deterministica que decida si dos numeros son coprimos.

## Idea no deterministica (testigo de Bezout)

Usamos el hecho:

`gcd(m, n) = 1  <=>  existen enteros x, y tales que m*x + n*y = 1`.

Entonces la NTM hace:

1. Lee `m` y `n` (positivos).
2. Calcula una cota `B = max(m, n)`.
3. No deterministamente adivina `x` e `y` en `[-B, B]`.
4. Verifica si `m*x + n*y = 1`.
5. Si se cumple, acepta esa rama; si no, rechaza esa rama.

Como el rango `[-B, B]` es finito, todas las ramas terminan.
La maquina acepta sii existe algun testigo, o sea sii `m` y `n` son coprimos.

## Implementacion (Python)

Archivo:

- `practicos/practica-repaso/ejercicio-5/ejercicio5_coprimos_ntm.py`

Ejecucion:

```bash
python3 practicos/practica-repaso/ejercicio-5/ejercicio5_coprimos_ntm.py
```

Salida esperada (ejemplo):

```text
m= 8, n=15 -> coprimos? True (esperado: True)
m=12, n=18 -> coprimos? False (esperado: False)
m=35, n=64 -> coprimos? True (esperado: True)
```
