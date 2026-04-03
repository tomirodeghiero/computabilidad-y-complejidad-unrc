# Ejercicio 1

## Enunciado

Mostrar que la clase PSPACE es la misma si se usan MT con una cinta o dos cintas. ¿Qué sucederá con \(k\) cintas?

## Proposición

El número de cintas no cambia la clase PSPACE (mientras \(k\) sea constante).

## Demostración

### (a) Una cinta \(\subseteq\) dos cintas

Trivial: toda MT de una cinta es un caso particular de MT de dos cintas (ignorando la segunda).

### (b) Dos cintas \(\subseteq\) una cinta

Sea \(M\) una MT de dos cintas que usa espacio \(s(n)\). Construimos una MT \(M'\) de una cinta que simula ambas cintas codificándolas en una sola (por ejemplo, intercalando símbolos y marcando posiciones de cabezal).

En esa codificación, cada celda usada de cada cinta de \(M\) aporta una cantidad constante de celdas en \(M'\).  
Por lo tanto, si \(M\) usa a lo sumo \(s(n)\) celdas por cinta, \(M'\) usa \(O(s(n))\) espacio total.

Luego, si \(s(n)\) es polinomial, \(M'\) sigue usando espacio polinomial.

Con (a) y (b), ambas definiciones de PSPACE coinciden.

### (c) Caso \(k\) cintas

El mismo argumento se generaliza para todo \(k\) constante:

- una MT de \(k\) cintas se codifica en una cinta,
- el espacio crece por un factor constante \(O(k)\),
- por ser \(k\) fijo, la clase sigue siendo PSPACE.

Conclusión: PSPACE es invariante respecto de usar 1, 2 o \(k\) cintas (con \(k\) constante).
