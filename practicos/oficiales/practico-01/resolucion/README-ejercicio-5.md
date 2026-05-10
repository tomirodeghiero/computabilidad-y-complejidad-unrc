# Ejercicio 5

## Enunciado

Demostrar que cualquier lenguaje infinito que es reconocible por una maquina de Turing tiene un subconjunto infinito que es decidible (Problema 3.19 de Sipser).

## Proposicion

Sea \(A\subseteq\Sigma^*\) un lenguaje infinito y Turing-reconocible. Entonces existe \(B\subseteq A\) tal que:

1. \(B\) es infinito.
2. \(B\) es decidible.

## Idea

La estrategia es construir un decidor \(D_B\) que enumere las palabras de \(B\) en orden creciente segun un orden total efectivo, y use ese orden para decidir pertenencia. Para que la enumeracion en orden creciente sea efectiva, partimos de un *enumerador* \(E\) de \(A\) (que existe por el Teorema 3.21 de Sipser) y construimos una subsecuencia estrictamente creciente.

## Demostracion

Como \(A\) es Turing-reconocible, por el **Teorema 3.21 de Sipser** existe un enumerador \(E\) que enumera \(A\). Es decir, \(E\) es una MT (con cinta de impresion) que produce, sin orden particular y posiblemente con repeticiones, la sucesion de las palabras de \(A\):
\[
  A = \{\, s : E \text{ imprime } s\text{ en algun momento}\,\}.
\]

Fijamos un orden total efectivo sobre \(\Sigma^*\); usaremos el **orden shortlex** (primero por longitud y luego lexicograficamente):
\[
  u < v \iff |u|<|v| \;\lor\; (|u|=|v| \;\land\; u<_{\text{lex}} v).
\]
Es un orden total bien fundado y efectivamente comparable: dadas dos cadenas \(u,v\), se puede decidir si \(u<v\) en tiempo finito comparando longitud y, en caso de empate, simbolo a simbolo.

### 1) Construccion de una sucesion creciente \(b_1<b_2<b_3<\cdots\) en \(A\)

Definimos \((b_i)_{i\ge 1}\) inductivamente:

- \(b_1\) es la primera palabra que imprime \(E\).
- Supuesto definido \(b_i\), tomamos \(b_{i+1}\) como la **primera** palabra que imprime \(E\) (en el orden de impresion de \(E\)) que satisface \(b_{i+1}>b_i\) en el orden shortlex.

Esta definicion es **efectiva** porque:

1. Para cada \(i\), un algoritmo puede simular paso a paso a \(E\) hasta ver imprimir una nueva palabra y decidir si es mayor o menor que \(b_i\) usando shortlex.
2. Como \(A\) es infinito, hay infinitas palabras en \(A\) y, en particular, infinitas palabras \(>b_i\) en shortlex (toda longitud suficientemente grande aporta candidatos). Como \(E\) imprime cada palabra de \(A\) en algun momento, en tiempo finito aparece una palabra \(>b_i\), que tomamos como \(b_{i+1}\).

Definimos
\[
  B = \{b_1, b_2, b_3, \dots\}.
\]

Por construccion:

- Cada \(b_i\) fue impresa por \(E\), luego \(b_i\in A\). Por lo tanto \(B\subseteq A\).
- La sucesion es estrictamente creciente, asi que todos los \(b_i\) son distintos. Como hay infinitos \(i\), \(B\) es **infinito**.

### 2) \(B\) es decidible

Construimos un decidor \(D_B\):

\(D_B =\) "Con entrada \(x\):

1. Generar \(b_1, b_2, b_3, \dots\) de a uno usando la construccion del paso 1.
2. Detenerse en el primer \(b_k\) con \(b_k\ge x\) (en el orden shortlex).
3. Si \(b_k = x\), aceptar. Si \(b_k > x\), rechazar."

#### Correctitud

- **Si \(x\in B\):** existe \(k\) con \(x=b_k\). Por la propiedad de monotonia, en cuanto la enumeracion alcanza \(b_k\), se cumple \(b_k\ge x\); como \(b_k=x\), \(D_B\) acepta.
- **Si \(x\notin B\):** sea \(k\) el primer indice con \(b_k\ge x\). No puede ser \(b_k=x\) (porque \(x\notin B\)), asi que \(b_k>x\). Por la monotonia y el hecho de que \(b_{k-1}<x\) (si \(k>1\)) o \(x\) precede a \(b_1\) en shortlex (si \(k=1\)), \(x\) no aparece en \(B\), y \(D_B\) rechaza.

#### Terminacion

Bajo el orden shortlex, el conjunto \(\{y\in\Sigma^* : y\le x\}\) es finito (a lo sumo \(\sum_{i=0}^{|x|}|\Sigma|^i\) palabras). Como \((b_i)\) es estrictamente creciente, en a lo sumo finitos pasos se alcanza algun \(b_k\ge x\). Cada \(b_i\) se calcula en tiempo finito siguiendo \(E\). Luego \(D_B\) **siempre** se detiene.

## Conclusion

\(B\) es un subconjunto infinito y decidible de \(A\). Por lo tanto:

> Todo lenguaje infinito Turing-reconocible contiene un subconjunto infinito decidible.

## Comentario

El argumento es esencialmente el truco de **enumeracion en orden creciente**. Es interesante notar que un lenguaje reconocible no es en general decidible (como muestra \(A_{TM}\), Capitulo 4 de Sipser y la teoria de la catedra), pero **siempre** se puede aislar dentro de el una "porcion" decidible que conserve la cardinalidad. Asi, la frontera entre reconocible y decidible se nota mas en el comportamiento global que en la "abundancia" de elementos.

Otro modo de ver el resultado: el enumerador \(E\) puede tener un comportamiento desordenado (palabras pequeñas mezcladas con palabras grandes, repeticiones), pero a partir de \(E\) podemos siempre extraer una **enumeracion estrictamente creciente y efectiva** de un subconjunto, y un lenguaje admite una enumeracion creciente efectiva si y solo si es decidible (Problema 3.18 de Sipser).
