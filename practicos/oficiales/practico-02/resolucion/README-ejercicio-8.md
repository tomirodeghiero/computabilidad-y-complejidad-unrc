# Ejercicio 8

## Enunciado

Demostrar que si \(A\) es reconocible y \(A\le_m \overline{A}\), entonces \(A\) es decidible.

(Este es el Ejercicio 5.7 de Sipser.)

## Proposicion

Si \(A\) es Turing-reconocible y \(A\le_m \overline{A}\), entonces \(A\) es decidible.

## Idea

Usaremos dos resultados clave:

1. **Teorema 4.22 de Sipser:** \(A\) es decidible si y solo si \(A\) y \(\overline{A}\) son ambos Turing-reconocibles.
2. **Teorema 5.28 de Sipser:** si \(X\le_m Y\) y \(Y\) es Turing-reconocible, entonces \(X\) es Turing-reconocible.

Ya tenemos que \(A\) es reconocible. La idea sera mostrar que \(\overline{A}\) tambien es reconocible, usando la hipotesis \(A\le_m \overline{A}\), lo cual implica (por simetria de la reduccion) \(\overline{A}\le_m A\).

## Demostracion

### Paso 1: De \(A\le_m \overline{A}\) deducimos \(\overline{A}\le_m A\) con la misma \(f\)

Sea \(f\) una funcion computable que reduce \(A\) a \(\overline{A}\). Por definicion, para toda cadena \(x\),

\[
x\in A \iff f(x)\in \overline{A}.
\]

Negando ambos lados de la equivalencia:

\[
x\notin A \iff f(x)\notin \overline{A}.
\]

Pero \(x\notin A\) es lo mismo que \(x\in\overline{A}\), y \(f(x)\notin\overline{A}\) es lo mismo que \(f(x)\in A\). Por lo tanto:

\[
x\in\overline{A} \iff f(x)\in A.
\]

Esto significa que la **misma** funcion \(f\) reduce \(\overline{A}\) a \(A\):

\[
\overline{A}\le_m A.
\]

### Paso 2: Como \(A\) es reconocible, \(\overline{A}\) tambien lo es

Por hipotesis \(A\) es Turing-reconocible. Aplicando el Teorema 5.28 de Sipser (preservacion de reconocibilidad bajo \(\le_m\)) a la reduccion \(\overline{A}\le_m A\):

\[
\overline{A} \text{ es Turing-reconocible}.
\]

Concretamente, si \(M_A\) reconoce \(A\), un reconocedor de \(\overline{A}\) procede asi:

\(R_{\overline A} =\) "Con entrada \(x\):

1. Computar \(f(x)\).
2. Simular \(M_A\) sobre \(f(x)\). Si \(M_A\) acepta, aceptar."

Por el Paso 1, \(R_{\overline A}\) acepta exactamente \(\overline{A}\).

### Paso 3: Aplicar el Teorema 4.22

Tenemos:

- \(A\) reconocible (hipotesis).
- \(\overline{A}\) reconocible (paso 2).

Por el Teorema 4.22 de Sipser, un lenguaje es decidible si y solo si tanto el como su complemento son reconocibles. Concluimos que

\[
A \text{ es decidible}.
\]

## Conclusion

\[
\boxed{A \text{ reconocible y } A\le_m \overline{A} \;\Rightarrow\; A \text{ decidible.}}
\]

## Observacion: por que el resultado es interesante

Este ejercicio nos da una *via* para decidir lenguajes: si encontramos una reduccion many-one entre \(A\) y \(\overline{A}\) y sabemos que \(A\) es reconocible, entonces no solo es reconocible sino tambien decidible. Esta es una herramienta util para "subir de nivel" en la jerarquia de Turing (de reconocible a decidible) usando informacion estructural sobre el lenguaje y su complemento.

El contrapositivo tambien es informativo: si \(A\) es reconocible pero **no** decidible (por ejemplo \(A=A_{TM}\)), entonces necesariamente \(A\not\le_m \overline{A}\). Asi, esta tecnica explica por que \(A_{TM}\not\le_m \overline{A_{TM}}\) (como pide mostrar el Ejercicio 5.5 de Sipser).
