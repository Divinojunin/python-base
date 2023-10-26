#!/usr/bin/env python3
import os
import sys

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # RAce Condition
    names = open("names.txt").readlines()
else:
    print("[ERROR] File names.txt not found")
    sys.exit(1)
if len(names) >= 4:
    print(names[3])
else:
    print("Missing name in the list")
    sys.exit(1)
