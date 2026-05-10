# Ejercicio 2

## Enunciado

Considere el problema de determinar si una MT con el input \(w\) alguna vez intenta mover el cabezal a la izquierda cuando esta en la posicion mas a la izquierda de la cinta. Demostrar que este problema es indecidible.

## Formalizacion

Definimos el lenguaje:

\[
LM = \{\langle M,w\rangle \mid M \text{ es una MT que, al ejecutarse con entrada }w, \text{ alguna vez intenta mover el cabezal a la izquierda desde la celda mas a la izquierda}\}.
\]

Queremos mostrar que \(LM\) es indecidible.

## Idea de la demostracion

Reducimos \(A_{TM}\) a \(LM\). Como \(A_{TM}\) es indecidible (Teorema 4.11 de Sipser), la existencia de tal reduccion forzara la indecidibilidad de \(LM\) (Corolario 5.23 de Sipser).

La idea intuitiva es construir, a partir de \(\langle M,w\rangle\), una nueva MT \(M'\) que se comporta "igual" que \(M\) pero con dos modificaciones cruciales:

1. Antes de simular a \(M\), \(M'\) se reserva la celda mas a la izquierda con un *marcador* especial \(\$\) y trabaja siempre desde la celda inmediatamente a la derecha en adelante. Mientras \(M'\) este simulando a \(M\), nunca intenta cruzar el marcador hacia la izquierda: si la simulacion deberia mover el cabezal a la izquierda y se encuentra con \(\$\), \(M'\) se queda en su lugar.
2. Si y solo si la simulacion alcanza el estado de aceptacion de \(M\), entonces \(M'\) se desplaza hasta la celda donde esta el marcador \(\$\) y, desde alli, **intenta** moverse a la izquierda.

De esa forma, \(M'\) intenta mover el cabezal a la izquierda desde el extremo izquierdo si y solo si \(M\) acepta \(w\).

## Construccion formal de la reduccion

La reduccion \(f\) toma una cadena \(\langle M,w\rangle\) y devuelve la codificacion \(\langle M',w\rangle\) donde \(M'\) es la MT descripta a continuacion. Si la entrada no tiene la forma esperada, \(f\) devuelve una cadena fuera de \(LM\) (por ejemplo, la codificacion de una MT que nunca intenta cruzar el extremo izquierdo).

\(M'=\) "Con entrada \(x\):

1. Marcar el inicio de la cinta. Mas precisamente: correr el contenido actual una posicion a la derecha y escribir el simbolo especial \(\$\) en la celda \(0\). Esto puede hacerse leyendo la cinta de izquierda a derecha hasta el primer blanco y volviendo a copiar de derecha a izquierda. Es una operacion estandar de las MTs.
2. Posicionar el cabezal en la celda \(1\) (la primera a la derecha de \(\$\)).
3. Simular \(M\) sobre \(w\) (la entrada original, ya que \(w\) esta fijo en la descripcion de \(M'\)). Durante la simulacion, si la transicion de \(M\) indicara mover el cabezal a la izquierda y la celda actual de \(M'\) contiene el simbolo \(\$\), entonces \(M'\) se queda en la celda actual (no cruza el marcador). Esto evita que \(M'\) intente moverse a la izquierda desde el extremo durante la simulacion.
4. Si en algun momento la simulacion entra en \(q_{accept}\) de \(M\):
   - \(M'\) se desplaza a la izquierda hasta encontrar el simbolo \(\$\).
   - Estando sobre \(\$\) (la celda mas a la izquierda), ejecuta una transicion que indica mover el cabezal a la izquierda.
5. Si la simulacion entra en \(q_{reject}\) de \(M\), \(M'\) se detiene sin haber intentado nunca cruzar el extremo izquierdo."

Notar que \(M'\) ignora su propia entrada \(x\): siempre simula a \(M\) con la palabra fija \(w\). Esto es valido porque \(w\) esta cableado en la descripcion de \(M'\).

## Funcion de reduccion: computabilidad

La funcion \(f\) que toma \(\langle M,w\rangle\) y produce \(\langle M',w\rangle\) es computable: dada la descripcion de \(M\), una MT puede mecanicamente:

- Agregar nuevos estados a \(M\) que implementan los pasos 1 y 2 (marcar y posicionar).
- Modificar las transiciones de \(M\) que mueven a la izquierda para chequear el simbolo \(\$\).
- Agregar las transiciones de los pasos 4 y 5.

Toda esta transformacion es algoritmica y produce una nueva descripcion finita \(\langle M'\rangle\), lo cual hace a \(f\) computable en el sentido de la Definicion 5.17 de Sipser.

## Correctitud de la reduccion

Mostramos que para todo \(\langle M,w\rangle\):

\[
\langle M,w\rangle\in A_{TM} \iff \langle M',w\rangle\in LM.
\]

**(\(\Rightarrow\))** Supongamos \(\langle M,w\rangle\in A_{TM}\), es decir, \(M\) acepta \(w\). Entonces, durante la simulacion del paso 3, \(M'\) eventualmente entra en \(q_{accept}\) de \(M\). Por el paso 4, \(M'\) se mueve hasta el simbolo \(\$\) (el extremo izquierdo) y desde alli intenta moverse a la izquierda. Por construccion, ese intento ocurre estando en la celda mas a la izquierda. Por lo tanto \(\langle M',w\rangle\in LM\).

**(\(\Leftarrow\))** Supongamos \(\langle M',w\rangle\in LM\). Por construccion, los unicos puntos donde \(M'\) podria intentar moverse a la izquierda desde el extremo izquierdo son:

- Durante la simulacion del paso 3: pero alli **no** se intenta cruzar \(\$\), porque la modificacion del paso 3 reemplaza explicitamente esos movimientos por "quedarse en el lugar".
- Despues del paso 4: solo si la simulacion alcanzo \(q_{accept}\).

Por lo tanto, si \(M'\) intenta moverse a la izquierda desde el extremo, debe ser porque la simulacion alcanzo \(q_{accept}\), es decir, \(M\) acepta \(w\). Luego \(\langle M,w\rangle\in A_{TM}\).

## Conclusion

Hemos exhibido una reduccion many-one computable

\[
A_{TM}\le_m LM.
\]

Como \(A_{TM}\) es indecidible y la reducibilidad many-one preserva la decidibilidad (Teorema 5.22 de Sipser), concluimos que \(LM\) tampoco lo es.

\[
\boxed{LM \text{ es indecidible.}}
\]
