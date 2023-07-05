# Automatisation de la résolution de Digits Solver

Ce script automatise la résolution des puzzles du jeu Digits sur le site web du New York Times en utilisant Selenium et un solveur personnalisé.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- La bibliothèque Selenium
- Chrome WebDriver
- Un dossier "solver"

## Mise en route

1. Clonez le dépôt ou téléchargez le script.
2. Installez les dépendances requises à l'aide de pip :

   ```shell
   pip install selenium
   ```

3. Téléchargez le fichier exécutable Chrome WebDriver et ajoutez son emplacement à la variable d'environnement PATH de votre système.

Bien sûr ! Voici la documentation pour l'interface en ligne de commande :

## Utilisation

```plaintext
solver/util/solve_auto [-h] [[-start S] [-level L] | [-daily]]
```

### Arguments facultatifs

- `-h, --help` : Affiche le message d'aide et quitte.

- `-start S, --startLevel S` : Spécifie le niveau de départ pour commencer à résoudre les puzzles. La valeur doit être un entier.

- `-level L, --levelToPlay L` : Spécifie le nombre total de niveaux à jouer. La valeur doit être un entier.

- `-daily, --dailyOnly` : Résout uniquement les puzzles quotidiens. Si cet indicateur est spécifié, l'outil ignorera les options `--startLevel` et `--levelToPlay` et résoudra uniquement le puzzle quotidien.

## Exemples

1. Résoudre 10 niveaux à partir du niveau 5 :
   ```plaintext
   python solver/util/solve_auto --startLevel 5 --levelToPlay 10
   ```

2. Résoudre uniquement les puzzles quotidiens :
   ```plaintext
   python solver/util/solve_auto --dailyOnly
   ```

Remarque : Si aucun argument n'est spécifié, l'outil utilisera les paramètres par défaut (démarrer du niveau 1 au niveau 20).

## Fonctionnalités

Le script automatise les actions suivantes :

1. Accéder au jeu Digits sur le site web du New York Times.

2. Manipuler l'horloge du jeu en utilisant le script `TimeShift.js` (uniquement solveMany.py).

3. Cliquer sur le bouton "Jouer" pour commencer un puzzle.

4. Résoudre chaque puzzle en effectuant les clics nécessaires sur les boutons de chiffres et les opérateurs.

5. Gérer les cas où le script se bloque, par exemple lorsque les boutons ou les éléments ne sont pas cliquables.

6. Passer au puzzle suivant ou revenir à l'écran de sélection des puzzles lorsque tous les puzzles d'un ensemble sont résolus.

7. Afficher le numéro de puzzle et la date actuels à des fins de référence (uniquement solveMany.py).

## Personnalisation

Si vous souhaitez modifier ou étendre la fonctionnalité du script, vous pouvez explorer les fonctions suivantes :

- `click_element(element_id, error_message)` : Gère le clic sur un élément identifié par son ID. Si l'élément n'est pas cliquable, il demande à l'utilisateur de saisir une entrée.

-

 `combine_numbers(step_list, buttons)` : Gère la combinaison des chiffres en effectuant les clics nécessaires sur les boutons de chiffres et en mettant à jour l'état des boutons.

- `next_puzzle_button_click()` : Gère le clic sur le bouton "Puzzle suivant" pour passer au puzzle suivant.

- `back_to_puzzles_button_click()` : Gère le clic sur le bouton "Retour aux puzzles" lorsqu'un ensemble de puzzles est terminé.

N'hésitez pas à modifier le code selon vos besoins spécifiques.

## Licence

Ce script est fourni sous la [licence MIT](LICENSE.md).

Veuillez noter que la documentation suppose que vous avez déjà configuré l'environnement et les dépendances nécessaires comme indiqué dans la section "Prérequis".
