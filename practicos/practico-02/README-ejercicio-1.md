# Ejercicio 1

## Enunciado

Encontrar un matching para el siguiente problema de Post:

\[
\frac{ab}{abab},\ \frac{b}{a},\ \frac{aba}{b},\ \frac{aa}{a}
\]

## Solucion

Numeramos las fichas como:

1. \(\dfrac{ab}{abab}\)
2. \(\dfrac{b}{a}\)
3. \(\dfrac{aba}{b}\)
4. \(\dfrac{aa}{a}\)

Una solución es la secuencia de índices:

\[
(4,4,2,1).
\]

Verificación:

- parte superior:
  \[
  aa\cdot aa\cdot b\cdot ab = aaaabab
  \]
- parte inferior:
  \[
  a\cdot a\cdot a\cdot abab = aaaabab
  \]

Como ambas concatenaciones coinciden, \((4,4,2,1)\) es un matching válido.
