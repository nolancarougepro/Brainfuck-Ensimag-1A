#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "brainfuck_helper.h"
#include "../pile_boucle.h"

/**
 * @brief Point d'entrée de notre interpréteur Brainfuck.
 *
 * @param argc le nombre d'arguments passés sur la ligne de commande
 * @param argv les arguments passés sur la ligne de commande
 * @return 0 si tout s'est bien passé et 1 sinon
 */
int main(int argc, char **argv) {

    if (argc != 2) {
        printf("Vous devez passer le nom du fichier Brainfuck à interpréter\n");
        return 1;
    }

    char* input_prog = get_input_prog(argv[1]);
    char* ip = input_prog;
    if (ip == NULL) {
        printf("Le fichier Brainfuck passé en paramètre n'existe pas dans le répertoire courant\n");
        return 1;
    }

    int nbr_boucle = nombre_boucle(input_prog);
    HashTable* ht = malloc(sizeof(HashTable));

    void* loops = build_loops(ip);

    // On construit ici la table de hashage
    build_hash_table(ht, loops, nbr_boucle);


    uint8_t* data_array = calloc(DATA_ARRAY_SIZE, sizeof(uint8_t));
    uint8_t* dp = data_array;
    size_t instruction_id = 0;

    while (*ip != '\0') {
        instruction_id++;
        // On passe la table de hashage en paramètre (adresse).
        execute_instruction(&ip, &dp, ht);
    }
    
    free(data_array);
    free_hash_table(ht, loops, nbr_boucle);
    free_loops(loops);
    free_input_prog(input_prog);
    return EXIT_SUCCESS;
}