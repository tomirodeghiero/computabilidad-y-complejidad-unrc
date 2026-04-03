# Ejercicio 2

## Enunciado

Implementar los algoritmos para ver si dos números son coprimos. Probarlos con números de 8 bits, 16 bits, 32 bits y 64 bits.

## Idea matemática

Dos enteros \(a,b\) son coprimos sii:

\[
\gcd(a,b)=1.
\]

Por lo tanto, cualquier algoritmo correcto para calcular \(\gcd\) permite decidir coprimalidad.

## Algoritmos implementados

Se implementaron dos algoritmos:

1. **Euclides clásico (con módulo)**  
   Repite \( (a,b)\leftarrow (b,a\bmod b)\) hasta \(b=0\).

2. **Algoritmo binario de Stein**  
   Usa solo operaciones binarias (corrimientos y restas), aprovechando paridad.

En ambos casos:

\[
\text{son\_coprimos}(a,b) \iff \gcd(a,b)=1.
\]

## Archivo de código

- [ejercicio2_coprimos.py](/Users/tomasrodeghiero/Documents/UNRC/computabilidad-y-complejidad-unrc/practicos/practico-04/ejercicio2_coprimos.py)

El script:

1. genera pares aleatorios de tamaño exacto de bits (8, 16, 32, 64),
2. ejecuta ambos algoritmos sobre los mismos pares,
3. verifica que ambos resultados coincidan,
4. reporta cantidad de casos coprimos y tiempo total por algoritmo.

## Ejecución

```bash
python3 practicos/practico-04/ejercicio2_coprimos.py
```

## Resultados obtenidos (200 muestras por tamaño)

```text
  bits   muestras   coprimos   euclides(ms)    stein(ms)
------------------------------------------------------------
     8        200        116          0.077        0.277
    16        200        127          0.123        0.540
    32        200        120          0.236        2.123
    64        200        138          1.807        3.304
```

## Conclusión

1. Ambos algoritmos dieron resultados idénticos en todos los tamaños (validación cruzada correcta).
2. Para estas muestras y esta implementación en Python, Euclides con módulo resultó más rápido que Stein.
3. Se cumplió la consigna de prueba en 8/16/32/64 bits.
