from __future__ import annotations


def inciso_a_es_decidible() -> tuple[bool, str]:
    """
    Inciso (a):
    "Para toda configuracion inicial, M termina antes de 100 pasos".

    Es decidible: el analisis se reduce a una cantidad finita de patrones
    relevantes (lo que la MT puede llegar a leer en <= 100 pasos).
    """

    justificacion = (
        "Decidible: en 100 pasos solo influye una porcion finita de la cinta; "
        "se pueden enumerar finitamente los patrones relevantes y simular "
        "acotadamente en cada caso."
    )
    return True, justificacion


def inciso_b_es_decidible() -> tuple[bool, str]:
    """
    Inciso (b):
    "Dada M, M imprimira alguna vez un 0".

    No es decidible por reduccion desde HALT.
    """

    justificacion = (
        "No decidible: por reduccion desde HALT. Construyendo M' que escribe 0 "
        "sii N(w) se detiene, decidir este problema decidiria HALT."
    )
    return False, justificacion


def demo() -> None:
    a_valor, a_just = inciso_a_es_decidible()
    b_valor, b_just = inciso_b_es_decidible()

    print("Ejercicio 3 - Decidibilidad")
    print(f"(a) decidible? {a_valor} -> {a_just}")
    print(f"(b) decidible? {b_valor} -> {b_just}")


if __name__ == "__main__":
    demo()
