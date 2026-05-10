# Ejercicio 6

## Enunciado

Demostrar que \(\le_M\) es transitiva.

## Proposicion

Si \(A\le_m B\) y \(B\le_m C\), entonces \(A\le_m C\).

(Este es el Ejercicio 5.6 de Sipser y aparece como ejercicio 3 en las laminas de la teoria.)

## Demostracion

Supongamos que se cumplen las dos hipotesis:

1. \(A\le_m B\): existe una funcion computable \(f:\Sigma^*\to\Sigma^*\) tal que para toda cadena \(x\),
   \[
   x\in A \iff f(x)\in B.
   \]
2. \(B\le_m C\): existe una funcion computable \(g:\Sigma^*\to\Sigma^*\) tal que para toda cadena \(y\),
   \[
   y\in B \iff g(y)\in C.
   \]

Definimos la funcion compuesta:

\[
h(x)=g(f(x)),\qquad x\in\Sigma^*.
\]

### \(h\) es computable

Sea \(M_f\) una MT que computa \(f\) (es decir, comenzando con \(x\) en la cinta, \(M_f\) termina con \(f(x)\) en la cinta). Sea \(M_g\) una MT que computa \(g\). Construimos una MT \(M_h\) para computar \(h\) de la siguiente forma:

\(M_h=\) "Con entrada \(x\):

1. Simular \(M_f\) sobre \(x\) hasta que termine. Al finalizar, la cinta contiene \(f(x)\).
2. Simular \(M_g\) sobre \(f(x)\) (es decir, sobre el contenido actual de la cinta). Al finalizar, la cinta contiene \(g(f(x))=h(x)\).
3. Detenerse."

Como ambas \(M_f\) y \(M_g\) terminan en cualquier entrada (por ser \(f\) y \(g\) computables, en el sentido de la Definicion 5.17 de Sipser), \(M_h\) tambien termina en cualquier entrada \(x\) y deja \(h(x)\) en la cinta. Por lo tanto, \(h\) es computable.

### \(h\) es una reduccion de \(A\) a \(C\)

Para toda cadena \(x\):

\[
x\in A
\stackrel{(1)}{\iff} f(x)\in B
\stackrel{(2)}{\iff} g(f(x))\in C
\iff h(x)\in C.
\]

donde la equivalencia \((1)\) es la hipotesis sobre \(f\), aplicada a \(x\); y la equivalencia \((2)\) es la hipotesis sobre \(g\), aplicada a \(f(x)\).

Es decir,

\[
x\in A \iff h(x)\in C.
\]

Esto muestra que \(h\) es una reduccion many-one computable de \(A\) a \(C\), por lo que

\[
A\le_m C.
\]

## Conclusion

\[
\boxed{A\le_m B \text{ y } B\le_m C \;\Rightarrow\; A\le_m C.}
\]

La relacion \(\le_m\) es transitiva.

## Comentario

Esta propiedad es esencial en la practica: una vez probado, por ejemplo, que \(A_{TM}\le_m HALT_{TM}\) y \(HALT_{TM}\le_m E_{TM}\), por transitividad \(A_{TM}\le_m E_{TM}\), sin necesidad de exhibir una nueva reduccion. Tambien explica por que las cadenas de reducciones que aparecen en las pruebas de indecidibilidad (por ejemplo \(A_{TM}\le_m MPCP \le_m PCP\), Ejemplo 5.25 de Sipser) implican \(A_{TM}\le_m PCP\) y por ende la indecibilidad de PCP.
