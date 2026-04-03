# Ejercicio 3

## Enunciado

Demostrar que cualquier lenguaje PSPACE-Completo es NP-hard.

## Demostración

Sea \(A\) un lenguaje PSPACE-completo.

Por definición de PSPACE-completitud:

1. \(A\in\) PSPACE,
2. para todo \(L\in\) PSPACE, \(L\le_p A\).

Además, se sabe que

\[
\text{NP}\subseteq \text{PSPACE}.
\]

Entonces, para todo \(L\in\) NP, como \(L\in\) PSPACE, se cumple \(L\le_p A\).

Eso es exactamente la definición de NP-hard.

Por lo tanto, todo lenguaje PSPACE-completo es NP-hard.
