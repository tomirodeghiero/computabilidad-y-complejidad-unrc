# Ejercicio 6

## Enunciado

Mostrar que Sudoku es NP-completo.

## Aclaración importante

La NP-completitud se refiere a la versión **generalizada**:

- tablero de tamaño \(n^2\times n^2\),
- subcuadrículas \(n\times n\),
- entrada parcial, pregunta: ¿existe completación válida?

La versión fija \(9\times 9\) tiene tamaño acotado por constante, por lo que no modela una familia infinita para complejidad asintótica.

## 1) Sudoku generalizado está en NP

Dada una solución candidata:

1. verificar filas: cada número \(1,\dots,n^2\) aparece una vez,
2. verificar columnas,
3. verificar subcuadrículas \(n\times n\),
4. verificar coincidencia con celdas prellenadas.

Todo se chequea en tiempo polinomial en el tamaño del tablero.

## 2) NP-hardness

Resultado clásico (Yato & Seta): el problema de completación de Sudoku generalizado es NP-hard, mediante reducción polinomial desde un problema NP-completo (vía variantes de Latin Square Completion / SAT).

En consecuencia:

\[
SAT \le_p SUDOKU_{gen}
\]

o equivalentemente se obtiene NP-hardness de \(SUDOKU_{gen}\).

## Conclusión

Como \(SUDOKU_{gen}\in NP\) y es NP-hard:

\[
SUDOKU_{gen} \text{ es NP-completo.}
\]
