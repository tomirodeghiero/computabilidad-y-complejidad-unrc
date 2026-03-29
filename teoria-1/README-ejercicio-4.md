# Ejercicio 4

Demostrar que una MT con cinta doblemente infinita reconoce los mismos lenguajes que la MT estandar.

## Objetivo

Probar:

`L(MT_doble) = L(MT_estandar)`

## Inclusion 1

`L(MT_estandar) subseteq L(MT_doble)`

Una MT doble puede simular a la estandar sin dificultad:

1. Copia la entrada igual.
2. Marca el borde izquierdo.
3. Simula cada transicion.
4. Si se quiere mover a la izquierda del borde, se queda en el borde.

Reconoce exactamente el mismo lenguaje.

## Inclusion 2

`L(MT_doble) subseteq L(MT_estandar)`

Simulacion clasica en una cinta:

1. Usar un separador `#`.
2. Codificar a la izquierda de `#` la parte izquierda de la cinta simulada.
3. Codificar a la derecha de `#` la celda actual y la parte derecha.
4. Mover el cabezal simulado equivale a mover `#` con barridos locales.
5. Si se necesita una nueva celda "mas a la izquierda", se crea con corrimiento.

Cada paso de la MT doble se simula con una cantidad finita de pasos de la MT estandar.
Se preservan aceptacion y rechazo.

## Conclusion

Como valen ambas inclusiones:

`L(MT_doble) = L(MT_estandar)`

Por lo tanto ambos modelos tienen el mismo poder de reconocimiento.
