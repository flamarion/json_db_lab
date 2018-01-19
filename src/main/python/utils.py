#!/usr/bin/env python

import base64


def _base64ToString(string_encoded):
    decoded_string = base64.b64decode(string_encoded).decode('UTF-8')
    return decoded_string


def _stringToBase64(some_string):
    byte_array = base64.b64encode(some_string.encode('UTF-8'))
    encoded_string = byte_array.decode("utf-8")
    return encoded_string

def _read(sample_file):
    with open(sample_file, 'r') as f:
        json_string = f.read()
    return json_string
