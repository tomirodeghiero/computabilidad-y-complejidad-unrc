# Ejercicio 2

Para la MT `M2`, dar secuencias de configuraciones para:

1. `0`
2. `00`
3. `000`
4. `000000`

Uso notacion `u q v`: el cabezal lee el primer simbolo de `v`.
`qA` es aceptacion y `qR` es rechazo.

## I) Entrada `0`

`q10 ⊢ _q2_ ⊢ _qA_`

Resultado: acepta.

## II) Entrada `00`

`q100 ⊢ _q20 ⊢ _xq3_ ⊢ _q5x ⊢ q5_x ⊢ _q2x ⊢ _xq2_ ⊢ _xqA_`

Resultado: acepta.

## III) Entrada `000`

`q1000 ⊢ _q200 ⊢ _xq30 ⊢ _x0q4_ ⊢ _x0qR_`

Resultado: rechaza.

## IV) Entrada `000000`

`q1000000`
`⊢ _q200000`
`⊢ _xq30000`
`⊢ _x0q4000`
`⊢ _x0xq300`
`⊢ _x0x0q40`
`⊢ _x0x0xq3_`
`⊢ _x0x0q5x`
`⊢ _x0xq50x`
`⊢ _x0q5x0x`
`⊢ _xq50x0x`
`⊢ _q5x0x0x`
`⊢ q5_x0x0x`
`⊢ _q2x0x0x`
`⊢ _xq20x0x`
`⊢ _xxq3x0x`
`⊢ _xxxq30x`
`⊢ _xxx0q4x`
`⊢ _xxx0xq4_`
`⊢ _xxx0xqR_`

Resultado: rechaza.
