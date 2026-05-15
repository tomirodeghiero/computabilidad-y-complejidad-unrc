# Practico 03 - Autoreferencia y Teorema de la Recursion (Resolucion)

Resolucion del Practico 3 - *AutoReferencia* de la asignatura **Computabilidad y Complejidad** (Teoria de la Computacion II), Primer Cuatrimestre de 2026, FCEFQyN - UNRC.

## Fundamento teorico

Las soluciones se apoyan principalmente en:

- **Capitulo 6 del libro de Sipser** (`chapter-06.pdf`), en particular:
  - Seccion 6.1 *The Recursion Theorem* (Lema 6.1, construccion de `SELF`, Teorema 6.3, Teorema 6.5, Teorema 6.7, Teorema 6.8).
  - Seccion 6.3 *Turing Reducibility* (Definicion 6.18 de oraculo, Definicion 6.20 de \(\le_T\), Teorema 6.21, Ejemplo 6.19).
  - Problema 6.6 (dos MT que se imprimen mutuamente).
  - Problema 6.19 (existencia de lenguajes no reconocibles por MT con oraculo \(A_{TM}\)).
  - Corolario 4.18 (la cantidad de lenguajes sobre \(\Sigma\) es incontable).
- **Laminas teoricas de la catedra** (`autoref.pdf`) de Pablo Castro:
  - Construccion explicita de la MT `Self` y de las MT `A` y `B` que la componen.
  - Enunciado del Teorema de la Recursion y su uso para reprobar la indecibilidad de \(A_{TM}\).
  - Lenguaje \(MIN\) y su no-reconocibilidad.
  - Maquinas con oraculos y reducibilidad de Turing \(\le_T\).
- **Introspeccion en Python**: modulo estandar `inspect` (`getmembers`, `getsource`, `getsourcelines`, `signature`), funcion `type()` como constructor dinamico de clases, atributos especiales `__dict__`, `__name__`, `__bases__`, etc. Estos contenidos son la "version concreta" del Teorema de la Recursion en un lenguaje de programacion real.

## Convencion de notacion

- \(\Sigma\) es un alfabeto y \(\Sigma^*\) el conjunto de cadenas finitas sobre \(\Sigma\).
- \(\langle M\rangle\) denota la descripcion (codificacion como cadena) de la MT \(M\); analogamente \(\langle M,w\rangle\) codifica un par MT-input.
- \(L(M)\) es el lenguaje reconocido por \(M\).
- \(A_{TM}=\{\langle M,w\rangle \mid M \text{ acepta } w\}\).
- \(M^{O}\) denota una MT \(M\) con un oraculo para el lenguaje \(O\).
- \(A\le_T B\) significa que \(A\) es decidible relativo a \(B\); es decir, existe \(M^B\) que decide \(A\) (Definicion 6.20 de Sipser).
- Cuando hablamos de "MT que imprime \(x\)" entendemos que al detenerse deja \(x\) escrito en la cinta (no es necesario un mecanismo de E/S externo).

## Indice de archivos

El **Ejercicio 1** del enunciado consiste en leer el Capitulo 6 de Sipser; no requiere resolucion escrita y se asume realizado como prerequisito teorico.

| Ejercicio | Tema | Archivo |
|-----------|------|---------|
| 2 | Implementacion en Python de la funcion `Self` que se reproduce | `README-ejercicio-2.md` |
| 3 | Dos MT \(M, N\) tales que \(M\) imprime \(\langle N\rangle\) y \(N\) imprime \(\langle M\rangle\) | `README-ejercicio-3.md` |
| 4 | Cardinalidad: existen lenguajes no reconocibles ni con oraculo \(A_{TM}\) | `README-ejercicio-4.md` |
| 5 | Clase `Persona` e introspeccion con `inspect` | `README-ejercicio-5.md` |
| 6 | Creacion dinamica de una clase usando introspeccion / `type()` | `README-ejercicio-6.md` |

> **Nota sobre el enunciado.** El item 3 del enunciado del practico (`practica03.pdf`) tiene una pequena errata: pide "\(M\) imprime \(\langle M\rangle\), y \(N\) imprime \(\langle M\rangle\)". Tanto la version original en Sipser (Problema 6.6) como las laminas de catedra (`autoref.pdf`) piden "\(M\) imprime \(\langle N\rangle\) y \(N\) imprime \(\langle M\rangle\)", que es lo que realmente representa un par de programas que se imprimen mutuamente. Resolvemos la version corregida.

## Archivo LaTeX

Ademas de los README por ejercicio, en el directorio padre `practico-03/` se incluyen:

- `resolucion-practico-03.tex`/`.pdf`: version final unificada en LaTeX de las resoluciones, en el mismo estilo del Practico 01 y 02.
- `resumen-teorico-practico-03.tex`/`.pdf`: resumen teorico-practico (recursion, autoreferencia, MT con oraculo, introspeccion).
