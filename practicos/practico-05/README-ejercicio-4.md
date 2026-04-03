# Ejercicio 4

## Enunciado

Demostrar que si cualquier lenguaje NP-hard es también PSPACE-hard, entonces \(NP=PSPACE\).

## Demostración

Siempre vale:

\[
NP\subseteq PSPACE.
\]

Para obtener la igualdad basta probar \(PSPACE\subseteq NP\).

Sea \(SAT\), que es NP-completo; en particular, \(SAT\) es NP-hard.

Por hipótesis del enunciado, todo NP-hard es PSPACE-hard. Entonces:

\[
SAT \text{ es PSPACE-hard}.
\]

Eso significa que para todo \(L\in PSPACE\), \(L\le_p SAT\).

Como \(SAT\in NP\), y NP es cerrado hacia atrás por reducciones many-one polinomiales, se deduce:

\[
L\in NP \quad \text{para todo } L\in PSPACE.
\]

Por tanto:

\[
PSPACE\subseteq NP.
\]

Combinando con \(NP\subseteq PSPACE\), concluimos:

\[
NP=PSPACE.
\]
