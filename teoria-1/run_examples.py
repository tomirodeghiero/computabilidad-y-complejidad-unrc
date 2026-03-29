from turing_machine import build_m1_w_hash_w_machine, build_m2_power_of_two_zeros_machine


def run_m1_examples() -> None:
    # Construimos la maquina M1 (lenguaje B = {w#w}).
    machine = build_m1_w_hash_w_machine()

    # Casos de prueba mezclando validos e invalidos.
    cases = [
        "#",
        "0#0",
        "01#01",
        "011000#011000",
        "0#1",
        "01#10",
        "01#010",
        "",
    ]

    # Ejecutamos cada cadena y mostramos status + pasos.
    print("M1 - B = { w#w | w in {0,1}* }")
    for w in cases:
        result = machine.run(w, max_steps=20_000)
        print(f"  input={w!r:16} -> {result.status:7} (steps={result.steps})")
    print()


def run_m2_examples() -> None:
    # Construimos la maquina M2 (potencias de 2 de ceros).
    machine = build_m2_power_of_two_zeros_machine()

    # Incluimos casos del enunciado (0, 00, 000, 000000)
    # y algunos extras para ver comportamiento general.
    cases = [
        "0",
        "00",
        "000",
        "0000",
        "000000",
        "00000000",
        "",
    ]

    # Ejecutamos cada entrada con un limite alto de pasos para evitar loops infinitos.
    print("M2 - A = { 0^(2^n) | n >= 0 }")
    for w in cases:
        result = machine.run(w, max_steps=20_000)
        print(f"  input={w!r:16} -> {result.status:7} (steps={result.steps})")
    print()


if __name__ == "__main__":
    # Punto de entrada para correr ejemplos manuales.
    run_m1_examples()
    run_m2_examples()
