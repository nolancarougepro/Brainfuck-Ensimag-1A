#include <stdio.h>

int main() {
	char tape[32000] = {0};
	char* ptr = tape;

	while (*ptr) {
		--(*ptr);
		putchar(*ptr);
		}
	++ptr;
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	while (*ptr) {
		--ptr;
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		++ptr;
		--(*ptr);
		}
	++ptr;
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
		--ptr;
		--(*ptr);
		}
	++ptr;
	++ptr;
	++(*ptr);
	++(*ptr);
	++ptr;
	++ptr;
	++ptr;
	++(*ptr);
	++ptr;
	++ptr;
	++ptr;
	++(*ptr);
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	--ptr;
	while (*ptr) {
		--(*ptr);
		while (*ptr) {
			--(*ptr);
			++ptr;
			++(*ptr);
			--ptr;
			}
		++ptr;
		while (*ptr) {
			--(*ptr);
			--ptr;
			++(*ptr);
			++ptr;
			++ptr;
			++ptr;
			putchar(*ptr);
			--ptr;
			--ptr;
			}
		++ptr;
		++ptr;
		++ptr;
		while (*ptr) {
			while (*ptr) {
				--(*ptr);
				++ptr;
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
					--ptr;
					--(*ptr);
					}
				++ptr;
				putchar(*ptr);
				--ptr;
				--ptr;
				while (*ptr) {
					--(*ptr);
					++ptr;
					++(*ptr);
					--ptr;
					}
				++(*ptr);
				++ptr;
				while (*ptr) {
					--(*ptr);
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
					++(*ptr);
					++ptr;
					}
				++ptr;
				putchar(*ptr);
				while (*ptr) {
					--(*ptr);
					}
				++ptr;
				}
			}
		++(*ptr);
		--ptr;
		--ptr;
		--ptr;
		while (*ptr) {
			--(*ptr);
			while (*ptr) {
				--(*ptr);
				++ptr;
				++(*ptr);
				--ptr;
				}
			++(*ptr);
			++ptr;
			while (*ptr) {
				--(*ptr);
				--ptr;
				++(*ptr);
				++ptr;
				++ptr;
				++ptr;
				--(*ptr);
				while (*ptr) {
					--(*ptr);
					++ptr;
					++(*ptr);
					--ptr;
					}
				++(*ptr);
				++(*ptr);
				++ptr;
				while (*ptr) {
					--(*ptr);
					--ptr;
					--(*ptr);
					++ptr;
					}
				--ptr;
				--ptr;
				--ptr;
				}
			--ptr;
			--ptr;
			--ptr;
			--ptr;
			}
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
		putchar(*ptr);
		++(*ptr);
		++(*ptr);
		++(*ptr);
		putchar(*ptr);
		while (*ptr) {
			--(*ptr);
			}
		--ptr;
		}
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);
	++(*ptr);

	return 0;
}
