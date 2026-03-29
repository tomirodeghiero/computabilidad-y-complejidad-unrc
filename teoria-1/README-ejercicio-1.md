# Ejercicio 1

Implementar en Python las maquinas de Turing, programar ejemplos y testear.

## Resolucion

En esta carpeta implemente una MT deterministica de una cinta en `turing_machine.py`.

La cinta se representa con un diccionario `posicion -> simbolo`, asi que:

1. Las celdas no escritas se interpretan como blanco `_`.
2. Se puede crecer hacia la derecha (y tambien a la izquierda si se permite).
3. Es facil serializar la configuracion final.

Tambien cargue dos ejemplos:

1. `build_m1_w_hash_w_machine()` para `B = { w#w | w in {0,1}* }`.
2. `build_m2_power_of_two_zeros_machine()` para `A = { 0^(2^n) | n >= 0 }`.

La salida de la ejecucion devuelve:

1. `status`: `accept`, `reject` o `timeout`.
2. `steps`: cantidad de pasos.
3. `final_state`, `head`, `tape`.

## Tests

En `test_turing_machine.py` deje tests con `unittest` para M1 y M2, con casos validos e invalidos.

## Como ejecutar

```bash
python3 teoria-1/run_examples.py
python3 -m unittest discover -s teoria-1 -p "test_*.py"
```
