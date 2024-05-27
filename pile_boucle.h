#include <stdlib.h>
#include <stdint.h>

// Cellule composant la pile.
typedef struct Cellule{
    char* adress;
    struct Cellule* next;
} Cellule;

// Structure de la Pile.
typedef struct Pile{
    struct Cellule* top;
    int nombre_elem;
} Pile;

/**
 * @brief Initialise une pile.
 * 
 * @return Pile initialisé.
 */
Pile* init_pile();

/**
 * @brief Ajoute une adresse à la pile.
 *
 * @param pile Pile où l'on veut ajouter.
 * @param adress Adresse a ajouter.
 */
void add_pile(Pile* pile, char* adress);

/**
 * @brief Dépile une adresse de la pile.
 *
 * @param pile Pile où l'on veut dépiler.
 * @return Retourne l'adresse depilé. 
 */
char* pop_pile(Pile* pile);

/**
 * @brief Affiche la pile pour le débuggage.
 *
 * @param pile Pile que l'on veut afficher.
 */
void affiche_pile(Pile* pile);
