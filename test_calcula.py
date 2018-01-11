import unittest
import calcula

class TestSoma(unittest.TestCase):
    def setUp(self):
        pass
    def test_soma_2_2(self):
        self.assertEqual(calcula.Calcula.soma(2, 2), 4)

if __name__ == '__main__':
    unittest.main()