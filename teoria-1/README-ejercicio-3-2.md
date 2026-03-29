# Ejercicio 3.2

Definir una MT que decida:

`L2 = { w | w contiene dos veces mas 0 que 1 }`

Formalmente: `#0(w) = 2 * #1(w)`.

## Idea

Por cada `1` sin marcar, consumir exactamente dos `0` sin marcar.
Al final no deben sobrar `0`.

## Definicion (nivel implementacion)

Alfabeto de entrada: `{0,1}`

Alfabeto de cinta: `{0,1,X,Y,_}`

1. Ir al inicio.
2. Buscar un `1` sin marcar.
3. Si no hay `1`, pasar a verificacion final.
4. Marcar ese `1` como `Y`.
5. Buscar un primer `0` sin marcar. Si no hay, rechazar. Marcar `X`.
6. Buscar un segundo `0` sin marcar. Si no hay, rechazar. Marcar `X`.
7. Volver al inicio y repetir.
8. Verificacion final: recorrer la cinta.
9. Si queda algun `0` sin marcar, rechazar.
10. Si no queda ninguno, aceptar.

## Correctitud (resumen)

1. Cada ciclo marca 1 uno y 2 ceros.
2. Si acepta, no quedan simbolos relevantes sin marcar y se cumple `#0=2#1`.
3. Si `#0=2#1`, el proceso puede completar todos los ciclos y no sobran ceros.
4. Termina siempre: en cada vuelta consume un `1` o rechaza.
