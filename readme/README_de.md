<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
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
 •  Deutsch
 • [Русский](README_ru.md)

Willkommen bei Digits Solver, dem ultimativen Python-Begleiter für das meisterhafte Lösen des faszinierenden [Digits](https://www.nytimes.com/games/digits)-Puzzlespiels, entwickelt von The New York Times. Tauche ein in eine fesselnde Welt numerischer Herausforderungen und meistere die Kunst der strategischen Manipulation. Mit Digits Solver manipulierst du geschickt eine Reihe von Ausgangszahlen mit mathematischen Operationen, um die schwer fassbare Zielzahl zu erreichen. Sein leistungsstarker Algorithmus und gründliche Analyse ermöglichen es dir, jedes Rätsel schnell zu lösen und Schritt-für-Schritt-Lösungen mit unerschütterlicher Präzision zu liefern. Erweitere dein Können im Lösen von Rätseln und entschlüssle die verborgenen Geheimnisse innerhalb der Zahlen. Mach dich bereit für eine aufregende Reise, um ein Meister der Digits zu werden!

[![Python-Anwendung](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint Score](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Python-Badge](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![Contributions Welcome](https://img.shields.io/badge/beiträge-willkommen-brightgreen.svg?style=flat&color=pink)
[![Lizenz](https://img.shields.io/badge/lizenz-MIT-yellow.svg)](LICENSE.md)
[![Code-Stil: black](https://img.shields.io/badge/code%20stil-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Sieh den Algorithmus in

 Aktion, indem du auf den grünen Ausführungsbutton klickst, nachdem du weitergeleitet wurdest:

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Du kannst auch diesen Speedrun ansehen, bei dem der Digits Solver-Algorithmus verwendet wird:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Hinweis: Die Demo zeigt die Funktion [solve_auto](solveAuto.md). Weitere Informationen findest du im weiteren Verlauf.*

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Beispiele](#beispiele)
- [Alternative Verwendung](#alternative-verwendung)
- [Hilfsmodule](#hilfsmodule)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)
- [Danksagungen](#danksagungen)

## Installation

Du kannst eine Kopie des Digits Solver-Programms auf eine der folgenden Arten erhalten:

1. **Repository klonen**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Zip-Datei herunterladen**:
   - Gehe zum [Release](https://github.com/yuchuehw/DigitsSolver/releases)-Tab im GitHub-Repository.
   - Lade die neueste Release-Zip-Datei herunter.
   - Entpacke den Inhalt der Zip-Datei an den gewünschten Speicherort.

Nachdem du das Programm erhalten hast, kannst du zur [Verwendung](#verwendung)-Sektion gehen, um das Digits Solver-Programm auszuführen.

## Verwendung

Um das Digits Solver-Programm auszuführen, öffne das Terminal und navigiere zu dem Verzeichnis, in dem du das DigitsSolver-Repository heruntergeladen oder geklont hast. Sobald du dich im entsprechenden Verzeichnis befindest, führe den folgenden Befehl im Terminal aus (ersetze Werte in spitzen Klammern durch deine Eingabe; siehe [Beispiele](#beispiele)-Sektion für weitere Details):

```bash
python solver <startzahlen> <zielzahl> [-os] [-h]
```

- `<startzahlen>`: Eine Leerzeichen getrennte Liste von Ganzzahlen, die die Ausgangszahlen repräsentieren.
- `<zielzahl>`: Die Zielzahl, die erreicht werden soll.
- `-os` oder `--onesolution` (optional): Wenn angegeben, findet das Programm nur eine Lösung. Andernfalls findet es alle möglichen Lösungen.
- `-h` oder `--help` (optional): Wenn verwendet, wird das Hilfemenü angezeigt.

## Beispiele

1. Finde alle Lösungen für das Zahlenrätsel:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Finde nur eine Lösung für das Zahlenrätsel:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```


3. Beachte, dass die Startzahlen immer vor den Zielzahlen stehen. Dies ist ein Beispiel für ein Rätsel mit 8 Startzahlen:
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## Ausgabe

Das Programm gibt die Anzahl der gefundenen Lösungen aus und zeigt jede Lösung im folgenden Format an:

```
Lösung gefunden:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Wir haben 1 Lösung(en) gefunden.
```

## Alternative Verwendung

Der Digits Solver kann auch als Python-Modul importiert und programmgesteuert verwendet werden. Du kannst weitere Funktionalitäten hinzufügen als das, was wir bereitgestellt haben. Hier ist ein minimales Beispiel, wie du es als Import verwenden kannst:

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# False in den Klammern ist optional. False löst alle Lösungen. True löst eine Lösung.
# Verwende solve.printer = some_function, um das Standardausgabe-Verhalten zu überschreiben.
anzahl_lösungen = solver.solve(False)
print(f"Wir haben {anzahl_lösungen} Lösung(en) gefunden.")
```

## Hilfsmodule

Wir haben auch ein paar zusätzliche Python-Programme beigefügt, die das Solver-Programm ergänzen. Sie befinden sich im Ordner solver/util. Hier kannst du mehr darüber lesen, wie du sie verwenden kannst:

- [Wie man pretty_solve.py verwendet](prettySolve.md): Bietet eine optisch aufgewertete Version des Solver-Programms.
- [Wie man solve_auto.py verwendet](solveAuto.md): Vollautomatischer Digits Solver mit Selenium

Du kannst diese Dateien erkunden und sie für bestimmte Anwendungsfälle oder Szenarien nutzen.

*Der Anhangsordner enthält 450 Probleme, die in den NYT-Spielen verwendet wurden. Du kannst diese Probleme gerne für das Testen des Programms verwenden.*

## Mitwirken

Beiträge zum Digits Solver-Programm sind willkommen! Wenn du Probleme findest oder Verbesserungsvorschläge hast, kannst du ein Issue öffnen oder einen Pull Request im GitHub-Repository erstellen.

Bei der Mitwirkung solltest du sicherstellen, dass du bewährte Verfahren befolgst, die Codequalität beibehältst und klare Beschreibungen deiner Änderungen bereitstellst.

## Lizenz

Das Digits Solver-Programm steht unter der [MIT-Lizenz](https://choosealicense.com/licenses/mit/). Du kannst dieses Programm für persönliche oder kommerzielle Zwecke verwenden, modifizieren und verteilen. Bitte siehe die Datei [LICENSE](LICENSE.md) für weitere Details.

## Danksagungen

Ein besonderer Dank geht an den Autor von [timeshift.js](https://github.com/plaa/TimeShift-js) für seinen Beitrag zu diesem Projekt. Teile seines Codes wurden bei der Implementierung des Hilfsmoduls solver.util verwendet.
