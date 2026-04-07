# Practica 1 - Maquinas de Turing (M2)

## Ejercicio 2

Para la MT `M2` (Sipser, capitulo 3, ejemplo 3.7), dar la secuencia de configuraciones para:

1. `0`
2. `00`
3. `000`
4. `000000`

### Convenciones

- Simbolo blanco: `!`
- Configuracion: `u q v`
  - `u`: contenido a la izquierda del cabezal
  - `q`: estado actual
  - `v`: contenido desde la celda bajo el cabezal hacia la derecha (incluye siempre el simbolo leido)

### Definicion de la maquina M2 usada

- `Q = {q1, q2, q3, q4, q5, qaccept, qreject}`
- `Sigma = {0}`
- `Gamma = {0, x, !}`

Transiciones `delta`:

- `delta(q1,0)=(q2,!,R)`
- `delta(q1,x)=(qreject,x,R)`
- `delta(q1,!)=(qreject,!,R)`

- `delta(q2,0)=(q3,x,R)`
- `delta(q2,x)=(q2,x,R)`
- `delta(q2,!)=(qaccept,!,R)`

- `delta(q3,0)=(q4,0,R)`
- `delta(q3,x)=(q3,x,R)`
- `delta(q3,!)=(q5,!,L)`

- `delta(q4,0)=(q3,x,R)`
- `delta(q4,x)=(q4,x,R)`
- `delta(q4,!)=(qreject,!,R)`

- `delta(q5,0)=(q5,0,L)`
- `delta(q5,x)=(q5,x,L)`
- `delta(q5,!)=(q2,!,R)`

### Secuencias de configuraciones

#### a) Entrada 0

- `C0 = q1 0`
- `C1 = ! q2 !`
- `C2 = !! qaccept !`

Resultado: **acepta**.

#### b) Entrada 00

- `C0 = q1 00`
- `C1 = ! q2 0`
- `C2 = !x q3 !`
- `C3 = ! q5 x`
- `C4 = q5 !x`
- `C5 = ! q2 x`
- `C6 = !x q2 !`
- `C7 = !x! qaccept !`

Resultado: **acepta**.

#### c) Entrada 000

- `C0 = q1 000`
- `C1 = ! q2 00`
- `C2 = !x q3 0`
- `C3 = !x0 q4 !`
- `C4 = !x0! qreject !`

Resultado: **rechaza**.

#### d) Entrada 000000

- `C0  = q1 000000`
- `C1  = ! q2 00000`
- `C2  = !x q3 0000`
- `C3  = !x0 q4 000`
- `C4  = !x0x q3 00`
- `C5  = !x0x0 q4 0`
- `C6  = !x0x0x q3 !`
- `C7  = !x0x0 q5 x`
- `C8  = !x0x q5 0x`
- `C9  = !x0 q5 x0x`
- `C10 = !x q5 0x0x`
- `C11 = ! q5 x0x0x`
- `C12 = q5 !x0x0x`
- `C13 = ! q2 x0x0x`
- `C14 = !x q2 0x0x`
- `C15 = !xx q3 x0x`
- `C16 = !xxx q3 0x`
- `C17 = !xxx0 q4 x`
- `C18 = !xxx0x q4 !`
- `C19 = !xxx0x! qreject !`

Resultado: **rechaza**.

### Verificacion final rapida

- `0` y `00` son longitudes potencia de 2 -> acepta.
- `000` y `000000` no son potencias de 2 -> rechaza.

Esto coincide con el lenguaje decidido por $M_2$:

$$
A=\{0^{2^n}\mid n\ge 0\}.
$$

---

## Ejercicio 3 - Definiciones de MT

Definir maquinas de Turing que decidan:

1. $L_1=\{\,w\in\{0,1\}^*\mid \#_0(w)=\#_1(w)\,\}$
2. $L_2=\{\,w\in\{0,1\}^*\mid \#_0(w)=2\cdot \#_1(w)\,\}$

donde $\#_a(w)$ denota la cantidad de apariciones del simbolo $a$ en $w$.

### Convenciones

- Usamos `!` como blanco.
- Usamos marcas auxiliares:
  - `x` para "0 ya usado"
  - `y` para "1 ya usado"

---

### (a) MT decider para $L_1$

$$
L_1=\{\,w\in\{0,1\}^*\mid \#_0(w)=\#_1(w)\,\}.
$$

#### Definicion (nivel implementacion, estilo Sipser)

Sea `M_eq` la MT:

`M_eq = "En entrada w:`

1. Ir al inicio de la cinta.
2. Buscar de izquierda a derecha el primer simbolo no marcado (`0` o `1`).
3. Si no existe ninguno (solo hay `x`, `y` y blancos), **aceptar**.
4. Si el simbolo encontrado es `0`, marcarlo como `x` y seguir a la derecha buscando un `1` no marcado.
5. Si se encuentra ese `1`, marcarlo como `y`, volver al inicio y repetir desde (2).
6. Si en (4) se llega a blanco sin encontrar `1`, **rechazar**.
7. Si el simbolo encontrado en (2) es `1`, marcarlo como `y` y seguir a la derecha buscando un `0` no marcado.
8. Si se encuentra ese `0`, marcarlo como `x`, volver al inicio y repetir desde (2).
9. Si en (7) se llega a blanco sin encontrar `0`, **rechazar**.

`"`

#### Forma matematica (7-tupla)

Definimos:

$$
M_{eq}=(Q,\Sigma,\Gamma,\delta,q_{seek},q_{accept},q_{reject})
$$

con:

- $$\Sigma=\{0,1\}$$
- $$\Gamma=\{0,1,x,y,!\}$$
- $$Q=\{q_{seek},q_{find1},q_{find0},q_{back},q_{accept},q_{reject}\}$$

Funcion de transicion $$\delta:Q\times\Gamma\to Q\times\Gamma\times\{L,R\}$$:

1. Estado de busqueda inicial:

   $$
   \delta(q_{seek},x)=(q_{seek},x,R),\quad
   \delta(q_{seek},y)=(q_{seek},y,R)
   $$

   $$
   \delta(q_{seek},0)=(q_{find1},x,R),\quad
   \delta(q_{seek},1)=(q_{find0},y,R),\quad
   \delta(q_{seek},!)=(q_{accept},!,R)
   $$

2. Buscar un `1` que empareje al `0` marcado:

   $$
   \delta(q_{find1},0)=(q_{find1},0,R),\;
   \delta(q_{find1},x)=(q_{find1},x,R),\;
   \delta(q_{find1},y)=(q_{find1},y,R)
   $$

   $$
   \delta(q_{find1},1)=(q_{back},y,L),\quad
   \delta(q_{find1},!)=(q_{reject},!,R)
   $$

3. Buscar un `0` que empareje al `1` marcado:

   $$
   \delta(q_{find0},1)=(q_{find0},1,R),\;
   \delta(q_{find0},x)=(q_{find0},x,R),\;
   \delta(q_{find0},y)=(q_{find0},y,R)
   $$

   $$
   \delta(q_{find0},0)=(q_{back},x,L),\quad
   \delta(q_{find0},!)=(q_{reject},!,R)
   $$

4. Volver al inicio:
   $$
   \delta(q_{back},a)=(q_{back},a,L)\ \text{para todo }a\in\{0,1,x,y\}
   $$
   $$
   \delta(q_{back},!)=(q_{seek},!,R)
   $$

#### Correctitud

- Si `M_eq` acepta, se marcaron parejas `0`-`1` hasta agotar todos los simbolos: entonces $\#_0(w)=\#_1(w)$.
- Si $\#_0(w)=\#_1(w)$, siempre que se toma un simbolo no marcado existe su pareja del otro tipo, por lo que la maquina nunca falla y termina aceptando.

#### Terminacion

Cada vuelta completa marca al menos dos simbolos nuevos. Como la entrada es finita, tras una cantidad finita de iteraciones la maquina acepta o rechaza.

---

### (b) MT decider para $L_2$

$$
L_2=\{\,w\in\{0,1\}^*\mid \#_0(w)=2\cdot \#_1(w)\,\}.
$$

#### Definicion (nivel implementacion, estilo Sipser)

Sea `M_2to1` la MT:

`M_2to1 = "En entrada w:`

1. Ir al inicio de la cinta.
2. Buscar de izquierda a derecha el primer `1` no marcado.
3. Si no existe `1` no marcado, ir a una fase final:
   - recorrer la cinta y verificar que no quede ningun `0` sin marcar;
   - si no queda ninguno, **aceptar**;
   - si queda al menos un `0`, **rechazar**.
4. Si se encontro `1`, marcarlo como `y`.
5. Volver al inicio y buscar el primer `0` no marcado. Si no existe, **rechazar**.
6. Marcar ese `0` como `x`.
7. Continuar buscando (hacia la derecha) un segundo `0` no marcado. Si no existe, **rechazar**.
8. Marcar ese segundo `0` como `x`.
9. Volver al inicio y repetir desde (2).

`"`

#### Forma matematica (7-tupla)

Definimos:

$$
M_{2:1}=(Q,\Sigma,\Gamma,\delta,q_{scan1},q_{accept},q_{reject})
$$

con:

- $$\Sigma=\{0,1\}$$
- $$\Gamma=\{0,1,x,y,!\}$$
- $$Q=\{q_{scan1},q_{back1},q_{find0a},q_{find0b},q_{back},q_{backf},q_{check0},q_{accept},q_{reject}\}$$

Intuicion de estados:

- `q_scan1`: busca un `1` no marcado.
- `q_find0a`: busca el primer `0` no marcado para ese `1`.
- `q_find0b`: busca el segundo `0` no marcado para ese `1`.
- `q_check0`: fase final (sin `1` pendientes), valida que no queden `0` sin marcar.

Funcion de transicion $$\delta:Q\times\Gamma\to Q\times\Gamma\times\{L,R\}$$:

1. Buscar `1` no marcado:

   $$
   \delta(q_{scan1},0)=(q_{scan1},0,R),\;
   \delta(q_{scan1},x)=(q_{scan1},x,R),\;
   \delta(q_{scan1},y)=(q_{scan1},y,R)
   $$

   $$
   \delta(q_{scan1},1)=(q_{back1},y,L),\quad
   \delta(q_{scan1},!)=(q_{backf},!,L)
   $$

2. Volver al inicio despues de marcar un `1`:

   $$
   \delta(q_{back1},a)=(q_{back1},a,L)\ \text{para todo }a\in\{0,1,x,y\}
   $$

   $$
   \delta(q_{back1},!)=(q_{find0a},!,R)
   $$

3. Buscar el primer `0` no marcado:

   $$
   \delta(q_{find0a},1)=(q_{find0a},1,R),\;
   \delta(q_{find0a},x)=(q_{find0a},x,R),\;
   \delta(q_{find0a},y)=(q_{find0a},y,R)
   $$

   $$
   \delta(q_{find0a},0)=(q_{find0b},x,R),\quad
   \delta(q_{find0a},!)=(q_{reject},!,R)
   $$

4. Buscar el segundo `0` no marcado:

   $$
   \delta(q_{find0b},1)=(q_{find0b},1,R),\;
   \delta(q_{find0b},x)=(q_{find0b},x,R),\;
   \delta(q_{find0b},y)=(q_{find0b},y,R)
   $$

   $$
   \delta(q_{find0b},0)=(q_{back},x,L),\quad
   \delta(q_{find0b},!)=(q_{reject},!,R)
   $$

5. Volver al inicio para repetir ciclo:

   $$
   \delta(q_{back},a)=(q_{back},a,L)\ \text{para todo }a\in\{0,1,x,y\}
   $$

   $$
   \delta(q_{back},!)=(q_{scan1},!,R)
   $$

6. Fase final (ya no quedan `1`):
   $$
   \delta(q_{backf},a)=(q_{backf},a,L)\ \text{para todo }a\in\{0,1,x,y\}
   $$
   $$
   \delta(q_{backf},!)=(q_{check0},!,R)
   $$
   $$
   \delta(q_{check0},x)=(q_{check0},x,R),\;
   \delta(q_{check0},y)=(q_{check0},y,R)
   $$
   $$
   \delta(q_{check0},0)=(q_{reject},0,R),\;
   \delta(q_{check0},1)=(q_{reject},1,R),\;
   \delta(q_{check0},!)=(q_{accept},!,R)
   $$

#### Correctitud

- Cada iteracion empareja exactamente `1` simbolo `1` con exactamente `2` simbolos `0`.
- Si la maquina acepta, no quedan `1` ni `0` sin marcar y todas las marcas se hicieron en bloques `2:1`, luego $\#_0(w)=2\cdot\#_1(w)$.
- Si $\#_0(w)=2\cdot\#_1(w)$, cada vez que se toma un `1` quedan disponibles dos `0` para marcar; al finalizar no quedaran `0` sueltos, por lo que acepta.
- Si la relacion no se cumple, en algun punto faltara un `0` para completar un bloque o sobraran `0` al final; en ambos casos rechaza.

#### Terminacion

Cada ciclo marca al menos un `1` (y hasta dos `0`), o rechaza. Como la cinta de entrada es finita, el proceso termina en tiempo finito.

---

### Conclusiones

- `M_eq` decide `L1`.
- `M_2to1` decide `L2`.

Por lo tanto, ambos lenguajes son decidibles.

---

## Ejercicio 4 - Cinta doblemente infinita

Una MT con cinta doblemente infinita (infinita a izquierda y derecha) reconoce los mismos lenguajes que una MT estandar.  
Demostrar:

$$
\mathcal{L}(TM_{2\text{-}way})=\mathcal{L}(TM_{std}).
$$

### Modelos

- `TM_std`: cinta infinita hacia la derecha, con extremo izquierdo.
- `TM_{2-way}`: cinta infinita en ambas direcciones, indices en `\mathbb{Z}`.

---

### Teorema

$$
\mathcal{L}(TM_{std})=\mathcal{L}(TM_{2\text{-}way}).
$$

### Demostracion

Probamos ambas inclusiones.

#### 1) Inclusion TM_std ⊆ TM_2-way

Sea `M` una MT estandar. Construimos una MT doblemente infinita `N` que simula `M`.

Idea: `N` usa un marcador de borde izquierdo `\vdash` y nunca permite que el cabezal cruce ese marcador.  
Cada paso de `M` se simula con una cantidad finita de pasos de `N`; cuando `M` acepta/rechaza, `N` acepta/rechaza.

Por lo tanto, todo lenguaje reconocible por una MT estandar tambien es reconocible por una MT de cinta doblemente infinita.

---

#### 2) Inclusion TM_2-way ⊆ TM_std

Sea

$$
B=(Q,\Sigma,\Gamma,\delta,q_0,q_{acc},q_{rej})
$$

una MT con cinta doblemente infinita. Construimos una MT estandar `S` que la simula.

#### 2.1 Codificacion de celdas

Codificamos la posicion entera `i\in\mathbb{Z}` en una posicion natural `e(i)\in\mathbb{N}`:

$$
e(i)=
\begin{cases}
2i & \text{si } i\ge 0,\\[2mm]
-2i-1 & \text{si } i<0.
\end{cases}
$$

Asi:

$$
0\mapsto 0,\;1\mapsto 2,\;2\mapsto 4,\dots,\;-1\mapsto 1,\;-2\mapsto 3,\dots
$$

En la cinta de `S`, la celda `e(i)` guarda el simbolo que `B` tiene en `i`.

Para marcar la posicion del cabezal de `B`, usamos una copia marcada del alfabeto:

$$
\dot{\Gamma}=\{\dot{a}:a\in\Gamma\}.
$$

Exactamente una celda contiene simbolo marcado (la celda bajo el cabezal simulado).

#### 2.2 Configuracion inicial

Si la entrada es `w=w_0w_1\cdots w_{n-1}`, la configuracion inicial de `B` pone:

- `w_j` en la celda `j` (para `0\le j<n`),
- blancos en el resto,
- cabezal en `0`.

`S` transforma la entrada a su codificacion en posiciones `0,2,4,\dots,2(n-1)` y marca la celda `0`.  
Esto se hace en tiempo finito.

#### 2.3 Simulacion de un paso

Supongamos que `S` esta simulando estado `q` de `B` y lee `\dot{a}` en la posicion codificada `k=e(h)`, donde `h` es la posicion del cabezal en `B`.

Si

$$
\delta(q,a)=(p,b,D),\quad D\in\{L,R\},
$$

`S` hace:

1. reemplaza `\dot{a}` por `b` (sin marca),
2. calcula la nueva posicion codificada `k'` del cabezal,
3. marca el simbolo en `k'`,
4. actualiza el estado simulado a `p`.

Las formulas de `k'` (derivadas de `e`) son:

Para `D=R`:

$$
k'=
\begin{cases}
k+2 & \text{si } k \text{ es par},\\
0 & \text{si } k=1,\\
k-2 & \text{si } k>1 \text{ impar}.
\end{cases}
$$

Para `D=L`:

$$
k'=
\begin{cases}
1 & \text{si } k=0,\\
k-2 & \text{si } k>0 \text{ par},\\
k+2 & \text{si } k \text{ es impar}.
\end{cases}
$$

Notar que `S` solo se mueve una distancia acotada (a lo sumo 2 celdas) para ubicar `k'`.

#### 2.4 Correctitud de la simulacion

Invariante: despues de cada fase de simulacion, la cinta de `S` codifica exactamente la cinta de `B` mediante `e`, y el unico simbolo marcado coincide con la posicion del cabezal de `B`.

- Base: vale en la configuracion inicial por construccion.
- Paso inductivo: las reglas de actualizacion de `k'` coinciden exactamente con mover `h` a `h\pm1` en `\mathbb{Z}`.

Luego, por induccion en el numero de pasos, `S` simula fielmente toda corrida de `B`.

Si `B` entra en `q_{acc}` (resp. `q_{rej}`), `S` entra en `q_{acc}` (resp. `q_{rej}`).

Por ende:

$$
L(S)=L(B).
$$

Concluimos:

$$
\mathcal{L}(TM_{2\text{-}way})\subseteq \mathcal{L}(TM_{std}).
$$

---

Como ya teniamos la inclusion opuesta, se obtiene la igualdad:

$$
\mathcal{L}(TM_{std})=\mathcal{L}(TM_{2\text{-}way}).
$$

Queda demostrado que ambos modelos reconocen exactamente los mismos lenguajes.

---

## Ejercicio 5 - Subconjunto infinito decidible

Demostrar que todo lenguaje infinito reconocible por MT tiene un subconjunto infinito que es decidible.

### Proposicion

Sea `A \subseteq \Sigma^*` un lenguaje infinito y Turing-reconocible.  
Entonces existe `B \subseteq A` tal que:

1. `B` es infinito.
2. `B` es decidible.

### Demostracion

Como `A` es Turing-reconocible, por el Teorema 3.21 de Sipser existe un enumerador `E` que enumera `A`.

Fijamos un orden total efectivo sobre `\Sigma^*`; tomamos `shortlex` (primero por longitud, luego lexicografico).  
Denotamos este orden por `<`.

#### 1) Construccion de una sucesion creciente en A

Definimos inductivamente una sucesion `(b_i)_{i\ge 1}`:

- `b_1`: primera cadena que imprime `E`.
- dado `b_i`, definimos `b_{i+1}` como la **primera** cadena que imprime `E` y satisface `b_{i+1} > b_i`.

Esta definicion es efectiva porque:

1. para cada `i`, podemos simular `E` paso a paso;
2. como `A` es infinito y `b_i \in A`, existe alguna cadena de `A` mayor que `b_i` en `shortlex`;
3. `E` imprime toda cadena de `A` en tiempo finito, asi que eventualmente aparece una mayor que `b_i`.

Luego cada `b_{i+1}` existe y se obtiene en tiempo finito.

Definimos:

$$
B=\{b_1,b_2,b_3,\dots\}.
$$

Por construccion:

$$
b_1 < b_2 < b_3 < \cdots
$$

y cada `b_i` es salida de `E`, luego `b_i \in A`. Por tanto:

$$
B \subseteq A.
$$

Ademas, la sucesion es estrictamente creciente e infinita, por lo que `B` es infinito.

#### 2) Decidibilidad de B

Construimos un decider `D_B` para `B`.

Entrada: `x`.

1. Generar `b_1,b_2,\dots` en orden (usando la construccion anterior).
2. Parar en el primer `b_k` tal que `b_k \ge x`.
3. Si `b_k = x`, aceptar. Si `b_k > x`, rechazar.

#### Correctitud

- Si `x \in B`, existe `k` con `x=b_k`; al llegar a ese `k`, `D_B` acepta.
- Si `x \notin B`, al primer `k` con `b_k \ge x` necesariamente `b_k > x`; `D_B` rechaza.

#### Terminacion

Bajo `shortlex`, el conjunto `{y \in \Sigma^* : y \le x}` es finito.  
Como `(b_i)` es estrictamente creciente e infinita, existe algun `k` con `b_k > x` o `b_k=x`.  
Cada `b_i` se calcula en tiempo finito, por lo que `D_B` siempre halta.

Concluimos que `B` es decidible e infinito, y `B \subseteq A`.

Por lo tanto, todo lenguaje infinito Turing-reconocible contiene un subconjunto infinito decidible.

---

## Ejercicio 6 - MT de una cinta sin escritura sobre el input

Mostrar que una MT de una sola cinta que no puede escribir sobre la parte que contiene el input solo puede reconocer lenguajes regulares.

### Aclaracion de modelo (hipotesis usada)

Tomamos la version estandar del ejercicio en teoria de automatas:

1. La maquina trabaja sobre una entrada de solo lectura (no modifica la zona de entrada).
2. El comportamiento sobre la entrada depende solo de estado actual y simbolo leido.
3. La cabeza puede moverse a izquierda/derecha dentro de la entrada (con marcadores de borde).

Bajo esta interpretacion, la maquina es esencialmente un automata finito de dos vias.

### Proposicion

Todo lenguaje reconocido por una maquina de ese tipo es regular.

### Demostracion

Sea

$$
M=(Q,\Sigma,\Gamma,\delta,q_0,q_{acc},q_{rej})
$$

una maquina de una cinta que no escribe sobre la zona de input.

Como no hay escritura en la entrada, el contenido de cada celda de entrada permanece fijo durante toda la computacion.  
Por lo tanto, en la parte de entrada la informacion dinamica de una configuracion queda determinada por:

1. el estado `q\in Q`,
2. la posicion del cabezal.

Eso coincide exactamente con el modelo de automata finito de dos vias (2DFA/2NFA): memoria finita (`Q`) y cinta de entrada de solo lectura.

### Construccion del 2DFA equivalente

Construimos un 2DFA

$$
A=(Q\cup\{q_{acc},q_{rej}\},\Sigma,\delta_A,q_0,F),
\quad F=\{q_{acc}\},
$$

con marcadores de extremos `\vdash,\dashv`, tal que:

- si en `M` una transicion sobre simbolo `a` (sin cambiarlo) es
  $$
  \delta(q,a)=(p,a,R),
  $$
  entonces en `A`:
  $$
  \delta_A(q,a)=(p,R);
  $$
- analogamente para movimiento `L`;
- cuando `M` entra en `q_{acc}` o `q_{rej}`, `A` entra en esos mismos estados de parada.

Como la entrada nunca se altera, cada paso de `M` en la zona de input se reproduce 1 a 1 en `A`. Luego:

$$
L(M)=L(A).
$$

### Cierre final

Por el teorema clasico de Rabin-Scott/Shepherdson:

$$
\text{Lenguajes reconocidos por 2DFA}=\text{Lenguajes regulares}.
$$

Entonces `L(A)` es regular, y por igualdad `L(M)=L(A)`, tambien `L(M)` es regular.

Concluimos que toda MT de una cinta de ese tipo reconoce solo lenguajes regulares.

---

## Parte de programacion

### Modelos implementados (items 1, 2 y 3)

Se implementaron los tres modelos pedidos:

1. MT de una cinta, infinita solo a derecha (`maquina_turing.py`).
2. MT de cinta doblemente infinita (`maquina_turing_doble_infinita.py`).
3. MT multicinta (`maquina_turing_multicinta.py`).

Ademas se agregaron demos:

- `ejercicio1_programar_mt.py`: `M2` de Sipser.
- `ejercicio2_programar_mt_doble.py`: demo con posiciones negativas reales.
- `ejercicio3_programar_mt_multicinta.py`: demo multicinta (copiadora de 2 cintas).

### Ejercicio 4 (programacion): implementar MT vistas en el teorico

Se implementaron, en codigo ejecutable, las MT definidas en la parte teorica:

1. `M_eq` que decide
   $$
   L_{eq}=\{w\in\{0,1\}^* : \#0(w)=\#1(w)\}.
   $$
2. `M_{2:1}` que decide
   $$
   L_{2:1}=\{w\in\{0,1\}^* : \#0(w)=2\cdot \#1(w)\}.
   $$

Archivo:

- `ejercicio4_mt_teorico.py`
  - construye ambas MT sobre `MaquinaTuringDobleInfinita`;
  - ejecuta casos de prueba;
  - verifica automaticamente el resultado contra el predicado matematico de cada lenguaje.

### Ejercicio 5 (programacion): algoritmos de traduccion entre 3 versiones de MT

Sea:

- `TM_1`: una cinta, infinita a derecha;
- `TM_2`: una cinta, doblemente infinita;
- `TM_k`: `k` cintas (con `k>=1`), cada una infinita a derecha.

Se piden algoritmos efectivos de traduccion. Los siguientes son correctos:

#### A) Traduccion TM_1 -> TM_2

Entrada: `M in TM_1`.

1. Reservar un marcador de borde izquierdo `⊢` (nuevo simbolo de cinta).
2. En la simulacion, ubicar `⊢` a la izquierda del input.
3. Copiar todas las transiciones de `M` sobre simbolos de trabajo normales.
4. Agregar transiciones para que nunca se cruce `⊢` hacia la izquierda:
   - si una transicion simulada intenta ir a la izquierda desde la primera celda util, dejar el cabezal en esa celda (comportamiento de borde de `TM_1`).

Resultado: una `N in TM_2` tal que `L(N)=L(M)`.

#### B) Traduccion TM_2 -> TM_1

Entrada: `B in TM_2`.

1. Codificar posiciones enteras `i in Z` en naturales con:
   $$
   e(i)=
   \begin{cases}
   2i & i\ge 0\\
   -2i-1 & i<0
   \end{cases}
   $$
2. En `TM_1`, la celda `e(i)` guarda el simbolo que `B` tiene en `i`.
3. Marcar exactamente una celda para indicar el cabezal simulado.
4. Para cada paso de `B`, actualizar:
   - simbolo marcado actual;
   - nueva posicion marcada segun mover `L` o `R` bajo la codificacion `e`.

Resultado: `S in TM_1` con `L(S)=L(B)`.

#### C) Traduccion TM_1 -> TM_k

Entrada: `M in TM_1`, `k>=1`.

1. Usar cinta 1 para simular exactamente la cinta de `M`.
2. Ignorar cintas `2..k` (dejarlas en blanco y sin efecto).
3. Copiar transiciones de `M` a transiciones de `TM_k` que solo cambian cinta 1.

Resultado: `N in TM_k` con `L(N)=L(M)`.

#### D) Traduccion TM_k -> TM_1

Entrada: `K in TM_k`.

1. Codificar en una sola cinta las `k` cintas usando bloques separados por `#`:
   $$
   \#u_1\#u_2\#\cdots\#u_k\#
   $$
2. En cada bloque, marcar el simbolo bajo el cabezal de esa cinta (version "punteada" del simbolo).
3. Simular un paso de `K` en fases:
   - Fase lectura: recorrer la cinta y leer los `k` simbolos marcados.
   - Fase transicion: calcular la regla de `K`.
   - Fase escritura/movimiento: segunda pasada para actualizar simbolos y mover marcas.
4. Repetir.

Resultado: `U in TM_1` con `L(U)=L(K)`.

#### E) Traducciones restantes

Se obtienen por composicion:

- `TM_2 -> TM_k` mediante `TM_2 -> TM_1 -> TM_k`.
- `TM_k -> TM_2` mediante `TM_k -> TM_1 -> TM_2`.

Por lo tanto, las tres variantes son equivalentes en poder de reconocimiento/decision.

### Ejecucion

Desde la raiz del repo:

```bash
python3 practicos/oficiales/practico-01/ejercicio1_programar_mt.py
python3 practicos/oficiales/practico-01/ejercicio2_programar_mt_doble.py
python3 practicos/oficiales/practico-01/ejercicio3_programar_mt_multicinta.py
python3 practicos/oficiales/practico-01/ejercicio4_mt_teorico.py
```
