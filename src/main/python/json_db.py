#!/usr/bin/env python

import json
import utils


class MyException(Exception):
    pass


class JsonDbHandler(object):

    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.decoded_json = json.loads(utils._base64ToString(
            utils._read(self.sample_file)))

    def add(self, new_key, new_value):
        if new_key in self.decoded_json:
            raise MyException('The key already exists')
        else:
            self.decoded_json[new_key] = new_value

    def delete(self, key):
        try:
            self.decoded_json.pop(key)
        except:
            raise MyException("Key not found for deletion")

    def change(self, key, new_value):
        if key in self.decoded_json:
            self.decoded_json[key] = new_value
        else:
            raise MyException("Key not found for changing")

    def query(self, key):
        if key not in self.decoded_json:
            raise MyException('Key not found')
        else:
            return self.decoded_json[key]

    def retrieve_all(self):
        return self.decoded_json

    def save(self):
        encoded_json = utils._stringToBase64(json.dumps(self.decoded_json))
        with open(self.sample_file, 'w') as f:
            f.write(encoded_json)

    def save_as(self, new_file):
        encoded_json = utils._stringToBase64(json.dumps(self.decoded_json))
        with open(new_file, 'w') as f:
            f.write(encoded_json)
