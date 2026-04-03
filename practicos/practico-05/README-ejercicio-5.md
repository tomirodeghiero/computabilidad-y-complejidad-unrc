# Ejercicio 5

## Enunciado

Mostrar que 3-color es NP-completo.

## Problema

\[
3\text{-}COLOR=\{G \mid G \text{ tiene una coloración propia con 3 colores}\}.
\]

## 1) \(3\)-COLOR está en NP

Dado un certificado (asignación de color a cada vértice), se verifica en tiempo polinomial:

1. que cada vértice tenga un color en \(\{1,2,3\}\),
2. que para toda arista \((u,v)\), \(color(u)\neq color(v)\).

El chequeo recorre vértices y aristas en tiempo \(O(|V|+|E|)\).  
Luego \(3\)-COLOR \(\in\) NP.

## 2) \(3\)-COLOR es NP-hard

Se usa una reducción polinomial clásica desde \(3\)-SAT:

\[
3\text{-}SAT \le_p 3\text{-}COLOR.
\]

La construcción (con gadgets de variables y cláusulas) fuerza:

1. cada variable \(x_i\) a elegir entre dos colores que representan \(x_i=\text{true}\) o \(x_i=\text{false}\),
2. cada cláusula \((\ell_1\vee \ell_2\vee \ell_3)\) a ser satisfacible sólo si al menos uno de sus literales toma el color "true".

La transformación es de tamaño polinomial y preserva satisfacibilidad:

\[
\varphi\in 3\text{-}SAT \iff G_\varphi\in 3\text{-}COLOR.
\]

Como \(3\)-SAT es NP-completo, se concluye que \(3\)-COLOR es NP-hard.

## Conclusión

Como \(3\)-COLOR \(\in\) NP y es NP-hard, resulta:

\[
3\text{-}COLOR \text{ es NP-completo.}
\]
