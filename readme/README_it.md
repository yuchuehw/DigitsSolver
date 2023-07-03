<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Icona Digits Solver"
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
 • Italiano
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)


Benvenuti in Digits Solver, un indispensabile programma Python progettato per conquistare il gioco del [Digits](https://www.nytimes.com/games/digits), sviluppato dal New York Times. Immergiti nel coinvolgente mondo delle sfide numeriche, manipolando strategicamente un insieme di cifre iniziali utilizzando operazioni matematiche per raggiungere l'elusiva cifra target. Con il suo potente algoritmo e un'analisi meticolosa, Digits Solver ti consente di svelare rapidamente ogni enigma, offrendo soluzioni passo dopo passo con una precisione incrollabile. Eleva la tua abilità nel risolvere puzzle e svela i segreti nascosti tra le cifre. Vivi l'esperienza del compagno definitivo per padroneggiare il gioco Digits.

[![Python application](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Punteggio PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Python badge](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![Licenza](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Stile del codice: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Puoi vedere l'algoritmo in azione qui (clicca il pulsante verde di esecuzione dopo il reindirizzamento):

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Puoi anche guardare questa speed run che utilizza questo algoritmo:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*nota: la demo utilizza le funzionalità solveAuto, continua a leggere per ulteriori informazioni*
## Indice
- [Utilizzo](#utilizzo)
- [Esempi](#esempi)
- [Utilizzo Alternativo](#utilizzo-alternativo)
- [Contributi](#contributi)
- [Licenza](#licenza)


## Utilizzo

Per eseguire il programma Digits Solver, esegui il seguente comando:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <cifre_iniziali> <cifra_target> [-os] [-

h]
```

- `<cifre_iniziali>`: Un elenco di interi separati da spazi che rappresentano le cifre iniziali.
- `<cifra_target>`: La cifra target da ottenere.
- `-os` o `--onesolution` (opzionale): Se specificato, il programma troverà solo una soluzione. In caso contrario, troverà tutte le soluzioni possibili.
- -`h` o `--help` (opzionale): Se usato, verrà mostrato il menu di aiuto.

## Esempi

1. Trova tutte le soluzioni per il puzzle delle cifre:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Trova solo una soluzione per il puzzle delle cifre:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
   ```

## Output

Il programma restituirà il numero di soluzioni trovate e visualizzerà ciascuna soluzione nel seguente formato:

```
soluzione trovata:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

abbiamo trovato 1 soluzione/e
```

## Utilizzo Alternativo
Digits Solver può anche essere importato come modulo Python e utilizzato in modo programmato. Ecco un esempio:
```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
numero_soluzioni = solver.solve(False)
print(f"abbiamo trovato {numero_soluzioni} soluzione/i")
```
## Altri File

Ho incluso anche alcuni programmi Python aggiuntivi che integrano il programma solver. Puoi trovare istruzioni dettagliate su come utilizzare ciascuno di questi programmi di seguito:

- [Come utilizzare pretty_solve.py](reference/prettySolve.md): Fornisce una versione visivamente migliorata del programma solver.
- [Come utilizzare solve_auto.py](reference/solveAuto.md): Solver automatico completo di Digits con Selenium.

Sentiti libero di esplorare questi file e utilizzarli per casi d'uso o scenari specifici.

*è inclusa una cartella "appendix" con 450 problemi utilizzati nei giochi del NYT. Sentiti libero di utilizzare questi problemi per il test del programma*

## Contributi

I contributi al programma Digits Solver sono benvenuti! Se trovi problemi o hai suggerimenti per miglioramenti, apri una segnalazione (issue) o invia una richiesta di modifica (pull request) nel repository GitHub.

Quando contribuisci, assicurati di seguire le migliori pratiche, mantenere la qualità del codice e fornire descrizioni chiare delle tue modifiche.


## Licenza

Il programma Digits Solver è distribuito con licenza [MIT License](https://choosealicense.com/licenses/mit/). Sei libero di utilizzare, modificare e distribuire questo programma per scopi personali o commerciali. Consulta il file [LICENSE](LICENSE.md) per ulteriori dettagli.

## Riconoscimenti

Un ringraziamento speciale all'autore di [timeshift.js](https://github.com/plaa/TimeShift-js) per il loro contributo a questo progetto. Parti del loro codice sono state utilizzate nell'implementazione del modulo solver.util.
