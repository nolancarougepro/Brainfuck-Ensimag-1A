#include <stdio.h>

int main() {
	char tape[32000] = {0};
	char* ptr = tape;

	while (*ptr) {
		*ptr = getchar();
		putchar(*ptr);
		while (*ptr) {
			putchar(*ptr);
			}
		*ptr = getchar();
		putchar(*ptr);
		putchar(*ptr);
		*ptr = getchar();
		*ptr = getchar();
		*ptr = getchar();
		++(*ptr);
		*ptr = getchar();
		--(*ptr);
		*ptr = getchar();
		--ptr;
		++ptr;
		*ptr = getchar();
		while (*ptr) {
			}
		putchar(*ptr);
		putchar(*ptr);
		}
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
		++(*ptr);
		++(*ptr);
		++(*ptr);
		while (*ptr) {
			++ptr;
			++(*ptr);
			++(*ptr);
			++ptr;
			++(*ptr);
			++(*ptr);
			++(*ptr);
			++ptr;
			++(*ptr);
			++(*ptr);
			++(*ptr);
			++ptr;
			++(*ptr);
			--ptr;
			--ptr;
			--ptr;
			--ptr;
			--(*ptr);
			}
		++ptr;
		++(*ptr);
		++ptr;
		++(*ptr);
		++ptr;
		--(*ptr);
		++ptr;
		++ptr;
		++(*ptr);
		while (*ptr) {
			--ptr;
			}
		--ptr;
		--(*ptr);
		}
	++ptr;
	++ptr;
	putchar(*ptr);
	++ptr;
	--(*ptr);
	--(*ptr);
	--(*ptr);
	putchar(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	putchar(*ptr);
	putchar(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	putchar(*ptr);
	++ptr;
	++ptr;
	putchar(*ptr);
	--ptr;
	--(*ptr);
	putchar(*ptr);
	--ptr;
	putchar(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	putchar(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	putchar(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	--(*ptr);
	putchar(*ptr);
	++ptr;
	++ptr;
	++(*ptr);
	putchar(*ptr);
	++ptr;
	++(*ptr);
	++(*ptr);
	putchar(*ptr);

	return 0;
}
