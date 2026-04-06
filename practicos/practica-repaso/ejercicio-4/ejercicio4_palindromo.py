from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from maquina_turing import MaqTuring, Resultado

Transition = Tuple[str, str, str]


def mt_palindromo(cinta: str) -> MaqTuring:
    """
    Decide PAL = { w in {a,b}* | w es palindromo }.

    Estrategia:
    1) Tomar el primer simbolo no marcado (izquierda), marcarlo con X.
    2) Ir al extremo derecho y buscar el ultimo no marcado.
    3) Comparar: si coincide, marcar y repetir; si no, rechazar.
    4) Si no quedan simbolos no marcados, aceptar.

    Nota de implementacion:
    se usa un marcador izquierdo interno '#', porque el simulador trabaja
    con cinta acotada a izquierda (indice 0).
    """

    estados = [
        "q_start",
        "q_seek_right_a",
        "q_seek_right_b",
        "q_match_a",
        "q_match_b",
        "q_back_left",
        "q_accept",
        "q_reject",
    ]

    transiciones: Dict[Tuple[str, str], Transition] = {
        # q_start: buscar primer simbolo no marcado desde la izquierda
        ("q_start", "#"): ("q_start", "#", "R"),
        ("q_start", "X"): ("q_start", "X", "R"),
        ("q_start", "a"): ("q_seek_right_a", "X", "R"),
        ("q_start", "b"): ("q_seek_right_b", "X", "R"),
        ("q_start", "_"): ("q_accept", "_", "R"),

        # Ir al extremo derecho
        ("q_seek_right_a", "a"): ("q_seek_right_a", "a", "R"),
        ("q_seek_right_a", "b"): ("q_seek_right_a", "b", "R"),
        ("q_seek_right_a", "X"): ("q_seek_right_a", "X", "R"),
        ("q_seek_right_a", "_"): ("q_match_a", "_", "L"),

        ("q_seek_right_b", "a"): ("q_seek_right_b", "a", "R"),
        ("q_seek_right_b", "b"): ("q_seek_right_b", "b", "R"),
        ("q_seek_right_b", "X"): ("q_seek_right_b", "X", "R"),
        ("q_seek_right_b", "_"): ("q_match_b", "_", "L"),

        # Comparar con el ultimo simbolo no marcado
        ("q_match_a", "X"): ("q_match_a", "X", "L"),
        ("q_match_a", "a"): ("q_back_left", "X", "L"),
        ("q_match_a", "b"): ("q_reject", "b", "S"),
        ("q_match_a", "#"): ("q_accept", "#", "R"),  # caso centro unico
        ("q_match_a", "_"): ("q_reject", "_", "S"),  # no deberia ocurrir

        ("q_match_b", "X"): ("q_match_b", "X", "L"),
        ("q_match_b", "b"): ("q_back_left", "X", "L"),
        ("q_match_b", "a"): ("q_reject", "a", "S"),
        ("q_match_b", "#"): ("q_accept", "#", "R"),  # caso centro unico
        ("q_match_b", "_"): ("q_reject", "_", "S"),  # no deberia ocurrir

        # Volver al inicio para siguiente iteracion
        ("q_back_left", "a"): ("q_back_left", "a", "L"),
        ("q_back_left", "b"): ("q_back_left", "b", "L"),
        ("q_back_left", "X"): ("q_back_left", "X", "L"),
        ("q_back_left", "#"): ("q_start", "#", "R"),
    }

    return MaqTuring(
        "#" + cinta,
        ["a", "b", "#"],
        ["a", "b", "X", "#", "_"],
        estados,
        transiciones,
        estado_inicial="q_start",
        estado_aceptacion="q_accept",
        estado_rechazo="q_reject",
        blanco="_",
    )


def demo() -> None:
    casos = [
        "",
        "a",
        "b",
        "aa",
        "aba",
        "abba",
        "ababa",
        "abab",
        "baab",
        "baa",
    ]

    for cadena in casos:
        maquina = mt_palindromo(cadena)
        resultado: Resultado = maquina.correr_cinta()
        es_pal = resultado.estado_final == "q_accept"
        print(
            f"entrada={cadena!r} -> palindromo={es_pal} "
            f"estado={resultado.estado_final} pasos={resultado.pasos}"
        )


if __name__ == "__main__":
    demo()
