#!/usr/bin/python3

import hashlib
import sys
from hmac import compare_digest

def compare_pass(argv1):
    password = "ipssi"
    password2 = argv1
    mdp = hashlib.md5(password.encode('utf8')).hexdigest()
    mdp2 = hashlib.md5(password2.encode('utf8')).hexdigest()

    print("md5 \"ipssi\": " + mdp)
    print("md5   pass : " + mdp2)

    if mdp == mdp2:
        print("login ok")
        return True
    else: 
        print("login failed")
        return False
