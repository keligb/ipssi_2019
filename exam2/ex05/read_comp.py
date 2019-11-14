#!/usr/bin/python3

import re

with open("docker-compose.yml", "r") as f:
    lines = f.readlines()
    for line in lines:
        if re.search(r"image", line):
            line = line.strip().split(":")[1]
            print(line.replace(" ", ""))
f.close()
