#!/usr/bin/env python3
tape = [0] * 32000
ptr = 0
ptr -= 1
tape[ptr] += 1
print(chr(tape[ptr]), end='')
