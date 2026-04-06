# Ejercicio 3 (a y b)

## Enunciado

Dada una MT `M`, decidir si son decidibles:

1. Para todas las configuraciones iniciales (entradas), `M` termina antes de 100 pasos.
2. Dada una MT `M`, esta imprimira alguna vez un `0`.

### a) "Para toda entrada, termina antes de 100 pasos"

**Resultado: decidible.**

Idea clave: en 100 pasos, una MT solo puede leer una porcion finita y acotada de la cinta.

- Si el cabezal inicia en la celda 0, en 100 pasos no puede leer mas alla de las primeras 101 celdas relevantes.
- Por lo tanto, el comportamiento de `M` en esos 100 pasos depende solo de un prefijo finito de la entrada (mas blancos).
- Aunque haya infinitas entradas, para este problema solo hay finitos patrones distintos que pueden afectar esos 100 pasos.

Decidor:

1. Enumerar todos los patrones de entrada relevantes para las primeras 101 celdas.
2. Simular `M` en cada caso por hasta 100 pasos.
3. Si en algun caso no se detiene antes del paso 100, rechazar.
4. Si en todos se detiene antes del paso 100, aceptar.

Como el conjunto a chequear es finito y cada simulacion es acotada, el algoritmo siempre termina.

### b) "Dada `M`, imprimira alguna vez un 0"

**Resultado: no decidible.**

Reduccion desde HALT:

- Partimos de una instancia `(N, w)` del problema de parada.
- Construimos una maquina `M'` que:
  1. Simula `N` sobre `w`.
  2. Si `N` se detiene, entonces `M'` escribe `0`.
  3. Si `N` no se detiene, `M'` nunca escribe `0`.

Entonces:

- `M'` imprime alguna vez `0` sii `N` se detiene con `w`.

Si existiera un decidor para "imprime alguna vez 0", podriamos decidir HALT, lo cual es imposible.
Por contradiccion, el problema es indecidible.

Observacion: este lenguaje es reconocible (semi-decidible), porque podemos simular `M` y aceptar apenas aparezca un `0` escrito.

## Implementacion de apoyo (Python)

Archivo:

- `practicos/practica-repaso/ejercicio-3/ejercicio3_decidibilidad.py`

Ejecucion:

```bash
python3 practicos/practica-repaso/ejercicio-3/ejercicio3_decidibilidad.py
```
