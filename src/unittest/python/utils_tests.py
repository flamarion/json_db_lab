import unittest
import os
import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.my_dir = os.path.dirname(__file__)
        self.sample_file = os.path.join(self.my_dir, "sample.json")
        self.alt_file = os.path.join(self.my_dir, "any_other.json")

    def test_base64ToString(self):
        with open(self.sample_file, 'r') as f:
            encoded_string = f.read()
            decoded_string = utils._base64ToString(encoded_string)
            self.assertIn(decoded_string,
                          '{"Ragul": "Indian", "Ricardo": "Polaco", "Flamarion": "Brazilian"}')

    def test_base64ToString_fail(self):
        with open(self.sample_file, 'r') as f:
            encoded_string = f.read()
            decoded_string = utils._base64ToString(encoded_string)
            self.assertNotIn(decoded_string, 'Z')

    def test_stringToBase64(self):
        string = '{"Ragul": "Indian", "Ricardo": "Polaco", "Flamarion": "Brazilian"}'
        encoded_string = utils._stringToBase64(string)
        self.assertIn(encoded_string,
                      "eyJSYWd1bCI6ICJJbmRpYW4iLCAiUmljYXJkbyI6ICJQb2xhY28iLCAiRmxhbWFyaW9uIjogIkJyYXppbGlhbiJ9")

    def test_stringToBase64_fail(self):
        string = '{"Ragul": "Indian", "Ricardo": "Polaco", "Flamarion": "Brazilian"}'
        encoded_string = utils._stringToBase64(string)
        self.assertNotIn(encoded_string, "Z")

    def test_read(self):
        string = utils._read(self.sample_file)
        self.assertIn(string,
                      "eyJSYWd1bCI6ICJJbmRpYW4iLCAiUmljYXJkbyI6ICJQb2xhY28iLCAiRmxhbWFyaW9uIjogIkJyYXppbGlhbiJ9")

    def test_read_fail(self):
        string = utils._read(self.sample_file)
        self.assertNotIn(string, "Z")


if __name__ == '__main__':
    unittest.main()
