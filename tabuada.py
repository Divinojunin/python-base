#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Divino"

#numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

#para cada numero em numeros
for numero1 in numeros:
    print("{:-^18}".format(f"Tabuada do {numero1}"))
    for numero2 in numeros:
        resultado = numero1 * numero2
        print("{:^18}".format(f"{numero1} X {numero2} = {resultado}"))
        
    print("-="*10)