import unittest
from app import app  # Asegúrate de que esta ruta es correcta

class TestMain(unittest.TestCase):
    def test_example(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
