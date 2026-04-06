# Ejercicio 2

## Enunciado

Describir una MT deterministica que mueva el primer elemento de la cinta al final.

Ejemplo esperado:

- `abab` -> `baba`

## Idea

1. En `q0` se borra el primer simbolo y se lo recuerda en el estado (`a` o `b`).
2. Se corre el resto de la cadena una posicion hacia la izquierda.
3. Cuando se llega al blanco final, se escribe el simbolo recordado.

## Definicion formal (resumen)

Sea:

`M = (Q, Sigma, Gamma, delta, q0, ⊔, F)`

- `Sigma = {a, b}`
- `Gamma = {a, b, ⊔}`
- `q0` inicial
- `F = {q_accept}`

Conjuntos principales de estados:

- `q_shift_a`, `q_shift_b`: desplazar mientras se recuerda el simbolo inicial.
- `q_copy_*`: copiar el simbolo actual al hueco de la izquierda.
- `q_back_*`: volver y avanzar al siguiente simbolo.
- `q_finish_a`, `q_finish_b`: escribir el simbolo inicial al final y aceptar.

## Implementacion (Python)

Archivo:

- `practicos/practica-repaso/ejercicio-2/ejercicio2_mover_primero_al_final.py`

Ejecucion:

```bash
python3 practicos/practica-repaso/ejercicio-2/ejercicio2_mover_primero_al_final.py
```

Salida esperada (ejemplo):

```text
entrada='abab' -> salida='baba' estado=q_accept pasos=12
entrada='ba' -> salida='ab' estado=q_accept pasos=6
entrada='a' -> salida='a' estado=q_accept pasos=3
entrada='b' -> salida='b' estado=q_accept pasos=3
entrada='' -> salida='' estado=q_accept pasos=1
```

## Observacion

- Tu idea inicial de guardar el primer simbolo en el estado era correcta.
- Faltaba el corrimiento a izquierda completo del resto de la cinta para eliminar el hueco inicial.
