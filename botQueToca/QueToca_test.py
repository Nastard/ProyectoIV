# -*- coding: utf-8 -*-

import unittest
from QueToca import QueToca

class TestQueToca(unittest.TestCase):
    def setUp(self):
        self.horario = QueToca()

    def test_objeto_inicializado_correctamente(self):
        self.assertIsInstance(self.horario, QueToca, "El objeto se ha creado correctamente.")

    def test_crear_horario(self):
        self.assertTrue(self.horario.CrearHorario(), "Se ha creado un nuevo horario.")

    def test_leer_horario(self):
        self.assertIsInstance(self.horario.LeerHorario(), str, "Se ha leido el horario.")

    def test_modificar_horario(self):
        self.assertTrue(self.horario.ModificarHorario(), "Se ha modificado el horario.")

    def test_borrar_horario(self):
        self.assertTrue(self.horario.BorrarHorario(), "Se ha borrado el horario.")

if __name__ == '__main__':
    unittest.main()
