# Ejercicio 1

## Enunciado

Leer el Capitulo 3 del libro de Sipser.

## Resumen de los conceptos prerrequisito

El Capitulo 3 introduce la maquina de Turing como modelo formal de computo y establece la **tesis de Church-Turing**, segun la cual la nocion intuitiva de algoritmo se identifica con la de funcion computable por una MT. Los conceptos que utilizaremos a partir del Ejercicio 2 son:

- **Definicion formal (Sipser 3.3):** una MT es una 7-tupla
  \[
    M = (Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}}),
  \]
  con \(Q\) conjunto finito de estados, \(\Sigma\) alfabeto de entrada (sin el blanco), \(\Gamma\supseteq \Sigma\cup\{\sqcup\}\) alfabeto de cinta y funcion de transicion \(\delta:Q\times\Gamma\to Q\times\Gamma\times\{L,R\}\).
- **Configuracion:** \(u\,q\,v\) con \(u,v\in\Gamma^*\) representa estado \(q\), cabezal sobre el primer simbolo de \(v\) y contenido de cinta \(uv\) seguido de blancos.
- **Reconocibilidad y decidibilidad (3.5--3.6):** \(L\) es Turing-reconocible si alguna MT lo reconoce; es decidible si alguna MT lo decide (es decir, halta en toda entrada).
- **Variantes (Seccion 3.2):** maquinas multicinta, no deterministas, doblemente infinitas, etc., todas equivalentes en poder a la MT estandar (Teoremas 3.13, 3.16 y Problema 3.11).
- **Enumeradores (Seccion 3.3, Teorema 3.21):** \(L\) es reconocible si y solo si existe un enumerador que enumera \(L\).
- **Tesis de Church-Turing:** la igualdad informal entre "algoritmo" y "MT" justifica describir maquinas a nivel implementacion o de alto nivel.

Cada ejercicio que sigue cita explicitamente las definiciones y resultados del capitulo que invoca.
