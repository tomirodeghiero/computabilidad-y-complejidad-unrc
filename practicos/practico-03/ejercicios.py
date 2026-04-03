import inspect


def Self():
    """Imprime su propio codigo fuente (quine de funcion)."""
    s = "def Self():\n    s = {0!r}\n    print(s.format(s))"
    print(s.format(s))


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


def crear_clase_dinamica(nombre_clase: str, clase_base: type):
    metodos = {}
    for nombre, miembro in inspect.getmembers(clase_base, predicate=inspect.isfunction):
        if not nombre.startswith("__"):
            metodos[nombre] = miembro

    namespace = {
        "origen": clase_base.__name__,
        "descripcion": lambda self: f"{nombre_clase} creada desde {self.origen}",
        **metodos,
    }
    return type(nombre_clase, (object,), namespace)


if __name__ == "__main__":
    print("=== Ejercicio 1: Self ===")
    Self()

    print("\n=== Ejercicio 4: Introspeccion Persona ===")
    introspeccion_persona()

    print("\n=== Ejercicio 5: Clase dinamica ===")
    class Base:
        def saludar(self):
            return "hola"

    C = crear_clase_dinamica("ClaseGenerada", Base)
    obj = C()
    print(obj.descripcion())
    print(obj.saludar())
