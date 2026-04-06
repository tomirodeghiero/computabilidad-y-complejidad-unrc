# Ejercicio 4

## Enunciado

Disenar una MT que decida si un string es palindromo (sobre `Sigma = {a,b}`).

## Idea

1. Marcar el primer simbolo no procesado de la izquierda (`a` o `b`) con `X`.
2. Ir al extremo derecho y buscar el ultimo simbolo no procesado.
3. Si coincide con el que se marco al inicio, marcarlo con `X`.
4. Volver al inicio y repetir.
5. Si ya no quedan simbolos sin marcar, aceptar. Si hay desigualdad, rechazar.

## Implementacion (Python)

Archivo:

- `practicos/practica-repaso/ejercicio-4/ejercicio4_palindromo.py`

Ejecucion:

```bash
python3 practicos/practica-repaso/ejercicio-4/ejercicio4_palindromo.py
```

Salida esperada (ejemplo):

```text
entrada='' -> palindromo=True estado=q_accept pasos=2
entrada='a' -> palindromo=True estado=q_accept pasos=5
entrada='abba' -> palindromo=True estado=q_accept pasos=26
entrada='abab' -> palindromo=False estado=q_reject pasos=7
```

## Nota

- Tu enfoque de marcado era bueno.
- Si el enunciado pide palindromo general `w`, no hace falta `#` como separador de entrada.
- En esta implementacion `#` se usa solo como marcador izquierdo interno para adaptarse al simulador.
