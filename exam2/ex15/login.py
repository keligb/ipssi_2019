#!/usr/bin/python3

import hashlib
import sys


def compare_pass(mdp):   
    

    if sys.argv[1] != mdp:
        print("login failed")
        return False
    else:
        print("login OK")
        return True
