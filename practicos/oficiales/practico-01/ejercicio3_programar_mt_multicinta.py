from __future__ import annotations

from maquina_turing_multicinta import MaquinaTuringMultiCinta


def construir_copiadora_2_cintas() -> MaquinaTuringMultiCinta:
    """Maquina multicinta (2 cintas) que copia la cinta 1 en cinta 2.

    Alfabeto de entrada: {0,1}
    Transiciones principales:
    - Mientras tape1 lee 0/1 y tape2 lee blanco, escribe ese simbolo en tape2 y avanza ambas.
    - Cuando tape1 llega a blanco, acepta.
    """

    estados = {"q0", "qaccept", "qreject"}

    transiciones = {
        ("q0", ("0", "!")): ("q0", ("0", "0"), ("R", "R")),
        ("q0", ("1", "!")): ("q0", ("1", "1"), ("R", "R")),
        ("q0", ("!", "!")): ("qaccept", ("!", "!"), ("S", "S")),
    }

    return MaquinaTuringMultiCinta(
        numero_cintas=2,
        alfabeto_entrada={"0", "1"},
        alfabeto_cinta={"0", "1", "!"},
        estados=estados,
        transiciones=transiciones,
        estado_inicial="q0",
        estado_aceptacion="qaccept",
        estado_rechazo="qreject",
        blanco="!",
    )


def main() -> None:
    m = construir_copiadora_2_cintas()

    for entrada in ["", "0", "1011"]:
        resultado, historial = m.ejecutar(entrada, guardar_historial=True)

        print(f"Entrada: {entrada!r}")
        for i, conf in enumerate(historial):
            print(f"  C{i}: {conf}")

        if resultado.halted:
            print(
                "  Resultado:",
                "acepta" if resultado.accepted else "rechaza",
                f"(estado final: {resultado.estado_final}, pasos: {resultado.pasos})",
            )
            for i, cinta in enumerate(resultado.cintas_visibles, start=1):
                print(f"    Cinta {i}: {cinta}")
        else:
            print("  Resultado: no detuvo")
        print()


if __name__ == "__main__":
    main()
