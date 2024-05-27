#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "../brainfuck_helper.h"


// Fonction pour afficher un message d'erreur
void print_error(const char* error_message) {
    fprintf(stderr, "Error: %s\n", error_message);
}

// Fonction de test pour vérifier l'égalité de deux pointeurs
void assert_pointer_equal(const void* expected, const void* actual, const char* error_message) {
    if (expected != actual) {
        print_error(error_message);
        exit(EXIT_FAILURE);
    }
}

// Fonction de test pour vérifier l'égalité de deux chaînes de caractères
void assert_string_equal(const char* expected, const char* actual, const char* error_message) {
    if (strcmp(expected, actual) != 0) {
        print_error(error_message);
        exit(EXIT_FAILURE);
    }
}

void affiche_tab(char* tab){
    // Fonction utile pour vérifier le fonctionnement de get_input_prog.
    if(tab != NULL){
        size_t i = 0;
        while (tab[i] != '\0'){
            printf("%c", tab[i]);
            i++;
        }
        printf("\n");
    }
}

// Test get_free_input, affiche_tab, free_input_prog et nombre_boucle.
void test_get_free_input(){
    char* prog1 = get_input_prog("test/bf/hello1.bf");
    char* prog2 = get_input_prog("test/bf/hello2.bf");

    // On affiche le contenu de deux fichiers.
    printf("===================================== Affichage hello1.bf =====================================\n\n");
    affiche_tab(prog1);
    printf("\n\n");
    printf("Nombres de boucles : %d; Attendu 6\n", nombre_boucle(prog1));
    printf("\n\n");
    printf("===================================== Affichage hello2.bf =====================================\n\n");
    affiche_tab(prog2);
    printf("\n\n");
    printf("Nombres de boucles : %d; Attendu 3\n", nombre_boucle(prog2));
    printf("\n\n");

    printf("===================================== Affichage inexistant =====================================\n\n");
    // On teste lorsque le fichier n'existe pas.
    char* prog3 = get_input_prog("fichier_inexistant.bf");
    affiche_tab(prog3);
    printf("Nombres de boucles : %d; Attendu 0\n", nombre_boucle(prog3));


    // On test notre fonction free.
    free_input_prog(prog1);
    free_input_prog(prog2);
    free_input_prog(prog3);
}

// 5 Fonctions qui suivent testent build loop.
// Pas de boucle.
void test_build_loop_empty(){
    char* program = "";
    TabLoop* loops = build_loops(program);
    assert_pointer_equal(NULL, loops, "Loop empty failed");
    free(loops);
}

// Une seule boucle.
void test_build_loop_single(){
    char* program = "[+++]";
    TabLoop* loops = build_loops(program);
    assert_pointer_equal(&program[0], loops[0].deb, "Single loop failed - 1");
    assert_pointer_equal(&program[4], loops[0].fin, "Single loop failed - 2)");
    free(loops);
}

// Boucle imbriqué.
void test_build_loop_matched() {
    char* program = "[[+]++]";
    TabLoop* loops = build_loops(program);
    assert_pointer_equal(&program[0], loops[1].deb, "Loop matched failed - 1");
    assert_pointer_equal(&program[1], loops[0].deb, "Loop matched failed - 2");
    assert_pointer_equal(&program[3], loops[0].fin, "Loop matched failed - 3");
    assert_pointer_equal(&program[6], loops[1].fin, "Loop matched failed - 4");
    free(loops);
}

// Problème de boucle.
void test_build_loop_unmatched(){
    char* program = "[++][]]";
    TabLoop* loops = build_loops(program);
    assert_pointer_equal(NULL, loops, "Unmatched failed");
    free(loops);
}


void test_loop(){
    test_build_loop_empty();
    test_build_loop_single();
    test_build_loop_matched();
    test_build_loop_unmatched();
}

// Test find other addr.
void test_find_other_addr() {
    TabLoop loops[2];
    char deb1 = 'a';
    char fin1 = 'b';
    char deb2 = 'c';
    char fin2 = 'd';
    loops[0].deb = &deb1;
    loops[0].fin = &fin1;
    loops[1].deb = &deb2;
    loops[1].fin = &fin2;

    char* result = find_other_addr(loops, &deb1, 0);
    if (result != &fin1) {
        print_error("Test Find Other Addr failed - 1");
    }

    result = find_other_addr(loops, &fin2, 1);
    if (result != &deb2) {
        print_error("Test Find Other Addr failed - 2");
    }

}

// Execute les tests.
int main(){
    test_get_free_input();
    test_loop();
    test_find_other_addr();
}