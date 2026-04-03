# Ejercicio 1

## Enunciado

Demostrar que el siguiente lenguaje es decidible:

\[
L = \{w \mid w \in \{0,1\}^*\}
\]

## Proposición

El lenguaje \(L\) es decidible.

## Demostración

Por definición (Sipser, Def. 3.6), alcanza exhibir una MT que halta en toda entrada y acepte exactamente \(L\).

Definimos el decider \(M\):

1. Entrada: una cadena \(w\).
2. Escanear \(w\) de izquierda a derecha.
3. Si se lee un símbolo distinto de \(0\) y \(1\), rechazar.
4. Si se alcanza el blanco inmediatamente posterior al final de la entrada, aceptar.

### Correctitud

1. Si \(M\) acepta \(w\), entonces durante todo el escaneo sólo aparecieron símbolos \(0\) o \(1\). Luego \(w \in \{0,1\}^*\), es decir, \(w \in L\).
2. Si \(w \in L\), todos los símbolos de \(w\) pertenecen a \(\{0,1\}\), por lo que \(M\) nunca dispara la condición de rechazo y al llegar al blanco final acepta.

Por (1) y (2), \(L(M)=L\).

### Terminación

En cada paso \(M\) avanza una celda a la derecha. Como la entrada es finita, en un número finito de pasos encuentra un símbolo inválido o el blanco final. En ambos casos halta.

Por lo tanto, \(M\) decide \(L\). Concluimos que \(L\) es decidible.
