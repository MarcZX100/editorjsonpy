import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from src import funciones


class CargarJSONTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "usuarios.json"
        previous_ids = funciones.ids[:]
        funciones.ids.clear()
        self.addCleanup(funciones.ids.__setitem__, slice(None), previous_ids)

    def test_invalid_json_raises_without_changing_existing_file(self):
        invalid_documents = (
            b'{"main":[{"id":1,"nombre":"Ana"}],"config":{"parametros":[]}',
            b'{"main":[{"id":1}],}',
            b"this is not JSON",
            b"",
            b" \n\t",
        )
        for original in invalid_documents:
            with self.subTest(original=original):
                self.path.write_bytes(original)
                with self.assertRaises(json.JSONDecodeError):
                    funciones.cargarJSON(str(self.path))
                self.assertEqual(self.path.read_bytes(), original)
                self.assertEqual(funciones.ids, [])

    def test_valid_json_loads_users_without_changing_file(self):
        original = b'{"main":[{"id":7,"nombre":"Ana"}],"config":{"parametros":[]}}'
        self.path.write_bytes(original)

        contenido = funciones.cargarJSON(str(self.path))

        self.assertEqual(contenido, json.loads(original))
        self.assertEqual(funciones.ids, [7])
        self.assertEqual(self.path.read_bytes(), original)

    def test_missing_file_creates_initial_document_and_shows_tutorial(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            contenido = funciones.cargarJSON(str(self.path))

        expected = {"main": [], "config": {"parametros": []}}
        self.assertEqual(contenido, expected)
        self.assertEqual(json.loads(self.path.read_text()), expected)
        self.assertIn("Bienvenido", output.getvalue())
        self.assertEqual(funciones.ids, [])


if __name__ == "__main__":
    unittest.main()
