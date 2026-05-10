# Ejercicio 3

## Enunciado

Sea \(T=\{\langle M\rangle \mid M \text{ es una MT que acepta } w^R \text{ si esta acepta } w\}\). Mostrar que este lenguaje es indecidible.

## Interpretacion

La condicion "\(M\) acepta \(w^R\) si acepta \(w\)" se entiende para *toda* cadena \(w\). Es decir, \(T\) es el conjunto de descripciones de MT cuyo lenguaje es **cerrado bajo reverso**:

\[
T = \{\langle M\rangle \mid \forall w\in\Sigma^*: w\in L(M)\Rightarrow w^R\in L(M)\}.
\]

Una observacion importante es que \(T\) depende solo de \(L(M)\) y no de la sintaxis o estructura interna de \(M\). Es decir, si \(L(M_1)=L(M_2)\), entonces \(\langle M_1\rangle\in T\) sii \(\langle M_2\rangle\in T\). Esto convierte a \(T\) en una *propiedad semantica* sobre lenguajes, lo cual sera relevante mas abajo.

## Estrategia

Daremos una reduccion directa \(A_{TM}\le_m T\) (en el espiritu de las reducciones del Capitulo 5 y de la teoria en `Reducibilidad.pdf`). Tambien observaremos que el resultado se deduce mas brevemente del Teorema de Rice.

## Reduccion \(A_{TM}\le_m T\)

Dada una entrada \(\langle M,w\rangle\), construimos la descripcion de una MT \(M_w\) cuyo lenguaje es cerrado bajo reverso si y solo si \(M\) acepta \(w\).

La idea es elegir un par de cadenas \(u\) y \(u^R\) con \(u\neq u^R\), por ejemplo \(u=01\) y \(u^R=10\), y disenar \(M_w\) para que:

- Acepte siempre \(u\).
- Acepte \(u^R\) **solo** si \(M\) acepta \(w\).
- Rechace cualquier otra cadena.

Asi, el lenguaje de \(M_w\) sera \(\{u,u^R\}\) (cerrado bajo reverso) cuando \(M\) acepte \(w\), y sera \(\{u\}\) (no cerrado bajo reverso, ya que \(u^R\notin\{u\}\)) en caso contrario.

### Definicion de \(M_w\)

\(M_w=\) "Con entrada \(x\):

1. Si \(x=01\), aceptar.
2. Si \(x=10\), simular \(M\) sobre \(w\). Si \(M\) acepta \(w\), aceptar; si \(M\) rechaza, rechazar.
3. Si \(x\) es cualquier otra cadena, rechazar."

La descripcion de \(M_w\) es construible algoritmicamente a partir de \(\langle M,w\rangle\): basta agregar a \(M\) algunos estados que primero comparen la entrada con \(01\) o \(10\), y en el caso \(10\) deriven al subprograma que simula \(M\) sobre \(w\). Por lo tanto, la funcion

\[
f(\langle M,w\rangle)=\langle M_w\rangle
\]

es **computable**.

## Correctitud

Verificamos que \(\langle M,w\rangle\in A_{TM} \iff \langle M_w\rangle\in T\).

**(\(\Rightarrow\))** Si \(M\) acepta \(w\):

- Para \(x=01\): \(M_w\) acepta (paso 1).
- Para \(x=10\): \(M_w\) simula \(M\) sobre \(w\), que acepta, por lo que \(M_w\) acepta.
- Cualquier otra \(x\): \(M_w\) rechaza.

Asi \(L(M_w)=\{01,10\}\). Este lenguaje es cerrado bajo reverso (\(01^R=10\in L(M_w)\) y \(10^R=01\in L(M_w)\)). Luego \(\langle M_w\rangle\in T\).

**(\(\Leftarrow\))** Si \(M\) **no** acepta \(w\) (rechaza o entra en bucle):

- Para \(x=01\): \(M_w\) acepta.
- Para \(x=10\): \(M_w\) simula \(M\) sobre \(w\), que no acepta. Entonces \(M_w\) no acepta \(10\) (rechaza si \(M\) rechaza, o entra en bucle si \(M\) entra en bucle; en ambos casos \(10\notin L(M_w)\)).
- Cualquier otra \(x\): \(M_w\) rechaza.

Por lo tanto \(L(M_w)=\{01\}\), y este lenguaje **no** es cerrado bajo reverso porque \(01^R=10\in L(M_w)\) seria requerido pero \(10\notin L(M_w)\). Luego \(\langle M_w\rangle\notin T\).

Concluimos:

\[
\langle M,w\rangle\in A_{TM} \iff \langle M_w\rangle\in T.
\]

## Conclusion

La reduccion \(f(\langle M,w\rangle)=\langle M_w\rangle\) es computable y satisface

\[
A_{TM}\le_m T.
\]

Como \(A_{TM}\) es indecidible, por el Corolario 5.23 de Sipser \(T\) tambien es indecidible.

\[
\boxed{T \text{ es indecidible.}}
\]

## Demostracion alternativa por Teorema de Rice

Una via mas breve usa el Teorema de Rice (Problema 5.28 de Sipser; ver tambien las laminas de la teoria):

- \(T\) define una propiedad semantica de lenguajes reconocibles, ya que pertenecer a \(T\) depende solo de \(L(M)\) (es invariante bajo equivalencia de lenguajes).
- \(T\) es **no trivial**:
  - Existe \(M\) con \(L(M)=\emptyset\), trivialmente cerrado bajo reverso, asi que \(\langle M\rangle\in T\); luego \(T\neq\emptyset\).
  - Existe \(M\) con \(L(M)=\{01\}\) (una MT que acepta unicamente \(01\)). Como \(10=01^R\notin L(M)\), \(\langle M\rangle\notin T\); luego \(T\neq\{\langle M\rangle\}\).

Por Rice, \(T\) es indecidible.
