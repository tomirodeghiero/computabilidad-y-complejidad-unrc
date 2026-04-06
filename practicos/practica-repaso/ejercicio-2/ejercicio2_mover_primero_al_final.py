from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from maquina_turing import MaqTuring, Resultado

Transition = Tuple[str, str, str]


def mover_primer_elemento_al_final(cinta: str) -> MaqTuring:
    """
    Mueve el primer simbolo de la cadena al final.

    Ejemplos:
    - "abab" -> "baba"
    - "a"    -> "a"
    - ""     -> ""
    """

    estados = [
        "q0",
        "q_shift_a",
        "q_shift_b",
        "q_copy_a_mem_a",
        "q_copy_b_mem_a",
        "q_copy_a_mem_b",
        "q_copy_b_mem_b",
        "q_back_mem_a",
        "q_back_mem_b",
        "q_finish_a",
        "q_finish_b",
        "q_accept",
        "q_reject",
    ]

    transiciones: Dict[Tuple[str, str], Transition] = {
        # q0: recordar primer simbolo en el estado y crear hueco en la celda 0
        ("q0", "a"): ("q_shift_a", "_", "R"),
        ("q0", "b"): ("q_shift_b", "_", "R"),
        ("q0", "_"): ("q_accept", "_", "R"),  # entrada vacia

        # q_shift_a: desplazar todo una posicion a izquierda, recordando que el primer simbolo era 'a'
        ("q_shift_a", "a"): ("q_copy_a_mem_a", "a", "L"),
        ("q_shift_a", "b"): ("q_copy_b_mem_a", "b", "L"),
        ("q_shift_a", "_"): ("q_finish_a", "_", "L"),

        # q_shift_b: igual, pero recordando primer simbolo 'b'
        ("q_shift_b", "a"): ("q_copy_a_mem_b", "a", "L"),
        ("q_shift_b", "b"): ("q_copy_b_mem_b", "b", "L"),
        ("q_shift_b", "_"): ("q_finish_b", "_", "L"),

        # Copiar simbolo leido a la celda de la izquierda
        ("q_copy_a_mem_a", "a"): ("q_back_mem_a", "a", "R"),
        ("q_copy_a_mem_a", "b"): ("q_back_mem_a", "a", "R"),
        ("q_copy_a_mem_a", "_"): ("q_back_mem_a", "a", "R"),

        ("q_copy_b_mem_a", "a"): ("q_back_mem_a", "b", "R"),
        ("q_copy_b_mem_a", "b"): ("q_back_mem_a", "b", "R"),
        ("q_copy_b_mem_a", "_"): ("q_back_mem_a", "b", "R"),

        ("q_copy_a_mem_b", "a"): ("q_back_mem_b", "a", "R"),
        ("q_copy_a_mem_b", "b"): ("q_back_mem_b", "a", "R"),
        ("q_copy_a_mem_b", "_"): ("q_back_mem_b", "a", "R"),

        ("q_copy_b_mem_b", "a"): ("q_back_mem_b", "b", "R"),
        ("q_copy_b_mem_b", "b"): ("q_back_mem_b", "b", "R"),
        ("q_copy_b_mem_b", "_"): ("q_back_mem_b", "b", "R"),

        # Volver a la celda original y avanzar al siguiente simbolo a procesar
        ("q_back_mem_a", "a"): ("q_shift_a", "a", "R"),
        ("q_back_mem_a", "b"): ("q_shift_a", "b", "R"),
        ("q_back_mem_a", "_"): ("q_shift_a", "_", "R"),

        ("q_back_mem_b", "a"): ("q_shift_b", "a", "R"),
        ("q_back_mem_b", "b"): ("q_shift_b", "b", "R"),
        ("q_back_mem_b", "_"): ("q_shift_b", "_", "R"),

        # Al llegar al blanco final, escribir el primer simbolo recordado y aceptar
        ("q_finish_a", "a"): ("q_accept", "a", "R"),
        ("q_finish_a", "b"): ("q_accept", "a", "R"),
        ("q_finish_a", "_"): ("q_accept", "a", "R"),

        ("q_finish_b", "a"): ("q_accept", "b", "R"),
        ("q_finish_b", "b"): ("q_accept", "b", "R"),
        ("q_finish_b", "_"): ("q_accept", "b", "R"),
    }

    return MaqTuring(
        cinta,
        ["a", "b"],
        ["a", "b", "_"],
        estados,
        transiciones,
    )


def demo() -> None:
    casos = ["abab", "ba", "a", "b", ""]

    for cadena in casos:
        maquina = mover_primer_elemento_al_final(cadena)
        resultado: Resultado = maquina.correr_cinta()
        print(
            f"entrada={cadena!r} -> salida={resultado.cinta_final!r} "
            f"estado={resultado.estado_final} pasos={resultado.pasos}"
        )


if __name__ == "__main__":
    demo()
