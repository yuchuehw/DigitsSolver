# Digits Solver Automatisierung

Dieses Skript automatisiert das Lösen von Rätseln im Spiel Digits auf der Website der New York Times mithilfe von Selenium und einem benutzerdefinierten Solver.

## Voraussetzungen

Stellen Sie vor dem Ausführen des Skripts sicher, dass Sie Folgendes installiert haben:

- Python 3.x
- Selenium-Bibliothek
- Chrome WebDriver
- Solver-Ordner

## Erste Schritte

1. Klonen Sie das Repository oder laden Sie das Skript herunter.
2. Installieren Sie die erforderlichen Abhängigkeiten mit pip:

   ```shell
   pip install selenium
   ```

3. Laden Sie das Chrome WebDriver-Executable herunter und fügen Sie den Speicherort zur PATH-Umgebungsvariablen Ihres Systems hinzu.

Natürlich! Hier ist die Dokumentation für die Befehlszeilenschnittstelle:

## Verwendung

```plaintext
solveAuto [-h] [[-start S] [-level L] | [-daily]]
```

### Optionale Argumente

- `-h, --help`: Zeigt die Hilfemeldung an und beendet das Programm.

- `-start S, --startLevel S`: Legt das Startlevel fest, um mit dem Lösen der Rätsel zu beginnen. Der Wert sollte eine Ganzzahl sein.

- `-level L, --levelToPlay L`: Legt die Gesamtanzahl der zu spielenden Level fest. Der Wert sollte eine Ganzzahl sein.

- `-daily, --dailyOnly`: Löst nur tägliche Rätsel. Wenn diese Option angegeben wird, ignoriert das Tool die Optionen `--startLevel` und `--levelToPlay` und löst nur das tägliche Rätsel.

## Beispiele

1. Löse 10 Level, beginnend ab Level 5:
   ```plaintext
   python solver/util/solveAuto --startLevel 5 --levelToPlay 10
   ```

2. Löse nur tägliche Rätsel:
   ```plaintext
   python solver/util/solveAuto --dailyOnly
   ```

Hinweis: Wenn keine Argumente angegeben werden, verwendet das Tool die Standardeinstellungen (beginnend bei Level 1 bis Level 20).

## Funktionalität

Das Skript automatisiert die folgenden Aktionen:

1. Navigation zur Digits-Spielseite auf der Website der New York Times.

2. Manipulation der Spielzeit mithilfe des Skripts `TimeShift.js` (nur solveMany.py).

3. Klicken auf die Schaltfläche "Play", um ein Rätsel zu starten.

4. Lösen jedes Rätsels durch Durchführen der erforderlichen Klicks auf die Zahlenbuttons und Operatoren.

5. Behandlung von Fällen, in denen das Skript stecken bleibt, z. B. wenn Buttons oder Elemente nicht anklickbar sind.

6. Fortschreiten zum nächsten Rätsel oder Zurückkehren zur Rätselauswahl, wenn ein Rätselsatz abgeschlossen ist.

7. Drucken der aktuellen Rätselnummer und des Datums zur Referenz (nur solveMany.py).

## Anpassung

Wenn Sie das Skript anpassen oder erweitern möchten, können Sie die folgenden Funktionen erkunden:

- `click_element(element

_id, error_message)`: Behandelt das Klicken auf ein Element, das anhand seiner ID identifiziert wird. Wenn das Element nicht anklickbar ist, fordert es den Benutzer zur Eingabe auf.

- `combine_numbers(step_list, buttons)`: Behandelt das Kombinieren von Zahlen durch Durchführen der erforderlichen Klicks auf die Zahlenbuttons und Aktualisieren des Zustands der Buttons.

- `next_puzzle_button_click()`: Behandelt das Klicken auf die Schaltfläche "Next Puzzle", um zum nächsten Rätsel zu gelangen.

- `back_to_puzzles_button_click()`: Behandelt das Klicken auf die Schaltfläche "Back to Puzzles", wenn ein Rätselsatz abgeschlossen ist.

Fühlen Sie sich frei, den Code entsprechend Ihren spezifischen Anforderungen anzupassen.

## Lizenz

Dieses Skript wird unter der [MIT-Lizenz](LICENSE.md) bereitgestellt.

Bitte beachten Sie, dass die Dokumentation davon ausgeht, dass Sie die erforderliche Umgebung und die Abhängigkeiten gemäß dem Abschnitt "Voraussetzungen" bereits eingerichtet haben.
