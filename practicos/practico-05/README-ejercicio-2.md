# Ejercicio 2

## Enunciado

Mostrar que PSPACE es cerrado bajo la unión, la complementación y la estrella.

## 1) Cierre por unión

Sean \(L_1,L_2\in\) PSPACE. Existen decidores deterministas \(M_1,M_2\) que usan espacio polinomial.

Para decidir \(L_1\cup L_2\), sobre entrada \(w\):

1. correr \(M_1(w)\); si acepta, aceptar;
2. si no, correr \(M_2(w)\); aceptar/rechazar según corresponda.

La máquina reutiliza espacio entre corridas, por lo que usa

\[
O(p_1(|w|)+p_2(|w|))
\]

espacio, que es polinomial. Entonces \(L_1\cup L_2\in\) PSPACE.

## 2) Cierre por complementación

Si \(L\in\) PSPACE, existe decidor determinista \(M\) en espacio polinomial para \(L\).
Para decidir \(\overline{L}\), usamos la misma máquina e invertimos estados de aceptación/rechazo.

El espacio no cambia. Por lo tanto \(\overline{L}\in\) PSPACE.

## 3) Cierre por estrella

Sea \(L\in\) PSPACE, decidido por \(M\) en espacio \(p(n)\).
Queremos decidir \(L^*\).

Entrada \(w\), \(|w|=n\). Definimos el problema de alcanzabilidad de cortes:

\[
R(i) := \text{``el sufijo } w[i:n] \text{ pertenece a } L^* \text{''}.
\]

Ecuación:

\[
R(i)=\bigvee_{j=i+1}^{n}\left( w[i:j]\in L \ \wedge\ R(j)\right),
\quad R(n)=\text{verdadero}.
\]

Podemos decidir \(R(0)\) con DFS recursivo:

1. en estado \(i\), iterar \(j=i+1,\dots,n\);
2. para cada \(j\), correr \(M\) sobre \(w[i:j]\);
3. si acepta y luego \(R(j)\) es verdadero, aceptar.

La profundidad es a lo sumo \(n\), cada nivel guarda índices \(O(\log n)\), y cada llamada a \(M\) usa a lo sumo \(p(n)\) (porque \(|w[i:j]|\le n\)).

Espacio total:

\[
O(n\log n + p(n)),
\]

que es polinomial. Luego \(L^*\in\) PSPACE.

## Conclusión

PSPACE es cerrado bajo:

1. unión,
2. complementación,
3. estrella de Kleene.
