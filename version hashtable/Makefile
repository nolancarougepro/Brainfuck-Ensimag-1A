CC=gcc
CFLAGS=-std=c99 -Wall -Wextra
LDFLAGS=
EXEC=brainfuck

$(EXEC): brainfuck_main.o brainfuck_helper.o ../pile_boucle.o
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f *~ *.o ../*.o brainfuck