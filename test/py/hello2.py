#!/usr/bin/env python3
tape = [0] * 32000
ptr = 0
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
while tape[ptr] != 0:
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		ptr += 1
		tape[ptr] += 1
		tape[ptr] += 1
		ptr += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		ptr += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		ptr += 1
		tape[ptr] += 1
		ptr -= 1
		ptr -= 1
		ptr -= 1
		ptr -= 1
		tape[ptr] -= 1
		pass
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	tape[ptr] -= 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		ptr -= 1
		pass
	ptr -= 1
	tape[ptr] -= 1
	pass
ptr += 1
ptr += 1
print(chr(tape[ptr]), end='')
ptr += 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
print(chr(tape[ptr]), end='')
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')
print(chr(tape[ptr]), end='')
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')
ptr += 1
ptr += 1
print(chr(tape[ptr]), end='')
ptr -= 1
tape[ptr] -= 1
print(chr(tape[ptr]), end='')
ptr -= 1
print(chr(tape[ptr]), end='')
tape[ptr] += 1
tape[ptr] += 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
print(chr(tape[ptr]), end='')
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
tape[ptr] -= 1
print(chr(tape[ptr]), end='')
ptr += 1
ptr += 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')
ptr += 1
tape[ptr] += 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')