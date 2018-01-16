#!/usr/bin/env python

import json
import utils


class JsonCabuloso:

    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.decoded_json = json.loads(utils._base64ToString(utils._read(self.sample_file)))

    def change(self, key_ori, new_value):
        try:
            if key_ori not in self.decoded_json:
                print("Key {key} not found for changing".format(key=key_ori))
                raise KeyError
            else:
                self.decoded_json[key_ori] = new_value
        except KeyError:
            raise

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
            self.decoded_json.pop(key)
        except KeyError:
            print("Key {key} not found for deletion".format(key=key))
            pass

    def save(self):
        encoded_json = utils._stringToBase64(json.dumps(self.decoded_json))
        with open(self.sample_file, 'w') as f:
            f.write(encoded_json)


x = JsonCabuloso("sample.json")
x.retrieveAll()
x.add("Lucio", "Africano")
print("==========")
x.retrieveAll()
print("==========")
x.change("Flamarion", "Polaco")
x.retrieveAll()
print("==========")
x.delete("Flamarion")
x.delete("Ragul")
x.delete("xpto")
x.change("Teste", "Nada")
x.retrieveAll()
