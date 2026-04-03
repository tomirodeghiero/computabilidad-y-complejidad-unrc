# Ejercicio 3

## Enunciado

Sea \(C\) un lenguaje, demostrar que \(C\) es reconocible, sii existe un lenguaje decidible \(D\) tal que:

\[
C = \{w \mid \exists y : \langle w,y\rangle \in D\}.
\]

## Teorema

Para todo lenguaje \(C\),

\[
C \text{ es Turing-reconocible } \iff \exists D \text{ decidible } \big(C=\{x\mid \exists y\ (\langle x,y\rangle\in D)\}\big).
\]

## Demostración

Demostramos ambas implicaciones.

### (\(\Rightarrow\)) Si \(C\) es reconocible, existe \(D\) decidible de la forma pedida

Supongamos que \(C\) es reconocido por una MT \(M\).

Definimos

\[
D=\{\langle x,t\rangle \mid M \text{ acepta } x \text{ en a lo sumo } t \text{ pasos}\},
\]

donde \(t\) codifica un número natural.

#### Lema 1

\(D\) es decidible.

#### Prueba del lema

Construimos un decider \(T_D\):

1. Entrada: \(\langle x,t\rangle\).
2. Simular \(M\) sobre \(x\) durante exactamente \(t\) pasos.
3. Aceptar si \(M\) acepta en ese prefijo de ejecución; en caso contrario, rechazar.

La simulación está acotada por \(t\), luego siempre termina. Por tanto \(T_D\) decide \(D\).

#### Lema 2

\[
x\in C \iff \exists t\ (\langle x,t\rangle\in D).
\]

#### Prueba del lema

1. Si \(x\in C\), como \(M\) reconoce \(C\), \(M\) acepta \(x\) en algún tiempo finito \(t_0\). Luego \(\langle x,t_0\rangle\in D\).
2. Si \(\exists t\) tal que \(\langle x,t\rangle\in D\), por definición de \(D\), \(M\) acepta \(x\). Por lo tanto \(x\in C\).

Con ambos lemas, queda probado el sentido \((\Rightarrow)\).

### (\(\Leftarrow\)) Si existe \(D\) decidible de esa forma, \(C\) es reconocible

Supongamos ahora que \(D\) es decidible y

\[
C=\{x\mid \exists y\ (\langle x,y\rangle\in D)\}.
\]

Sea \(T_D\) un decider para \(D\). Construimos una MT \(R\):

1. Entrada: \(x\).
2. Enumerar todas las cadenas \(y_1,y_2,\dots\) de \(\Sigma^*\) (por ejemplo, shortlex).
3. Para \(i=1,2,\dots\), ejecutar \(T_D\) sobre \(\langle x,y_i\rangle\).
4. Si alguna ejecución acepta, aceptar.

#### Correctitud

1. Si \(x\in C\), existe testigo \(y^*\) con \(\langle x,y^*\rangle\in D\). Cuando la enumeración alcanza \(y^*\), \(T_D\) acepta y \(R\) acepta.
2. Si \(x\notin C\), no existe testigo; todas las ejecuciones de \(T_D\) rechazan y \(R\) no acepta nunca.

Eso coincide exactamente con la definición de reconocibilidad (Sipser, Def. 3.5).

Concluimos el doble implicado.

## Referencia

Este resultado corresponde al ejercicio 4.18 de Sipser.
