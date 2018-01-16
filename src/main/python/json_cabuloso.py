#!/usr/bin/env python

import json
import utils


class JsonCabuloso:

    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.decoded_json = json.loads(utils._base64ToString(utils._read(self.sample_file)))

    def change(self, key_ori, new_value):
        if key_ori in self.decoded_json:
            self.decoded_json[key_ori] = new_value

    def add(self, new_key, new_value):
        self.decoded_json[new_key] = new_value

    def retrieve(self, key):
        if key in self.decoded_json:
            print("The value of {key} is {value}".format(key=key, value=self.decoded_json[key]))

    def retrieveAll(self):
        for key, value in self.decoded_json.items():
            print("The value of {key} is {value}".format(key=key, value=self.decoded_json[key]))

    def delete(self, key):
        try:
            assert key in self.decoded_json
            if key in self.decoded_json:
                self.decoded_json.pop(key)
        except AssertionError:
            print("Key {key} not found".format(key=key))
            raise

    def save(self):
        encoded_json = utils._stringToBase64(json.dumps(self.decoded_json))
        with open(self.sample_file, 'w') as f:
            f.write(encoded_json)
