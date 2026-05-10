# Practico 01 - Maquinas de Turing (Resolucion)

Resolucion mejorada del Practico 1 - *Maquinas de Turing* de la asignatura **Computabilidad y Complejidad** (Teoria de la Computacion II), Primer Cuatrimestre de 2026, FCEFQyN - UNRC.

## Fundamento teorico

Las soluciones se apoyan en:

- **Capitulo 3 del libro de Sipser** (`chapter-03.pdf`), en particular:
  - Definicion 3.3 (MT como 7-tupla) y Definicion 3.5--3.6 (reconocible vs decidible).
  - Ejemplo 3.7 (la maquina \(M_2\) que decide \(\{0^{2^n}\mid n\ge 0\}\)).
  - Seccion 3.2 (variantes de MT: multicinta, no determinismo).
  - Teorema 3.13 (multicinta \(\equiv\) una cinta).
  - Teorema 3.21 / Problema 3.19 (todo lenguaje reconocible infinito tiene un subconjunto decidible infinito).
  - Problema 3.11 (cinta doblemente infinita) y Problema 3.20 (read-only sobre el input).
- **Teoria en PDF de la catedra** (`Diag.pdf` de Pablo Castro):
  - Codificacion de problemas como lenguajes y nocion de decidibilidad/reconocibilidad.
  - Cardinalidad y existencia de lenguajes no computables.
  - El problema de la terminacion y la indecibilidad de \(A_{TM}\) por diagonalizacion.

## Convencion de notacion

- \(\Sigma\) es el alfabeto de entrada y \(\Gamma\) el alfabeto de cinta (con \(\Sigma\subseteq\Gamma\)).
- \(\sqcup\) (o \(\bot\) en algunos pasajes) denota el simbolo blanco; \(\sqcup\in\Gamma\setminus\Sigma\).
- Una *configuracion* se escribe \(u\,q\,v\), con \(u,v\in\Gamma^*\) y \(q\in Q\), e indica que el contenido de la cinta es \(uv\) (seguido de blancos), el estado actual es \(q\) y el cabezal esta sobre el primer simbolo de \(v\).
- \(L(M)\) es el lenguaje reconocido por \(M\).
- "Reconocible" = Turing-reconocible; "decidible" = Turing-decidible.

## Indice

| Ejercicio | Tema | Archivo |
|-----------|------|---------|
| 1 | Lectura del Capitulo 3 de Sipser | `README-ejercicio-1.md` |
| 2 | Secuencia de configuraciones de \(M_2\) sobre `0`, `00`, `000`, `000000` | `README-ejercicio-2.md` |
| 3 | Deciders para \(\{w:\#_0(w)=\#_1(w)\}\) y \(\{w:\#_0(w)=2\#_1(w)\}\) | `README-ejercicio-3.md` |
| 4 | Equivalencia: cinta doblemente infinita \(\equiv\) cinta estandar | `README-ejercicio-4.md` |
| 5 | Todo lenguaje reconocible infinito contiene un subconjunto decidible infinito | `README-ejercicio-5.md` |
| 6 | MT con input read-only solo reconoce regulares | `README-ejercicio-6.md` |
| Programacion | Implementaciones en Python y traducciones entre modelos | `README-programacion.md` |

## Archivo LaTeX

Ademas de los README por ejercicio, se incluye `practico-01.tex` con la version final unificada en LaTeX, en el mismo estilo del Practico 02.
