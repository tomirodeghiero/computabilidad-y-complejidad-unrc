from __future__ import annotations

from maquina_turing import MaquinaTuringUnaCinta


# M2 de Sipser (ejemplo 3.7), decide A = { 0^(2^n) | n >= 0 }
def construir_m2() -> MaquinaTuringUnaCinta:
    estados = {
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "qaccept",
        "qreject",
    }

    transiciones = {
        ("q1", "0"): ("q2", "!", "R"),
        ("q1", "x"): ("qreject", "x", "R"),
        ("q1", "!"): ("qreject", "!", "R"),

        ("q2", "0"): ("q3", "x", "R"),
        ("q2", "x"): ("q2", "x", "R"),
        ("q2", "!"): ("qaccept", "!", "R"),

        ("q3", "0"): ("q4", "0", "R"),
        ("q3", "x"): ("q3", "x", "R"),
        ("q3", "!"): ("q5", "!", "L"),

        ("q4", "0"): ("q3", "x", "R"),
        ("q4", "x"): ("q4", "x", "R"),
        ("q4", "!"): ("qreject", "!", "R"),

        ("q5", "0"): ("q5", "0", "L"),
        ("q5", "x"): ("q5", "x", "L"),
        ("q5", "!"): ("q2", "!", "R"),
    }

    return MaquinaTuringUnaCinta(
        alfabeto_entrada={"0"},
        alfabeto_cinta={"0", "x", "!"},
        estados=estados,
        transiciones=transiciones,
        estado_inicial="q1",
        estado_aceptacion="qaccept",
        estado_rechazo="qreject",
        blanco="!",
    )


def main() -> None:
    m2 = construir_m2()
    entradas = ["0", "00", "000", "000000"]

    for entrada in entradas:
        resultado, historial = m2.ejecutar(entrada, guardar_historial=True)

        print(f"Entrada: {entrada}")
        for i, conf in enumerate(historial):
            print(f"  C{i}: {conf}")

        if not resultado.halted:
            print("  Resultado: no detuvo (max_pasos alcanzado)")
        else:
            print(
                "  Resultado:",
                "acepta" if resultado.accepted else "rechaza",
                f"(estado final: {resultado.estado_final}, pasos: {resultado.pasos})",
            )
        print()


if __name__ == "__main__":
    main()
