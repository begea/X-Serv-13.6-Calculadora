#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
	sys.exit("Solo acepto 3 parametros")

_, operador, op1, op2 = sys.argv

operadores = ["suma", "resta", "multi", "div"]

if operador not in operadores:
	sys.exit("Solo acepto suma, resta, multi o div")

try:
	op1 = int(op1)
	op2 = float(op2)
except ValueError:
	sys.exit("Dame un numero")

if operador == "suma":
	print (op1 + op2)

if operador == "resta":
	print (op1 - op2)

if operador == "multi":
	print (op1 * op2)

if operador == "div":
	try:
		print (op1 / op2)
	except ZeroDivisionError:
		sys.exit("No me dividas entre cero")
