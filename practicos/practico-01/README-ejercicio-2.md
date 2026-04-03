# Ejercicio 2

## Enunciado

Demostrar que el conjunto \(\{w \mid w\ \text{es una cadena infinita de 0s y 1s}\}\) es no contable.

## Notación

Denotemos

\[
B=\{0,1\}^{\mathbb N},
\]

el conjunto de todas las secuencias binarias infinitas.

## Proposición

El conjunto \(B\) es no contable.

## Demostración (diagonalización de Cantor)

Procedemos por contradicción.

Supongamos que \(B\) es contable. Entonces existe una enumeración

\[
b_1,b_2,b_3,\dots
\]

de todos los elementos de \(B\), donde cada \(b_i\) es una sucesión infinita

\[
b_i=(b_i(1),b_i(2),b_i(3),\dots), \quad b_i(j)\in\{0,1\}.
\]

Definimos una nueva sucesión \(d\in B\) por

\[
d(n)=
\begin{cases}
1 & \text{si } b_n(n)=0,\\
0 & \text{si } b_n(n)=1.
\end{cases}
\]

Entonces, para todo \(n\), se cumple \(d(n)\neq b_n(n)\). En consecuencia,

\[
d\neq b_n \quad \text{para todo } n\in\mathbb N,
\]

porque \(d\) y \(b_n\) difieren al menos en la coordenada \(n\).

Pero \(d\in B\), así que debería aparecer en la enumeración \((b_i)_{i\ge 1}\). Contradicción.

Por lo tanto, \(B\) no es contable.

## Comentario (Sipser)

Este es exactamente el mecanismo diagonal que se usa en Sipser para argumentar que hay más lenguajes que máquinas de Turing, y de allí obtener que existen lenguajes no Turing-reconocibles.
