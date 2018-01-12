import base64
import ast

''' 
This class will decrypt the file content and replace the key equal 'flamarion' by 'lucio'
It receive a json file with content encrypted using base64 
For test purpose we will use this encrypted initial content eydmbGFtYXJpb24nOiAndmlhZG8nfQ== 
'''


class JsonCabuloso:

    def __init__(self, file):
        self.file = file

    def change_json(self):
        with open(self.file, 'r') as f:
            a = f.read()

        d = ast.literal_eval(base64.b64decode(a).decode('UTF-8'))

        for key in d.keys():
            if key == 'flamarion':
                d['lucio'] = d.pop(key)

        e = base64.b64encode(str(d).encode('utf-8'))
        with open(self.file, 'w') as f:
            f.write(str(e).strip('b\''))
