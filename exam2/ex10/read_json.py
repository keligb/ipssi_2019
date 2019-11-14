#!/usr/bin/python3

import json

with open('students.json') as json_file:
    json_data = json.load(json_file)
    print(json_data)
