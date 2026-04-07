from __future__ import annotations

from maquina_turing_doble_infinita import MaquinaTuringDobleInfinita


def construir_mt_eq_01() -> MaquinaTuringDobleInfinita:
    """Decide L_eq = { w in {0,1}* | #0(w) = #1(w) }."""

    estados = {"q_seek", "q_find1", "q_find0", "q_back", "qaccept", "qreject"}

    transiciones = {
        # Buscar primer simbolo no marcado.
        ("q_seek", "x"): ("q_seek", "x", "R"),
        ("q_seek", "y"): ("q_seek", "y", "R"),
        ("q_seek", "0"): ("q_find1", "x", "R"),
        ("q_seek", "1"): ("q_find0", "y", "R"),
        ("q_seek", "!"): ("qaccept", "!", "S"),
        # Buscar un 1 para emparejar el 0 marcado.
        ("q_find1", "0"): ("q_find1", "0", "R"),
        ("q_find1", "x"): ("q_find1", "x", "R"),
        ("q_find1", "y"): ("q_find1", "y", "R"),
        ("q_find1", "1"): ("q_back", "y", "L"),
        ("q_find1", "!"): ("qreject", "!", "S"),
        # Buscar un 0 para emparejar el 1 marcado.
        ("q_find0", "1"): ("q_find0", "1", "R"),
        ("q_find0", "x"): ("q_find0", "x", "R"),
        ("q_find0", "y"): ("q_find0", "y", "R"),
        ("q_find0", "0"): ("q_back", "x", "L"),
        ("q_find0", "!"): ("qreject", "!", "S"),
        # Volver al inicio (primer blanco a la izquierda, luego R).
        ("q_back", "0"): ("q_back", "0", "L"),
        ("q_back", "1"): ("q_back", "1", "L"),
        ("q_back", "x"): ("q_back", "x", "L"),
        ("q_back", "y"): ("q_back", "y", "L"),
        ("q_back", "!"): ("q_seek", "!", "R"),
    }

    return MaquinaTuringDobleInfinita(
        alfabeto_entrada={"0", "1"},
        alfabeto_cinta={"0", "1", "x", "y", "!"},
        estados=estados,
        transiciones=transiciones,
        estado_inicial="q_seek",
        estado_aceptacion="qaccept",
        estado_rechazo="qreject",
        blanco="!",
    )


def construir_mt_2a1() -> MaquinaTuringDobleInfinita:
    """Decide L_2:1 = { w in {0,1}* | #0(w) = 2*#1(w) }."""

    estados = {
        "q_scan1",
        "q_back1",
        "q_find0a",
        "q_find0b",
        "q_back",
        "q_backf",
        "q_check0",
        "qaccept",
        "qreject",
    }

    transiciones = {
        # Buscar 1 no marcado.
        ("q_scan1", "0"): ("q_scan1", "0", "R"),
        ("q_scan1", "x"): ("q_scan1", "x", "R"),
        ("q_scan1", "y"): ("q_scan1", "y", "R"),
        ("q_scan1", "1"): ("q_back1", "y", "L"),
        ("q_scan1", "!"): ("q_backf", "!", "L"),
        # Volver al inicio tras marcar un 1.
        ("q_back1", "0"): ("q_back1", "0", "L"),
        ("q_back1", "1"): ("q_back1", "1", "L"),
        ("q_back1", "x"): ("q_back1", "x", "L"),
        ("q_back1", "y"): ("q_back1", "y", "L"),
        ("q_back1", "!"): ("q_find0a", "!", "R"),
        # Buscar primer 0 no marcado.
        ("q_find0a", "1"): ("q_find0a", "1", "R"),
        ("q_find0a", "x"): ("q_find0a", "x", "R"),
        ("q_find0a", "y"): ("q_find0a", "y", "R"),
        ("q_find0a", "0"): ("q_find0b", "x", "R"),
        ("q_find0a", "!"): ("qreject", "!", "S"),
        # Buscar segundo 0 no marcado.
        ("q_find0b", "1"): ("q_find0b", "1", "R"),
        ("q_find0b", "x"): ("q_find0b", "x", "R"),
        ("q_find0b", "y"): ("q_find0b", "y", "R"),
        ("q_find0b", "0"): ("q_back", "x", "L"),
        ("q_find0b", "!"): ("qreject", "!", "S"),
        # Volver al inicio para siguiente iteracion.
        ("q_back", "0"): ("q_back", "0", "L"),
        ("q_back", "1"): ("q_back", "1", "L"),
        ("q_back", "x"): ("q_back", "x", "L"),
        ("q_back", "y"): ("q_back", "y", "L"),
        ("q_back", "!"): ("q_scan1", "!", "R"),
        # Fase final: no quedan 1; verificar que no queden 0.
        ("q_backf", "0"): ("q_backf", "0", "L"),
        ("q_backf", "1"): ("q_backf", "1", "L"),
        ("q_backf", "x"): ("q_backf", "x", "L"),
        ("q_backf", "y"): ("q_backf", "y", "L"),
        ("q_backf", "!"): ("q_check0", "!", "R"),
        ("q_check0", "x"): ("q_check0", "x", "R"),
        ("q_check0", "y"): ("q_check0", "y", "R"),
        ("q_check0", "0"): ("qreject", "0", "S"),
        ("q_check0", "1"): ("qreject", "1", "S"),
        ("q_check0", "!"): ("qaccept", "!", "S"),
    }

    return MaquinaTuringDobleInfinita(
        alfabeto_entrada={"0", "1"},
        alfabeto_cinta={"0", "1", "x", "y", "!"},
        estados=estados,
        transiciones=transiciones,
        estado_inicial="q_scan1",
        estado_aceptacion="qaccept",
        estado_rechazo="qreject",
        blanco="!",
    )


def verificar(
    nombre: str,
    maquina: MaquinaTuringDobleInfinita,
    entradas: list[str],
    pertenece,
) -> None:
    print(f"=== {nombre} ===")
    hubo_error = False
    for w in entradas:
        resultado, _ = maquina.ejecutar(w, guardar_historial=False)
        esperado = pertenece(w)
        ok = resultado.accepted == esperado
        if not ok:
            hubo_error = True
        print(
            f"w={w!r:8} -> {'acepta' if resultado.accepted else 'rechaza'} "
            f"(esperado: {'acepta' if esperado else 'rechaza'}) "
            f"{'OK' if ok else 'ERROR'}"
        )
    if hubo_error:
        raise AssertionError(f"Fallo la verificacion en {nombre}")
    print()


def main() -> None:
    mt_eq = construir_mt_eq_01()
    mt_2a1 = construir_mt_2a1()

    verificar(
        "M_eq (#0 = #1)",
        mt_eq,
        ["", "0", "1", "01", "10", "0011", "0101", "001"],
        lambda w: w.count("0") == w.count("1"),
    )

    verificar(
        "M_2a1 (#0 = 2*#1)",
        mt_2a1,
        ["", "0", "1", "00", "001", "100", "001100", "0100", "011"],
        lambda w: w.count("0") == 2 * w.count("1"),
    )


if __name__ == "__main__":
    main()
