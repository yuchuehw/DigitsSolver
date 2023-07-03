<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Icona di Digits Solver"
        width="500"
       />
    </picture>
<p>

[English](README_en.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • Italiano
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Benvenuti in Digits Solver, il compagno definitivo in Python per conquistare il rompicapo [Digits](https://www.nytimes.com/games/digits) che sfida la mente, sviluppato da The New York Times. Tuffati in un affascinante mondo di sfide numeriche e padroneggia l'arte della manipolazione strategica. Con Digits Solver, manipolerai strategicamente un insieme di cifre iniziali utilizzando operazioni matematiche per raggiungere la cifra obiettivo sfuggente. Il suo potente algoritmo e l'analisi meticolosa ti consentiranno di svelare rapidamente ogni rompicapo, offrendo soluzioni passo dopo passo con una precisione infallibile. Potenzia la tua abilità nel risolvere rompicapi e sblocca i segreti nascosti tra le cifre. Preparati per un entusiasmante viaggio per diventare un maestro di Digits!

[![Applicazione Python](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![Punteggio di PyLint](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![Badge di Python](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![contributions welcome](https://img.shields.io/badge/contributi-graditi-brightgreen.svg?style=flat&color=pink)
[![Licenza](https://img.shields.io/badge/Licenza-MIT-yellow.svg)](LICENSE.md)
[![Stile del codice: black](https://img.shields.io/badge/Stile%20del%20codice-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
Guarda l'algoritmo

 in azione facendo clic sul pulsante verde di esecuzione dopo essere stato reindirizzato:

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

Puoi anche guardare questa esecuzione veloce che utilizza l'algoritmo Digits Solver:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Nota: La demo mostra la funzione [solve_auto](solveAuto.md). Continua a leggere per ulteriori informazioni.*

## Tabella dei contenuti

- [Installazione](#installazione)
- [Utilizzo](#utilizzo)
- [Esempi](#esempi)
- [Utilizzo Alternativo](#utilizzo-alternativo)
- [Moduli di Utilità](#moduli-di-utilità)
- [Contributi](#contributi)
- [Licenza](#licenza)
- [Ringraziamenti](#ringraziamenti)

## Installazione

Puoi ottenere una copia del programma Digits Solver utilizzando uno dei seguenti metodi:

1. **Clonare il Repository**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Scaricare il File Zip**:
   - Vai alla scheda [Release](https://github.com/yuchuehw/DigitsSolver/releases) sul repository GitHub.
   - Scarica il file zip dell'ultima release.
   - Estrai il contenuto del file zip nella posizione desiderata.

Dopo aver ottenuto il programma, puoi procedere alla sezione [Utilizzo](#utilizzo) per eseguire il programma Digits Solver.

## Utilizzo

Per eseguire il programma Digits Solver, apri il terminale e vai alla directory in cui hai scaricato o clonato il repository DigitsSolver. Una volta nella directory corretta, esegui il seguente comando nel terminale (sostituisci i valori tra parentesi angolari con i tuoi input; consulta la sezione [Esempi](#esempi) per ulteriori dettagli):

```bash
python solver <cifre_iniziali> <cifra_obiettivo> [-os] [-h]
```

- `<cifre_iniziali>`: Una lista di interi separati da spazi che rappresentano le cifre iniziali.
- `<cifra_obiettivo>`: La cifra obiettivo da ottenere.
- `-os` o `--onesolution` (opzionale): Se specificato, il programma troverà solo una soluzione. Altrimenti, troverà tutte le soluzioni possibili.
- `-h` o `--help` (opzionale): Se usato, verrà visualizzato il menu di aiuto.

## Esempi

1. Trova tutte le soluzioni per il rompicapo delle cifre:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Trova solo una soluzione per il rompicapo delle cifre:
   ```bash
   python solver 3 12 15 20 23 25 439 -os


   ```


3. Nota che le cifre iniziali vanno sempre prima delle cifre obiettivo. Questo è un esempio di un rompicapo con 8 cifre iniziali:
   ```bash
   python solver 2 3 5 7 11 13 17 19 323 -os
   ```

## Output

Il programma restituirà il numero di soluzioni trovate e mostrerà ogni soluzione nel seguente formato:

```
Soluzione trovata:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

Abbiamo trovato 1 soluzione/e
```

## Utilizzo Alternativo

Il Digits Solver può anche essere importato come modulo Python e utilizzato programmatticamente. Sei libero di aggiungere ulteriori funzionalità rispetto a quelle che abbiamo fornito. Ecco un esempio minimo di come utilizzarlo come import:

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
# False tra parentesi è opzionale. False risolve tutte le soluzioni. True risolve una sola soluzione.
# usa solve.printer = some_function per sovrascrivere il comportamento predefinito dell'output.
numero_soluzioni = solver.solve(False)
print(f"Abbiamo trovato {numero_soluzioni} soluzione/e")
```

## Moduli di Utilità

Abbiamo incluso anche alcuni programmi Python aggiuntivi che integrano il programma del risolutore. Sono situati all'interno della cartella solver/util. Puoi leggere ulteriori informazioni su come utilizzarli qui:

- [Come Utilizzare pretty_solve.py](prettySolve.md): Fornisce una versione visivamente migliorata del programma del risolutore.
- [Come Utilizzare solve_auto.py](solveAuto.md): Risolutore automatico completo di Digits con Selenium

Sentiti libero di esplorare questi file e utilizzarli per casi d'uso o scenari specifici.

*La cartella Appendice include 450 problemi utilizzati nei giochi del NYT. Sentiti libero di utilizzare questi problemi per il testing del programma.*

## Contributi

I contributi al programma Digits Solver sono i benvenuti! Se trovi problemi o hai suggerimenti per miglioramenti, apri una segnalazione o invia una richiesta di pull sul repository GitHub.

Quando contribuisci, assicurati di seguire le migliori pratiche, mantenere la qualità del codice e fornire descrizioni chiare delle tue modifiche.

## Licenza

Il programma Digits Solver è distribuito con licenza [MIT](https://choosealicense.com/licenses/mit/). Sei libero di utilizzare, modificare e distribuire questo programma per scopi personali o commerciali. Consulta il file [LICENSE](LICENSE.md) per ulteriori dettagli.

## Ringraziamenti

Un ringraziamento speciale all'autore di [timeshift.js](https://github.com/plaa/TimeShift-js) per il loro contributo a questo progetto. Porzioni del loro codice sono state utilizzate nell'implementazione del modulo solver.util.
