#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "brainfuck_helper.h"
#include "../pile_boucle.h"

int is_brain_char(char c){
    if (c == '<' || c == '>' || c == '+' || c == '-' || c == '.' || c == ',' || c == '[' || c == ']'){
        return 1;
    }else{
        return 0;
    }
}

char* get_input_prog(char* input_filename){
    // On tente d'ouvrir le fichier.
    FILE* file = fopen(input_filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Erreur lors de l'ouverture du fichier : %s.\n", input_filename);
        return NULL;
    }

    // On se déplace à la fin du fichier pour récuperer la taille du fichier pour faire un malloc.
    // le malloc excède la taille nécessaire mais cela importe peu. On aurait pu parcourir le fichie deux fois pour éviter cela.
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // On alloue la mémoire.
    char* tab = malloc((file_size + 1) * sizeof(char)); // +1 pour '\0'
    
    // On vérifie que la mémoire est bien alloué.
    if (tab == NULL){
        fprintf(stderr, "Erreur  lors de l'allocation de la mémoire.");
        fclose(file);
        return NULL;
    }

    int c;
    int i = 0;
    // Si le caractère fait partit de la liste des caractères autorisés ont l'écrit.
    while((c = fgetc(file)) != EOF){
        if(is_brain_char(c)){
            tab[i] = c;
            i++;
        }
    }

    // On rajoute le '\0' et on ferme le fichier.
    tab[i] = '\0';
    fclose(file);

    return tab;
}

void free_input_prog(char* input_prog){
    // On vérifie bien que input_prog est différent de NULL.
    if(input_prog != NULL){
        free(input_prog);
    }
}

int nombre_boucle(char* input_prog){
    if(input_prog != NULL){
        int cr_ouv = 0;
        int cr_ferm = 0;
        size_t len_tab = strlen(input_prog);
        for(size_t i = 0; i < len_tab; i++){
            if(input_prog[i] == '['){
                cr_ouv++;
            }else if(input_prog[i] == ']'){
                cr_ferm++;
            }
        }
        if(cr_ouv == cr_ferm){
            return cr_ouv;
        }
    }
    return 0;
}

void* build_loops(char* input_prog){
    Pile* pile = init_pile();
    int nbr_boucle = nombre_boucle(input_prog);

    if (nbr_boucle <= 0) {
        free(pile);
        return NULL; // Pas besoin de tab si aucune boucle n'est trouvée
    }

    TabLoop* tab = malloc(nbr_boucle * sizeof(TabLoop));
    if (tab == NULL) {
        free(pile);
        return NULL; // Échec d'allocation de mémoire pour tab
    }

    int compteur_tab = 0;
    size_t taille_prog = strlen(input_prog);
    for(size_t i = 0; i < taille_prog; i++){
        if(input_prog[i] == '['){
            // Si l'on croise '[', on empile l'adresse du crochet ouvrant.
            add_pile(pile, &input_prog[i]);
        }else if(input_prog[i] == ']'){
            // Si l'on croise ']', on doit verifier que la pile n'est pas vide.
            if(pile->nombre_elem == 0){
                free(pile);
                free(tab);
                return NULL;
            }
            // Dans ce cas, on dépile l'adresse du crochet ouvrant.
            // Et on met dans la structure tab l'adresse du crochet ouvrant et fermant.
            char* adress_deb = pop_pile(pile);
            tab[compteur_tab].deb = adress_deb;
            tab[compteur_tab].fin = &input_prog[i];
            compteur_tab++;
        }
    }
    free(pile);
    return tab;
}

void free_loops(void* loops){
    free(loops);
}


size_t hash_function(const char* addr) {
    /*
    Fonction de hashage basique. J'ai essayé
    d'en trouver d'autres mais cela n'a pas beaucoup 
    joué sur la performance de l'algo.
    */
    size_t hash = 0;
    while (*addr != '\0') {
        hash += *addr;
        ++addr;
    }
    return hash % TABLE_SIZE;
}

// Fonction pour insérer un élément dans la table de hachage
void insert(HashTable* ht, char* addr, char* other_addr) {
    size_t index_addr = hash_function(addr);
    size_t index_other_addr = hash_function(other_addr);

    HashNode* newNode_1 = malloc(sizeof(HashNode));
    HashNode* newNode_2 = malloc(sizeof(HashNode));

    if (newNode_1 == NULL) {
        // Gestion de l'erreur d'allocation mémoire
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }
    if (newNode_2 == NULL) {
        // Gestion de l'erreur d'allocation mémoire
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }

    // Il faut faire attention car on peut avoir deux fois le même
    // hash. Ici je décide de chainer les éléments.

    newNode_1->addr = addr;
    newNode_1->other_addr = other_addr;
    newNode_1->next = ht->array[index_addr];

    newNode_2->addr = other_addr;
    newNode_2->other_addr = addr;
    newNode_2->next = ht->array[index_other_addr];

    ht->array[index_addr] = newNode_1;
    ht->array[index_other_addr] = newNode_2;
}

void build_hash_table(HashTable* ht, TabLoop* tab_loop, int nbr_loop){
    // Construction de la table de hashage.
    for (int i = 0; i < nbr_loop; i++){
        insert(ht, (tab_loop[i]).deb, (tab_loop[i]).fin);
    }
}

void free_hash_table(HashTable* ht, TabLoop* tab, int nbr_loop) {
    // Libère la table.
    for (int i = 0; i < nbr_loop; i++) {
        size_t index_addr = hash_function(tab[i].deb);
        size_t other_addr = hash_function(tab[i].fin);

        HashNode* current_deb = ht->array[index_addr];
        HashNode* current_fin = ht->array[other_addr];

        ht->array[index_addr] = current_deb->next;
        free(current_deb);

        ht->array[other_addr] = current_fin->next;
        free(current_fin);
    }
    free(ht);
}

void cleanBuffer()
{
    int c=0;
    //Temps que C est différent de la fin de la chaine
    while(c!='\n' && c!=EOF)
    {
        c=getchar();
    }
}


char* find_other_addr(HashTable* ht, char* addr){
    size_t index = hash_function(addr);
    HashNode* current = ht->array[index];

    // Dans le cas où il y a plusieurs adresse sur le noeud.
    while(current != NULL){
        if (strcmp(current->addr, addr) == 0) {
            return current->other_addr;
        }
        current = current->next;
    }
    return NULL;
}

void execute_instruction(char** ipp, uint8_t** dpp, HashTable* ht){
    char c = (**ipp);
    switch (c)
    {
        case '+':
            (**dpp)++;
            break;

        case '-':
            (**dpp)--;
            break;

        case '.':
            printf("%c", **dpp);
            break;

        case ',':
            printf("Entrer un char : ");
            int c = fgetc(stdin);
            (**dpp) = c;
            break;

        case '>':
            (*dpp)++;
            break;

        case '<':
            (*dpp)--;
            break;

        case '[':
            if(**dpp == 0){
                *ipp = find_other_addr(ht, *ipp);
            }
            break;

        case ']':
            *ipp = find_other_addr(ht, *ipp);
            (*ipp)--;
            break;

        default:
            break;
    }
    (*ipp)++;
}