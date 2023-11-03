#!/usr/bin/env python3
import os
import sys
# EAFP - Easy to ASk Forgiveness than permission 
#  
try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))
try:
    names = open("names.txt").readlines()
    print(names.append)
except FileNotFoundError as e:
    print(f"[ERROR] {str(e)}")
    sys.exit(1)
    #TODO: Usar retry
else:
    print("Sucesso!!")
finally:
    print("Execute isso sempre!!")
try:
    print(names[0])
except:
    print("Missing name in the list")
    sys.exit(1)
