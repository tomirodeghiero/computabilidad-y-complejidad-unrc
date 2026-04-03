# Ejercicio 1

## Enunciado

Decir cuáles son verdaderas y cuáles falsas:

1. \(2n \in O(n)\)
2. \(n^2 \in O(n)\)
3. \(n^2 \in O(n\log^2 n)\)
4. \(3^n \in 2^{O(n)}\)
5. \(2^n \in o(3^n)\)
6. \(1 \in o(1/n)\)

---

## Definiciones que usamos

Sean \(f,g:\mathbb N\to\mathbb R_{\ge 0}\).

1. \(f(n)\in O(g(n))\) sii existen constantes \(c>0\) y \(n_0\) tales que
   \[
   f(n)\le c\,g(n)\quad \forall n\ge n_0.
   \]

2. \(f(n)\in o(g(n))\) sii
   \[
   \lim_{n\to\infty}\frac{f(n)}{g(n)}=0.
   \]
   (equivalentemente: para todo \(\varepsilon>0\), existe \(n_0\) tal que \(f(n)\le \varepsilon g(n)\) para todo \(n\ge n_0\)).

3. \(2^{O(n)}\) significa el conjunto de funciones de la forma \(2^{h(n)}\) con \(h(n)\in O(n)\).

---

## Resolución detallada

### a) \(2n \in O(n)\)

Queremos ver si existe \(c>0\) con \(2n\le c\,n\) para \(n\) grande.

Tomando \(c=2\), se cumple \(2n\le 2n\) para todo \(n\ge 1\).  
Por lo tanto:

\[
2n\in O(n).
\]

Resultado: **Verdadera**.

---

### b) \(n^2 \in O(n)\)

Si fuera cierto, existirían \(c,n_0\) tales que \(n^2\le c\,n\) para \(n\ge n_0\).  
Dividiendo por \(n>0\):

\[
n\le c \quad \forall n\ge n_0,
\]

lo cual es imposible porque \(n\) no está acotado superiormente.

Equivalentemente, \(\frac{n^2}{n}=n\to\infty\), así que no puede estar en \(O(n)\).

Resultado: **Falsa**.

---

### c) \(n^2 \in O(n\log^2 n)\)

Estudiamos el cociente:

\[
\frac{n^2}{n\log^2 n}=\frac{n}{\log^2 n}.
\]

Como \(n\) crece más rápido que cualquier potencia de \(\log n\), se tiene

\[
\frac{n}{\log^2 n}\to\infty.
\]

Entonces no existe una constante \(c\) que acote ese cociente para \(n\) grande.

Resultado: **Falsa**.

---

### d) \(3^n \in 2^{O(n)}\)

Usamos cambio de base:

\[
3^n = 2^{n\log_2 3}.
\]

Definimos \(h(n)=n\log_2 3\). Como \(\log_2 3\) es constante, \(h(n)\in O(n)\).  
Luego \(3^n\) es de la forma \(2^{h(n)}\) con \(h(n)\in O(n)\), es decir:

\[
3^n \in 2^{O(n)}.
\]

Resultado: **Verdadera**.

---

### e) \(2^n \in o(3^n)\)

Calculamos el límite:

\[
\lim_{n\to\infty}\frac{2^n}{3^n}
=\lim_{n\to\infty}\left(\frac{2}{3}\right)^n
=0.
\]

Por definición de \(o(\cdot)\):

\[
2^n\in o(3^n).
\]

Resultado: **Verdadera**.

---

### f) \(1 \in o(1/n)\)

Miramos el cociente:

\[
\frac{1}{1/n}=n.
\]

Entonces

\[
\lim_{n\to\infty} n = \infty \neq 0.
\]

No se cumple la condición de \(o(\cdot)\).

Resultado: **Falsa**.

---

## Resumen final

1. \(2n \in O(n)\): **Verdadera**  
2. \(n^2 \in O(n)\): **Falsa**  
3. \(n^2 \in O(n\log^2 n)\): **Falsa**  
4. \(3^n \in 2^{O(n)}\): **Verdadera**  
5. \(2^n \in o(3^n)\): **Verdadera**  
6. \(1 \in o(1/n)\): **Falsa**
