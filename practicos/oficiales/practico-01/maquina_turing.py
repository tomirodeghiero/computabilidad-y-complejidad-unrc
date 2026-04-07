from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Tuple

Move = Literal["L", "R", "S"]
Transition = Tuple[str, str, Move]


@dataclass
class ResultadoEjecucion:
    halted: bool
    accepted: bool
    estado_final: str
    pasos: int
    cabezal_final: int
    cinta_visible: str


class MaquinaTuringUnaCinta:
    """MT deterministica de una cinta, infinita solo hacia la derecha.

    - La posicion 0 es el borde izquierdo.
    - Si una transicion pide mover a la izquierda en 0, el cabezal permanece en 0.
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

        self._cinta: list[str] = [self.blanco]
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

        self._cinta = list(entrada) if entrada else [self.blanco]
        self._cabezal = 0
        self._estado_actual = self.estado_inicial

    def _leer(self) -> str:
        if self._cabezal >= len(self._cinta):
            self._cinta.extend([self.blanco] * (self._cabezal - len(self._cinta) + 1))
        return self._cinta[self._cabezal]

    def _escribir(self, simbolo: str) -> None:
        if self._cabezal >= len(self._cinta):
            self._cinta.extend([self.blanco] * (self._cabezal - len(self._cinta) + 1))
        self._cinta[self._cabezal] = simbolo

    def _mover(self, movimiento: Move) -> None:
        if movimiento == "R":
            self._cabezal += 1
            return
        if movimiento == "L":
            self._cabezal = max(0, self._cabezal - 1)
            return
        # movimiento == "S": no cambia

    def configuracion_actual(self) -> tuple[str, str, str]:
        """Devuelve (u, q, v) con v incluyendo el simbolo bajo el cabezal."""
        leido = self._leer()
        _ = leido  # asegura extension de cinta si hace falta

        # recorte visible: hasta el ultimo no blanco o hasta el cabezal
        ultimo_no_blanco = -1
        for i, s in enumerate(self._cinta):
            if s != self.blanco:
                ultimo_no_blanco = i
        derecha = max(ultimo_no_blanco, self._cabezal)

        u = "".join(self._cinta[: self._cabezal])
        v = "".join(self._cinta[self._cabezal : derecha + 1])

        if not v:
            v = self.blanco

        return u, self._estado_actual, v

    @staticmethod
    def formatear_configuracion(u: str, q: str, v: str) -> str:
        if u:
            return f"{u} {q} {v}"
        return f"{q} {v}"

    def paso(self) -> bool:
        """Ejecuta un paso. Devuelve False si ya estaba en estado de parada."""
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
    ) -> tuple[ResultadoEjecucion, list[str]]:
        self.reset(entrada)

        historial: list[str] = []
        pasos = 0

        if guardar_historial:
            historial.append(self.formatear_configuracion(*self.configuracion_actual()))

        while (
            self._estado_actual not in {self.estado_aceptacion, self.estado_rechazo}
            and pasos < max_pasos
        ):
            self.paso()
            pasos += 1
            if guardar_historial:
                historial.append(self.formatear_configuracion(*self.configuracion_actual()))

        halted = self._estado_actual in {self.estado_aceptacion, self.estado_rechazo}
        accepted = self._estado_actual == self.estado_aceptacion

        cinta_visible = "".join(self._cinta)
        while len(cinta_visible) > 1 and cinta_visible.endswith(self.blanco):
            cinta_visible = cinta_visible[:-1]

        resultado = ResultadoEjecucion(
            halted=halted,
            accepted=accepted,
            estado_final=self._estado_actual,
            pasos=pasos,
            cabezal_final=self._cabezal,
            cinta_visible=cinta_visible,
        )
        return resultado, historial
