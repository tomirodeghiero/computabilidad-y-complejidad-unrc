# Ejercicio 2

## Enunciado

Describir dos máquina de Turing \(M\) y \(N\) tal que cuando comienza en cualquier input, \(M\) imprime \(\langle N\rangle\) y \(N\) imprime \(\langle M\rangle\).

## Construccion (idea formal)

Definimos dos transformaciones computables sobre descripciones de MT:

1. \(F(x)\): devuelve la descripción de una MT que, ignorando la entrada, imprime \(x\) y se detiene.
2. \(G(x)\): devuelve la descripción de una MT que, ignorando la entrada, imprime \(x\) y se detiene.

Ahora buscamos \(m,n\) tales que:

\[
m = F(n), \qquad n = G(m).
\]

Esto se obtiene por una construcción de punto fijo (autorreferencia mutua, variante del Teorema de la Recursión).

Tomamos:

\[
\langle M\rangle = m, \qquad \langle N\rangle = n.
\]

Entonces:

- \(M\), en toda entrada, imprime \(n=\langle N\rangle\).
- \(N\), en toda entrada, imprime \(m=\langle M\rangle\).

## Version operativa en pseudocodigo de alto nivel

- `M(w): escribir <N>; halt`
- `N(w): escribir <M>; halt`

La sutileza está en justificar que tales descripciones existen de manera efectiva; eso es precisamente lo que garantiza el principio de autorreferencia de máquinas de Turing.
