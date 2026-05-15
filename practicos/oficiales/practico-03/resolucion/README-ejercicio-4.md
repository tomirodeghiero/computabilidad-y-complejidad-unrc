# Ejercicio 4

## Enunciado

Usar la propiedad de que el conjunto de lenguajes es incontable para demostrar que existen lenguajes que no pueden ser reconocidos con una maquina con un oraculo \(A_{TM}\).

## Idea

La estrategia es un argumento clasico de *cardinalidad* (Cantor):

- El conjunto de **lenguajes** sobre cualquier alfabeto \(\Sigma\) no vacio es **incontable** (Corolario 4.18 de Sipser).
- El conjunto de **maquinas de Turing con oraculo** para \(A_{TM}\) es **contable**: cada una es un objeto finito y se codifica como una cadena.
- Por lo tanto, el conjunto de lenguajes reconocibles por una MT con oraculo \(A_{TM}\) es contable.
- Una *funcion sobreyectiva* de un conjunto contable a un conjunto incontable es imposible. Luego, existen lenguajes que **no** son reconocibles por ninguna MT con oraculo \(A_{TM}\).

Este es el mismo argumento que Sipser usa para probar la existencia de lenguajes no reconocibles (Teorema 4.17 / Corolario 4.18), pero "subido un nivel": ahora la maquina dispone de un oraculo para \(A_{TM}\). El resultado se mantiene porque agregar un oraculo no agranda la cardinalidad de las maquinas.

## Recordatorios

### Cardinalidad de los lenguajes

Sea \(\Sigma\) un alfabeto finito no vacio. \(\Sigma^*\) es contable (las cadenas se enumeran por longitud y, dentro de cada longitud, lexicograficamente). El conjunto de **lenguajes** sobre \(\Sigma\) es:

\[
\mathcal{P}(\Sigma^*) = \{ L \mid L \subseteq \Sigma^* \}.
\]

Por el Teorema de Cantor, \(\mathcal{P}(\Sigma^*)\) tiene cardinal estrictamente mayor que \(\Sigma^*\); en particular, **es incontable**. Equivalentemente: cualquier funcion \(f:\mathbb{N}\to\mathcal{P}(\Sigma^*)\) deja afuera algun lenguaje (diagonalizacion).

### MT con oraculo

**Definicion 6.18 de Sipser.** Una *MT con oraculo* para un lenguaje \(B\) es una MT \(M^B\) con la capacidad adicional de consultar, en un solo paso, si una cadena \(w\) pertenece o no a \(B\). Formalmente se modela con una cinta de oraculo y dos estados especiales \(q_?\), \(q_{\text{sí}}\), \(q_{\text{no}}\).

Cada MT con oraculo \(M^B\) se describe en su totalidad por:
- el alfabeto de cinta \(\Gamma\),
- el conjunto finito de estados \(Q\),
- la funcion de transicion (incluyendo los estados de oraculo).

La descripcion es finita y se codifica como una cadena \(\langle M^B\rangle\) sobre un alfabeto finito fijo. La codificacion no depende de \(B\) (solo se introduce un par de estados especiales para representar la consulta).

## Demostracion

### Proposicion

Existe un lenguaje \(L\subseteq\Sigma^*\) que **no** es reconocido por ninguna maquina de Turing con oraculo \(A_{TM}\).

### Prueba

**1. Las MT con oraculo \(A_{TM}\) son contables.**

Sea \(\mathcal{M}_{A_{TM}}\) la familia de todas las MT con oraculo \(A_{TM}\). Cada \(M\in\mathcal{M}_{A_{TM}}\) tiene una descripcion finita \(\langle M\rangle\in\Sigma^*\). Por lo tanto la asignacion

\[
M \;\longmapsto\; \langle M\rangle
\]

es una inyeccion de \(\mathcal{M}_{A_{TM}}\) en \(\Sigma^*\). Como \(\Sigma^*\) es contable, \(\mathcal{M}_{A_{TM}}\) tambien lo es.

**2. La familia de lenguajes reconocidos por \(\mathcal{M}_{A_{TM}}\) es contable.**

Definamos la funcion

\[
\Phi: \mathcal{M}_{A_{TM}} \;\longrightarrow\; \mathcal{P}(\Sigma^*),\qquad \Phi(M) = L(M).
\]

Sea

\[
\mathcal{R}_{A_{TM}} \;=\; \Phi(\mathcal{M}_{A_{TM}}) \;=\; \{\, L(M) : M\in\mathcal{M}_{A_{TM}}\,\}.
\]

Como la imagen de un conjunto contable bajo cualquier funcion es contable, \(\mathcal{R}_{A_{TM}}\) es **contable**.

**3. El conjunto de todos los lenguajes es incontable.**

Por Cantor (Corolario 4.18 de Sipser), \(\mathcal{P}(\Sigma^*)\) es incontable.

**4. Conclusion.**

Comparando cardinalidades:

\[
|\mathcal{R}_{A_{TM}}| \;\le\; \aleph_0 \;<\; 2^{\aleph_0} \;=\; |\mathcal{P}(\Sigma^*)|.
\]

Por lo tanto

\[
\mathcal{R}_{A_{TM}} \;\subsetneq\; \mathcal{P}(\Sigma^*),
\]

y existe \(L\in\mathcal{P}(\Sigma^*)\setminus \mathcal{R}_{A_{TM}}\). Ese \(L\) no es reconocido por ninguna MT con oraculo \(A_{TM}\). \(\blacksquare\)

## Interpretacion

Este resultado es interesante porque pone en perspectiva el poder de los oraculos:

- Una MT con oraculo \(A_{TM}\) puede decidir muchos problemas indecidibles (por ejemplo, \(E_{TM}\), \(HALT_{TM}\), \(EQ_{TM}\); ver Ejemplo 6.19 y Ejercicio 6.4 de Sipser).
- Sin embargo, el "salto" sigue siendo finito en terminos de cardinalidad: solo se pueden reconocer una cantidad numerable de lenguajes mas.
- Como hay incontables lenguajes, *cualquier* maquina con un oraculo concreto deja afuera incontables lenguajes.

Es decir, el argumento de cardinalidad es **invariante bajo cambios de oraculo**: vale para MT estandar, para MT con oraculo \(A_{TM}\), e incluso para MT con cualquier oraculo *fijo*.

## Generalizacion

El argumento prueba algo mas general:

> Para cualquier lenguaje \(B\subseteq\Sigma^*\), existen lenguajes que no son reconocidos por ninguna MT con oraculo \(B\).

En efecto, la descripcion de las MT con oraculo \(B\) sigue siendo una cadena finita; la familia de tales maquinas es contable; y la familia de lenguajes \(\mathcal{P}(\Sigma^*)\) es incontable.

Este resultado es exactamente el contenido del **Problema 6.19** de Sipser, que es el ejercicio que se nos pide resolver.

## Conclusion

\[
\boxed{\;\text{Existe } L\subseteq\Sigma^* \text{ tal que } L \notin \{ L(M^{A_{TM}}) : M \text{ es MT}\}.\;}
\]

El resultado se obtiene comparando cardinalidades: las MT con oraculo \(A_{TM}\) son contables, mientras que los lenguajes son incontables.
