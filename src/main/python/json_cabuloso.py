import base64
import ast

'''
This class will decrypt the file content and replace key_replacement by lucio
It receive a json file with content encrypted using base64
'''


class JsonCabuloso:

    def __init__(self, file, replace_key):
        self.file = file
        self.replace_key = replace_key

    def change_json(self):
        with open(self.file, 'r') as f:
            a = f.read()

        d = ast.literal_eval(base64.b64decode(a).decode('UTF-8'))

        for key in d.keys():
            if key == self.replace_key:
                d['lucio'] = d.pop(key)
                e = base64.b64encode(str(d).encode('UTF-8'))
                with open(self.file, 'w') as f:
                    f.write(str(e).strip('b\''))
                return True
            else:
                return False
