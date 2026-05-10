# Practico 02 - Reducciones (Resolucion)

Resolucion del Practico 2 - *Reducciones* de la asignatura **Computabilidad y Complejidad** (Teoria de la Computacion II), Primer Cuatrimestre de 2026, FCEFQyN - UNRC.

## Fundamento teorico

Las soluciones se apoyan principalmente en:

- **Capitulo 5 del libro de Sipser** (`chapter-05.pdf`), en particular las secciones:
  - 5.1 *Undecidable problems from language theory* (problemas \(A_{TM}\), \(HALT_{TM}\), \(E_{TM}\), \(REGULAR_{TM}\), \(EQ_{TM}\), \(E_{LBA}\)).
  - 5.2 *A simple undecidable problem* (Problema de Correspondencia de Post).
  - 5.3 *Mapping reducibility* (definicion formal de \(\le_m\), Teorema 5.22, Corolario 5.23, Teorema 5.28).
  - Problema 5.28 (Teorema de Rice).
- **Teoria en PDF** (`Reducibilidad.pdf`) de Pablo Castro, en particular las laminas sobre:
  - Idea general de reduccion para indecidibilidad.
  - Reducciones de \(A_{TM}\) a \(HALT_{TM}\), \(E_{TM}\), \(REG_{TM}\), \(EQ_{TM}\).
  - Problema de Correspondencia de Post.
  - Teorema de Rice.
  - Funciones computables y nocion formal de \(\le_m\).

## Convencion de notacion

- \(\Sigma\) denota el alfabeto de entrada y \(\Sigma^*\) el conjunto de cadenas sobre \(\Sigma\).
- \(\langle M\rangle\) denota una codificacion (descripcion) de la MT \(M\) como cadena.
- \(\langle M,w\rangle\) denota una codificacion del par MT y entrada.
- \(L(M)\) o \(\mathcal L(M)\) es el lenguaje reconocido por \(M\).
- \(\overline{A}\) denota el complemento de \(A\) (es decir, \(\Sigma^*\setminus A\)).
- \(A\le B\) significa \(A\le_m B\): existe una funcion computable \(f\) tal que \(x\in A \iff f(x)\in B\).
- "Indecidible" = no es Turing-decidible.
- "Reconocible" = Turing-reconocible (existe una MT que acepta exactamente las cadenas de \(A\)).

Lenguajes de referencia que se asumen *indecidibles*:

\[
\begin{aligned}
A_{TM} &= \{\langle M,w\rangle \mid M \text{ es una MT que acepta } w\},\\
HALT_{TM} &= \{\langle M,w\rangle \mid M \text{ se detiene con entrada } w\},\\
E_{TM} &= \{\langle M\rangle \mid L(M)=\emptyset\}.
\end{aligned}
\]

## Indice de archivos

El **Ejercicio 1** del enunciado consiste en leer el Capitulo 5 de Sipser; no requiere resolucion escrita y se asume realizado como prerequisito teorico.

| Ejercicio | Tema | Archivo |
|-----------|------|---------|
| 2 | MT que mueve el cabezal a la izquierda desde el extremo izquierdo | `README-ejercicio-2.md` |
| 3 | Lenguaje \(T=\{\langle M\rangle \mid M\text{ acepta }w^R \text{ si acepta }w\}\) | `README-ejercicio-3.md` |
| 4 | Existencia de estados inalcanzables (codigo muerto) | `README-ejercicio-4.md` |
| 5 | Matching para una instancia del Problema de Post | `README-ejercicio-5.md` |
| 6 | Transitividad de \(\le_m\) | `README-ejercicio-6.md` |
| 7 | \(A\le_m B\) con \(B\) regular: implica que \(A\) es regular? | `README-ejercicio-7.md` |
| 8 | Si \(A\) es reconocible y \(A\le_m \overline{A}\), entonces \(A\) es decidible | `README-ejercicio-8.md` |
| 9 | \(A\) es reconocible sii \(A\le_m A_{TM}\) | `README-ejercicio-9.md` |
| 10 | Indecibilidad de \(All=\{\langle M\rangle \mid L(M)=\Sigma^*\}\) por Rice | `README-ejercicio-10.md` |
