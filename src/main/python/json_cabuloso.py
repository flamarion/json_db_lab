#!/usr/bin/env python

import json
import utils


class JsonCabuloso:

    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.decoded_json = json.loads(utils._base64ToString(utils._read(self.sample_file)))

    def add(self, new_key, new_value):
        self.decoded_json[new_key] = new_value

    def delete(self, key):
        if key not in self.decoded_json:
            return False
        else:
            self.decoded_json.pop(key)
            return True

    def change(self, key, new_value):
        if key not in self.decoded_json:
            return False
        else:
            self.decoded_json[key] = new_value
            return True

    def retrieve(self, key):
        if key not in self.decoded_json:
            return False
        else:
            return key, self.decoded_json[key]

    def retrieveAll(self):
        return self.decoded_json

    def save(self):
        encoded_json = utils._stringToBase64(json.dumps(self.decoded_json))
        with open(self.sample_file, 'w') as f:
            f.write(encoded_json)