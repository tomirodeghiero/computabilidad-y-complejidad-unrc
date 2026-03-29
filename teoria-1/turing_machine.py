from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Tuple

Move = Literal["L", "R", "S"]
Transition = Tuple[str, str, Move]


@dataclass(frozen=True)
class TMResult:
    # Estado final de la corrida: accept / reject / timeout.
    status: str
    # Cantidad de pasos ejecutados.
    steps: int
    # Nombre del estado donde termino la maquina.
    final_state: str
    # Posicion final del cabezal.
    head: int
    # Cinta final serializada a string (solo el rango no vacio).
    tape: str


class TuringMachine:
    """
    Simulador de una MT deterministica de una cinta.

    La cinta se modela como diccionario:
    - clave   -> posicion entera (puede ser negativa si la cinta no esta acotada a izquierda)
    - valor   -> simbolo en esa celda

    Las celdas vacias no se guardan en memoria; se asumen como blank_symbol.
    """

    def __init__(
        self,
        *,
        input_alphabet: set[str],
        tape_alphabet: set[str],
        transitions: Dict[Tuple[str, str], Transition],
        start_state: str,
        accept_state: str,
        reject_state: str,
        blank_symbol: str = "_",
        left_bounded: bool = False,
    ) -> None:
        # Parametros "estructurales" de la maquina.
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol
        # Si left_bounded=True, el cabezal no puede pasar de la posicion 0 hacia la izquierda.
        self.left_bounded = left_bounded

        if blank_symbol not in tape_alphabet:
            raise ValueError("blank_symbol debe pertenecer al alfabeto de cinta")

    def run(self, input_string: str, max_steps: int = 100_000) -> TMResult:
        # Cargamos el input desde la celda 0 hacia la derecha.
        tape: Dict[int, str] = {}
        for i, symbol in enumerate(input_string):
            tape[i] = symbol

        # Configuracion inicial clasica.
        state = self.start_state
        head = 0
        steps = 0

        # Bucle principal de simulacion.
        while state not in (self.accept_state, self.reject_state) and steps < max_steps:
            # Leemos la celda actual; si no existe, tomamos blanco.
            read_symbol = tape.get(head, self.blank_symbol)
            # Buscamos una regla delta para (estado_actual, simbolo_leido).
            transition = self.transitions.get((state, read_symbol))

            # Si no hay transicion definida, hacemos rechazo implicito.
            if transition is None:
                state = self.reject_state
                break

            new_state, write_symbol, move = transition
            # Escribimos el simbolo indicado por delta.
            self._write_tape(tape, head, write_symbol)

            # Movemos el cabezal segun delta.
            if move == "R":
                head += 1
            elif move == "L":
                # En modelo acotado a izquierda, quedarse en 0 si se intenta ir mas a la izquierda.
                if self.left_bounded and head == 0:
                    pass
                else:
                    head -= 1
            elif move == "S":
                # Stay: no mover el cabezal.
                pass
            else:
                raise ValueError(f"Movimiento inválido: {move}")

            # Avanzamos al siguiente estado y contamos un paso.
            state = new_state
            steps += 1

        # Clasificamos resultado de ejecucion.
        if state == self.accept_state:
            status = "accept"
        elif state == self.reject_state:
            status = "reject"
        else:
            status = "timeout"

        return TMResult(
            status=status,
            steps=steps,
            final_state=state,
            head=head,
            tape=self._tape_to_string(tape),
        )

    def _write_tape(self, tape: Dict[int, str], head: int, symbol: str) -> None:
        # Optimizacion simple:
        # - escribir blank equivale a "borrar" la celda del diccionario.
        # - escribir no-blank guarda/actualiza el valor.
        if symbol == self.blank_symbol:
            tape.pop(head, None)
        else:
            tape[head] = symbol

    def _tape_to_string(self, tape: Dict[int, str]) -> str:
        # Para mostrar la cinta final, imprimimos solo desde min(posiciones) hasta max(posiciones).
        # Las posiciones intermedias sin dato explicito se muestran como blank_symbol.
        if not tape:
            return ""
        left = min(tape.keys())
        right = max(tape.keys())
        return "".join(tape.get(i, self.blank_symbol) for i in range(left, right + 1))


def build_m1_w_hash_w_machine() -> TuringMachine:
    """
    Decide B = { w#w | w in {0,1}* }.
    """
    transitions: Dict[Tuple[str, str], Transition] = {
        # q_start:
        # 1) Buscamos el primer simbolo no marcado a la izquierda del '#'.
        # 2) Si vemos 0 o 1, lo marcamos con x y vamos a buscar su par del lado derecho.
        ("q_start", "0"): ("q_seek_hash_0", "x", "R"),
        ("q_start", "1"): ("q_seek_hash_1", "x", "R"),
        # Saltamos simbolos ya procesados.
        ("q_start", "x"): ("q_start", "x", "R"),
        # Si llegamos a '#', no queda nada sin marcar del lado izquierdo.
        # Entonces solo falta verificar que a la derecha tambien este todo marcado.
        ("q_start", "#"): ("q_check_right_done", "#", "R"),

        # q_seek_hash_0 / q_seek_hash_1:
        # Recorremos hacia la derecha hasta encontrar el separador '#'.
        ("q_seek_hash_0", "0"): ("q_seek_hash_0", "0", "R"),
        ("q_seek_hash_0", "1"): ("q_seek_hash_0", "1", "R"),
        ("q_seek_hash_0", "x"): ("q_seek_hash_0", "x", "R"),
        ("q_seek_hash_0", "#"): ("q_match_0", "#", "R"),
        ("q_seek_hash_1", "0"): ("q_seek_hash_1", "0", "R"),
        ("q_seek_hash_1", "1"): ("q_seek_hash_1", "1", "R"),
        ("q_seek_hash_1", "x"): ("q_seek_hash_1", "x", "R"),
        ("q_seek_hash_1", "#"): ("q_match_1", "#", "R"),

        # q_match_0 / q_match_1:
        # En el lado derecho saltamos x hasta hallar el primer simbolo no marcado.
        # Debe coincidir con el que marcamos a la izquierda.
        ("q_match_0", "x"): ("q_match_0", "x", "R"),
        ("q_match_0", "0"): ("q_back", "x", "L"),
        ("q_match_1", "x"): ("q_match_1", "x", "R"),
        ("q_match_1", "1"): ("q_back", "x", "L"),

        # q_back:
        # Volvemos al inicio de la cinta para arrancar una nueva comparacion.
        ("q_back", "0"): ("q_back", "0", "L"),
        ("q_back", "1"): ("q_back", "1", "L"),
        ("q_back", "x"): ("q_back", "x", "L"),
        ("q_back", "#"): ("q_back", "#", "L"),
        ("q_back", "_"): ("q_start", "_", "R"),

        # q_check_right_done:
        # Si a la derecha del '#' queda algo distinto de x, rechazo implicito.
        # Si solo quedan x y luego blanco, aceptamos.
        ("q_check_right_done", "x"): ("q_check_right_done", "x", "R"),
        ("q_check_right_done", "_"): ("qaccept", "_", "S"),

        # Nota: cualquier combinacion no listada cae en rechazo implicito.
    }
    return TuringMachine(
        input_alphabet={"0", "1", "#"},
        tape_alphabet={"0", "1", "#", "x", "_"},
        transitions=transitions,
        start_state="q_start",
        accept_state="qaccept",
        reject_state="qreject",
        blank_symbol="_",
        left_bounded=False,
    )


def build_m2_power_of_two_zeros_machine() -> TuringMachine:
    """
    Decide A = { 0^(2^n) | n >= 0 }.
    """
    transitions: Dict[Tuple[str, str], Transition] = {
        # q1: "consumimos" el primer 0 reemplazandolo por blanco para tener marca de borde izquierdo.
        ("q1", "0"): ("q2", "_", "R"),

        # q2: buscamos el primer 0 disponible para iniciar el barrido "cada dos".
        # Si no hay 0 (solo x y luego blanco), queda exactamente un simbolo activo -> aceptar.
        ("q2", "x"): ("q2", "x", "R"),
        ("q2", "0"): ("q3", "x", "R"),
        ("q2", "_"): ("qaccept", "_", "S"),

        # q3: alternamos para detectar paridad.
        # Avanzamos sobre x; si encontramos 0, pasamos a q4 (el siguiente no se marca).
        # Si llegamos a blanco, terminamos barrido y volvemos a la izquierda.
        ("q3", "x"): ("q3", "x", "R"),
        ("q3", "0"): ("q4", "0", "R"),
        ("q3", "_"): ("q5", "_", "L"),

        # q4: ahora si toca marcar el siguiente 0.
        # Si encontramos blanco aqui, quedo cantidad impar (>1) y rechazamos.
        ("q4", "x"): ("q4", "x", "R"),
        ("q4", "0"): ("q3", "x", "R"),
        ("q4", "_"): ("qreject", "_", "S"),

        # q5: retorno al borde izquierdo (blanco inicial) para repetir ronda.
        ("q5", "x"): ("q5", "x", "L"),
        ("q5", "0"): ("q5", "0", "L"),
        ("q5", "_"): ("q2", "_", "R"),

        # Igual que en M1, toda transicion faltante implica rechazo implicito.
    }
    return TuringMachine(
        input_alphabet={"0"},
        tape_alphabet={"0", "x", "_"},
        transitions=transitions,
        start_state="q1",
        accept_state="qaccept",
        reject_state="qreject",
        blank_symbol="_",
        left_bounded=False,
    )
