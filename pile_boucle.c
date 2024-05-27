#include "pile_boucle.h"
#include <stdio.h>

Pile* init_pile(){
    Pile* pile = malloc(sizeof(Pile));
    pile->nombre_elem = 0;
    pile->top = NULL;

    return pile;
}

void add_pile(Pile* pile, char* adress){
    Cellule* new_cell = malloc(sizeof(Cellule));
    new_cell->adress = adress;
    new_cell->next = pile->top;
    pile->top = new_cell;
    (pile->nombre_elem)++;
}

char* pop_pile(Pile* pile){
    if(pile->nombre_elem != 0){
        Cellule* copy = pile->top;
        char* adress_return = copy->adress;
        pile->top = pile->top->next;
        pile->nombre_elem--;
        free(copy);

        return adress_return;
    }else{
        fprintf(stderr, "La pile est vide, impossible de retirer un élément.\n");
        return NULL;
    }


}

void affiche_pile(Pile* pile){
    if(pile->nombre_elem != 0){
        Cellule* copy = pile->top;
        while(copy != NULL){
            printf("%s\n", copy->adress);
            printf("↓\n");
            copy = copy->next;
        }
        printf("Bas de la pile.\n");
    }else{
        printf("La pile est vide.\n");
    }
}
