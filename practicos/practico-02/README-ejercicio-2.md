# Ejercicio 2

## Enunciado

Si \(A \le B\) y \(B\) es un lenguaje regular, esto implica que \(A\) es un lenguaje regular? Fundamentar.

## Respuesta

No. La implicación es falsa en general.

## Demostracion por contraejemplo

Tomemos:

\[
A=\{0^n1^n \mid n\ge 0\}, \qquad B=\{1\}.
\]

- \(B\) es regular.
- \(A\) no es regular (resultado clásico por lema de bombeo).

Mostramos \(A \le_m B\). Definimos:

\[
f(x)=
\begin{cases}
1 & \text{si } x\in A,\\
0 & \text{si } x\notin A.
\end{cases}
\]

La función \(f\) es computable porque la pertenencia a \(A\) es decidible (aunque \(A\) no sea regular).

Además, para todo \(x\):

\[
x\in A \iff f(x)=1 \iff f(x)\in B.
\]

Por lo tanto, \(A\le_m B\), con \(B\) regular, pero \(A\) no regular.

Concluimos que de \(A\le B\) y \(B\) regular **no** se sigue que \(A\) sea regular.
