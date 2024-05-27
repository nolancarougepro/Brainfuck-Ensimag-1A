#!/usr/bin/env python3
tape = [0] * 32000
ptr = 0
while tape[ptr] != 0:
	print(chr(tape[ptr]), end='')
	pass
tape[ptr] = ord(input()[0])
print(chr(tape[ptr]), end='')
tape[ptr] = ord(input()[0])
tape[ptr] = ord(input()[0])
tape[ptr] = ord(input()[0])
print(chr(tape[ptr]), end='')
print(chr(tape[ptr]), end='')
