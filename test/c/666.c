#include <stdio.h>

int main() {
	char tape[32000] = {0};
	char* ptr = tape;

	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	while (*ptr) {
		++ptr;
		++(*ptr);
		++ptr;
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++ptr;
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++ptr;
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		--ptr;
		--ptr;
		--ptr;
		--ptr;
		--(*ptr);
		}
	++ptr;
	++ptr;
	++ptr;
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	putchar(*ptr);
	putchar(*ptr);
	putchar(*ptr);
	--ptr;
	--ptr;
	putchar(*ptr);

	return 0;
}
