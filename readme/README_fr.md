<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Icône Digits Solver"
        width="500"
       />
    </picture>
<p>

Anglais
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Bienvenue dans Digits Solver, l'ultime compagnon Python pour conquérir le jeu de puzzle [Digits](https://www.nytimes.com/games/digits) qui vous fait perdre la tête, développé par le New York Times. Plongez dans un monde captivant de défis numériques et maîtrisez l'art de la manipulation stratégique. Avec Digits Solver, vous manipulerez de manière stratégique un ensemble de chiffres de départ à l'aide d'opérations mathématiques pour atteindre le chiffre cible insaisissable. Son puissant algorithme et son analyse minutieuse vous permettent de résoudre rapidement chaque puzzle en fournissant des solutions étape par étape avec une précision inébranlable. Rehaussez votre talent de résolution de puzzles et déverrouillez les secrets cachés dans les chiffres. Préparez-vous pour un voyage passionnant pour devenir un maître des Digits !

[![Application Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Score PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Insigne python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![contribution bienvenue](https://img.shields.io/badge/contribution-bienvenue-brightgreen.svg?style=flat&color=pink)
[![Licence](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Style de code : noir](https://img.shields.io/badge/style%20de%20code-black-000000.svg)](https://github.com/psf/black)
![Compteur d'accès](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Démo
Regardez l'algorithme en action en cliquant sur

 le bouton d'exécution vert après avoir été redirigé :

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Vous pouvez également regarder cette démonstration rapide qui utilise l'algorithme Digits Solver :

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Remarque : La démo présente la fonction [solve_auto](solveAuto.md). Continuez à lire pour plus d'informations.*

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemples](#exemples)
- [Utilisation alternative](#utilisation-alternative)
- [Modules utilitaires](#modules-utilitaires)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Remerciements](#remerciements)

## Installation

Vous pouvez obtenir une copie du programme Digits Solver en utilisant l'une des méthodes suivantes :

1. **Cloner le référentiel** :
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Télécharger le fichier Zip** :
   - Rendez-vous dans l'onglet [Release](https://github.com/yuchuehw/DigitsSolver/releases) du référentiel GitHub.
   - Téléchargez le dernier fichier zip de la version.
   - Extrayez le contenu du fichier zip à l'emplacement souhaité.

Après avoir obtenu le programme, vous pouvez passer à la section [Utilisation](#utilisation) pour exécuter le programme Digits Solver.

## Utilisation

Pour exécuter le programme Digits Solver, ouvrez le terminal et naviguez vers le répertoire où vous avez téléchargé ou cloné le référentiel DigitsSolver. Une fois dans le répertoire approprié, exécutez la commande suivante dans le terminal (remplacez les valeurs entre crochets par vos entrées ; consultez la section [Exemples](#exemples) pour plus de détails) :

```bash
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>` : Une liste d'entiers séparés par des espaces représentant les chiffres de départ.
- `<target_digit>` : Le chiffre cible à atteindre.
- `-os` ou `--onesolution` (facultatif) : Si spécifié, le programme trouvera seulement une solution. Sinon, il trouvera toutes les solutions possibles.
- `-h` ou `--help` (facultatif) : Si utilisé, le menu d'aide sera affiché.

## Exemples

1. Trouver toutes les solutions pour le puzzle des chiffres :
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Trouver seulement une solution pour le puzzle des chiffres :
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. Notez que les chiffres de départ vont toujours avant les chiffres cibles. Voici un exemple de puzzle avec 8 chiffres de départ

 :
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## Sortie

Le programme affichera le nombre de solutions trouvées et affichera chaque solution dans le format suivant :

```
Solution trouvée :
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Nous avons trouvé 1 solution(s)
```

## Utilisation alternative

Le Digits Solver peut également être importé en tant que module Python et utilisé de manière programmatique. Vous êtes libre d'ajouter plus de fonctionnalités que celles que nous avons fournies. Voici un exemple minimal de son utilisation en tant qu'importation :

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# False entre parenthèses est facultatif. False résout toutes les solutions. True résout une seule solution.
# utilisez solve.printer = some_function pour remplacer le comportement de sortie par défaut.
solution_count = solver.solve(False)
print(f"Nous avons trouvé {solution_count} solution(s)")
```

## Modules utilitaires

Nous avons également inclus quelques programmes Python supplémentaires qui complètent le programme solveur. Ils se trouvent dans le dossier solver/util. Vous pouvez en savoir plus sur leur utilisation ici :

- [Comment utiliser pretty_solve.py](prettySolve.md) : Fournit une version visuellement améliorée du programme solveur.
- [Comment utiliser solve_auto.py](solveAuto.md) : Solveur Digits entièrement automatique avec Selenium.

N'hésitez pas à explorer ces fichiers et à les utiliser pour des cas d'utilisation ou des scénarios spécifiques.

*Le dossier Appendix contient 450 problèmes utilisés dans les jeux NYT. N'hésitez pas à utiliser ces problèmes pour tester le programme.*

## Contribuer

Les contributions au programme Digits Solver sont les bienvenues ! Si vous trouvez des problèmes ou avez des suggestions d'améliorations, veuillez ouvrir une issue ou soumettre une demande d'extraction sur le référentiel GitHub.

Lorsque vous contribuez, veuillez vous assurer de suivre les meilleures pratiques, de maintenir la qualité du code et de fournir des descriptions claires de vos modifications.

## Licence

Le programme Digits Solver est sous licence [MIT License](https://choosealicense.com/licenses/mit/). Vous êtes libre d'utiliser, de modifier et de distribuer ce programme à des fins personnelles ou commerciales. Veuillez consulter le fichier [LICENSE](LICENSE.md) pour plus de détails.

## Remerciements

Un grand merci à l'auteur de [timeshift.js](https://github.com/plaa/TimeShift-js) pour sa contribution à ce projet. Des parties de leur code ont été utilisées dans la mise en œuvre du module solveur.util.
