# Parte de programacion

## Resumen

La parte de programacion del Practico 01 pide:

1. Implementar la MT estandar (cinta unica e infinita a derecha).
2. Implementar la MT doblemente infinita.
3. Implementar la MT multicinta.
4. Implementar las MT vistas en clases (las del Ejercicio 3 teorico).
5. Escribir los algoritmos para traducir entre las tres versiones.

Las implementaciones existen ya en la carpeta del practico (no se modifican):

- `maquina_turing.py` -- MT estandar.
- `maquina_turing_doble_infinita.py` -- MT doblemente infinita.
- `maquina_turing_multicinta.py` -- MT multicinta.
- `ejercicio1_programar_mt.py` -- demo: \(M_2\) de Sipser.
- `ejercicio2_programar_mt_doble.py` -- demo: posiciones negativas.
- `ejercicio3_programar_mt_multicinta.py` -- demo: copiadora de 2 cintas.
- `ejercicio4_mt_teorico.py` -- las MT del Ejercicio 3 teorico (\(M_{eq}\) y \(M_{2{:}1}\)) ejecutadas y verificadas.

A continuacion se documentan los **algoritmos de traduccion** entre los tres modelos, que es el item 5 y la parte mas conceptual.

## Notacion

Denotamos por:

- \(\TM_1\) el modelo de MT con una cinta infinita a derecha;
- \(\TM_2\) el modelo de MT con una cinta doblemente infinita;
- \(\TM_k\) el modelo de MT con \(k\) cintas (cada una infinita a derecha), \(k\ge 1\).

Los tres modelos son equivalentes (Capitulo 3 de Sipser, Teoremas 3.13 y Problema 3.11). Damos algoritmos efectivos para traducir entre ellos.

## A) \(\TM_1 \to \TM_2\)

Entrada: \(M\in\TM_1\). Construir \(N\in\TM_2\) con \(L(N)=L(M)\).

1. Reservar un nuevo simbolo \(\vdash\in\Gamma_N\setminus\Gamma_M\) como marcador de borde izquierdo.
2. En la fase de inicializacion, \(N\) escribe \(\vdash\) en la celda \(-1\) (o equivalente), de modo que el cabezal "sepa" donde esta el extremo izquierdo simulado.
3. Transferir cada transicion de \(M\) a \(N\) literalmente. Para cualquier transicion de \(M\) que mueva el cabezal a la izquierda y la celda actual sea la del marcador \(\vdash\), \(N\) ejecuta una transicion que deja el cabezal en su lugar (replicando el comportamiento de borde izquierdo de \(\TM_1\)).
4. Estados de aceptacion y rechazo se preservan.

Esta es la construccion del Ejercicio 4, parte (1). Garantiza \(L(N)=L(M)\) por simulacion paso a paso.

## B) \(\TM_2 \to \TM_1\)

Entrada: \(B\in\TM_2\). Construir \(S\in\TM_1\) con \(L(S)=L(B)\).

1. Codificar las posiciones enteras \(i\in\mathbb Z\) en naturales mediante
   \[
     e(i) = \begin{cases} 2i & i\ge 0,\\ -2i-1 & i<0.\end{cases}
   \]
2. En la cinta de \(S\), la celda \(e(i)\) guarda el simbolo que \(B\) tiene en la celda \(i\).
3. Marcar exactamente una celda con un simbolo "punteado" \(\dot a\) para indicar la posicion del cabezal de \(B\).
4. La inicializacion reorganiza la entrada \(w_0w_1\cdots w_{n-1}\) en las celdas pares \(0,2,\dots,2(n-1)\), dejando blancos en las impares y marcando \(\dot w_0\).
5. Para cada paso de \(B\), \(S\) actualiza el simbolo escrito y mueve la marca a la nueva celda \(e(i\pm 1)\), usando las formulas explicitas del Ejercicio 4 (a lo sumo dos celdas de movimiento en la cinta de \(S\)).

Esta es la construccion del Ejercicio 4, parte (2).

## C) \(\TM_1 \to \TM_k\)

Entrada: \(M\in\TM_1\), \(k\ge 1\). Construir \(N\in\TM_k\) con \(L(N)=L(M)\).

Trivial:

1. Usar la cinta 1 de \(N\) para simular exactamente la cinta unica de \(M\).
2. Mantener las cintas \(2,3,\dots,k\) en blanco y sin movimientos efectivos (el cabezal queda fijo o sin cambios).
3. Cada transicion \(\delta_M(q,a)=(p,b,D)\) se traduce a \(\delta_N(q,a,\sqcup,\dots,\sqcup)=(p,b,\sqcup,\dots,\sqcup,D,S,\dots,S)\), donde \(S\) (stay put) puede simularse con un par de movimientos \(R,L\) si el modelo no admite \(S\) explicito.

## D) \(\TM_k \to \TM_1\)

Entrada: \(K\in\TM_k\). Construir \(U\in\TM_1\) con \(L(U)=L(K)\).

Esta es la construccion del Teorema 3.13 de Sipser. Idea:

1. Codificar las \(k\) cintas de \(K\) en una unica cinta de \(U\) usando bloques separados por un delimitador especial \(\#\):
   \[
     \#\,u_1\,\#\,u_2\,\#\,\cdots\,\#\,u_k\,\#,
   \]
   donde \(u_i\) es el contenido relevante de la \(i\)-esima cinta de \(K\).
2. En cada bloque, marcar con un simbolo "punteado" \(\dot a\) el simbolo bajo el cabezal de la cinta correspondiente.
3. Simular un paso de \(K\) en tres fases:
   - **Lectura:** \(U\) recorre su cinta de izquierda a derecha y memoriza en su control finito los \(k\) simbolos marcados.
   - **Calculo:** \(U\) consulta \(\delta_K\) con esos simbolos y el estado actual; obtiene la nueva tupla \((p, b_1,\dots,b_k, D_1,\dots,D_k)\).
   - **Escritura/movimiento:** \(U\) recorre nuevamente la cinta y, en cada bloque, reemplaza el simbolo marcado y mueve la marca a la celda vecina segun \(D_i\). Si una marca debe avanzar mas alla del fin de su bloque, \(U\) "expande" el bloque correspondiente desplazando todo el contenido a la derecha (operacion estandar de MT).

Por simulacion paso a paso, \(L(U)=L(K)\).

## E) Traducciones restantes

Las restantes traducciones se obtienen por composicion de las anteriores:

- \(\TM_2 \to \TM_k\): aplicar B luego C.
- \(\TM_k \to \TM_2\): aplicar D luego A.

Por ello, los tres modelos son **equivalentes** en poder de reconocimiento (y de decision):
\[
  \mathcal L(\TM_1) = \mathcal L(\TM_2) = \mathcal L(\TM_k) \quad\text{para todo }k\ge 1.
\]

Esta equivalencia es la **robustez** del modelo de MT que destacan tanto Sipser (pag. 176) como la teoria de la catedra: pequeñas variaciones en la cinta no cambian la clase de lenguajes reconocibles.

## Ejecucion de las demos

Desde la raiz del repositorio:

```bash
python3 practicos/oficiales/practico-01/ejercicio1_programar_mt.py
python3 practicos/oficiales/practico-01/ejercicio2_programar_mt_doble.py
python3 practicos/oficiales/practico-01/ejercicio3_programar_mt_multicinta.py
python3 practicos/oficiales/practico-01/ejercicio4_mt_teorico.py
```

Cada script imprime las trazas de configuracion y verifica el resultado contra el predicado matematico esperado.
