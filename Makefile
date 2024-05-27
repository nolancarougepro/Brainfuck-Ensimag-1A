CC=gcc
CFLAGS=-std=c99 -Wall -Wextra
LDFLAGS=
EXEC=brainfuck

$(EXEC): brainfuck_main.o brainfuck_helper.o pile_boucle.o
	$(CC) $(CFLAGS) $^ -o $@

all: $(EXEC) test_brainfuck compile

test_brainfuck: test/brainfuck_test.o brainfuck_helper.o pile_boucle.o
	$(CC) $(CFLAGS) $^ -o $@

compile: compile_to_c compile_to_py

compile_to_c: compilateur/compile_to_c.o compilateur/compile.o brainfuck_helper.o pile_boucle.o 
	$(CC) $(CFLAGS) $^ -o $@

compile_to_py: compilateur/compile_to_py.o compilateur/compile.o brainfuck_helper.o pile_boucle.o 
	$(CC) $(CFLAGS) $^ -o $@

realclean: clean rendu

clean:
	rm -f *~ *.o test/*.o compilateur/*.o brainfuck test_brainfuck compile_to_c compile_to_py

rendu:
	@if [ -d .vscode ]; then \
	rm -r .vscode; \
	fi
	@if [ -d .git ]; then \
	rm -r .git; \
	fi
