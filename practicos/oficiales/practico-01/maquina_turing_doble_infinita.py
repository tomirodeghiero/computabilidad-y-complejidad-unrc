from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Tuple

Move = Literal["L", "R", "S"]
Transition = Tuple[str, str, Move]


@dataclass
class ResultadoEjecucionDoble:
    halted: bool
    accepted: bool
    estado_final: str
    pasos: int
    cabezal_final: int
    cinta_visible: str


class MaquinaTuringDobleInfinita:
    """MT deterministica de una cinta doblemente infinita.

    La cinta se modela sobre indices enteros (..., -2, -1, 0, 1, 2, ...).
    """

    def __init__(
        self,
        *,
        alfabeto_entrada: set[str],
        alfabeto_cinta: set[str],
        estados: set[str],
        transiciones: Dict[Tuple[str, str], Transition],
        estado_inicial: str,
        estado_aceptacion: str,
        estado_rechazo: str,
        blanco: str = "_",
    ) -> None:
        self.alfabeto_entrada = set(alfabeto_entrada)
        self.alfabeto_cinta = set(alfabeto_cinta)
        self.estados = set(estados)
        self.transiciones = dict(transiciones)

        self.estado_inicial = estado_inicial
        self.estado_aceptacion = estado_aceptacion
        self.estado_rechazo = estado_rechazo
        self.blanco = blanco

        if self.blanco not in self.alfabeto_cinta:
            raise ValueError("El simbolo blanco debe pertenecer al alfabeto de cinta")
        if self.estado_inicial not in self.estados:
            raise ValueError("Estado inicial invalido")
        if self.estado_aceptacion not in self.estados:
            raise ValueError("Estado de aceptacion invalido")
        if self.estado_rechazo not in self.estados:
            raise ValueError("Estado de rechazo invalido")

        self._validar_transiciones()

        self._cinta: dict[int, str] = {}
        self._cabezal = 0
        self._estado_actual = self.estado_inicial

    def _validar_transiciones(self) -> None:
        for (estado, simbolo), (nuevo_estado, escribir, mover) in self.transiciones.items():
            if estado not in self.estados:
                raise ValueError(f"Estado invalido en transicion: {estado}")
            if simbolo not in self.alfabeto_cinta:
                raise ValueError(f"Simbolo leido invalido en transicion: {simbolo}")
            if nuevo_estado not in self.estados:
                raise ValueError(f"Nuevo estado invalido en transicion: {nuevo_estado}")
            if escribir not in self.alfabeto_cinta:
                raise ValueError(f"Simbolo escrito invalido en transicion: {escribir}")
            if mover not in {"L", "R", "S"}:
                raise ValueError(f"Movimiento invalido en transicion: {mover}")

    def reset(self, entrada: str) -> None:
        for simbolo in entrada:
            if simbolo not in self.alfabeto_entrada:
                raise ValueError(f"Simbolo fuera del alfabeto de entrada: {simbolo!r}")

        self._cinta = {}
        for i, simbolo in enumerate(entrada):
            if simbolo != self.blanco:
                self._cinta[i] = simbolo

        self._cabezal = 0
        self._estado_actual = self.estado_inicial

    def _leer(self) -> str:
        return self._cinta.get(self._cabezal, self.blanco)

    def _escribir(self, simbolo: str) -> None:
        if simbolo == self.blanco:
            self._cinta.pop(self._cabezal, None)
        else:
            self._cinta[self._cabezal] = simbolo

    def _mover(self, movimiento: Move) -> None:
        if movimiento == "R":
            self._cabezal += 1
            return
        if movimiento == "L":
            self._cabezal -= 1
            return
        # movimiento == "S": no cambia

    def _rango_visible(self) -> tuple[int, int]:
        if not self._cinta:
            return self._cabezal, self._cabezal
        izquierda = min(min(self._cinta.keys()), self._cabezal)
        derecha = max(max(self._cinta.keys()), self._cabezal)
        return izquierda, derecha

    def configuracion_actual(self) -> str:
        izq, der = self._rango_visible()
        partes: list[str] = []

        for i in range(izq, der + 1):
            if i == self._cabezal:
                partes.append(f"[{self._estado_actual}]")
            partes.append(self._cinta.get(i, self.blanco))

        return f"({izq}..{der}) " + "".join(partes)

    def _cinta_visible(self) -> str:
        izq, der = self._rango_visible()
        return " ".join(f"{i}:{self._cinta.get(i, self.blanco)}" for i in range(izq, der + 1))

    def paso(self) -> bool:
        if self._estado_actual in {self.estado_aceptacion, self.estado_rechazo}:
            return False

        simbolo = self._leer()
        regla = self.transiciones.get((self._estado_actual, simbolo))

        if regla is None:
            self._estado_actual = self.estado_rechazo
            return True

        nuevo_estado, escribir, mover = regla
        self._escribir(escribir)
        self._mover(mover)
        self._estado_actual = nuevo_estado
        return True

    def ejecutar(
        self,
        entrada: str,
        *,
        max_pasos: int = 100_000,
        guardar_historial: bool = False,
    ) -> tuple[ResultadoEjecucionDoble, list[str]]:
        self.reset(entrada)

        historial: list[str] = []
        pasos = 0

        if guardar_historial:
            historial.append(self.configuracion_actual())

        while (
            self._estado_actual not in {self.estado_aceptacion, self.estado_rechazo}
            and pasos < max_pasos
        ):
            self.paso()
            pasos += 1
            if guardar_historial:
                historial.append(self.configuracion_actual())

        halted = self._estado_actual in {self.estado_aceptacion, self.estado_rechazo}
        accepted = self._estado_actual == self.estado_aceptacion

        resultado = ResultadoEjecucionDoble(
            halted=halted,
            accepted=accepted,
            estado_final=self._estado_actual,
            pasos=pasos,
            cabezal_final=self._cabezal,
            cinta_visible=self._cinta_visible(),
        )
        return resultado, historial
