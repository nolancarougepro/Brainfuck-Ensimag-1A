#include <stdio.h>
#include "../brainfuck_helper.h"
#include "compile.h"
#include <string.h>

// Fonction qui genère le code python.
void generate_c_code(const char* source_prog, const char* output_file) {
    FILE* output = fopen(output_file, "w");
    int tab = 0;

    if (output == NULL) {
        printf("Erreur lors de l'ouverture du fichiers.\n");
        return;
    }

    fprintf(output, "#!/usr/bin/env python3\n");
    fprintf(output, "tape = [0] * 32000\n");
    fprintf(output, "ptr = 0\n");


    int c;
    size_t taille_prog = strlen(source_prog);

    for(size_t i = 0; i < taille_prog; i++){
        c = source_prog[i];
        print_tab(tab, output);
        switch (c) {
            case '>':
                fprintf(output, "ptr += 1\n");
                break;
            case '<':
                fprintf(output, "ptr -= 1\n");
                break;
            case '+':
                fprintf(output, "tape[ptr] += 1\n");
                break;
            case '-':
                fprintf(output, "tape[ptr] -= 1\n");
                break;
            case '.':
                fprintf(output, "print(chr(tape[ptr]), end='')\n");
                break;
            case ',':
                fprintf(output, "tape[ptr] = ord(input()[0])\n");
                break;
            case '[':
                fprintf(output, "while tape[ptr] != 0:\n");
                tab++;
                break;
            case ']':
                fprintf(output, "pass\n");
                tab--;
                break;
            default:
                break;
        }
    }

    fclose(output);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    char* input_prog = get_input_prog(argv[1]);
    char* output_file = argv[2];

    generate_c_code(input_prog, output_file);

    printf("Compilation Brainfuck vers Python terminée.\n");
    free_input_prog(input_prog);
    return 0;
}