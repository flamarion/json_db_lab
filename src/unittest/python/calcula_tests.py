import unittest
from calcula import Calcula


class TestSoma(unittest.TestCase):

    def setUp(self):
        pass

    def test_soma_2_2(self):
        x = Calcula(2, 2)
        self.assertTrue(x.soma() == 4)

    def teste_soma_3_3_fail(self):
        x = Calcula(3, 3)
        self.assertFalse(x.soma() == 5)

    def teste_multiplica_2_3(self):
        x = Calcula(2, 3)
        self.assertTrue(x.multiplica() == 6)

    def test_multiplica_4_2(self):
        x = Calcula(4, 2)
        self.assertFalse(x.multiplica() == 9)


if __name__ == '__main__':
    unittest.main()
