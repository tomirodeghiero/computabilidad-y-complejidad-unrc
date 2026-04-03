# Ejercicio 3

## Enunciado

Demostrar que \(\le\) es transitiva.

## Proposición

Si \(A\le_m B\) y \(B\le_m C\), entonces \(A\le_m C\).

## Demostración

Por hipótesis:

1. \(A\le_m B\): existe una función computable \(f\) tal que
   \[
   x\in A \iff f(x)\in B.
   \]
2. \(B\le_m C\): existe una función computable \(g\) tal que
   \[
   y\in B \iff g(y)\in C.
   \]

Definimos:

\[
h = g\circ f.
\]

Como composición de funciones computables, \(h\) es computable.

Ahora, para todo \(x\):

\[
x\in A
\iff f(x)\in B
\iff g(f(x))\in C
\iff h(x)\in C.
\]

Luego \(A\le_m C\). Queda probada la transitividad.
