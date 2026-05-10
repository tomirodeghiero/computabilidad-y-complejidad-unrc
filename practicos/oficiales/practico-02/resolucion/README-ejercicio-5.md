# Ejercicio 5

## Enunciado

Encontrar un *matching* para el siguiente problema de Post:

\[
\left\{\frac{ab}{abab},\ \frac{b}{a},\ \frac{aba}{b},\ \frac{aa}{a}\right\}.
\]

## Recordatorio teorico

Una instancia del Problema de Correspondencia de Post (PCP, Seccion 5.2 de Sipser) consiste en una coleccion finita de "fichas" (dominos):

\[
P=\left\{\Big[\tfrac{t_1}{b_1}\Big],\Big[\tfrac{t_2}{b_2}\Big],\dots,\Big[\tfrac{t_k}{b_k}\Big]\right\}.
\]

Un *matching* es una secuencia de indices \(i_1,i_2,\dots,i_l\) (con repeticiones permitidas) tal que la concatenacion de los \(t_{i_j}\) en orden coincide con la concatenacion de los \(b_{i_j}\) en orden:

\[
t_{i_1}t_{i_2}\cdots t_{i_l}=b_{i_1}b_{i_2}\cdots b_{i_l}.
\]

## Numeracion de las fichas

Numeramos las fichas dadas:

| Indice | Arriba (\(t_i\)) | Abajo (\(b_i\)) |
|--------|----------------|-----------------|
| 1 | \(ab\) | \(abab\) |
| 2 | \(b\) | \(a\) |
| 3 | \(aba\) | \(b\) |
| 4 | \(aa\) | \(a\) |

## Busqueda del matching

Notamos algunas propiedades utiles antes de buscar:

- La ficha \(1\) tiene mas simbolos abajo (\(|b_1|=4\)) que arriba (\(|t_1|=2\)). Para que la concatenacion total coincida en longitud, necesitamos compensar con fichas en las que arriba aparezcan **mas** simbolos que abajo. Las candidatas son las fichas \(3\) (\(|t_3|=3>|b_3|=1\)) y \(4\) (\(|t_4|=2>|b_4|=1\)).
- Cualquier matching debe terminar con un caracter en comun en arriba y abajo.

Probamos la secuencia de indices

\[
(4,4,2,1).
\]

### Verificacion

Concatenacion de la parte superior:

\[
t_4 \cdot t_4 \cdot t_2 \cdot t_1 = aa\cdot aa\cdot b\cdot ab = aaaabab.
\]

Concatenacion de la parte inferior:

\[
b_4 \cdot b_4 \cdot b_2 \cdot b_1 = a\cdot a\cdot a\cdot abab = aaaabab.
\]

Ambas cadenas coinciden:

\[
aaaabab = aaaabab.
\]

Por lo tanto \((4,4,2,1)\) es un matching valido para la instancia dada.

## Visualizacion del emparejamiento

Mostramos el alineamiento ficha por ficha (la ficha \(i\) se escribe \([t_i/b_i]\)):

\[
\Big[\tfrac{aa}{a}\Big]\,\Big[\tfrac{aa}{a}\Big]\,\Big[\tfrac{b}{a}\Big]\,\Big[\tfrac{ab}{abab}\Big]
\]

Arriba: \(aa\,aa\,b\,ab = aaaabab\).
Abajo: \(a\,a\,a\,abab = aaaabab\).

Las fichas se acomodan asi:

```
| a a | a a | b | a b   |
| a   | a   | a | a b a b |
```

Reagrupando los simbolos para que se vean alineados:

\[
\begin{array}{c|c|c|c|c|c|c|c}
a & a & a & a & b & a & b & \\
\hline
a & a & a & a & b & a & b & 
\end{array}
\]

Las cadenas resultantes son identicas, confirmando el matching.

## Conclusion

Una solucion al problema de Post dado es la secuencia de indices

\[
\boxed{(4,4,2,1)}
\]

que produce arriba y abajo la cadena comun \(aaaabab\).
