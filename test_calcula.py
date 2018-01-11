import unittest
from calcula import Calcula


class TestSoma(unittest.TestCase):
    def setUp(self):
        pass
    def test_soma_2_2(self):
        x = Calcula(2,2)
        self.assertEqual(x.soma(), 4)
    def teste_soma_2_2_fail(self):
        x = Calcula(2,2)
        self.assertIsNot(x.soma(), 5)

if __name__ == '__main__':
    unittest.main()