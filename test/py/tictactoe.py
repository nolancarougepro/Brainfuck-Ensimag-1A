#!/usr/bin/env python3
tape = [0] * 32000
ptr = 0
tape[ptr] += 1
ptr += 1
tape[ptr] -= 1
while tape[ptr] != 0:
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		pass
	tape[ptr] -= 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		ptr -= 1
		tape[ptr] += 1
		pass
	tape[ptr] -= 1
	ptr -= 1
	ptr -= 1
	ptr -= 1
	ptr -= 1
	tape[ptr] += 1
	ptr -= 1
	ptr -= 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		ptr += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		ptr -= 1
		pass
	ptr -= 1
	tape[ptr] += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		ptr += 1
		tape[ptr] += 1
		ptr -= 1
		pass
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	ptr -= 1
	ptr -= 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		ptr += 1
		tape[ptr] += 1
		tape[ptr] += 1
		ptr -= 1
		pass
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	ptr -= 1
	ptr -= 1
	tape[ptr] -= 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		tape[ptr] -= 1
		tape[ptr] -= 1
		ptr += 1
		tape[ptr] += 1
		ptr -= 1
		pass
	ptr += 1
	tape[ptr] -= 1
	tape[ptr] -= 1
	tape[ptr] -= 1
	tape[ptr] -= 1
	tape[ptr] -= 1
	tape[ptr] -= 1
	ptr -= 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		ptr -= 1
		tape[ptr] += 1
		pass
	tape[ptr] -= 1
	ptr -= 1
	while tape[ptr] != 0:
		ptr += 1
		ptr += 1
		tape[ptr] += 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			ptr += 1
			tape[ptr] += 1
			pass
		tape[ptr] -= 1
		ptr -= 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			pass
		ptr -= 1
		ptr -= 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			pass
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		while tape[ptr] != 0:
			ptr += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					tape[ptr] += 1
					ptr -= 1
					ptr -= 1
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr -= 1
					ptr -= 1
					tape[ptr] += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					tape[ptr] += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					tape[ptr] -= 1
					pass
				ptr -= 1
				ptr -= 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								while tape[ptr] != 0:
									tape[ptr] -= 1
									while tape[ptr] != 0:
										tape[ptr] -= 1
										while tape[ptr] != 0:
											tape[ptr] -= 1
											while tape[ptr] != 0:
												tape[ptr] -= 1
												ptr += 1
												ptr += 1
												ptr += 1
												pass
											ptr += 1
											ptr += 1
											ptr += 1
											pass
										ptr += 1
										ptr += 1
										ptr += 1
										pass
									ptr += 1
									ptr += 1
									ptr += 1
									pass
								ptr += 1
								ptr += 1
								ptr += 1
								pass
							ptr += 1
							ptr += 1
							ptr += 1
							pass
						ptr += 1
						ptr += 1
						ptr += 1
						pass
					ptr += 1
					ptr += 1
					ptr += 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					print(chr(tape[ptr]), end='')
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					pass
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					print(chr(tape[ptr]), end='')
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					pass
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					print(chr(tape[ptr]), end='')
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				print(chr(tape[ptr]), end='')
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] -= 1
				pass
			ptr -= 1
			tape[ptr] -= 1
			pass
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		tape[ptr] += 1
		print(chr(tape[ptr]), end='')
		while tape[ptr] != 0:
			tape[ptr] -= 1
			pass
		ptr -= 1
		ptr -= 1
		ptr -= 1
		ptr -= 1
		ptr -= 1
		ptr -= 1
		while tape[ptr] != 0:
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] -= 1
			tape[ptr] -= 1
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			while tape[ptr] != 0:
				print(chr(tape[ptr]), end='')
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] -= 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			pass
		ptr -= 1
		while tape[ptr] != 0:
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr += 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr += 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] -= 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] -= 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			pass
		ptr -= 1
		while tape[ptr] != 0:
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				tape[ptr] += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			tape[ptr] -= 1
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			print(chr(tape[ptr]), end='')
			while tape[ptr] != 0:
				tape[ptr] -= 1
				tape[ptr] -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				ptr -= 1
				pass
			ptr += 1
			tape[ptr] -= 1
			print(chr(tape[ptr]), end='')
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			pass
		ptr -= 1
		tape[ptr] += 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			ptr -= 1
			tape[ptr] += 1
			pass
		tape[ptr] -= 1
		ptr -= 1
		while tape[ptr] != 0:
			ptr += 1
			ptr += 1
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] -= 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					ptr -= 1
					ptr -= 1
					tape[ptr] += 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						tape[ptr] -= 1
						tape[ptr] -= 1
						tape[ptr] -= 1
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						ptr -= 1
						pass
					ptr += 1
					tape[ptr] -= 1
					tape[ptr] -= 1
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] = ord(input()[0])
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] -= 1
						ptr += 1
						pass
					ptr -= 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						tape[ptr] += 1
						ptr += 1
						tape[ptr] += 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						tape[ptr] -= 1
						pass
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr -= 1
						ptr -= 1
						tape[ptr] += 1
						ptr += 1
						ptr += 1
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] -= 1
						while tape[ptr] != 0:
							ptr -= 1
							ptr -= 1
							pass
						ptr += 1
						pass
					ptr += 1
					ptr += 1
					tape[ptr] -= 1
					pass
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				tape[ptr] += 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					tape[ptr] += 1
					ptr += 1
					tape[ptr] += 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr -= 1
					ptr -= 1
					tape[ptr] += 1
					ptr += 1
					ptr += 1
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				pass
			ptr += 1
			ptr += 1
			tape[ptr] -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				pass
			ptr -= 1
			ptr -= 1
			while tape[ptr] != 0:
				ptr -= 1
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] -= 1
				pass
			ptr -= 1
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								while tape[ptr] != 0:
									tape[ptr] -= 1
									while tape[ptr] != 0:
										tape[ptr] -= 1
										while tape[ptr] != 0:
											tape[ptr] -= 1
											ptr += 1
											ptr += 1
											ptr += 1
											pass
										ptr += 1
										ptr += 1
										ptr += 1
										pass
									ptr += 1
									ptr += 1
									ptr += 1
									pass
								ptr += 1
								ptr += 1
								ptr += 1
								pass
							ptr += 1
							ptr += 1
							ptr += 1
							pass
						ptr += 1
						ptr += 1
						ptr += 1
						pass
					ptr += 1
					ptr += 1
					ptr += 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				pass
			pass
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		ptr += 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			ptr += 1
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			ptr += 1
			while tape[ptr] != 0:
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					pass
				pass
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr -= 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			ptr -= 1
			tape[ptr] -= 1
			while tape[ptr] != 0:
				tape[ptr] += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr += 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				tape[ptr] += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr += 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				tape[ptr] += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				ptr += 1
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						ptr -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							pass
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						pass
					ptr -= 1
					while tape[ptr] != 0:
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr -= 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr += 1
						tape[ptr] += 1
						tape[ptr] += 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							ptr += 1
							tape[ptr] += 1
							pass
						tape[ptr] -= 1
						ptr -= 1
						ptr -= 1
						tape[ptr] -= 1
						pass
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					tape[ptr] -= 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						while tape[ptr] != 0:
							tape[ptr] -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								while tape[ptr] != 0:
									tape[ptr] -= 1
									while tape[ptr] != 0:
										tape[ptr] -= 1
										while tape[ptr] != 0:
											tape[ptr] -= 1
											while tape[ptr] != 0:
												tape[ptr] -= 1
												while tape[ptr] != 0:
													tape[ptr] -= 1
													ptr += 1
													ptr += 1
													ptr += 1
													pass
												ptr += 1
												ptr += 1
												ptr += 1
												pass
											ptr += 1
											ptr += 1
											ptr += 1
											pass
										ptr += 1
										ptr += 1
										ptr += 1
										pass
									ptr += 1
									ptr += 1
									ptr += 1
									pass
								ptr += 1
								ptr += 1
								ptr += 1
								pass
							ptr += 1
							ptr += 1
							ptr += 1
							pass
						ptr += 1
						ptr += 1
						ptr += 1
						pass
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					tape[ptr] -= 1
					ptr += 1
					ptr += 1
					tape[ptr] += 1
					tape[ptr] += 1
					while tape[ptr] != 0:
						tape[ptr] -= 1
						ptr -= 1
						tape[ptr] += 1
						pass
					tape[ptr] -= 1
					ptr += 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				ptr += 1
				while tape[ptr] != 0:
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					ptr += 1
					while tape[ptr] != 0:
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						ptr += 1
						while tape[ptr] != 0:
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr -= 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							ptr -= 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								pass
							tape[ptr] += 1
							tape[ptr] += 1
							while tape[ptr] != 0:
								tape[ptr] -= 1
								ptr += 1
								tape[ptr] += 1
								pass
							tape[ptr] -= 1
							ptr += 1
							pass
						pass
					pass
				tape[ptr] += 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					ptr -= 1
					tape[ptr] += 1
					pass
				tape[ptr] -= 1
				ptr -= 1
				while tape[ptr] != 0:
					tape[ptr] -= 1
					pass
				pass
			tape[ptr] += 1
			tape[ptr] += 1
			while tape[ptr] != 0:
				tape[ptr] -= 1
				ptr += 1
				tape[ptr] += 1
				pass
			tape[ptr] -= 1
			ptr += 1
			pass
		tape[ptr] += 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			ptr -= 1
			tape[ptr] += 1
			pass
		tape[ptr] -= 1
		ptr -= 1
		tape[ptr] += 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			ptr -= 1
			tape[ptr] += 1
			pass
		tape[ptr] -= 1
		ptr -= 1
		pass
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		ptr += 1
		tape[ptr] += 1
		pass
	tape[ptr] -= 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	ptr += 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			pass
		ptr -= 1
		tape[ptr] += 1
		pass
	tape[ptr] -= 1
	ptr -= 1
	tape[ptr] += 1
	while tape[ptr] != 0:
		tape[ptr] -= 1
		while tape[ptr] != 0:
			tape[ptr] -= 1
			pass
		ptr -= 1
		tape[ptr] += 1
		pass
	tape[ptr] -= 1
	ptr -= 1
	tape[ptr] += 1
	ptr += 1
	pass
