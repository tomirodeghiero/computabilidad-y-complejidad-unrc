# Ejercicio 3.1

Definir una MT que decida:

`L1 = { w | w contiene igual cantidad de 0 y 1 }`

## Idea

Marcar de a pares:

1. Tomar un simbolo sin marcar.
2. Buscar uno del otro tipo.
3. Marcar ambos.
4. Repetir.

Si en algun momento no se encuentra pareja, rechazar.
Si al final no queda nada sin marcar, aceptar.

## Definicion (nivel implementacion)

Alfabeto de entrada: `{0,1}`

Alfabeto de cinta: `{0,1,X,Y,_}`

1. Ir al inicio.
2. Buscar primer simbolo sin marcar (`0` o `1`), saltando `X` y `Y`.
3. Si no hay, aceptar.
4. Si aparece `0`, marcarlo `X` y buscar un `1` sin marcar.
5. Si lo encuentra, marcar `1` como `Y`, volver al inicio y repetir.
6. Si llega a blanco sin encontrar ese `1`, rechazar.
7. Si en el paso 2 aparece `1`, hacer simetrico:
8. Marcar `1` con `Y`, buscar `0` sin marcar, marcarlo con `X`.
9. Si no aparece ese `0`, rechazar.
10. Volver al inicio y repetir.

## Correctitud (resumen)

1. Cada ciclo completo marca exactamente un `0` y un `1`.
2. Si acepta, todos fueron emparejados, por lo tanto `#0(w)=#1(w)`.
3. Si `#0(w)=#1(w)`, siempre existe pareja en cada ciclo y termina aceptando.
4. La maquina termina porque en cada ciclo marca 2 simbolos o rechaza.
