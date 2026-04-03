# Ejercicio 5

## Enunciado

Usando introspección hacer una función que cree una clase dinámicamente.

## Solucion

Podemos usar `type(nombre, bases, namespace)` para construir clases en tiempo de ejecución y combinarlo con introspección para decidir qué atributos/métodos incluir.

```python
import inspect


def crear_clase_dinamica(nombre_clase: str, clase_base: type):
    # Introspeccion de la base
    metodos = {}
    for nombre, miembro in inspect.getmembers(clase_base, predicate=inspect.isfunction):
        if not nombre.startswith("__"):
            metodos[nombre] = miembro

    # Atributos nuevos para la clase dinamica
    namespace = {
        "origen": clase_base.__name__,
        "descripcion": lambda self: f"{nombre_clase} creada desde {self.origen}",
        **metodos,
    }

    # Creacion dinamica de clase
    NuevaClase = type(nombre_clase, (object,), namespace)
    return NuevaClase
```

## Ejemplo de uso

```python
class Base:
    def saludar(self):
        return "hola"


C = crear_clase_dinamica("ClaseGenerada", Base)
obj = C()
print(obj.descripcion())  # ClaseGenerada creada desde Base
print(obj.saludar())      # hola
```

## Comentario

La introspección aparece al inspeccionar `clase_base` para recuperar sus métodos; la construcción dinámica se realiza con `type`.
