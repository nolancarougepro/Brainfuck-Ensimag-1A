#include <stdio.h>

int main() {
	char tape[32000] = {0};
	char* ptr = tape;

	--ptr;
	++(*ptr);
	putchar(*ptr);

	return 0;
}
