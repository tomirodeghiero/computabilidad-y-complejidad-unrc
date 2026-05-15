# Ejercicio 3

## Enunciado

Describir dos maquinas de Turing \(M\) y \(N\) tales que, cuando comienzan en cualquier input, \(M\) imprime \(\langle N\rangle\) y \(N\) imprime \(\langle M\rangle\).

> **Sobre el enunciado.** El enunciado del practico tiene una errata: pide "\(M\) imprime \(\langle M\rangle\), y \(N\) imprime \(\langle M\rangle\)", lo cual es trivial (alcanza con dos copias de la MT `SELF`). La version original (Problema 6.6 de Sipser, repetida en `autoref.pdf`) pide imprimirse *mutuamente*; resolvemos esta version, que es la interesante.

## Idea

Si \(M\) "imprime \(\langle N\rangle\)" y \(N\) "imprime \(\langle M\rangle\)", entonces cada una conoce a la otra. El problema es analogo al de `SELF` pero con dos programas que se referencian cruzadamente. La herramienta clave es la misma:

- **Lema 6.1 de Sipser**: existe \(q:\Sigma^*\to\Sigma^*\) computable tal que \(q(w)\) es la descripcion de una MT \(P_w\) que imprime \(w\) y se detiene.
- Tomamos \(q\), aplicado a la cadena que queremos que la MT imprima, para obtener la maquina deseada.

Pero ahora hay una sutileza: si simplemente definimos \(M = P_{\langle N\rangle}\) y \(N = P_{\langle M\rangle}\), la definicion es *circular* (cada una se define en terminos de la otra). Para romper la circularidad recurrimos al mismo truco que para `SELF`: una de las dos maquinas obtiene la descripcion de la otra desde la cinta, y la otra hace lo mismo a partir de la simulacion.

## Construccion

Construimos primero una MT auxiliar \(N\), siguiendo la estrategia de `SELF` pero ajustada para que su salida sea la descripcion *de la otra* maquina, \(M\). Para esto basta intercambiar los roles de "imprimir esto" en la fase final de \(B\).

### Definicion de \(N\) (analoga a `SELF`, pero produce \(\langle M\rangle\))

Descomponemos \(N\) en dos partes \(A_N\) y \(B_N\):

1. **Parte \(A_N\)**: es \(P_{\langle B_N\rangle}\), la maquina que imprime \(\langle B_N\rangle\) en la cinta y se detiene. Existe por el Lema 6.1.
2. **Parte \(B_N\)**: en entrada \(\langle B_N\rangle\) (lo que dejo \(A_N\) en la cinta):
   1. computar \(q(\langle B_N\rangle)\), que es \(\langle A_N\rangle\);
   2. combinar \(A_N\) y \(B_N\) para obtener \(\langle A_N B_N\rangle = \langle N\rangle\);
   3. construir la MT \(M\) (definida abajo) a partir de \(\langle N\rangle\) y escribir su descripcion \(\langle M\rangle\) en la cinta.

Es decir, \(N\) reconstruye su propia descripcion \(\langle N\rangle\) y luego *transforma* esa descripcion en la descripcion de \(M\). El paso de transformacion es lo unico nuevo respecto de `SELF`: una funcion computable \(\tau:\Sigma^*\to\Sigma^*\) tal que \(\tau(\langle N\rangle)=\langle M\rangle\). La definimos a continuacion.

### Definicion de \(M\) en funcion de \(N\)

Definimos:

> \(M\) = "En cualquier entrada \(x\):
> 1. Ignorar \(x\).
> 2. Escribir en la cinta la cadena \(\langle N\rangle\) (cableada en la propia descripcion de \(M\)) y detenerse."

Equivalentemente, \(M = P_{\langle N\rangle}\) en la notacion del Lema 6.1. La funcion \(\tau\) que envia \(\langle N\rangle\) a \(\langle M\rangle\) es exactamente \(q\):

\[
\tau(\langle N\rangle) \;=\; q(\langle N\rangle) \;=\; \langle P_{\langle N\rangle}\rangle \;=\; \langle M\rangle.
\]

Esto cierra la construccion: \(N\) obtiene su propia descripcion \(\langle N\rangle\) (al estilo `SELF`) y aplica \(q\) para producir \(\langle M\rangle\), y \(M\) solo necesita tener \(\langle N\rangle\) cableado para imprimirlo.

## Pseudocodigo unificado

```text
M = "En entrada x:
       1. Borrar la cinta.
       2. Escribir <N> (cableado).
       3. Detener."

N = "En entrada x:
       Parte A_N: ejecutar P_{<B_N>}, dejando <B_N> en la cinta.
       Parte B_N:
         1. Aplicar q a <B_N> para obtener <A_N>.
         2. Combinar <A_N> y <B_N> en <N> = <A_N B_N>.
         3. Calcular q(<N>) = <M>.
         4. Borrar la cinta y escribir <M>.
         5. Detener."
```

Observemos que aqui hay una sola "circularidad aparente": para escribir \(M\) necesitamos \(\langle N\rangle\), y para que \(N\) produzca \(\langle M\rangle\) necesita conocer \(\langle N\rangle\). Pero esa "circularidad" se rompe porque \(N\) **calcula** \(\langle N\rangle\) en tiempo de ejecucion (al estilo `SELF`) y solo entonces produce \(\langle M\rangle\). En la *definicion* de \(M\), por su parte, la cadena \(\langle N\rangle\) ya esta dada (es una constante que se obtiene una vez construida \(N\)).

## Por que no se usa el Teorema de la Recursion explicitamente

Una solucion mas corta consiste en usar directamente el Teorema 6.3 (Recursion):

> \(N\) = "En entrada \(x\):
> 1. Obtener su propia descripcion \(\langle N\rangle\) (Teorema 6.3).
> 2. Computar \(q(\langle N\rangle) = \langle M\rangle\).
> 3. Imprimir \(\langle M\rangle\)."

y simetricamente:

> \(M\) = "En entrada \(x\): imprimir \(\langle N\rangle\) (cableado)."

Ambas vias son correctas y dan el mismo par \((M,N)\); la primera muestra explicitamente como, sin invocar el Teorema, construir \(M\) y \(N\) "a mano" siguiendo la receta de `SELF`. La segunda usa el Teorema como caja negra.

## Correctitud

- En cualquier entrada \(x\), \(M\) ignora \(x\) y escribe \(\langle N\rangle\) en la cinta (paso 2 de \(M\)).
- En cualquier entrada \(x\), \(N\) ignora \(x\), reconstruye su propia descripcion como en `SELF`, le aplica \(q\) y termina con \(\langle M\rangle\) en la cinta.

Por construccion, \(M\) y \(N\) son MT bien definidas y se imprimen *mutuamente*.

## Conexion con la teoria

- El truco es exactamente el del Teorema de la Recursion (Sipser 6.3): permite a una MT obtener su propia descripcion y operar con ella.
- En el lenguaje de los quines, esto se llama un *par de quines* o *quines mutuos*: dos programas \(M\) y \(N\) tales que ejecutando \(M\) se imprime el codigo de \(N\) y viceversa. Es un caso clasico de programacion recreativa y, simultaneamente, una aplicacion seria de la teoria de la recursion.

## Conclusion

Las dos MT pueden describirse imitando `SELF` y agregando un unico paso final que aplica la funcion \(q\) del Lema 6.1:

\[
\boxed{\;N \text{ obtiene } \langle N\rangle \text{ a la Sipser y luego escribe } q(\langle N\rangle)=\langle M\rangle; \quad M=P_{\langle N\rangle}.\;}
\]
