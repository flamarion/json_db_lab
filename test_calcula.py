import unittest
from calcula import Calcula


class TestSoma(unittest.TestCase):
    def setUp(self):
        pass
    def test_soma_2_2(self):
        self.assertEqual(Calcula.soma(2, 2), 4)
    def teste_soma_2_2_fail(self):
        self.assertEqual(Calcula.soma(2, 4), 5)

if __name__ == '__main__':
    unittest.main()