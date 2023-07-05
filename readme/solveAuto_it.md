# Automazione della risoluzione di Digits Solver

Questo script automatizza la risoluzione dei puzzle nel gioco Digits sul sito web del New York Times utilizzando Selenium e un risolutore personalizzato.

## Prerequisiti

Prima di eseguire lo script, assicurati di avere installato quanto segue:

- Python 3.x
- Libreria Selenium
- Chrome WebDriver
- Cartella del risolutore

## Per iniziare

1. Clona il repository o scarica lo script.
2. Installa le dipendenze richieste utilizzando pip:

   ```shell
   pip install selenium
   ```

3. Scarica l'eseguibile del Chrome WebDriver e aggiungi la sua posizione alla variabile di ambiente PATH del tuo sistema.

Certamente! Ecco la documentazione per l'interfaccia della riga di comando:


## Utilizzo

```plaintext
solver/util/solve_auto [-h] [[-start S] [-level L] | [-daily]]
```

### Argomenti opzionali

- `-h, --help`: Mostra il messaggio di aiuto ed esce.

- `-start S, --startLevel S`: Specifica il livello di partenza per iniziare a risolvere i puzzle. Il valore deve essere un numero intero.

- `-level L, --levelToPlay L`: Specifica il numero totale di livelli da giocare. Il valore deve essere un numero intero.

- `-daily, --dailyOnly`: Risolvi solo i puzzle giornalieri. Se viene fornita questa opzione, lo strumento ignorerà le opzioni `--startLevel` e `--levelToPlay` e risolverà solo il puzzle giornaliero.

## Esempi


1. Risolvi 10 livelli a partire dal livello 5:
   ```plaintext
   python solver/util/solve_auto --startLevel 5 --levelToPlay 10
   ```

2. Risolvi solo i puzzle giornalieri:
   ```plaintext
   python solver/util/solve_auto --dailyOnly
   ```

Nota: Se non vengono forniti argomenti, lo strumento utilizzerà le impostazioni predefinite (partenza dal livello 1 al livello 20).


## Funzionalità

Lo script automatizza le seguenti azioni:

1. Navigazione al gioco Digits sul sito web del New York Times.

2. Manipolazione del tempo di gioco utilizzando lo script `TimeShift.js`. (solo solveMany.py)

3. Cliccando sul pulsante "Gioca" per avviare un puzzle.

4. Risoluzione di ogni puzzle eseguendo i clic necessari sui pulsanti dei numeri e degli operatori.

5. Gestione dei casi in cui lo script si blocca, ad esempio quando i pulsanti o gli elementi non sono cliccabili.

6. Avanzamento al puzzle successivo o ritorno alla schermata di selezione del puzzle quando viene completato un set di puzzle.

7. Stampa del numero di puzzle corrente e della data come riferimento. (solo solveMany.py)

## Personalizzazione

Se desideri modificare o estendere la funzionalità dello script, puoi esplorare le seguenti funzioni:

- `click_element(element_id, error_message)`: Gestisce il clic su un elemento identificato dal suo ID. Se l'elemento non è cliccabile, richiede

 all'utente un input.

- `combine_numbers(step_list, buttons)`: Gestisce la combinazione di numeri eseguendo i clic necessari sui pulsanti dei numeri e aggiornando lo stato dei pulsanti.

- `next_puzzle_button_click()`: Gestisce il clic sul pulsante "Puzzle successivo" per passare al puzzle successivo.

- `back_to_puzzles_button_click()`: Gestisce il clic sul pulsante "Torna ai puzzle" quando viene completato un set di puzzle.

Sentiti libero di modificare il codice in base alle tue specifiche esigenze.

## Licenza

Questo script è fornito con la [Licenza MIT](LICENSE.md).

Si prega di notare che la documentazione presuppone che tu abbia già configurato l'ambiente e le dipendenze necessarie come indicato nella sezione "Prerequisiti".
