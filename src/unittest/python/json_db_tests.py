import unittest
from json_db import JsonDbHandler, MyException


class TestJsonDb(unittest.TestCase):
    def setUp(self):
        self.op = JsonDbHandler("/Users/fjorg1/Labs/mentoring/src/unittest/python/sample.json")

    def test_success_add(self):
        self.assertRaises(MyException, self.op.add("Y", "Y"))


if __name__ == '__main__':
    unittest.main()
