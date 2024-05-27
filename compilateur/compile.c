#include "compile.h"

void print_tab(int nbr, FILE* output){
    for(int i = 0; i < nbr; i++){
        fprintf(output, "\t");
    }
}