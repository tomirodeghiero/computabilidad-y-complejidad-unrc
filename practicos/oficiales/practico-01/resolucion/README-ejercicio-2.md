# Ejercicio 2

## Enunciado

Para la maquina de Turing \(M_2\) dada en clases (Ejemplo 3.7 de Sipser), dar la secuencia de configuraciones que recorre con las entradas:

(a) `0`, (b) `00`, (c) `000`, (d) `000000`.

## La maquina \(M_2\)

\(M_2\) es la MT que decide
\[
  A = \{0^{2^n}\mid n\ge 0\},
\]
es decir, las cadenas de ceros cuya longitud es una potencia de 2. Su descripcion de alto nivel (Sipser, pag. 171) es:

```
M_2 = "Con entrada w:
  1. Recorrer la cinta de izquierda a derecha tachando cada segundo 0.
  2. Si en la etapa 1 quedo un solo 0, aceptar.
  3. Si en la etapa 1 quedaron mas de un 0 y la cantidad fue impar, rechazar.
  4. Volver al inicio de la cinta.
  5. Volver a la etapa 1."
```

Cada pasada divide a la mitad la cantidad de ceros: si la longitud no es potencia de 2, en algun momento la cantidad sera impar y \(M_2\) rechazara; si la longitud es potencia de 2, terminara con un unico cero y aceptara.

### Definicion formal

\[
  M_2 = (Q, \Sigma, \Gamma, \delta, q_1, q_{\text{accept}}, q_{\text{reject}}),
\]
con
- \(Q = \{q_1, q_2, q_3, q_4, q_5, q_{\text{accept}}, q_{\text{reject}}\}\),
- \(\Sigma = \{0\}\),
- \(\Gamma = \{0, x, \sqcup\}\),
- \(\delta\) dada por (figura 3.8 de Sipser):

| Estado | \(0\) | \(x\) | \(\sqcup\) |
|--------|-------|-------|------------|
| \(q_1\) | \((q_2,\sqcup,R)\) | \((q_{\text{reject}},x,R)\) | \((q_{\text{reject}},\sqcup,R)\) |
| \(q_2\) | \((q_3,x,R)\) | \((q_2,x,R)\) | \((q_{\text{accept}},\sqcup,R)\) |
| \(q_3\) | \((q_4,0,R)\) | \((q_3,x,R)\) | \((q_5,\sqcup,L)\) |
| \(q_4\) | \((q_3,x,R)\) | \((q_4,x,R)\) | \((q_{\text{reject}},\sqcup,R)\) |
| \(q_5\) | \((q_5,0,L)\) | \((q_5,x,L)\) | \((q_2,\sqcup,R)\) |

Intuitivamente:

- \(q_1\): borra el primer \(0\) (lo reemplaza por blanco; sirve como marcador del extremo izquierdo) y pasa a \(q_2\).
- \(q_2\): recorre la cinta hacia la derecha tachando un \(0\) si y solo si esta en una posicion par (a partir del primero no tachado).
- \(q_3\) y \(q_4\): se alternan para tachar uno de cada dos ceros.
- \(q_5\): vuelve al extremo izquierdo (busca el blanco sentinela) y reinicia el barrido.

## Convencion para escribir configuraciones

Usamos la convencion \(u\,q\,v\) de Sipser (pag. 168): el cabezal esta sobre el primer simbolo de \(v\) y el contenido completo de la cinta es \(uv\) seguido de blancos. Para mayor legibilidad escribimos el blanco como \(\sqcup\).

## (a) Entrada `0`

\[
\begin{aligned}
C_0 &= q_1\,0 \\
C_1 &= \sqcup\,q_2\,\sqcup \quad &&\text{por } \delta(q_1,0)=(q_2,\sqcup,R)\\
C_2 &= \sqcup\sqcup\,q_{\text{accept}}\,\sqcup &&\text{por } \delta(q_2,\sqcup)=(q_{\text{accept}},\sqcup,R)
\end{aligned}
\]

**Resultado:** acepta. Como \(|0|=1=2^0\), la entrada esta en \(A\).

## (b) Entrada `00`

\[
\begin{aligned}
C_0 &= q_1\,00 \\
C_1 &= \sqcup\,q_2\,0 &&\delta(q_1,0)=(q_2,\sqcup,R)\\
C_2 &= \sqcup x\,q_3\,\sqcup &&\delta(q_2,0)=(q_3,x,R)\\
C_3 &= \sqcup\,q_5\,x &&\delta(q_3,\sqcup)=(q_5,\sqcup,L)\\
C_4 &= q_5\,\sqcup x &&\delta(q_5,x)=(q_5,x,L)\\
C_5 &= \sqcup\,q_2\,x &&\delta(q_5,\sqcup)=(q_2,\sqcup,R)\\
C_6 &= \sqcup x\,q_2\,\sqcup &&\delta(q_2,x)=(q_2,x,R)\\
C_7 &= \sqcup x\sqcup\,q_{\text{accept}}\,\sqcup &&\delta(q_2,\sqcup)=(q_{\text{accept}},\sqcup,R)
\end{aligned}
\]

**Resultado:** acepta. Como \(|00|=2=2^1\), pertenece a \(A\).

## (c) Entrada `000`

\[
\begin{aligned}
C_0 &= q_1\,000 \\
C_1 &= \sqcup\,q_2\,00 &&\delta(q_1,0)=(q_2,\sqcup,R)\\
C_2 &= \sqcup x\,q_3\,0 &&\delta(q_2,0)=(q_3,x,R)\\
C_3 &= \sqcup x0\,q_4\,\sqcup &&\delta(q_3,0)=(q_4,0,R)\\
C_4 &= \sqcup x0\sqcup\,q_{\text{reject}}\,\sqcup &&\delta(q_4,\sqcup)=(q_{\text{reject}},\sqcup,R)
\end{aligned}
\]

**Resultado:** rechaza. La cantidad de \(0\)s es \(3\), impar y mayor que \(1\); la maquina detecta esto al estar en \(q_4\) y leer un blanco (lo que indica "fin de pasada con cantidad impar").

## (d) Entrada `000000`

Esta entrada genera una traza mas larga porque \(M_2\) realiza dos pasadas completas antes de rechazar. La primera pasada deja tres ceros a procesar; la segunda detecta que \(3\) es impar.

\[
\begin{aligned}
C_0 &= q_1\,000000 \\
C_1 &= \sqcup\,q_2\,00000 &&\delta(q_1,0)=(q_2,\sqcup,R)\\
C_2 &= \sqcup x\,q_3\,0000 &&\delta(q_2,0)=(q_3,x,R)\\
C_3 &= \sqcup x0\,q_4\,000 &&\delta(q_3,0)=(q_4,0,R)\\
C_4 &= \sqcup x0x\,q_3\,00 &&\delta(q_4,0)=(q_3,x,R)\\
C_5 &= \sqcup x0x0\,q_4\,0 &&\delta(q_3,0)=(q_4,0,R)\\
C_6 &= \sqcup x0x0x\,q_3\,\sqcup &&\delta(q_4,0)=(q_3,x,R)\\
C_7 &= \sqcup x0x0\,q_5\,x &&\delta(q_3,\sqcup)=(q_5,\sqcup,L)\\
C_8 &= \sqcup x0x\,q_5\,0x &&\delta(q_5,x)=(q_5,x,L)\\
C_9 &= \sqcup x0\,q_5\,x0x &&\delta(q_5,0)=(q_5,0,L)\\
C_{10} &= \sqcup x\,q_5\,0x0x &&\delta(q_5,x)=(q_5,x,L)\\
C_{11} &= \sqcup\,q_5\,x0x0x &&\delta(q_5,0)=(q_5,0,L)\\
C_{12} &= q_5\,\sqcup x0x0x &&\delta(q_5,x)=(q_5,x,L)\\
C_{13} &= \sqcup\,q_2\,x0x0x &&\delta(q_5,\sqcup)=(q_2,\sqcup,R)\\
C_{14} &= \sqcup x\,q_2\,0x0x &&\delta(q_2,x)=(q_2,x,R)\\
C_{15} &= \sqcup xx\,q_3\,x0x &&\delta(q_2,0)=(q_3,x,R)\\
C_{16} &= \sqcup xxx\,q_3\,0x &&\delta(q_3,x)=(q_3,x,R)\\
C_{17} &= \sqcup xxx0\,q_4\,x &&\delta(q_3,0)=(q_4,0,R)\\
C_{18} &= \sqcup xxx0x\,q_4\,\sqcup &&\delta(q_4,x)=(q_4,x,R)\\
C_{19} &= \sqcup xxx0x\sqcup\,q_{\text{reject}}\,\sqcup &&\delta(q_4,\sqcup)=(q_{\text{reject}},\sqcup,R)
\end{aligned}
\]

**Resultado:** rechaza. Tras la primera pasada quedan tres ceros sin tachar; en la segunda pasada el patron de paridad cambia y \(M_2\) detecta la cantidad impar al llegar al blanco final estando en \(q_4\).

## Verificacion

\[
0 \in A,\quad 00\in A,\quad 000\notin A,\quad 000000\notin A,
\]
porque \(1=2^0\) y \(2=2^1\) son potencias de \(2\), y \(3,6\) no lo son. Esto coincide con los resultados obtenidos.

## Comentario

El ejemplo ilustra el funcionamiento "tipico" de una MT: pasadas sucesivas sobre la cinta usando estados como contador finito (paridad) y simbolos auxiliares como marcas. El patron de tachar uno de cada dos simbolos es tambien la idea base detras de varios algoritmos de divide-and-conquer sobre cinta (binarizacion).
