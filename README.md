# Labyrinthe (20053 & 22037)

Le projet est constitué de plusieurs fichiers ayant chacun sa propre fonction.

Tout d'abord le fichier "game" qui permet tout simplement de lancer la requête afin de se connecter au serveur du jeu labyrinthe et de jouer une partie.

Il y a ensuite les différents tests unitaires contenus dans les fichiers nommés "test_*" qui permettent de vérifier si chacune des fonctions du code remplissent bien leurs objectifs.

Et enfin il y a le fichier "IA" qui contient tout le code permettant de concevoir l'intelligence artificielle. Celui-ci est divisé en 3 parties ou plutôt en 3 classes.


## Le code

Premièrement la classe "ServerAI" qui contient toutes les fonctions permettant de communiquer avec le serveur du jeu. Elle permet de recevoir des requêtes et d'y répondre instantanément pour que ce dernier puisse lancer le jeu et qu'il sache quelle coup notre IA veut jouer.

Deuxièmement la classe "RandomAI" qui contient toutes les fonctions concernant la création de notre première IA. Celle-ci possède toutes les données permetttant de pouvoir jouer correctement au jeu elle ne possède pas de logique particulière. C'est-à-dire, que commme son nom l'indique, elle joue de manière totalement Random. Cette "RandomAI" a été conçue pour tester notre intelligence artificielle.

Troisièment la classe "IA" (ainsi que la classe "Queue") qui est tout simplement une version améliorée de notre RandomAI. Celle-ci contient entre-autre une fonction BFS (Breadth-First Search) qui est un algorithme permettant de parcourir en largeur tous les chemins accessibles et de trouver la solution la plus convenable. 
Pour une position donnée sur le board du jeu, l'IA est capable de trouver tous les chemins possibles dans le labyrinthe.
Si un chemin mène au trésor que le joueur recherche, alors l'IA joue ce coup sinon elle se déplace d'une case aléatoirement.
Ce petit ajout rend notre IA bien plus intelligente que le RandomAI.

Pour ce qui est de la tuile qui doit être insérée à chaque tour, l'IA et le RandomIA font en sorte que cela ne perturbe pas notre chemin. Elle est donc placée aléatoirement parmis les entrées disponibles.

En termes de bibliothèques, seule celle du "pytest" a été utilisé afin de pouvoir tester toutes les fonctions du code.
