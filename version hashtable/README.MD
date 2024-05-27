Après avoir utilisé la première version sur le .bf mandelbrot. J'ai
remarqué que le temps d'exécution était très long. Lême si la note 
ne dépendait pas des performances, j'ai essayé d'améliorer mon code.

J'ai utilisé un profiler (kcachegrind) pour essayer de déterminer
quelles fonctions étaient les plus lentes. Il est venu assez logiquement
que la fonction "find_other_addr" était la plus couteuse. En effet, je passe 
près de 99% du temps dans cette fonction. 

Je me suis donc dis que d'utiliser une table de hashage pour avoir la
correspondance entre les crochets ouvrants et fermants était une bonne
idée.

Cepandant, je me suis rendu compte que maintenant, je passais 
plus de 95% du temps dans la fonction qui calcule les hashs. Le programme
est donc très très long (encore plus long qu'avant).

Je tenais à le garder, car il s'agissait d'une implémentation en C des tables
de hashage. J'ai décidé de ne pas réaliser des tests, car même si on peut lancer
tous les .bf, en pratique, il est inutilisable.