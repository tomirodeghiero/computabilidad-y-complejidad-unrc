# Ejercicio 4

## Enunciado

Demostrar que el problema de ver si una gramática libre de contexto genera alguna palabra con todos unos es decidible.

## Formalización

Definimos el lenguaje del problema:

\[
ALL1_{CFG}=\{\langle G\rangle \mid G \text{ es una CFG y } L(G)\cap 1^*\neq\varnothing\}.
\]

## Proposición

El lenguaje \(ALL1_{CFG}\) es decidible.

## Demostración

Construimos un decider \(T\) para \(ALL1_{CFG}\).

### Construcción de \(T\)

En entrada \(\langle G\rangle\):

1. Construir una PDA \(P_G\) tal que \(L(P_G)=L(G)\) (Sipser, Thm. 2.20).
2. Construir un DFA \(A_1\) que reconoce \(1^*\).
3. Construir la PDA producto \(P_\cap\) que simula a \(P_G\) y \(A_1\) en paralelo, de modo que
   \[
   L(P_\cap)=L(P_G)\cap L(A_1)=L(G)\cap 1^*.
   \]
4. Convertir \(P_\cap\) a una CFG \(G_\cap\) con
   \[
   L(G_\cap)=L(P_\cap)
   \]
   (de nuevo por Thm. 2.20).
5. Ejecutar el decider de
   \[
   E_{CFG}=\{\langle H\rangle \mid L(H)=\varnothing\}
   \]
   sobre \(\langle G_\cap\rangle\) (Sipser, Thm. 4.8).
6. Si \(L(G_\cap)=\varnothing\), rechazar. En caso contrario, aceptar.

### Correctitud

Debemos probar:

\[
\langle G\rangle\in ALL1_{CFG} \iff T \text{ acepta } \langle G\rangle.
\]

1. (\(\Rightarrow\)) Si \(\langle G\rangle\in ALL1_{CFG}\), existe \(w\in L(G)\cap 1^*\). Por construcción, \(w\in L(G_\cap)\), luego \(L(G_\cap)\neq\varnothing\). El test de vaciedad no acepta y \(T\) acepta.
2. (\(\Leftarrow\)) Si \(T\) acepta, necesariamente \(L(G_\cap)\neq\varnothing\). Sea \(w\in L(G_\cap)\). Por construcción de \(G_\cap\), \(w\in L(G)\cap 1^*\). Entonces \(\langle G\rangle\in ALL1_{CFG}\).

### Terminación

Todos los pasos son efectivos y finitos:

1. conversiones CFG \(\leftrightarrow\) PDA;
2. construcción del producto PDA\(\times\)DFA;
3. ejecución del decider de \(E_{CFG}\), que siempre halta.

Por lo tanto, \(T\) halta en toda entrada.

Concluimos que \(ALL1_{CFG}\) es decidible.
