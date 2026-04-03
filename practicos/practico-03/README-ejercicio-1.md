# Ejercicio 1

## Enunciado

Escribir en Python la función `Self` que se reproduce a sí misma.

## Solucion

Una solución estándar es un *quine*: una función que imprime su propia definición sin leer su archivo.

```python
def Self():
    s = "def Self():\n    s = {0!r}\n    print(s.format(s))"
    print(s.format(s))
```

Al ejecutar `Self()`, la salida es exactamente el código fuente de `Self`.

## Comentario teorico

Este tipo de construcción está relacionado con la autorreferencia y con el Teorema de la Recursión: un programa puede, de manera efectiva, incorporar una representación de sí mismo.
