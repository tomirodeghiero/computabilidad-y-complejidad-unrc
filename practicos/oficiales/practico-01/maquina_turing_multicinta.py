from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Tuple

Move = Literal["L", "R", "S"]
ReadTuple = Tuple[str, ...]
WriteTuple = Tuple[str, ...]
MoveTuple = Tuple[Move, ...]
TransitionMulti = Tuple[str, WriteTuple, MoveTuple]


@dataclass
class ResultadoEjecucionMulti:
    halted: bool
    accepted: bool
    estado_final: str
    pasos: int
    cabezales_finales: list[int]
    cintas_visibles: list[str]


class MaquinaTuringMultiCinta:
    """MT deterministica de k cintas (cada cinta infinita a derecha)."""

    def __init__(
        self,
        *,
        numero_cintas: int,
        alfabeto_entrada: set[str],
        alfabeto_cinta: set[str],
        estados: set[str],
        transiciones: Dict[Tuple[str, ReadTuple], TransitionMulti],
        estado_inicial: str,
        estado_aceptacion: str,
        estado_rechazo: str,
        blanco: str = "_",
    ) -> None:
        if numero_cintas < 1:
            raise ValueError("numero_cintas debe ser >= 1")

        self.k = numero_cintas
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

        self._cintas: list[list[str]] = [[self.blanco] for _ in range(self.k)]
        self._cabezales: list[int] = [0 for _ in range(self.k)]
        self._estado_actual = self.estado_inicial

    def _validar_transiciones(self) -> None:
        for (estado, lectura), (nuevo_estado, escritura, movimientos) in self.transiciones.items():
            if estado not in self.estados:
                raise ValueError(f"Estado invalido en transicion: {estado}")
            if len(lectura) != self.k:
                raise ValueError("Tupla de lectura con aridad incorrecta")
            if len(escritura) != self.k:
                raise ValueError("Tupla de escritura con aridad incorrecta")
            if len(movimientos) != self.k:
                raise ValueError("Tupla de movimientos con aridad incorrecta")

            for simbolo in lectura:
                if simbolo not in self.alfabeto_cinta:
                    raise ValueError(f"Simbolo leido invalido en transicion: {simbolo}")
            for simbolo in escritura:
                if simbolo not in self.alfabeto_cinta:
                    raise ValueError(f"Simbolo escrito invalido en transicion: {simbolo}")
            for mov in movimientos:
                if mov not in {"L", "R", "S"}:
                    raise ValueError(f"Movimiento invalido en transicion: {mov}")

            if nuevo_estado not in self.estados:
                raise ValueError(f"Nuevo estado invalido en transicion: {nuevo_estado}")

    def reset(self, entrada: str) -> None:
        for simbolo in entrada:
            if simbolo not in self.alfabeto_entrada:
                raise ValueError(f"Simbolo fuera del alfabeto de entrada: {simbolo!r}")

        self._cintas = [[self.blanco] for _ in range(self.k)]
        self._cabezales = [0 for _ in range(self.k)]
        self._estado_actual = self.estado_inicial

        self._cintas[0] = list(entrada) if entrada else [self.blanco]

    def _leer_simbolo(self, i: int) -> str:
        cabeza = self._cabezales[i]
        cinta = self._cintas[i]
        if cabeza >= len(cinta):
            cinta.extend([self.blanco] * (cabeza - len(cinta) + 1))
        return cinta[cabeza]

    def _escribir_simbolo(self, i: int, simbolo: str) -> None:
        cabeza = self._cabezales[i]
        cinta = self._cintas[i]
        if cabeza >= len(cinta):
            cinta.extend([self.blanco] * (cabeza - len(cinta) + 1))
        cinta[cabeza] = simbolo

    def _mover_cabezal(self, i: int, mov: Move) -> None:
        if mov == "R":
            self._cabezales[i] += 1
            return
        if mov == "L":
            self._cabezales[i] = max(0, self._cabezales[i] - 1)
            return
        # mov == "S": no cambia

    def _lectura_actual(self) -> ReadTuple:
        return tuple(self._leer_simbolo(i) for i in range(self.k))

    def _cinta_visible(self, i: int) -> str:
        cinta = self._cintas[i]
        cabeza = self._cabezales[i]

        ultimo_no_blanco = -1
        for idx, s in enumerate(cinta):
            if s != self.blanco:
                ultimo_no_blanco = idx

        derecha = max(ultimo_no_blanco, cabeza)
        cinta_ext = cinta[: derecha + 1]
        while len(cinta_ext) <= cabeza:
            cinta_ext.append(self.blanco)

        out: list[str] = []
        for idx, s in enumerate(cinta_ext):
            if idx == cabeza:
                out.append(f"[{s}]")
            else:
                out.append(s)
        return "".join(out)

    def configuracion_actual(self) -> str:
        partes = [f"q={self._estado_actual}"]
        for i in range(self.k):
            partes.append(f"T{i+1}:{self._cinta_visible(i)}")
        return " | ".join(partes)

    def paso(self) -> bool:
        if self._estado_actual in {self.estado_aceptacion, self.estado_rechazo}:
            return False

        lectura = self._lectura_actual()
        regla = self.transiciones.get((self._estado_actual, lectura))

        if regla is None:
            self._estado_actual = self.estado_rechazo
            return True

        nuevo_estado, escritura, movimientos = regla

        for i in range(self.k):
            self._escribir_simbolo(i, escritura[i])
        for i in range(self.k):
            self._mover_cabezal(i, movimientos[i])

        self._estado_actual = nuevo_estado
        return True

    def ejecutar(
        self,
        entrada: str,
        *,
        max_pasos: int = 100_000,
        guardar_historial: bool = False,
    ) -> tuple[ResultadoEjecucionMulti, list[str]]:
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

        resultado = ResultadoEjecucionMulti(
            halted=halted,
            accepted=accepted,
            estado_final=self._estado_actual,
            pasos=pasos,
            cabezales_finales=list(self._cabezales),
            cintas_visibles=[self._cinta_visible(i) for i in range(self.k)],
        )
        return resultado, historial
