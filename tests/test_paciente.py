import unittest
from src.modelo.paciente import Paciente
from src.excepciones import DatosInvalidosException


class TestPaciente(unittest.TestCase):

    def test_crear_paciente_valido(self):
        paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.obtener_nombre(), "Juan Perez")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "01/01/1990")

    def test_crear_paciente_sin_nombre(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "12345678", "01/01/1990")

    def test_crear_paciente_nombre_none(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente(None, "12345678", "01/01/1990")

    def test_crear_paciente_sin_dni(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "", "01/01/1990")

    def test_crear_paciente_dni_none(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", None, "01/01/1990")

    def test_crear_paciente_sin_fecha(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "12345678", "")

    def test_crear_paciente_fecha_none(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "12345678", None)

    def test_fecha_formato_invalido(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "12345678", "1990-01-01")

        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "12345678", "01/13/1990")

    def test_tipos_datos_invalidos(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente(123, "12345678", "01/01/1990")

        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", 12345678, "01/01/1990")

        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Perez", "12345678", 20240101)

    def test_representacion_paciente(self):
        paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        representacion = str(paciente)
        self.assertIn("Juan Perez", representacion)
        self.assertIn("12345678", representacion)
        self.assertIn("01/01/1990", representacion)
        self.assertIn("Paciente:", representacion)


if __name__ == "__main__":
    unittest.main()
