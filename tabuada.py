"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.0"
__author__ = "Divino"

#numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

#para cada numero em numeros
for numero in numeros:
    print(f"Tabuada do {numero}: ")
    print()
    for outro_numero in numeros:
        print(f"{numero} X {outro_numero} = " ,numero * outro_numero)
    print("-"*20)