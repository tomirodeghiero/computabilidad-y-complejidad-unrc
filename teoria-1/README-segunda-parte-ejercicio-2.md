# Segunda parte - Ejercicio 2

Demostrar que la clase de lenguajes **reconocibles** (Turing-reconocibles) es cerrada bajo:

1. Union
2. Concatenacion
3. Interseccion
4. Iteracion (estrella de Kleene)

---

## Contexto

Sean `L1` y `L2` reconocibles.
Entonces existen maquinas `R1` y `R2` tales que:

1. Si `w` pertenece al lenguaje, la maquina eventualmente **acepta**.
2. Si `w` no pertenece, puede rechazar o quedarse en loop.

Como puede haber loops, para combinar maquinas no sirve "esperar una y despues la otra".
La tecnica correcta es **entrelazado (dovetailing)**: avanzar de a pasos en todas las simulaciones.

---

## F) Cerradura por union

Queremos reconocer `L1 U L2`.

### Construccion de reconocedor `RU`

Entrada: `w`.

1. Simular `R1(w)` y `R2(w)` en paralelo por rondas.
2. En cada ronda, ejecutar un paso de cada simulacion.
3. Si alguna acepta, aceptar.

### Correctitud

1. Si `w` esta en `L1 U L2`, al menos una de `R1(w)` o `R2(w)` acepta en tiempo finito.
2. Con dovetailing, esa aceptacion se alcanza en alguna ronda y `RU` acepta.
3. Si `w` no esta en la union, ninguna esta obligada a aceptar; `RU` puede no detenerse.
4. Eso coincide exactamente con ser reconocedor.

---

## H) Cerradura por interseccion

Queremos reconocer `L1 n L2`.

### Construccion de reconocedor `RI`

Entrada: `w`.

1. Simular `R1(w)` y `R2(w)` en paralelo por rondas.
2. Mantener dos banderas: `a1` (si `R1` ya acepto) y `a2` (si `R2` ya acepto).
3. Si en alguna ronda una maquina acepta, activar su bandera.
4. Aceptar cuando `a1` y `a2` sean verdaderas.

### Correctitud

1. Si `w` esta en `L1 n L2`, ambas aceptan en tiempo finito, y por dovetailing eventualmente ambas banderas se activan.
2. Entonces `RI` acepta.
3. Si `w` no pertenece a la interseccion, al menos una no acepta nunca; por lo tanto `RI` no acepta.
4. Nuevamente, comportamiento correcto de reconocedor.

---

## G) Cerradura por concatenacion

Queremos reconocer `L1 . L2`.

Recordemos:
`w` pertenece a `L1.L2` sii existe corte `w = xy` con `x` en `L1` e `y` en `L2`.

### Dificultad

Para un corte fijo, `R1(x)` o `R2(y)` pueden loop.
No podemos procesar cortes uno por uno "hasta terminar".

### Construccion de reconocedor `RConcat`

Entrada: `w`, `n = |w|`.

1. Enumerar los `n+1` cortes `i = 0..n`, con:
   - `x_i = w[0:i]`
   - `y_i = w[i:n]`
2. Para cada `i`, abrir dos simulaciones:
   - `S1_i = R1(x_i)`
   - `S2_i = R2(y_i)`
3. Ejecutar rondas infinitas. En cada ronda:
   - avanzar un paso en cada simulacion aun no detenida.
   - registrar si `S1_i` acepto y si `S2_i` acepto.
4. Si para algun `i` ambas simulaciones aceptaron, aceptar.

### Correctitud

1. Si `w` esta en `L1.L2`, existe `i*` tal que `x_i*` en `L1` e `y_i*` en `L2`.
2. Entonces `S1_i*` y `S2_i*` aceptan tras una cantidad finita de pasos.
3. Con dovetailing global, ambos eventos ocurren en alguna ronda finita y `RConcat` acepta.
4. Si `w` no esta en `L1.L2`, no existe corte con ambas aceptaciones; `RConcat` no acepta.

---

## I) Cerradura por iteracion (estrella de Kleene)

Queremos reconocer `L1*`, donde `L1` es reconocible por `R1`.

### Dificultad

Hay que considerar muchas descomposiciones de `w`.
Cada prueba de pertenencia de un bloque puede loop.

### Construccion de reconocedor `RStar`

Entrada: `w` de longitud `n`.

1. Si `w = epsilon`, aceptar.
2. Enumerar todas las particiones de `w` en bloques no vacios.
   - Son finitas: `2^(n-1)` particiones.
3. Para cada particion `p = (u1,...,uk)`, abrir simulaciones:
   - `Rp,1 = R1(u1)`, ..., `Rp,k = R1(uk)`.
4. Ejecutar dovetailing por rondas sobre **todas** las simulaciones de **todas** las particiones.
5. Si existe una particion `p` tal que todas sus simulaciones aceptaron, aceptar.

### Correctitud

1. Si `w` pertenece a `L1*`, existe una particion valida `w = u1...uk` con cada `ui` en `L1`.
2. Para esa particion, todas las corridas `R1(ui)` aceptan en tiempo finito.
3. Dovetailing garantiza alcanzar todas esas aceptaciones y entonces `RStar` acepta.
4. Si `w` no pertenece a `L1*`, ninguna particion tiene todos los bloques en `L1`; por ende `RStar` no acepta.

---

## Conclusion del ejercicio 2

La clase de lenguajes reconocibles es cerrada bajo:

1. Union
2. Concatenacion
3. Interseccion
4. Iteracion (estrella de Kleene)

Observacion: no se pidio complemento, y de hecho los reconocibles no son cerrados bajo complemento en general.
