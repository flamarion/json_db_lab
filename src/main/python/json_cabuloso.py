import base64
import json

'''
This class accept 4 parameters
1 - json file to bechanged ("sample.json" on example)
2 - new json file to be created ("novo.json" on the example)
3 - key to be replaced ("buceta" on the example)
4 - key to replace ("caceta" on the example)

The content of the "sample.json" is

eyAiYnVjZXRhIiA6ICJjdSIgfQ== ( {"buceta" : "cu" })

Example:

If you want to replace "buceta" by "caceta":

x = JsonCabuloso("sample.json", "novo.json", "buceta", "caceta")
b = (x.read_json())
x.change_json(b)


'''


class JsonCabuloso:

    def __init__(self, sample_file, new_file, key_ori, key_rep):
        self.sample_file = sample_file
        self.new_file = new_file
        self.key_ori = key_ori
        self.key_rep = key_rep

    def _base64ToString(self, string_encoded):
        decoded_string = base64.b64decode(string_encoded).decode('UTF-8')
        return decoded_string

    def _stringToBase64(self, some_string):
        byte_array = base64.b64encode(some_string.encode('UTF-8'))
        encoded_string = byte_array.decode("utf-8")
        return encoded_string

    def read_json(self):
        with open(self.sample_file, 'r') as f:
            json_string = f.read()
        decoded_json = json.loads(self._base64ToString(json_string))
        return decoded_json

    def change_json(self, decoded_json):
        for key in decoded_json.keys():
            if key == self.key_ori:
                decoded_json[self.key_rep] = decoded_json.pop(self.key_ori)
            new_json = json.dumps(decoded_json)
            encoded_json = self._stringToBase64(new_json)
            with open(self.new_file, 'w') as f:
                f.write(encoded_json)
                return encoded_json
