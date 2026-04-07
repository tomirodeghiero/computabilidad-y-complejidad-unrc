from __future__ import annotations

from maquina_turing_doble_infinita import MaquinaTuringDobleInfinita


def construir_demo_doble() -> MaquinaTuringDobleInfinita:
    """Demo simple para mostrar uso de posiciones negativas.

    Entrada: cualquier cadena sobre {0,1}.
    Comportamiento:
    - va una celda a la izquierda de la posicion inicial,
    - escribe 'L',
    - vuelve a la derecha y acepta.
    """

    estados = {"q0", "q1", "q2", "qaccept", "qreject"}

    # Se define para simbolos posibles en la demo: 0, 1, ! y L.
    simbolos = ["0", "1", "!", "L"]

    transiciones = {}
    for s in simbolos:
        transiciones[("q0", s)] = ("q1", s, "L")
        transiciones[("q1", s)] = ("q2", "L", "R")
        transiciones[("q2", s)] = ("qaccept", s, "S")

    return MaquinaTuringDobleInfinita(
        alfabeto_entrada={"0", "1"},
        alfabeto_cinta={"0", "1", "!", "L"},
        estados=estados,
        transiciones=transiciones,
        estado_inicial="q0",
        estado_aceptacion="qaccept",
        estado_rechazo="qreject",
        blanco="!",
    )


def main() -> None:
    m = construir_demo_doble()

    for entrada in ["", "010"]:
        resultado, historial = m.ejecutar(entrada, guardar_historial=True)

        print(f"Entrada: {entrada!r}")
        for i, conf in enumerate(historial):
            print(f"  C{i}: {conf}")

        if resultado.halted:
            print(
                "  Resultado:",
                "acepta" if resultado.accepted else "rechaza",
                f"(estado final: {resultado.estado_final}, pasos: {resultado.pasos}, cabezal: {resultado.cabezal_final})",
            )
            print(f"  Cinta visible: {resultado.cinta_visible}")
        else:
            print("  Resultado: no detuvo")
        print()


if __name__ == "__main__":
    main()
