# Ejercicio 7

## Enunciado

Decir si se cumple o no la siguiente afirmacion: si \(A\le_m B\) y \(B\) es un lenguaje regular, esto implica que \(A\) es un lenguaje regular. Fundamentar su respuesta.

(Este es el Ejercicio 5.4 de Sipser.)

## Respuesta

**No**, la afirmacion es falsa en general.

La intuicion es la siguiente: la relacion \(\le_m\) preserva *decidibilidad* y *reconocibilidad* (como muestran los Teoremas 5.22 y 5.28 de Sipser), pero **no** preserva propiedades mas finas como la regularidad o la libertad de contexto. La razon es que la "potencia de computo" disponible para construir la funcion de reduccion \(f\) es la de una MT general, no la de un automata finito. Por lo tanto, \(f\) puede ocultar tareas no regulares dentro de una clasificacion binaria de cadenas.

## Contraejemplo

Tomemos los lenguajes:

\[
A=\{0^n1^n \mid n\ge 0\},\qquad B=\{1\}.
\]

- \(B\) es **regular**: es un singleton, reconocido por un AFD trivial.
- \(A\) **no es regular**: es el ejemplo clasico de lenguaje no regular, lo cual se demuestra con el lema de bombeo.

### Construccion de la reduccion \(A\le_m B\)

Como \(A\) es decidible (por ejemplo, una MT que cuenta ceros y unos puede decidirlo), hay un algoritmo que decide la pertenencia a \(A\). Con eso definimos la funcion computable

\[
f(x)=
\begin{cases}
1 & \text{si } x\in A,\\
0 & \text{si } x\notin A.
\end{cases}
\]

\(f\) es computable: una MT simula el algoritmo decidor de \(A\), borra la cinta, y escribe \(1\) o \(0\) segun la respuesta. Esto cumple la Definicion 5.17 de Sipser de funcion computable.

Verifiquemos que \(f\) reduce \(A\) a \(B\). Para toda \(x\):

\[
x\in A \iff f(x)=1 \iff f(x)\in B,
\]

(la ultima equivalencia se debe a que \(B=\{1\}\): \(f(x)\in B\) ssi \(f(x)=1\)).

Por lo tanto, \(A\le_m B\).

### Conclusion del contraejemplo

Tenemos:

- \(A\le_m B\) (por la reduccion construida).
- \(B\) es regular.
- \(A\) **no** es regular.

Esto demuestra que la afirmacion del enunciado falla: existe \(A\le_m B\) con \(B\) regular y sin embargo \(A\) no es regular.

## Por que falla la afirmacion

El punto clave es que \(\le_m\) usa funciones computables arbitrarias, y una MT puede ejecutar tareas arbitrariamente complejas (por ejemplo, contar ceros y unos para decidir \(0^n1^n\)) antes de devolver una respuesta binaria que cae en un lenguaje regular trivial. La regularidad es una propiedad sintactica/automatica que depende de la *estructura* del lenguaje, mientras que \(\le_m\) solo controla la *pertenencia* mediante una funcion potencialmente compleja.

En cambio, las propiedades que **si** se preservan bajo \(\le_m\) son aquellas que se "comportan bien" frente a maquinas potentes:

- **Decidibilidad** (Teorema 5.22 de Sipser): si \(A\le_m B\) y \(B\) es decidible, entonces \(A\) es decidible.
- **Reconocibilidad** (Teorema 5.28 de Sipser): si \(A\le_m B\) y \(B\) es reconocible, entonces \(A\) es reconocible.

## Conclusion

\[
\boxed{\text{La afirmacion es falsa: } A\le_m B \text{ con } B \text{ regular no implica que } A \text{ sea regular.}}
\]

El contraejemplo \(A=\{0^n1^n\mid n\ge 0\}\) y \(B=\{1\}\) muestra que la regularidad no se preserva bajo \(\le_m\).
