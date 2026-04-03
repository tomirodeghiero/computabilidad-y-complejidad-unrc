# Ejercicio 3

## Enunciado

Usar la propiedad que el conjunto de lenguajes es incontable para demostrar que existen lenguajes que no pueden ser reconocidos con una máquina con un oráculo \(A_{TM}\).

## Proposición

Existen lenguajes \(L\subseteq\Sigma^*\) que no son reconocibles por ninguna MT con oráculo \(A_{TM}\).

## Demostración

1. El conjunto de todas las máquinas de Turing con oráculo \(A_{TM}\) es contable.
   - Cada máquina con oráculo tiene una descripción finita (código + estados + alfabeto + transiciones + estado de consulta).
   - El conjunto de descripciones finitas sobre un alfabeto finito es contable.

2. Cada una de esas máquinas reconoce a lo sumo un lenguaje.

3. El conjunto de todos los lenguajes sobre \(\Sigma\), es decir \(\mathcal P(\Sigma^*)\), es no contable.
   - Esto se prueba por diagonalización (Cantor), tal como en Sipser.

Si todos los lenguajes fueran reconocibles por alguna máquina con oráculo \(A_{TM}\), tendríamos una sobreyección de un conjunto contable (máquinas-oráculo) sobre un conjunto no contable (todos los lenguajes), lo cual es imposible.

Por lo tanto, hay lenguajes que no son reconocibles incluso disponiendo del oráculo \(A_{TM}\).
