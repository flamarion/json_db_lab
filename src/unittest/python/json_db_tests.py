import unittest
import os
from json_db import JsonDbHandler, MyException


class TestJsonDb(unittest.TestCase):

    def setUp(self):
        my_dir = os.path.dirname(__file__)
        sample_file = os.path.join(my_dir, "sample.json")
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


if __name__ == '__main__':
    unittest.main()
