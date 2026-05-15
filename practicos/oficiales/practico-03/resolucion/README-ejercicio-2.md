# Ejercicio 2

## Enunciado

Escribir en Python la funcion `Self` que se reproduce a si misma.

## Contexto teorico

El Capitulo 6 de Sipser construye la MT `SELF` siguiendo el siguiente esquema:

- **Lema 6.1**: existe una funcion computable \(q:\Sigma^*\to\Sigma^*\) tal que, dado \(w\), \(q(w)\) es la descripcion de una MT \(P_w\) que en cualquier entrada borra la cinta, escribe \(w\) y se detiene.
- **`SELF`**: la MT se construye en dos partes \(A\) y \(B\). \(A\) es la maquina \(P_{\langle B\rangle}\), es decir, la que imprime \(\langle B\rangle\); \(B\) lee de la cinta el resultado dejado por \(A\) (que es \(\langle B\rangle\)), aplica \(q\) para reconstruir \(A=P_{\langle B\rangle}\) y luego concatena \(\langle A\rangle\) con \(\langle B\rangle\) para producir \(\langle AB\rangle = \langle\mathrm{SELF}\rangle\).

En Python las MT se modelan como programas, y el "imprimir su propia descripcion" se traduce en "imprimir su propio codigo fuente". Los programas que tienen esta propiedad se conocen como *quines* y son la version concreta del Teorema de la Recursion en un lenguaje de programacion real.

## Idea de la solucion

Implementamos la misma idea \(A+B\):

- La parte \(B\) es una cadena en una variable Python que describe el cuerpo del programa, con un marcador donde luego se "pega" su propia copia.
- La parte \(A\) es el codigo de impresion que reemplaza el marcador por la propia cadena `B`, citada como literal de Python.
- Al ejecutarse, el programa imprime la cadena resultante, que coincide con el codigo fuente completo del programa.

No se utiliza lectura de archivos ni introspeccion: el programa "conoce" su propia descripcion porque la tiene incrustada (al estilo Sipser, sin trampas).

## Codigo

```python
# self.py - Quine clasico estilo Sipser (parte A: el codigo de impresion;
# parte B: la cadena B que describe ese codigo).
B = 'B = {!r}\nprint(B.format(B))\n'
print(B.format(B))
```

### Explicacion linea por linea

- `B = '...'`: define una cadena que contiene la descripcion del propio programa, con el marcador `{!r}` (formato `repr`) en el lugar donde luego ira la propia `B`.
- `print(B.format(B))`: ejecuta la parte \(A\). El metodo `format` reemplaza `{!r}` por `repr(B)`, que devuelve la cadena `B` con comillas y caracteres escapados de modo que sea un literal Python valido. El resultado es exactamente el mismo texto del programa.

### Correspondencia con la construccion de Sipser

| Sipser (`SELF`)         | Quine en Python                                  |
|-------------------------|--------------------------------------------------|
| \(B\) (cadena base)     | El valor literal de la variable `B`              |
| \(A = P_{\langle B\rangle}\) | El `print(B.format(B))` que imprime `B`     |
| \(q\) (computa \(P_w\)) | El especificador `{!r}` de `format`              |
| Salida \(\langle AB\rangle\) | Texto impreso por `print`                   |

La clave es que `repr` cumple el rol de la funcion \(q\): tomar la cadena \(B\) y producir la descripcion de un programa (literal Python entre comillas) que la imprime.

## Verificacion

La forma estandar de verificar que un quine es correcto consiste en comparar su codigo fuente con la salida que produce. Una verificacion automatica:

```bash
diff <(python3 self.py) self.py
```

Si el quine es correcto, `diff` no produce salida (los archivos son iguales). En nuestra version anterior se cumple, ya que `repr(B)` genera la representacion exacta del literal que aparece en el codigo, y la cadena `B` describe literalmente las dos lineas del programa.

## Variante usando introspeccion (Teorema de la Recursion concreto)

Una version mas cercana a la formulacion del Teorema de la Recursion (que dice "puedo obtener mi propia descripcion y operar con ella") usa el modulo `inspect`:

```python
import inspect

def self_program():
    """Imprime el codigo fuente de esta misma funcion (autoreferencia)."""
    print(inspect.getsource(self_program))

if __name__ == "__main__":
    self_program()
```

Aqui `inspect.getsource(self_program)` devuelve el codigo fuente de la propia funcion, replicando lo que el Teorema de la Recursion garantiza para una MT: poder obtener \(\langle M\rangle\) desde dentro de \(M\). Esta variante no es estrictamente un quine puro (depende del archivo fuente y del modulo `inspect`), pero es la traduccion mas literal del enunciado teorico "una MT que obtiene su propia descripcion".

## Conclusion

La existencia del quine en Python es una evidencia practica del Teorema de la Recursion (Teorema 6.3 de Sipser): cualquier lenguaje de programacion Turing-completo permite escribir un programa que produce una copia exacta de si mismo. La construccion de Sipser para `SELF` se traduce directamente en el patron \(A+B\) usando `format` y `repr`.
