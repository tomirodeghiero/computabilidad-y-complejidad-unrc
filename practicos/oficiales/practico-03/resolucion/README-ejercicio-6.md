# Ejercicio 6

## Enunciado

Usando introspeccion, hacer una funcion que cree una clase dinamicamente.

## Contexto teorico

En la jerga del Capitulo 6 de Sipser:

- El Teorema de la Recursion (Teorema 6.3) garantiza que una MT puede obtener su propia descripcion y operar con ella.
- Una consecuencia natural es la capacidad de **construir programas en tiempo de ejecucion**: a partir de descripciones manipuladas como datos, sintetizar nuevos objetos ejecutables.

En Python esto se llama **metaprogramacion**. La forma estandar de crear una clase en tiempo de ejecucion es usar la funcion built-in:

\[
\texttt{type(nombre, bases, atributos)}
\]

con la siguiente semantica:

- `nombre`: cadena con el nombre de la nueva clase.
- `bases`: tupla con las clases base de las que hereda.
- `atributos`: diccionario que mapea nombres (de campos y metodos) a sus valores.

`type(...)` con tres argumentos es exactamente el constructor que invoca Python por debajo cuando se evalua `class Foo(...): ...`. Es decir, escribir una `class` es solo *azucar sintactico* sobre `type`.

## Diseno

Vamos a escribir una funcion `crear_clase` que recibe:

- el nombre de la clase;
- una lista de nombres de atributos de instancia (que se asignaran en `__init__`);
- un diccionario opcional con metodos adicionales;
- una tupla opcional con clases base.

Y devuelve una nueva clase construida con `type`. Antes de retornarla, la inspecciona con `inspect` para mostrar que efectivamente quedo bien formada (cumple el item "usando introspeccion").

## Codigo

```python
# clase_dinamica.py
import inspect
from typing import Callable, Iterable


def crear_clase(
    nombre: str,
    campos: Iterable[str],
    metodos: dict[str, Callable] | None = None,
    bases: tuple[type, ...] = (object,),
):
    """Crea una clase dinamicamente y la devuelve.

    Parametros
    ----------
    nombre   : nombre de la nueva clase.
    campos   : iterable de nombres de atributos de instancia.
    metodos  : mapping nombre -> funcion. Se agregaran como metodos.
    bases    : tupla de clases base.
    """
    metodos = metodos or {}

    # --- 1. Construir el __init__ a partir de la lista de campos ----------
    campos = list(campos)

    def __init__(self, *args, **kwargs):
        if len(args) > len(campos):
            raise TypeError(
                f"{nombre}.__init__() recibe a lo sumo {len(campos)} argumentos posicionales"
            )
        for nombre_campo, valor in zip(campos, args):
            setattr(self, nombre_campo, valor)
        for nombre_campo, valor in kwargs.items():
            if nombre_campo not in campos:
                raise TypeError(f"campo desconocido para {nombre}: {nombre_campo!r}")
            setattr(self, nombre_campo, valor)

    def __repr__(self):
        partes = ", ".join(f"{c}={getattr(self, c, None)!r}" for c in campos)
        return f"{nombre}({partes})"

    # --- 2. Armar el diccionario de atributos -----------------------------
    atributos = {
        "__init__": __init__,
        "__repr__": __repr__,
        "__doc__": f"Clase generada dinamicamente con campos: {campos}",
        **metodos,
    }

    # --- 3. Construir la clase con type(...) ------------------------------
    cls = type(nombre, bases, atributos)

    # --- 4. Introspeccion: verificar la clase recien creada ---------------
    print(f"[ok] Clase creada: {cls.__name__}")
    print(f"     Bases       : {tuple(b.__name__ for b in cls.__bases__)}")
    print(f"     Docstring   : {cls.__doc__}")
    metodos_publicos = [
        n for n, v in inspect.getmembers(cls, inspect.isfunction)
        if not n.startswith("__")
    ]
    print(f"     Metodos     : {metodos_publicos or '(ninguno)'}")
    firma_init = inspect.signature(cls.__init__)
    print(f"     Firma init  : {firma_init}")

    return cls


# ------------------------ Ejemplo de uso --------------------------------- #
if __name__ == "__main__":
    Punto = crear_clase(
        "Punto",
        campos=["x", "y"],
        metodos={
            "norma": lambda self: (self.x ** 2 + self.y ** 2) ** 0.5,
            "trasladar": lambda self, dx, dy: Punto(self.x + dx, self.y + dy),
        },
    )

    print()
    p = Punto(3, 4)
    print("Instancia    :", p)
    print("norma        :", p.norma())
    print("trasladar    :", p.trasladar(1, 1))
    print("vars(p)      :", vars(p))
    print("type(p) es Punto:", type(p) is Punto)
```

## Explicacion paso a paso

1. **`type(nombre, bases, atributos)`** es el constructor universal de clases en Python. Llamarla con tres argumentos crea una nueva clase. Es exactamente lo que hace internamente la sentencia `class`.
2. Definimos un `__init__` cerrado sobre la lista `campos`: asigna los valores recibidos como argumentos a los atributos correspondientes. Validamos que no se pasen mas argumentos de los esperados y que las claves keyword esten en `campos`.
3. Definimos `__repr__` para que las instancias se muestren con sus campos.
4. Combinamos los metodos generados (`__init__`, `__repr__`) con los metodos adicionales pasados por el usuario en un unico `dict`.
5. Pasamos todo a `type(...)` para sintetizar la clase.
6. Antes de devolverla, hacemos **introspeccion** con `inspect.getmembers`, `inspect.signature`, y los atributos especiales `__bases__`, `__doc__`, etc., para mostrar concretamente que la clase quedo bien formada.

## Salida esperada (resumida)

```text
[ok] Clase creada: Punto
     Bases       : ('object',)
     Docstring   : Clase generada dinamicamente con campos: ['x', 'y']
     Metodos     : ['norma', 'trasladar']
     Firma init  : (self, *args, **kwargs)

Instancia    : Punto(x=3, y=4)
norma        : 5.0
trasladar    : Punto(x=4, y=5)
vars(p)      : {'x': 3, 'y': 4}
type(p) es Punto: True
```

## Variante: clases que heredan

La firma de `crear_clase` admite una tupla `bases`. Por ejemplo, se podria crear una clase que herede de `Persona` (Ejercicio 5):

```python
from persona import Persona

Empleado = crear_clase(
    "Empleado",
    campos=["nombre", "edad", "dni", "email", "salario"],
    metodos={"impuestos": lambda self: self.salario * 0.21},
    bases=(Persona,),
)
```

Aqui aprovechamos toda la maquinaria estandar de OOP: la clase nueva hereda metodos y la sintaxis de invocacion es identica a la de una clase definida estaticamente.

## Conexion con la teoria

Esta funcion es la version programable de la construccion del Teorema de la Recursion:

- En el plano teorico, una MT construye otra MT a partir de su descripcion (el `q` del Lema 6.1).
- En el plano practico, una funcion construye una clase a partir de su "descripcion" (nombre + bases + diccionario de atributos), usando `type` como `q`.

Asi como `SELF` puede manipular `\(\langle\mathrm{SELF}\rangle\)` para producir nuevas maquinas, `crear_clase` puede manipular descripciones de clases para producir nuevas clases.

## Conclusion

El uso de `type(...)` con tres argumentos, junto con el modulo `inspect` para verificar el resultado, permite crear clases en tiempo de ejecucion de manera completamente programatica. Esta capacidad es la traduccion concreta, en Python, de la libertad de manipular descripciones de programas como datos que el Teorema de la Recursion garantiza en abstracto.
