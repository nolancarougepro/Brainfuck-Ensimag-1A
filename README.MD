# Brainfuck Interpreter and Compiler

Welcome to the Brainfuck Interpreter and Compiler project! This repository contains an interpreter and compilers for the Brainfuck programming language, allowing you to execute Brainfuck code or compile it to C or Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Interpreter](#interpreter)
  - [Tests](#tests)
  - [Compilers](#compilers)
- [Makefile Commands](#makefile-commands)
- [Contributions](#contributions)
- [License](#license)

## Introduction

Brainfuck is a minimalist programming language created in 1993 by Urban Müller. It is known for its extreme minimalism, using only eight commands, and is primarily used for educational purposes and challenges.

This project includes:
- A Brainfuck interpreter.
- A Brainfuck-to-C compiler.
- A Brainfuck-to-Python compiler.
- A suite of tests for the interpreter.

## Features

- **Interpreter**: Execute Brainfuck code directly.
- **Compilers**: Compile Brainfuck code to C or Python for further execution or analysis.
- **Tests**: Run tests to ensure the functionality of the interpreter.

## Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/brainfuck-interpreter-compiler.git
cd brainfuck-interpreter-compiler
```

## Usage

### Interpreter

To use the Brainfuck interpreter, run:

```sh
./brainfuck <files>
```

### Tests

To run the tests for the Brainfuck interpreter, execute:

```sh
./test_brainfuck
```

### Compilers

#### Brainfuck to C

To compile Brainfuck code to C:

```sh
./compile_to_c <input_file> <output_file>
```

#### Brainfuck to Python

To compile Brainfuck code to Python:

```sh
./compile_to_py <input_file> <output_file>
```

## Makefile Commands

The following `make` commands are available for convenience:

- **Run Tests**: `make test_brainfuck`
- **Clean Build Files**: `make clean`
- **Compile Brainfuck to C**: `make compile_to_c`
- **Compile Brainfuck to Python**: `make compile_to_py`
- **Build Brainfuck Interpreter**: `make brainfuck`

## Contributions

Contributions are welcome! If you have ideas for improvements or have found bugs, please submit an issue or a pull request. Ensure your code adheres to the existing style and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the Brainfuck Interpreter and Compiler project. Happy coding!
