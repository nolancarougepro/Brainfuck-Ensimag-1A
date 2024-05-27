#include <stdlib.h>
#include <stdint.h>

// Taille de la table de hashage.
#define DATA_ARRAY_SIZE 32000

// Structure représentant une boucle.
// Adresse de début et de fin de boucle.
typedef struct TabLoop{
    char* deb;
    char* fin;
} TabLoop;

#define TABLE_SIZE 32000

typedef struct HashNode {
    char* addr;
    char* other_addr;
    struct HashNode* next;
} HashNode;

typedef struct HashTable {
    HashNode* array[TABLE_SIZE];
} HashTable;


/**
 * @brief Teste si le caractère est dans les caractères du langages.
 *
 * @param c caractère que l'on veut vérifier.
 * @return 1 si Oui, 0 si Non.
 */
int is_brain_char(char c);

/**
 * @brief Récupère le programme Brainfuck à interpréter depuis un fichier
 *
 * @param input_filename le nom du fichier Brainfuck à récupérer
 * @return un tableau de caractère terminé par le caractère '\0' ou NULL si input_filename
 *         n'existe pas dans le répertoire courant
 */
char* get_input_prog(char* input_filename);

/**
 * @brief Libère ce qui a été alloué par get_input_prog.
 *
 * @param loops
 */
void free_input_prog(char* input_prog);

/**
 * @brief retourne le nombre de boucle d'un fichier
 *
 * @param input_prog le programme BrainFuck à analyser
 * @return un entier représentant le nombre de boucle.
 */
int nombre_boucle(char* input_prog);

/**
 * @brief Analyse le programme Brainfuck passé en paramètre pour construire "quelque chose"
 *        qui représente les boucles du programme. Ce "quelque chose" sera ensuite utilisé
 *        lors de l'exécution des instructions, cf 'execute_instruction'.
 *        C'est à vous de décider ce que sera "quelque chose".
 *
 * @param input_prog le programme BrainFuck à analyser
 * @return "quelque chose" qui représente les boucles du programme
 */
void* build_loops(char* input_prog);

/**
 * @brief Libère ce qui a été alloué par build_loops.
 *
 * @param loops
 */
void free_loops(void* loops);


/**
 * @brief Clean le buffer pour ne pas garder le '\n' après le fgetc.
 */
void cleanBuffer();

/**
 * @brief Renvoie l'adresse du crochet associé.
 *
 * @param loops Tableau de "tuples" représentant
 * les boucles ou chaque tuple est composé
 * d'une adresse de début et une adresse de fin.
 * @param addr adresse correspondant au crochet que l'on analyse dans le fichier.
 * @param way Adresse que l'on veut retrouver 0 pour l'adresse de début et
 * 1 pour l'adresse de fin de la boucle.
 * @return Adresse correspondant au crochet associé.
 */
char* find_other_addr(HashTable* ht, char* addr);


/**
 * @brief Exécute l'instruction pointée par le pointeur pointé par ipp,
 *........et incrémente ce pointeur.
 *
 * @param ipp un pointeur vers le pointeur d'instructions
 * @param dpp un pointeur vers le pointeur de données
 * @param ht Table de hashage.
 */
void execute_instruction(char** ipp, uint8_t** dpp, HashTable* ht);

/**
 * @brief Fonction de hashage
 *
 * @param addr adresse que l'on veut hasher.
 * @return Identifiant pas forcement unique.
 */
size_t hash_function(const char* addr);

/**
 * @brief insère deux éléments dans la table de hashage.
 * Une adresse de crochet ouvrant et une de crochet fermant.
 *
 * @param ht Table de hashage.
 * @param addr Adresse du crochet ouvrant.
 * @param other_addr Adresse du crochet fermant.
 */
void insert(HashTable* ht, char* addr, char* other_addr);

/**
 * @brief Construit la table de hashage avec les boucles.
 *
 * @param ht Table de hashage.
 * @param tab_loop Tableau de boucles.
 * @param nbr_loop Nombre de boucles dans le programme.
 */
void build_hash_table(HashTable* ht, TabLoop* tab_loop, int nbr_loop);

/**
 * @brief Libère toute la mémoire utilisé pabère toute la mémoire utilisé pr la table de hashage.
 *
 * @param ht Table de hashage.
 * @param tab Tableau de boucles.
 * @param nbr_loop Nombre de boucles dans le programme.
 */
void free_hash_table(HashTable* ht, TabLoop* tab, int nbr_loop);