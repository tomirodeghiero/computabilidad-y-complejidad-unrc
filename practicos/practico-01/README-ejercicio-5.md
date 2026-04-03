# Ejercicio 5

## Enunciado

Escribir en Python una función que enumere todos los pares de naturales.

## Implementación

```python
def enumerar_pares_naturales():
    s = 0
    while True:
        for a in range(s + 1):
            b = s - a
            yield (a, b)
        s += 1
```

## Proposición

La función anterior enumera exactamente \(\mathbb N\times\mathbb N\).

## Demostración

Sea

\[
D_s=\{(a,b)\in\mathbb N^2 \mid a+b=s\},\quad s=0,1,2,\dots
\]

la \(s\)-ésima diagonal.

La función recorre primero \(D_0\), luego \(D_1\), luego \(D_2\), etc.

### Cobertura

Tomemos un par arbitrario \((m,n)\in\mathbb N^2\). Definimos \(s=m+n\).  
Cuando el bucle externo toma ese valor \(s\), el bucle interno visita \(a=0,1,\dots,s\). En particular visita \(a=m\), y entonces produce

\[
(a,s-a)=(m,m+n-m)=(m,n).
\]

Luego todo par de \(\mathbb N^2\) aparece.

### Unicidad

Supongamos que \((a,b)\) aparece dos veces. Entonces en ambas apariciones debe cumplirse \(a+b=s\), por lo que ambas estarían en la misma diagonal \(D_s\).  
Pero en una diagonal fija, el bucle interno recorre cada valor de \(a\) exactamente una vez. Contradicción.

Luego ningún par se repite.

Con cobertura y unicidad, la secuencia generada es una enumeración de \(\mathbb N^2\).

## Primeros términos

\[
(0,0),\ (0,1),\ (1,0),\ (0,2),\ (1,1),\ (2,0),\ (0,3),\dots
\]
