# Segunda parte - Ejercicio 1

Demostrar que la clase de lenguajes **decidibles** es cerrada bajo:

1. Union
2. Concatenacion
3. Complemento
4. Interseccion
5. Iteracion (estrella de Kleene)

---

## Contexto

Sean `L1` y `L2` lenguajes decidibles.
Entonces existen maquinas de Turing **decisoras** `D1` y `D2` tales que:

1. `D1` decide `L1` (siempre termina y responde aceptar/rechazar).
2. `D2` decide `L2` (siempre termina y responde aceptar/rechazar).

La estrategia en todos los incisos es construir una nueva maquina y verificar:

1. **Correctitud**: acepta exactamente las cadenas del lenguaje objetivo.
2. **Terminacion**: siempre se detiene.

---

## A) Cerradura por union

Queremos probar que `L1 U L2` es decidible.

### Construccion de decidor `DU`

Entrada: cadena `w`.

1. Ejecutar `D1` sobre `w`.
2. Si `D1` acepta, aceptar.
3. Si `D1` rechaza, ejecutar `D2` sobre `w`.
4. Si `D2` acepta, aceptar; en caso contrario, rechazar.

### Correctitud

1. Si `w` esta en `L1 U L2`, entonces `w` esta en `L1` o en `L2`.
2. Si esta en `L1`, `D1` acepta y `DU` acepta.
3. Si no esta en `L1` pero si en `L2`, `D1` rechaza, luego `D2` acepta y `DU` acepta.
4. Si `w` no pertenece a ninguna de las dos, ambas rechazan y `DU` rechaza.

### Terminacion

`D1` y `D2` siempre terminan, por lo tanto `DU` siempre termina.

---

## D) Cerradura por interseccion

Queremos probar que `L1 n L2` es decidible.

### Construccion de decidor `DI`

Entrada: `w`.

1. Ejecutar `D1(w)`. Si rechaza, rechazar.
2. Ejecutar `D2(w)`. Si rechaza, rechazar.
3. Si ambas aceptaron, aceptar.

### Correctitud

`DI` acepta si y solo si `w` pertenece simultaneamente a `L1` y `L2`, o sea a `L1 n L2`.

### Terminacion

Como `D1` y `D2` son decisores, el proceso termina siempre.

---

## C) Cerradura por complemento

Queremos probar que `co-L1` es decidible.

### Construccion de decidor `DC`

Entrada: `w`.

1. Ejecutar `D1(w)`.
2. Si `D1` acepta, `DC` rechaza.
3. Si `D1` rechaza, `DC` acepta.

### Correctitud

`DC` invierte la respuesta exacta de `D1`, por lo que acepta exactamente las cadenas fuera de `L1`.

### Terminacion

`D1` siempre termina, luego `DC` tambien.

---

## B) Cerradura por concatenacion

Queremos probar que `L1 . L2` es decidible.

Recordemos:
`w` pertenece a `L1 . L2` sii existe una particion `w = xy` con `x` en `L1` y `y` en `L2`.

### Construccion de decidor `DConcat`

Entrada: `w` con `n = |w|`.

1. Para cada `i` desde `0` hasta `n`:
2. Definir `x = prefijo de w de longitud i`.
3. Definir `y = sufijo de w desde i`.
4. Ejecutar `D1(x)` y `D2(y)`.
5. Si ambas aceptan para algun `i`, aceptar.
6. Si se revisaron todos los `i` y ninguno funciona, rechazar.

### Correctitud

1. Si `DConcat` acepta, encontro un corte `i` tal que `x` pertenece a `L1` e `y` a `L2`, luego `w` pertenece a `L1.L2`.
2. Si `w` pertenece a `L1.L2`, existe algun corte `i` valido; en ese `i`, `D1` y `D2` aceptan y `DConcat` acepta.

### Terminacion

1. Hay solo `n+1` cortes posibles.
2. En cada corte se ejecutan `D1` y `D2`, que terminan siempre.
3. Por lo tanto, `DConcat` termina siempre.

---

## E) Cerradura por iteracion (estrella de Kleene)

Queremos probar que `L1*` es decidible.

Recordemos:
`w` pertenece a `L1*` sii puede escribirse como concatenacion finita de cadenas de `L1`
(incluyendo 0 cadenas, caso `w = epsilon`).

### Construccion de decidor `DStar` (version con programacion dinamica)

Entrada: `w` de longitud `n`.

1. Si `w = epsilon`, aceptar.
2. Crear arreglo booleano `dp[0..n]`.
3. `dp[0] = verdadero`.
4. Para `j` desde `1` hasta `n`:
5. `dp[j] = verdadero` sii existe `i` con `0 <= i < j` tal que:
   - `dp[i] = verdadero`, y
   - `D1(w[i:j])` acepta.
6. Al final, aceptar sii `dp[n] = verdadero`; en caso contrario rechazar.

### Intuicion del invariante

`dp[j]` es verdadero sii el prefijo `w[0:j]` puede descomponerse en bloques de `L1`.

### Correctitud

1. Por definicion del invariante, `dp[n]` verdadero equivale a que todo `w` se descompone en piezas de `L1`.
2. Eso es exactamente `w` en `L1*`.

### Terminacion

1. Los bucles son finitos (`j` e `i` acotados por `n`).
2. Cada llamada a `D1` termina.
3. Entonces `DStar` termina siempre.

---

## Conclusion del ejercicio 1

La clase de lenguajes decidibles es cerrada bajo:

1. Union
2. Concatenacion
3. Complemento
4. Interseccion
5. Iteracion (estrella de Kleene)
