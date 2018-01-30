import unittest
import os
import utils
from json_db import JsonDbHandler, MyException

my_dir = os.path.dirname(__file__)
sample_file = os.path.join(my_dir, "sample.json")
alt_file = os.path.join(my_dir, "any_other.json")


class TestJsonDb(unittest.TestCase):

    def setUp(self):
        self.op = JsonDbHandler(sample_file)

    def test_add(self):
        self.op.add("X", "Y")

    def test_add_fail(self):
        self.op.add("X", "Y")
        with self.assertRaises(MyException):
            self.op.add("X", "Y")

    def test_delete(self):
        self.op.delete("Flamarion")

    def test_delete_fail(self):
        with self.assertRaises(MyException):
            self.op.delete("Z")

    def test_change(self):
        self.op.change("Flamarion", "Test")

    def test_change_fail(self):
        with self.assertRaises(MyException):
            self.op.change("Z", "Y")

    def test_query(self):
        self.op.query("Flamarion")

    def test_query_fail(self):
        with self.assertRaises(MyException):
            self.op.query("Z")

    def test_query_all(self):
        self.op.retrieve_all()

    def test_save_default(self):
        self.op.save(file=None)

    def test_save_alt_file(self):
        self.op.save(file=alt_file)

    def test_base64ToString(self):
        with open(sample_file, 'r') as f:
            encoded_string = f.read()
            decoded_string = utils._base64ToString(encoded_string)
            self.assertIn(decoded_string,
                          '{"Ragul": "Indian", "Ricardo": "Polaco", "Flamarion": "Brazilian"}')

    def test_base64ToString_fail(self):
        with open(sample_file, 'r') as f:
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
        string = utils._read(sample_file)
        self.assertIn(string,
                      "eyJSYWd1bCI6ICJJbmRpYW4iLCAiUmljYXJkbyI6ICJQb2xhY28iLCAiRmxhbWFyaW9uIjogIkJyYXppbGlhbiJ9")

    def test_read_fail(self):
        string = utils._read(sample_file)
        self.assertNotIn(string, "Z")


if __name__ == '__main__':
    unittest.main()
