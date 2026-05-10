# Ejercicio 5

## Enunciado

Demostrar que \(A\) es reconocible sii \(A \le A_{TM}\).

## Proposición

\[
A \text{ es reconocible } \iff A\le_m A_{TM}.
\]

## Demostración

Probamos ambos sentidos.

### (\(\Rightarrow\)) Si \(A\) es reconocible, entonces \(A\le_m A_{TM}\)

Supongamos que \(A\) es reconocido por una MT \(M_A\).

Definimos la función:

\[
f(x)=\langle M_A,x\rangle.
\]

La función \(f\) es computable (solo construye una codificación).

Además, para todo \(x\):

\[
x\in A
\iff M_A \text{ acepta } x
\iff \langle M_A,x\rangle\in A_{TM}
\iff f(x)\in A_{TM}.
\]

Luego \(A\le_m A_{TM}\).

### (\(\Leftarrow\)) Si \(A\le_m A_{TM}\), entonces \(A\) es reconocible

Sabemos que \(A_{TM}\) es Turing-reconocible.

Sea \(f\) una reducción computable de \(A\) a \(A_{TM}\):

\[
x\in A \iff f(x)\in A_{TM}.
\]

Construimos un reconocedor \(R\) para \(A\):

1. Entrada: \(x\).
2. Calcular \(f(x)\).
3. Ejecutar el reconocedor de \(A_{TM}\) sobre \(f(x)\).
4. Si acepta, aceptar.

Correctitud:

- Si \(x\in A\), entonces \(f(x)\in A_{TM}\), y el reconocedor de \(A_{TM}\) acepta eventualmente.
- Si \(x\notin A\), entonces \(f(x)\notin A_{TM}\), por lo que \(R\) no acepta.

Así, \(R\) reconoce \(A\). Por lo tanto \(A\) es reconocible.

Con ambos sentidos, queda probado el "sii".
