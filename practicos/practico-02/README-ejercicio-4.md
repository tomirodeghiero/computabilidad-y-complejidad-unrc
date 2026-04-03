# Ejercicio 4

## Enunciado

Demostrar que si \(A\) es reconocible y \(A \le \overline{A}\) entonces \(A\) es decidible.

## Proposición

Si \(A\) es Turing-reconocible y \(A\le_m \overline{A}\), entonces \(A\) es decidible.

## Demostración

Sea \(f\) la reducción computable de \(A\) a \(\overline{A}\). Entonces:

\[
x\in A \iff f(x)\in \overline{A}.
\]

Negando ambos lados:

\[
x\in \overline{A} \iff f(x)\in A.
\]

Por lo tanto, la misma función \(f\) da una reducción

\[
\overline{A}\le_m A.
\]

Ahora, como \(A\) es reconocible, y \(\overline{A}\le_m A\), se sigue que \(\overline{A}\) es reconocible (teorema estándar: si \(X\le_m Y\) y \(Y\) es reconocible, entonces \(X\) es reconocible).

Entonces \(A\) y \(\overline{A}\) son ambos reconocibles.  
Por Sipser (Thm. 4.22), un lenguaje es decidible sii es reconocible y co-reconocible.

Concluimos que \(A\) es decidible.
