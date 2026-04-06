# Ejercicio 1

## Enunciado

Describir una MT deterministica que borre el primer simbolo de la cinta y corra todos los demas una posicion hacia la izquierda.

Se asume entrada sobre `Sigma = {a, b}` y blanco `⊔`.

## Idea

1. En `q0` se borra el primer simbolo (si existe).
2. Luego se itera: se toma el siguiente simbolo, se borra, se lo "carga" en el hueco de la izquierda y se avanza al siguiente.
3. Cuando ya no quedan simbolos (`⊔`), la maquina acepta.

## Definicion formal

Sea la MT:

`M = (Q, Sigma, Gamma, delta, q0, ⊔, F)`

- `Q = {q0, q1, q_cargandoA, q_cargandoB, q3, q_accept, q_reject}`
- `Sigma = {a, b}`
- `Gamma = {a, b, ⊔}`
- Estado inicial: `q0`
- Blanco: `⊔`
- Estados de aceptacion: `F = {q_accept}`

### Funcion de transicion `delta`

- `delta(q0, a) = (q1, ⊔, R)`
- `delta(q0, b) = (q1, ⊔, R)`
- `delta(q0, ⊔) = (q_accept, ⊔, R)`  (entrada vacia)

- `delta(q1, a) = (q_cargandoA, ⊔, L)`
- `delta(q1, b) = (q_cargandoB, ⊔, L)`
- `delta(q1, ⊔) = (q_accept, ⊔, L)`  (no quedan mas simbolos)

- `delta(q_cargandoA, ⊔) = (q3, a, R)`
- `delta(q_cargandoB, ⊔) = (q3, b, R)`

- `delta(q3, ⊔) = (q1, ⊔, R)`

## Implementacion (Python)

Archivo:

- `practicos/practica-repaso/ejercicio-1/ejercicio1_borrar_primer_elemento.py`

El script incluye:

1. Un simulador minimo de MT deterministica (`MaqTuring`).
2. La funcion `borrar_primer_elemento(cinta)` con la `delta` del ejercicio.
3. Un `demo()` con varios casos de prueba.

Ejecucion:

```bash
python3 practicos/practica-repaso/ejercicio-1/ejercicio1_borrar_primer_elemento.py
```

Salida esperada (ejemplo):

```text
entrada='aba' -> salida='ba' estado=q_accept pasos=8
entrada='a' -> salida='' estado=q_accept pasos=2
entrada='' -> salida='' estado=q_accept pasos=1
entrada='bbab' -> salida='bab' estado=q_accept pasos=11
```

Uso desde otro archivo:

```python
from ejercicio1_borrar_primer_elemento import borrar_primer_elemento

maquina = borrar_primer_elemento("aba")
resultado = maquina.correr_cinta()
print(resultado.cinta_final)  # ba
```

## Verificacion rapida

- Entrada `"aba"` -> salida esperada `"ba"`
- Entrada `"a"` -> salida esperada `""` (solo blancos)
- Entrada `""` -> salida esperada `""`

Con esto la solucion queda completa (estados, alfabetos, transiciones y ejemplo de ejecucion).
