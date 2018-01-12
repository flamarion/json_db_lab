import unittest
from json_cabuloso import JsonCabuloso

class TestKeyReplace(unittest.TestCase):
    def setUp(self):
        pass

    def test_replace_flamarion_lucio(self):
        i = JsonCabuloso(file='test1.json', replace_key='flamarion')
        result = i.change_json()
        self.assertTrue(result)

    def test_replace_key_not_found(self):
        i = JsonCabuloso(file='test2.json', replace_key='flamarion')
        result = i.change_json()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
