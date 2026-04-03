# Ejercicio 3

## Enunciado

Demostrar que \(P\) es cerrada con respecto a la unión, intersección y concatenación.

## Definición recordatoria

\[
P=\{L \mid L \text{ es decidible en tiempo polinomial por una MT determinista}\}.
\]

Sea \(L_1,L_2\in P\). Entonces existen decidores deterministas \(M_1,M_2\) y polinomios \(p_1,p_2\) tales que:

- \(M_1\) decide \(L_1\) en tiempo \(\le p_1(n)\),
- \(M_2\) decide \(L_2\) en tiempo \(\le p_2(n)\),

donde \(n=|w|\).

---

## 1) Cierre por unión

Queremos mostrar \(L_1\cup L_2\in P\).

Algoritmo \(M_\cup\) sobre entrada \(w\):

1. Ejecutar \(M_1(w)\). Si acepta, aceptar.
2. Ejecutar \(M_2(w)\). Si acepta, aceptar.
3. En otro caso, rechazar.

Correctitud: acepta ssi \(w\in L_1\) o \(w\in L_2\).  
Tiempo:

\[
T_\cup(n)\le p_1(n)+p_2(n)+O(1),
\]

que es polinomial. Luego \(L_1\cup L_2\in P\).

---

## 2) Cierre por intersección

Queremos mostrar \(L_1\cap L_2\in P\).

Algoritmo \(M_\cap\) sobre entrada \(w\):

1. Ejecutar \(M_1(w)\). Si rechaza, rechazar.
2. Ejecutar \(M_2(w)\). Si acepta, aceptar; si no, rechazar.

Correctitud: acepta ssi \(w\in L_1\) y \(w\in L_2\).  
Tiempo:

\[
T_\cap(n)\le p_1(n)+p_2(n)+O(1),
\]

polinomial. Luego \(L_1\cap L_2\in P\).

---

## 3) Cierre por concatenación

Queremos mostrar \(L_1\cdot L_2\in P\), donde

\[
L_1\cdot L_2=\{w\mid \exists i,\ w=u v,\ |u|=i,\ u\in L_1,\ v\in L_2\}.
\]

Algoritmo \(M_{\circ}\) sobre entrada \(w\), con \(n=|w|\):

1. Para cada \(i=0,1,\dots,n\):
   - definir \(u=w[0:i]\), \(v=w[i:n]\),
   - ejecutar \(M_1(u)\) y \(M_2(v)\),
   - si ambos aceptan, aceptar.
2. Si ningún corte funciona, rechazar.

Correctitud:

- Si el algoritmo acepta, existe corte \(w=uv\) con \(u\in L_1\) y \(v\in L_2\), luego \(w\in L_1\cdot L_2\).
- Si \(w\in L_1\cdot L_2\), existe algún corte \(w=uv\) con \(u\in L_1\), \(v\in L_2\); cuando el bucle prueba ese \(i\), acepta.

Tiempo:

- Hay \(n+1\) cortes.
- En cada corte, \(|u|,|v|\le n\), luego
  \[
  T_i \le p_1(n)+p_2(n)+O(n)
  \]
  (incluyendo costo de formar subcadenas).

Entonces

\[
T_{\circ}(n)\le (n+1)\big(p_1(n)+p_2(n)+O(n)\big),
\]

que sigue siendo polinomial.

Por lo tanto \(L_1\cdot L_2\in P\).

---

## Conclusión

La clase \(P\) es cerrada bajo:

1. unión,
2. intersección,
3. concatenación.
