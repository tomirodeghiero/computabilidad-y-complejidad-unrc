from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Tuple

Move = Literal["L", "R", "S"]
Transition = Tuple[str, str, Move]


@dataclass
class Resultado:
    estado_final: str
    pasos: int
    cinta_final: str


class MaqTuring:
    """Simulador minimo de MT deterministica de una cinta (acotada a izquierda)."""

    def __init__(
        self,
        cinta: str,
        alfabeto_entrada: list[str],
        alfabeto_cinta: list[str],
        estados: list[str],
        transiciones: Dict[Tuple[str, str], Transition],
        *,
        estado_inicial: str = "q0",
        estado_aceptacion: str = "q_accept",
        estado_rechazo: str = "q_reject",
        blanco: str = "_",
    ) -> None:
        self.alfabeto_entrada = set(alfabeto_entrada)
        self.alfabeto_cinta = set(alfabeto_cinta)
        self.estados = set(estados)
        self.transiciones = transiciones

        self.estado_inicial = estado_inicial
        self.estado_aceptacion = estado_aceptacion
        self.estado_rechazo = estado_rechazo
        self.blanco = blanco

        if self.blanco not in self.alfabeto_cinta:
            raise ValueError("El simbolo blanco debe pertenecer al alfabeto de cinta")

        for simbolo in cinta:
            if simbolo not in self.alfabeto_entrada:
                raise ValueError(f"Simbolo fuera del alfabeto de entrada: {simbolo!r}")

        self._cinta = list(cinta) if cinta else [self.blanco]
        self._cabezal = 0
        self._estado_actual = self.estado_inicial

    @property
    def cinta(self) -> str:
        # Devuelve el contenido util de la cinta (sin blancos de borde).
        texto = "".join(self._cinta)
        return texto.replace(self.blanco, "")

    def _leer(self) -> str:
        if self._cabezal >= len(self._cinta):
            self._cinta.extend([self.blanco] * (self._cabezal - len(self._cinta) + 1))
        return self._cinta[self._cabezal]

    def _escribir(self, simbolo: str) -> None:
        if simbolo not in self.alfabeto_cinta:
            raise ValueError(f"Simbolo fuera del alfabeto de cinta: {simbolo!r}")
        if self._cabezal >= len(self._cinta):
            self._cinta.extend([self.blanco] * (self._cabezal - len(self._cinta) + 1))
        self._cinta[self._cabezal] = simbolo

    def _mover(self, movimiento: Move) -> None:
        if movimiento == "R":
            self._cabezal += 1
            return
        if movimiento == "L":
            # Cinta acotada a izquierda: no se permite cabezal < 0.
            self._cabezal = max(0, self._cabezal - 1)
            return
        if movimiento == "S":
            return
        raise ValueError(f"Movimiento invalido: {movimiento!r}")

    def correr_cinta(self, max_pasos: int = 10_000) -> Resultado:
        pasos = 0

        while (
            self._estado_actual not in {self.estado_aceptacion, self.estado_rechazo}
            and pasos < max_pasos
        ):
            leido = self._leer()
            regla = self.transiciones.get((self._estado_actual, leido))

            if regla is None:
                self._estado_actual = self.estado_rechazo
                break

            nuevo_estado, escribir, mover = regla
            self._escribir(escribir)
            self._mover(mover)
            self._estado_actual = nuevo_estado
            pasos += 1

        # Limpieza de blancos a derecha para dejar una representacion estable.
        while len(self._cinta) > 1 and self._cinta[-1] == self.blanco:
            self._cinta.pop()

        return Resultado(
            estado_final=self._estado_actual,
            pasos=pasos,
            cinta_final=self.cinta,
        )


def borrar_primer_elemento(cinta: str) -> MaqTuring:
    estados = ["q0", "q1", "q_cargandoA", "q_cargandoB", "q3", "q_accept", "q_reject"]

    transiciones: Dict[Tuple[str, str], Transition] = {
        # Borrar primer simbolo
        ("q0", "a"): ("q1", "_", "R"),
        ("q0", "b"): ("q1", "_", "R"),
        ("q0", "_"): ("q_accept", "_", "R"),  # entrada vacia

        # Leer siguiente simbolo y dejar hueco
        ("q1", "a"): ("q_cargandoA", "_", "L"),
        ("q1", "b"): ("q_cargandoB", "_", "L"),
        ("q1", "_"): ("q_accept", "_", "L"),  # fin de cadena

        # Cargar simbolo en el hueco izquierdo
        ("q_cargandoA", "_"): ("q3", "a", "R"),
        ("q_cargandoB", "_"): ("q3", "b", "R"),

        # Volver a posicion de trabajo
        ("q3", "_"): ("q1", "_", "R"),
    }

    return MaqTuring(
        cinta,
        ["a", "b"],
        ["a", "b", "_"],
        estados,
        transiciones,
    )


def demo() -> None:
    casos = ["aba", "a", "", "bbab"]

    for cadena in casos:
        maquina = borrar_primer_elemento(cadena)
        resultado = maquina.correr_cinta()
        print(
            f"entrada={cadena!r} -> salida={resultado.cinta_final!r} "
            f"estado={resultado.estado_final} pasos={resultado.pasos}"
        )


if __name__ == "__main__":
    demo()
