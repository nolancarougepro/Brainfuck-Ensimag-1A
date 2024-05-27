#include <stdio.h>
#include "../brainfuck_helper.h"
#include "compile.h"
#include <string.h>

// Fonction qui genère le code c.
/*
En fonction du caractère que l'on lit, on écrit
dans un fichier une certaine ligne. Ici on utilise 
une fonction pour rajouter des tabulations. Cela sera pratique
pour réaliser le compilateur en python.
*/
void generate_c_code(const char* source_prog, const char* output_file) {
    FILE* output = fopen(output_file, "w");
    int tab = 0;

    if (output == NULL) {
        printf("Erreur lors de l'ouverture du fichiers.\n");
        return;
    }

    fprintf(output, "#include <stdio.h>\n\n");
    fprintf(output, "int main() {\n");
    tab++;
    print_tab(tab, output);
    fprintf(output, "char tape[32000] = {0};\n");
    print_tab(tab, output);
    fprintf(output, "char* ptr = tape;\n\n");


    int c;
    size_t taille_prog = strlen(source_prog);

    for(size_t i = 0; i < taille_prog; i++){
        c = source_prog[i];
        print_tab(tab, output);
        switch (c) {
            case '>':
                fprintf(output, "++ptr;\n");
                break;
            case '<':
                fprintf(output, "--ptr;\n");
                break;
            case '+':
                fprintf(output, "++(*ptr);\n");
                break;
            case '-':
                fprintf(output, "--(*ptr);\n");
                break;
            case '.':
                fprintf(output, "putchar(*ptr);\n");
                break;
            case ',':
                fprintf(output, "*ptr = getchar();\n");
                break;
            case '[':
                fprintf(output, "while (*ptr) {\n");
                tab++;
                break;
            case ']':
                fprintf(output, "}\n");
                tab--;
                break;
            default:
                break;
        }
    }

    fprintf(output, "\n\treturn 0;\n");
    fprintf(output, "}\n");

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

    printf("Compilation Brainfuck vers C terminée.\n");
    free_input_prog(input_prog);
    return 0;
}