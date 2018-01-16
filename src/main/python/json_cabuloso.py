import base64
import json

"""
Class read a json file with content encoded using base64, replace the values of keys 
and update the file.

Ex.:

x = JsonCabuloso("sample.json")
x.change("Key1", "NewValue1")
x.change("Key2", "NewValue2")
x.save

"""


class JsonCabuloso:

    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.decoded_json = json.loads(self._base64ToString(self._read()))

    def _base64ToString(self, string_encoded):
        decoded_string = base64.b64decode(string_encoded).decode('UTF-8')
        return decoded_string

    def _stringToBase64(self, some_string):
        byte_array = base64.b64encode(some_string.encode('UTF-8'))
        encoded_string = byte_array.decode("utf-8")
        return encoded_string

    def _read(self):
        with open(self.sample_file, 'r') as f:
            json_string = f.read()
        return json_string

    def change(self, key_ori, new_value):
        if key_ori in self.decoded_json:
            self.decoded_json[key_ori] = new_value

    def save(self):
        encoded_json = self._stringToBase64(json.dumps(self.decoded_json))
        with open(self.sample_file, 'w') as f:
            f.write(encoded_json)


x = JsonCabuloso("sample.json")
x.change("Ragul", "Brazilian")
x.change("Flamarion", "Indian")
x.save()
