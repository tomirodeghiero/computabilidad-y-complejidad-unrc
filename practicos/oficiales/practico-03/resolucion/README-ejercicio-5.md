# Ejercicio 5

## Enunciado

Escribir una clase `Persona` en Python, con los atributos clasicos. Ademas, hacer una funcion que, mediante **introspeccion**:

- Imprima la lista de atributos de la clase.
- Imprima el codigo de alguno de los metodos.

## Contexto teorico

El Teorema de la Recursion (Sipser 6.3) dice que cualquier MT puede obtener su propia descripcion y operar con ella. En un lenguaje de programacion real esto se concreta como **introspeccion**: la posibilidad de inspeccionar, en tiempo de ejecucion, el codigo y la estructura de los propios objetos del programa.

Python expone esta capacidad mediante:

- el modulo estandar `inspect` (`inspect.getmembers`, `inspect.getsource`, `inspect.signature`, etc.);
- atributos especiales sobre clases e instancias: `__dict__`, `__name__`, `__bases__`, `__class__`, `__annotations__`;
- la funcion built-in `vars(obj)`, equivalente a `obj.__dict__`.

Las laminas de `autoref.pdf` resaltan esta correspondencia: la introspeccion en lenguajes como Python es la version practica del Teorema de la Recursion.

## Diseno de la clase `Persona`

Eligimos los atributos "clasicos" (nombre, edad, DNI, email) y un par de metodos representativos (`saludar`, `es_mayor_de_edad`, `__str__`):

```python
# persona.py
class Persona:
    """Representa a una persona con datos personales clasicos."""

    especie = "Homo sapiens"  # atributo de clase

    def __init__(self, nombre: str, edad: int, dni: str, email: str):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.email = email

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre} y tengo {self.edad} anios."

    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18

    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre!r}, edad={self.edad}, dni={self.dni!r})"
```

Observaciones:

- `especie` es un atributo *de clase* (compartido por todas las instancias).
- `nombre`, `edad`, `dni`, `email` son atributos *de instancia* (creados en `__init__`).
- Los metodos definidos son funciones invocables sobre instancias.

## Funcion de introspeccion

```python
import inspect

def inspeccionar(cls, metodo: str | None = None) -> None:
    """Imprime la lista de atributos de la clase y el codigo de un metodo.

    - Lista (atributos de clase, atributos de instancia, metodos).
    - Si se pasa `metodo`, imprime el codigo fuente de ese metodo;
      en caso contrario, se elige el primer metodo "normal" encontrado.
    """
    print(f"--- Inspeccion de la clase {cls.__name__} ---")

    # 1) Lista de atributos (incluye campos y metodos visibles via getmembers)
    miembros = inspect.getmembers(cls)
    atributos = [n for n, _ in miembros if not n.startswith("__")]
    print("Atributos y metodos publicos:")
    for nombre in atributos:
        print(f"  - {nombre}")

    # 2) Distincion fina entre atributos de datos y metodos
    print("\nClasificacion:")
    for nombre in atributos:
        valor = getattr(cls, nombre)
        tipo = "metodo" if inspect.isfunction(valor) else "atributo de clase"
        print(f"  - {nombre} ({tipo})")

    # 3) Codigo fuente de un metodo
    if metodo is None:
        metodos = [n for n, v in miembros if inspect.isfunction(v) and not n.startswith("__")]
        if not metodos:
            print("\n(No hay metodos publicos para mostrar.)")
            return
        metodo = metodos[0]

    print(f"\nCodigo del metodo `{metodo}`:")
    fuente = inspect.getsource(getattr(cls, metodo))
    print(fuente)


if __name__ == "__main__":
    inspeccionar(Persona)            # elige automaticamente saludar
    print()
    inspeccionar(Persona, "es_mayor_de_edad")
```

## Explicacion

- `inspect.getmembers(cls)` devuelve una lista de pares `(nombre, valor)` de todos los miembros de la clase, incluyendo metodos heredados y dunder methods. Filtramos los que empiezan con `__` para mostrar solo lo relevante.
- `inspect.isfunction(valor)` distingue metodos *definidos por el usuario* (`saludar`, `es_mayor_de_edad`) de atributos de clase (`especie`) o de dunder methods heredados.
- `inspect.getsource(funcion)` recupera, a partir del archivo fuente y del numero de linea, el texto exacto del metodo. Esta llamada es la "lectura de la propia descripcion" que el Teorema de la Recursion garantiza en abstracto.

## Salida esperada (resumida)

Al ejecutar `python3 persona.py`:

```text
--- Inspeccion de la clase Persona ---
Atributos y metodos publicos:
  - es_mayor_de_edad
  - especie
  - saludar

Clasificacion:
  - es_mayor_de_edad (metodo)
  - especie (atributo de clase)
  - saludar (metodo)

Codigo del metodo `es_mayor_de_edad`:
    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18

--- Inspeccion de la clase Persona ---
...
Codigo del metodo `es_mayor_de_edad`:
    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18
```

Notar que los **atributos de instancia** (`nombre`, `edad`, `dni`, `email`) **no** aparecen en la lista, porque solo se crean al instanciar `Persona`. Si quisieramos verlos tendriamos que inspeccionar una instancia particular:

```python
p = Persona("Ada", 36, "00000000", "ada@example.org")
print(vars(p))  # {'nombre': 'Ada', 'edad': 36, 'dni': '00000000', 'email': 'ada@example.org'}
```

Esta distincion es importante para no confundir el *molde* (clase) con sus *instancias*.

## Conexion con el Teorema de la Recursion

`inspect.getsource` es la materializacion del enunciado teorico

> "una MT puede obtener su propia descripcion \(\langle M\rangle\) y operar con ella"

en un lenguaje concreto. La funcion `inspeccionar` puede pensarse como una MT con oraculo a la *descripcion* de `Persona`. Si la propia funcion `inspeccionar` se inspeccionase a si misma, obtendriamos un caso autoreferencial completo (al estilo `SELF`):

```python
inspeccionar(type(inspeccionar))   # detalles tecnicos de la clase de la funcion
print(inspect.getsource(inspeccionar))
```

## Conclusion

Python provee de fabrica todas las herramientas necesarias para la introspeccion exigida por el ejercicio:

- `inspect.getmembers` para la lista de atributos y metodos.
- `inspect.isfunction` para separar metodos de atributos.
- `inspect.getsource` para imprimir el codigo de un metodo.

La existencia de estas funciones es una instancia practica del Teorema de la Recursion: el programa puede acceder a su propia descripcion y razonar sobre ella.
