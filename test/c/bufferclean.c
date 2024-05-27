#include <stdio.h>

int main() {
	char tape[32000] = {0};
	char* ptr = tape;

	while (*ptr) {
		putchar(*ptr);
		}
	*ptr = getchar();
	putchar(*ptr);
	*ptr = getchar();
	*ptr = getchar();
	*ptr = getchar();
	putchar(*ptr);
	putchar(*ptr);

	return 0;
}
