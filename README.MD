Interpréteur et compilateur brainfuck.
On rappelle qu'ici, les codes sont corrects.

Deux versions pour l'interpréteur. 
Les deux utilisent une pile pour construire les boucles.

La première version stocke dans un tableau des tuples (adresse de début et de fin).
La deuxième version utilise une table de hashage. (Readme dans le dossier 
version hashtable).

Il y a des tests que sur la première version, car en pratique, c'est
la seule utilisable. Il faut make test puis exécuter ./test_brainfuck
S'il y a une erreur, il y aura marqué : "Error : ...".

L'ensemble des fichiers que l'on peut tester sont dans le dossier /test/bf.
Il y a aussi les résultats des compilations en c et en python dans les dossiers
respectifs.

Les compilateurs se trouvent dans le dossier /compilateur.