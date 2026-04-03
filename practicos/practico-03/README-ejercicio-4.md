# Ejercicio 4

## Enunciado

Escribir una clase `Persona` en Python, con los atributos clásicos. Y hacer una función que con introspección:

- imprima la lista de atributos de la clase,
- imprima el código de alguno de los métodos.

## Solucion

```python
import inspect


class Persona:
    especie = "Humano"

    def __init__(self, nombre: str, apellido: str, edad: int, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def es_mayor(self) -> bool:
        return self.edad >= 18


def introspeccion_persona():
    print("Atributos de clase (sin metodos):")
    attrs_clase = []
    for k, v in Persona.__dict__.items():
        if not k.startswith("__") and not callable(v):
            attrs_clase.append(k)
    print(attrs_clase)

    print("\nAtributos de instancia:")
    p = Persona("Ada", "Lovelace", 36, "12345678")
    print(list(vars(p).keys()))

    print("\nCodigo del metodo nombre_completo:")
    print(inspect.getsource(Persona.nombre_completo))
```

## Comentario

`Persona.__dict__` permite inspeccionar miembros definidos en la clase, `vars(p)` muestra atributos de instancia, e `inspect.getsource` recupera el código fuente del método.
