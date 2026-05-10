# Ejercicio 4

## Enunciado

Un estado de una MT se dice **inalcanzable** cuando no se puede llegar a el con ningun input. Demostrar que el problema de ver si una MT tiene un estado inalcanzable es indecidible. (Esta es, en la practica, la deteccion de codigo muerto.)

## Formalizacion

Decimos que un estado \(q\) de la MT \(M\) es *inalcanzable* si no existe ninguna entrada \(x\) y ningun paso de la ejecucion de \(M\) sobre \(x\) en el cual \(M\) este en el estado \(q\). Definimos:

\[
UNREACH = \{\langle M\rangle \mid M \text{ tiene al menos un estado inalcanzable}\}.
\]

Queremos mostrar que \(UNREACH\) es indecidible.

## Estrategia

Reduciremos \(A_{TM}\) a \(\overline{UNREACH}\) (equivalentemente, daremos una reduccion many-one tal que "\(M\) acepta \(w\)" se corresponde con "todos los estados de \(M'\) son alcanzables"). Como \(A_{TM}\) es indecidible y la decidibilidad se preserva por complemento, esto basta para concluir que \(UNREACH\) es indecidible.

La idea: a partir de \(\langle M,w\rangle\) construimos una MT \(M'\) con un estado distinguido \(q_*\) (testigo) que sera alcanzable solo si \(M\) acepta \(w\). El resto de los estados de \(M'\) seran alcanzables en cualquier caso, gracias a un "tour inicial" que se ejecuta con ciertas entradas auxiliares y que recorre todos los estados de \(M'\) excepto posiblemente \(q_*\).

## Construccion de \(M'\)

Dado \(\langle M,w\rangle\), construimos la MT \(M'\) con los siguientes estados:

- \(q_0\): estado inicial.
- \(q_R\): estado de rechazo de \(M'\).
- \(q_A\): estado de aceptacion de \(M'\).
- \(q_*\): estado *testigo*, distinguido.
- Estados auxiliares \(q_{sim}\) usados para implementar la simulacion de \(M\) sobre \(w\). Estos se reusan al ejecutar siempre la misma simulacion sobre la palabra fija \(w\) (cableada en la descripcion de \(M'\)).

\(M'=\) "Con entrada \(x\):

1. **Caso 1:** Si \(x=0\), \(M'\) ejecuta una secuencia de movimientos triviales que la llevan por todos los estados de \(M'\) excepto \(q_*\), y luego rechaza (entra en \(q_R\)). Por construccion, todos los estados \(q_0, q_R, q_A, q_{sim},\ldots\) (todos salvo \(q_*\)) son alcanzables a traves de esta entrada.
2. **Caso 2:** Si \(x=1\), \(M'\) simula \(M\) sobre \(w\):
   - Si \(M\) acepta \(w\), \(M'\) transita al estado testigo \(q_*\) y luego a \(q_A\) (acepta).
   - Si \(M\) rechaza \(w\), \(M'\) va a \(q_R\) (rechaza).
3. **Caso 3:** Para cualquier otra entrada \(x\), \(M'\) rechaza (yendo a \(q_R\))."

El paso 1 (un "tour" inicial sobre los estados) es siempre realizable mecanicamente: dada una MT cualquiera, podemos agregar una rutina inicial finita que mueve el cabezal y cambia de estado pasando por cada estado existente al menos una vez, antes de seguir con el comportamiento principal. En nuestro caso solo hace falta diseñar \(M'\) de modo que con la entrada \(0\) recorra (en los primeros pasos) los estados \(q_0,q_R,q_A,q_{sim,1},q_{sim,2},\dots\). Esto es estandar y no usa \(q_*\).

## Computabilidad de la reduccion

La funcion

\[
f(\langle M,w\rangle)=\langle M'\rangle
\]

es computable: a partir de \(\langle M\rangle\) y \(w\), una MT puede generar mecanicamente una nueva descripcion finita que incorpora:

- Los estados nuevos \(q_0,q_R,q_A,q_*\).
- El "tour" inicial sobre la entrada \(0\).
- La rama del paso 2 que simula \(M\) sobre \(w\).
- La rama del paso 3 para cualquier otra entrada.

## Correctitud

Mostramos que

\[
\langle M,w\rangle\in A_{TM} \iff \langle M'\rangle\notin UNREACH.
\]

**(\(\Rightarrow\))** Supongamos que \(M\) acepta \(w\).

- Sobre la entrada \(0\), \(M'\) recorre todos los estados salvo \(q_*\) (paso 1). Asi todos esos estados son alcanzables.
- Sobre la entrada \(1\), \(M'\) simula \(M\) sobre \(w\); como \(M\) acepta \(w\), la simulacion alcanza \(q_*\) (paso 2). Por lo tanto \(q_*\) es alcanzable.

Conclusion: todos los estados de \(M'\) son alcanzables, es decir, \(\langle M'\rangle\notin UNREACH\).

**(\(\Leftarrow\))** Supongamos que \(M\) **no** acepta \(w\) (rechaza o entra en bucle). Entonces:

- Sobre cualquier entrada distinta de \(1\), \(M'\) nunca pasa por \(q_*\) (no entra en la rama del paso 2 que conduce a \(q_*\)).
- Sobre la entrada \(1\), \(M'\) simula \(M\) sobre \(w\); como \(M\) no acepta, la simulacion nunca alcanza \(q_{accept}\) de \(M\), y por ende \(M'\) nunca transita a \(q_*\).

Conclusion: \(q_*\) es inalcanzable, asi que \(\langle M'\rangle\in UNREACH\).

Equivalentemente:

\[
\langle M,w\rangle\notin A_{TM} \iff \langle M'\rangle\in UNREACH,
\]

es decir, \(\overline{A_{TM}}\le_m UNREACH\).

## Conclusion

Hemos construido una reduccion many-one computable de \(\overline{A_{TM}}\) a \(UNREACH\). Como \(A_{TM}\) es indecidible, su complemento \(\overline{A_{TM}}\) tambien lo es (un lenguaje es decidible sii lo es su complemento). Por el Corolario 5.23 de Sipser, \(UNREACH\) es indecidible.

\[
\boxed{UNREACH \text{ es indecidible.}}
\]

## Observacion: interpretacion practica

Como menciona la nota al pie del enunciado, este resultado puede leerse como: **el problema de detectar codigo muerto en una MT (estados a los que ningun flujo de entrada llega) es indecidible**. Esto justifica por que las herramientas reales de analisis de codigo muerto usan aproximaciones conservadoras: sobre una MT (modelo general de computadora) la pregunta exacta no admite algoritmo.
