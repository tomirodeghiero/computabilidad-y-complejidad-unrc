import unittest

from turing_machine import build_m1_w_hash_w_machine, build_m2_power_of_two_zeros_machine


class TestM1WHashW(unittest.TestCase):
    def setUp(self) -> None:
        # Se crea una maquina nueva por test para mantener independencia.
        self.machine = build_m1_w_hash_w_machine()

    def test_accepts_valid_strings(self) -> None:
        # Todas estas deberian pertenecer a B = {w#w}.
        valid = [
            "#",
            "0#0",
            "1#1",
            "01#01",
            "110010#110010",
        ]
        for w in valid:
            with self.subTest(w=w):
                result = self.machine.run(w, max_steps=40_000)
                self.assertEqual(result.status, "accept")

    def test_rejects_invalid_strings(self) -> None:
        # Casos con formato incorrecto, mismatch o simbolos fuera de alfabeto.
        invalid = [
            "",
            "0#",
            "#0",
            "01#10",
            "01#010",
            "01##01",
            "abc",
        ]
        for w in invalid:
            with self.subTest(w=w):
                result = self.machine.run(w, max_steps=40_000)
                self.assertEqual(result.status, "reject")


class TestM2PowerOfTwo(unittest.TestCase):
    def setUp(self) -> None:
        # M2 decide si la longitud en ceros es potencia de 2.
        self.machine = build_m2_power_of_two_zeros_machine()

    def test_accepts_powers_of_two(self) -> None:
        # 1, 2, 4, 8...
        valid = [
            "0",
            "00",
            "0000",
            "00000000",
        ]
        for w in valid:
            with self.subTest(w=w):
                result = self.machine.run(w, max_steps=40_000)
                self.assertEqual(result.status, "accept")

    def test_rejects_non_powers_of_two(self) -> None:
        # Vacio, longitudes no potencia de 2, o simbolos no permitidos.
        invalid = [
            "",
            "000",
            "00000",
            "000000",
            "1",
            "010",
        ]
        for w in invalid:
            with self.subTest(w=w):
                result = self.machine.run(w, max_steps=40_000)
                self.assertEqual(result.status, "reject")


if __name__ == "__main__":
    # Permite ejecutar tests con: python3 teoria-1/test_turing_machine.py
    unittest.main()
