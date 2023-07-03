<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Icône Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • Français
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Bienvenue dans Digits Solver, un programme Python indispensable conçu pour conquérir le jeu [Digits](https://www.nytimes.com/games/digits) développé par le New York Times. Plongez-vous dans le monde captivant des défis numériques alors que vous manipulez stratégiquement un ensemble de chiffres de départ en utilisant des opérations mathématiques pour atteindre le chiffre cible insaisissable. Grâce à son puissant algorithme et à son analyse méticuleuse, Digits Solver vous permet de résoudre rapidement chaque puzzle, en fournissant des solutions étape par étape avec une précision infaillible. Améliorez votre talent pour résoudre des énigmes et déverrouillez les secrets cachés au sein des chiffres. Découvrez le compagnon ultime pour maîtriser le jeu Digits.

[![Application Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Score PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Badge Python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![Contributions bienvenues](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![Licence](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Style de code: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Démo
Vous pouvez voir l'algorithme en action ici (cliquez sur le bouton d'exécution verte après redirection):

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Vous pouvez également regarder cette exécution rapide qui utilise cet algorithme:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*note: la démo utilise les fonctionnalités solveAuto, continuez à lire pour plus d'informations*
## Table des matières
- [Utilisation](#utilisation)
- [Exemples](#exemples)
- [Utilisation alternative](#utilisation-alternative)
- [Contribuer](#contribuer)
- [Licence](#licence)


## Utilisation

Pour exécuter le programme Digits Solver, exécutez la commande suivante:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <starting_digits> <target_digit> [-os]

 [-h]
```

- `<starting_digits>`: Une liste d'entiers séparés par des espaces représentant les chiffres de départ.
- `<target_digit>`: Le chiffre cible à obtenir.
- `-os` ou `--onesolution` (optionnel): Si spécifié, le programme trouvera seulement une solution. Sinon, il trouvera toutes les solutions possibles.
- -`h` ou `--help` (optionnel): Si utilisé, le menu d'aide sera affiché.

## Exemples

1. Trouver toutes les solutions pour le puzzle de chiffres:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Trouver seulement une solution pour le puzzle de chiffres:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## Sortie

Le programme affichera le nombre de solutions trouvées et affichera chaque solution dans le format suivant:

```
solution trouvée:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

nous avons trouvé 1 solution(s)
```

## Utilisation alternative
Digits Solver peut également être importé en tant que module Python et utilisé de manière programmable. Voici un exemple:
```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
compteur_solution = solver.solve(False)
print(f"nous avons trouvé {compteur_solution} solution(s)")
```
## Autres fichiers

J'ai également inclus quelques autres programmes Python supplémentaires qui complètent le programme solver. Vous pouvez trouver des instructions détaillées sur l'utilisation de chacun de ces programmes ci-dessous:

- [Comment utiliser pretty_solve.py](prettySolve.md): Fournit une version visuellement améliorée du programme solver.
- [Comment utiliser solve_auto.py](solveAuto.md): Résolveur de chiffres entièrement automatique avec Selenium.

N'hésitez pas à explorer ces fichiers et à les utiliser pour des cas d'utilisation ou des scénarios spécifiques.

*dossier des annexes inclus 450 problèmes utilisés dans les jeux du NYT. N'hésitez pas à utiliser ces problèmes pour des tests de programme*

## Contribuer

Les contributions au programme Digits Solver sont les bienvenues ! Si vous trouvez des problèmes ou avez des suggestions d'amélioration, veuillez ouvrir un problème ou soumettre une demande d'extraction sur le référentiel GitHub.

Lorsque vous contribuez, veuillez vous assurer de suivre les meilleures pratiques, de maintenir la qualité du code et de fournir des descriptions claires de vos modifications.

## Licence

Le programme Digits Solver est sous licence [MIT](https://choosealicense.com/licenses/mit/). Vous êtes libre d'utiliser, de modifier et de distribuer ce programme à des fins personnelles ou commerciales. Veuillez consulter le fichier [LICENSE](LICENSE.md) pour plus de détails.

## Remerciements

Un grand merci à l'auteur de [timeshift.js](https://github.com/plaa/TimeShift-js) pour sa contribution à ce projet. Des parties de leur code ont été utilisées dans l'implémentation du module solver.util.
