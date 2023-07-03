<p align="center">
    <picture>
      <img 
        src="new_logo.png" 
        alt="Digits Solver Icon"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • Deutsche
 • [Русский](README_ru.md)


Digits Solver ist ein Python-Programm, das ein Zahlenrätselspiel löst, indem es mathematische Operationen findet, die auf eine Reihe von Startzahlen angewendet werden können, um eine Zielzahl zu erhalten.

[![Python-Anwendung](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint Score](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Python Badge](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![Beiträge willkommen](https://img.shields.io/badge/Beiträge-willkommen-brightgreen.svg?style=flat&color=pink)
[![Lizenz](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Code-Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Sie können den Algorithmus in Aktion hier sehen (klicken Sie nach der Weiterleitung auf die grüne Ausführungsschaltfläche):

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Sie können auch diesen Speedrun ansehen, der diesen Algorithmus verwendet:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Hinweis: Die Demo verwendet die solveAuto-Funktionen. Lesen Sie weiter für weitere Informationen.*
## Inhaltsverzeichnis
- [Verwendung](#verwendung)
- [Beispiele](#beispiele)
- [Alternative Verwendung](#alternative-verwendung)
- [Mitarbeit](#mitarbeit)
- [Lizenz](#lizenz)


## Verwendung

Um das Digits Solver-Programm auszuführen, verwenden Sie den folgenden Befehl:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <start

ende_zahlen> <ziel_zahl> [-os] [-h]
```

- `<startende_zahlen>`: Eine Leerzeichen-getrennte Liste von Ganzzahlen, die die Startzahlen repräsentieren.
- `<ziel_zahl>`: Die Zielzahl, die erreicht werden soll.
- `-os` oder `--onesolution` (optional): Wenn angegeben, findet das Programm nur eine Lösung. Andernfalls werden alle möglichen Lösungen gefunden.
- -`h` oder `--help` (optional): Wenn verwendet, wird das Hilfemenü angezeigt.

## Beispiele

1. Finde alle Lösungen für das Zahlenrätsel:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Finde nur eine Lösung für das Zahlenrätsel:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## Ausgabe

Das Programm gibt die Anzahl der gefundenen Lösungen aus und zeigt jede Lösung im folgenden Format an:

```
Lösung gefunden:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Wir haben 1 Lösung(en) gefunden
```

## Alternative Verwendung
Der Digits Solver kann auch als Python-Modul importiert und programmgesteuert verwendet werden. Hier ist ein Beispiel:
```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
anzahl_lösungen = solver.solve(False)
print(f"Wir haben {anzahl_lösungen} Lösung(en) gefunden")
```
## Weitere Dateien

Ich habe auch einige zusätzliche Python-Programme hinzugefügt, die das Solver-Programm ergänzen. Sie finden detaillierte Anweisungen zur Verwendung dieser Programme unten:

- [So verwenden Sie pretty_solve.py](reference/prettySolve.md): Bietet eine visuell verbesserte Version des Solver-Programms.
- [So verwenden Sie solve_auto.py](reference/solveAuto.md): Vollautomatischer Digits Solver mit Selenium.

Fühlen Sie sich frei, diese Dateien zu erkunden und sie für spezifische Anwendungsfälle oder Szenarien zu nutzen.

*Der Anhangsordner enthält 450 Probleme, die in den NYT-Spielen verwendet werden. Verwenden Sie diese Probleme gerne zum Testen des Programms.*

## Mitarbeit

Beiträge zum Digits Solver-Programm sind willkommen! Wenn Sie Probleme finden oder Verbesserungsvorschläge haben, öffnen Sie bitte ein Issue oder reichen Sie einen Pull Request im GitHub-Repository ein.

Bitte stellen Sie sicher, dass Sie bei Ihrer Mitarbeit bewährte Verfahren befolgen, die Codequalität aufrechterhalten und klare Beschreibungen Ihrer Änderungen bereitstellen.

## Lizenz

Das Digits Solver-Programm steht unter der [MIT-Lizenz](https://choosealicense.com/licenses/mit/). Sie können dieses Programm frei für persönliche oder kommerzielle Zwecke verwenden, ändern und verteilen. Bitte beachten Sie die [LICENSE](LICENSE.md)-Datei für weitere Details.

## Danksagungen

Besonderer Dank gilt dem Autor von [timeshift.js](https://github.com/plaa/TimeShift-js) für seinen Beitrag zu diesem Projekt. Teile seines Codes wurden in der

 Implementierung des solver.util-Moduls verwendet.
