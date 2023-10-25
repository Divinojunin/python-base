#!/usr/bin/ env python
"""Calculadora infix
Funcionamento:
[operação] [n1] [n2]

operações:
sum → +
sub → -
mul → *
div → /
Uso: 
$ infixcalc.py sum 5 2
7
$ infixcalc.py mult 10 5
50

$ infixcalc.py
operação: sum
n1 : 5
n2 : 4
9

Os resultados serão salvos em 'operacao.txt'
"""

__version__ = "0.1.0" 
from datetime import datetime
import os
import sys
arguments = sys.argv[1:]

print('''
    Escolha uma operação:
        Soma : +
        Subtração: -
        Multiplicação : *
        Divisão : /
''')
if not arguments:
    operação = input("Qual é sua operação: ")
    n1 = input("1º valor:  ")
    n2 = input("2º valor: ")
    arguments = [operação, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("Ex: sum 5 5")
    sys.exit(1)

operação, *nums = arguments
validad_operação =("soma", "subtração", "multiplicação", "divisão")
if operação not in validad_operação:
    print("Operação inválida")
    print(validad_operação)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operação == "soma":
    resultado = n1 + n2
elif operação == "subtração":
    resultado = n1 - n2
elif operação == "divisão":
    resultado = n1 / n2
elif operação == "multiplicação":
    resultado = n1 * n2

path = os.curdir
filepath = os.path.join(path, 'operacao.log')
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')
with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operação}, {n1}, {n2} = {resultado}\n")

print(f"O resultado é {resultado}")