# Ejercicio 9

## Enunciado

Demostrar que \(A\) es reconocible si y solo si \(A\le_m A_{TM}\).

(Este es el Ejercicio 5.22 de Sipser.)

## Proposicion

Para todo lenguaje \(A\subseteq\Sigma^*\):

\[
A \text{ es Turing-reconocible} \iff A\le_m A_{TM}.
\]

## Demostracion

Probamos por separado las dos direcciones de la equivalencia.

### \((\Rightarrow)\) Si \(A\) es Turing-reconocible, entonces \(A\le_m A_{TM}\)

Supongamos que \(A\) es reconocible. Por definicion, existe una MT \(M_A\) tal que

\[
L(M_A)=A,
\]

es decir, para toda cadena \(x\):

\[
x\in A \iff M_A \text{ acepta } x.
\]

Definimos la funcion

\[
f:\Sigma^*\to\Sigma^*,\qquad f(x)=\langle M_A,x\rangle,
\]

donde \(\langle M_A,x\rangle\) es la codificacion del par formado por la (fija) descripcion de \(M_A\) y la cadena \(x\).

#### \(f\) es computable

Para computar \(f(x)\) basta una MT que:

1. En la cinta esta inicialmente \(x\).
2. Genera (precede al contenido) la descripcion fija \(\langle M_A\rangle\) seguida de un separador.
3. El resultado en la cinta es \(\langle M_A,x\rangle\).

Como \(\langle M_A\rangle\) es una cadena fija (cableada en la descripcion de la MT que computa \(f\)), la operacion es claramente algoritmica y termina siempre. Por lo tanto, \(f\) es una funcion computable en el sentido de la Definicion 5.17 de Sipser.

#### \(f\) es una reduccion de \(A\) a \(A_{TM}\)

Para toda \(x\):

\[
x\in A \iff M_A \text{ acepta } x \iff \langle M_A,x\rangle\in A_{TM} \iff f(x)\in A_{TM}.
\]

(La primera equivalencia es por definicion de \(A=L(M_A)\); la segunda por definicion de \(A_{TM}\); la tercera por definicion de \(f\).)

Concluimos: \(A\le_m A_{TM}\).

### \((\Leftarrow)\) Si \(A\le_m A_{TM}\), entonces \(A\) es Turing-reconocible

Supongamos que existe una funcion computable \(f\) tal que para toda \(x\),

\[
x\in A \iff f(x)\in A_{TM}.
\]

Sabemos que \(A_{TM}\) es Turing-reconocible: una MT universal \(U\) reconoce \(A_{TM}\) simulando \(M\) sobre \(w\) y aceptando si \(M\) acepta (Teorema 4.11 de Sipser y la nocion clasica de UTM).

Construimos un reconocedor \(R\) para \(A\):

\(R=\) "Con entrada \(x\):

1. Computar \(f(x)\) usando la MT que computa \(f\).
2. Simular la maquina universal \(U\) sobre la entrada \(f(x)\).
3. Si \(U\) acepta, aceptar."

#### Correctitud de \(R\)

- Si \(x\in A\): por hipotesis, \(f(x)\in A_{TM}\). Entonces \(U\) eventualmente acepta sobre \(f(x)\), y por lo tanto \(R\) acepta \(x\).
- Si \(x\notin A\): por hipotesis, \(f(x)\notin A_{TM}\). Entonces \(U\) sobre \(f(x)\) no acepta (puede rechazar o entrar en bucle), y por lo tanto \(R\) no acepta \(x\).

Asi, \(L(R)=A\), es decir, \(R\) es un reconocedor para \(A\). Conclusion: \(A\) es reconocible.

(Este es el contenido del Teorema 5.28 de Sipser, aplicado al caso particular \(B=A_{TM}\).)

## Conclusion

\[
\boxed{A \text{ es reconocible} \iff A\le_m A_{TM}.}
\]

## Observacion: \(A_{TM}\) como "lenguaje universal" para la reconocibilidad

Este resultado es muy informativo. Dice que \(A_{TM}\) es un lenguaje **completo** respecto de la reconocibilidad bajo \(\le_m\): todo lenguaje reconocible se reduce a el. En la terminologia mas general, \(A_{TM}\) es un lenguaje *RE-completo*. Cualquier lenguaje "al menos tan dificil" como \(A_{TM}\) (es decir, al cual \(A_{TM}\) se reduzca) que ademas no este por encima del nivel reconocible no puede serlo: heredaria la indecibilidad de \(A_{TM}\).

En particular, este lema explica por que \(A_{TM}\) aparece en tantas demostraciones de indecidibilidad: cualquier problema que sea reconocible y al cual \(A_{TM}\) se reduzca tiene la "misma dureza" maxima dentro de la jerarquia reconocible.
