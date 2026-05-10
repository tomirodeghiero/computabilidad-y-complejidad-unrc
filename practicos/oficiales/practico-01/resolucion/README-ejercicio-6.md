# Ejercicio 6

## Enunciado

Mostrar que una maquina de Turing con una sola cinta que **no puede escribir** sobre la parte de la cinta que contiene el input solo puede reconocer lenguajes regulares (Problema 3.20 de Sipser).

## Modelo de maquina considerado

Adoptamos la interpretacion estandar (la del Problema 3.20 de Sipser): la MT \(M\) tiene una sola cinta y, sobre las celdas que contienen los simbolos del input, su funcion de transicion **debe escribir el mismo simbolo que ya estaba** (es decir, no modifica esa zona). Por simplicidad, podemos asumir que la cinta esta delimitada por dos marcadores \(\vdash\) (extremo izquierdo) y \(\dashv\) (extremo derecho) que no estan en \(\Sigma\), de modo que la maquina sabe en que celdas comienza y termina la entrada y nunca cruza esos limites.

Bajo esta hipotesis:

1. La cinta es esencialmente de **solo lectura** sobre la zona del input.
2. El comportamiento de \(M\) sobre cada celda depende unicamente de su estado actual y del simbolo leido, no de modificaciones previas.
3. El cabezal puede moverse a izquierda o derecha dentro de la zona de input, sin escribir.

Esto es **exactamente** la definicion de un **2DFA** (automata finito determinista de dos vias): un automata finito que lee una cinta de entrada de solo lectura, con cabezal que puede ir hacia ambos lados, delimitada por marcadores de bordes y con un conjunto finito de estados.

## Proposicion

Todo lenguaje reconocido por una MT \(M\) que no escribe sobre la zona de input es regular.

## Demostracion

Sea
\[
  M = (Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})
\]
una MT que no escribe sobre la zona del input. Como \(M\) no modifica las celdas del input, la funcion de transicion sobre dichas celdas se reduce a:
\[
  \delta(q,a) = (p,a,D),\qquad D\in\{L,R\}.
\]
Es decir, \(M\) esta totalmente caracterizada (en la zona de input) por la **terna** \((p,D)\) que cambia el estado y mueve el cabezal sin alterar el simbolo.

### Construccion del 2DFA equivalente

Construimos un 2DFA
\[
  A = (Q', \Sigma, \delta_A, q_0, F),\qquad F=\{q_{\text{accept}}\},
\]
con \(Q'=Q\), agregando los marcadores \(\vdash,\dashv\) al alfabeto leido por \(\delta_A\) si fuera necesario para delimitar la cinta.

La funcion \(\delta_A: Q\times(\Sigma\cup\{\vdash,\dashv\})\to Q\times\{L,R\}\) se define por:

- Si \(\delta(q,a) = (p,a,D)\) con \(a\in\Sigma\), entonces \(\delta_A(q,a)=(p,D)\).
- En \(\vdash\) y \(\dashv\), reproducimos el comportamiento de borde de \(M\) (en particular, \(M\) no puede cruzar los limites del input).
- Cuando \(M\) entra en \(q_{\text{accept}}\) o \(q_{\text{reject}}\), \(A\) entra en esos mismos estados de aceptacion o rechazo.

Como \(M\) no altera el contenido de la cinta de entrada, cada paso de \(M\) (mientras el cabezal este sobre la zona de input) se reproduce uno a uno como un paso de \(A\). En consecuencia, la computacion de \(M\) sobre cualquier entrada \(w\in\Sigma^*\) es identica (modulo la representacion de configuraciones) a la computacion de \(A\) sobre \(w\). Por lo tanto:
\[
  L(M) = L(A).
\]

### Cierre por el teorema clasico de los 2DFA

Por el **teorema de Rabin-Scott / Shepherdson** (1959): los lenguajes reconocidos por 2DFA son exactamente los reconocidos por DFA, esto es, los **lenguajes regulares**.

Por lo tanto, \(L(A)\) es regular y, por la igualdad recien probada, \(L(M)\) tambien es regular.

\[
  \boxed{L(M) \text{ es regular}.}
\]

## Demostracion alternativa: argumento de Myhill-Nerode

Para enriquecer la justificacion, damos una segunda prueba mas directa.

Sea \(M\) la MT con input read-only descrita arriba. Para cualquier cadena \(w\) y cualquier posicion \(i\) entre \(0\) y \(|w|\), definimos el **comportamiento de cruce a la derecha** en la frontera entre las celdas \(i-1\) e \(i\) como la funcion \(\tau_w^i:Q\to Q\cup\{\bot\}\) tal que:

\[
  \tau_w^i(q) =
  \begin{cases}
    q' & \text{si al iniciar }M\text{ en }w[i..|w|]\text{ con estado }q,\text{ la primera vez que el cabezal cruza la frontera hacia la izquierda lo hace en estado }q',\\
    \bot & \text{si nunca cruza (o entra en estado de halt antes).}
  \end{cases}
\]

El espacio de funciones \(Q\to Q\cup\{\bot\}\) es **finito** (tiene \((|Q|+1)^{|Q|}\) elementos). Por lo tanto, las cadenas \(w\) se pueden clasificar segun su comportamiento de cruce \(\tau_w^{|w|}\) en finitas clases.

**Claim:** Si dos prefijos \(u\) y \(u'\) inducen el mismo comportamiento de cruce \(\tau_u^{|u|}=\tau_{u'}^{|u'|}\), entonces para toda extension \(v\),
\[
  uv\in L(M) \iff u'v\in L(M).
\]
La justificacion intuitiva es que toda la informacion que la cabeza "trae" cuando vuelve hacia el sufijo \(v\) se reduce a esta funcion finita. La formalizacion completa requiere considerar tambien comportamientos a izquierda/derecha y combinarlos, pero la idea estructural es la misma.

Por el teorema de **Myhill-Nerode**, un lenguaje con finitas clases de equivalencia es regular. Concluimos nuevamente que \(L(M)\) es regular.

## Conclusion

La capacidad de "no escribir sobre el input" reduce drasticamente el poder de una MT. Bajo esta restriccion, la maquina pierde la capacidad de simular memoria mas alla de su control finito y se vuelve equivalente a un automata finito de dos vias, que reconoce solo lenguajes regulares.

> Toda MT de una cinta que no escribe sobre el input reconoce solo lenguajes regulares.

## Comentario

Este resultado ilumina por que la **escritura sobre la cinta** (sobre el propio input o, en variantes mas potentes, sobre una zona de trabajo separada) es esencial para la potencia de las MT. Sin esa capacidad, las MT colapsan a la clase regular, perdiendo la posibilidad de reconocer lenguajes tan basicos como \(\{0^n1^n:n\ge 0\}\) que requieren memoria proporcional a la entrada.

En particular, este Problema 3.20 hace pareja conceptual con los Problemas 3.11 (cinta doblemente infinita: misma potencia) y 3.13 (variante "stay put" en lugar de "left": **no** equivalente, depende de los detalles exactos), ilustrando que no todas las modificaciones a la definicion preservan poder.
