# Piano di Test

### LOGIN TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| successo   | login va a buon fine  | 1. inserimento username 2. inserimento password 3. invio    | Reindirizzamento alla home            |                   |
| username sbagliato    | username non presente o non conforme alle regole |          | errore: inserisci nuovamente          |                   |
| password sbagliata   | La password non segue le regole o non è collegata a quell'account  |         | errore: inserisci nuovamente         |                   |

------------------
------------------

### REGISTRAZIONE TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| successo   | La registrazione va a buon fine  | 1. inserimento username 2. inserimento password 3. invio    | Reindirizzamento al Login            |                   |
| password non conforme   | La password non segue le regole  |         | errore: inserisci nuovamente         |                   |
| controllo ripetizione password   | le due password inserite non sono uguali  |      | errore: inserisci nuovamente          |                   |
| controllo username   | username già presente |      | errore: inserisci nuovamente          |                   |

------------
------------

### ADMIN_LOGIN TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| successo   | login va a buon fine  | 1. inserimento username 2. inserimento password 3. invio    | Reindirizzamento alla home_amministratore            |                   |
| username sbagliato    | username non presente o non conforme alle regole |          | errore: inserisci nuovamente          |                   |
| password sbagliata   | La password non segue le regole o non è collegata a quell'account  |         | errore: inserisci nuovamente         |                   |

------------------
------------------

### CARRELLO TEST

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| aggiungi nuovo prodotto   | aggiunta di un prodotto non ancora presente nel carrello  | interazione con il bottone aggiungi al carrello  | prodotto aggiunto nel carrello |                   |
| aggiungi prodotto (quantità)   | aggiungere un prodotto già presente nel carrello | 1. interazione con il bottone per aggiungere il prodotto    | cambio della quantità del prodotto        |                   |
| visualizza carrello  | collegamento con la pagina carrello.html | 1. interazione con il bottone carrello        | accesso al carrello.html         |                   |
| modifica quantità | cambio della quantità di un prodotto del carrello | 1. accesso al carrello 2. interazione con la selezione delle unità del prodotto       | aggiornamento del numero relativo alle unità del prodotto        |                   |
| rimozione prodotto | rimozione prodotto dal carrello | 1. accesso al carrello 2. interazione con la selezione delle unità del prodotto       | rimozione del prodotto dal carrello |                   |

------------------
------------------

### RICERCA TEST
| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| successo   | la ricerca ha prodotto il risultato atteso  | 1. inserimento parola nella barra di ricerca 2. avvio   | viene visualizzato il prodotto cercato            |                   |
| errore   | il prodotto cercato non esiste |          | errore: prodotto mancante         |                   |

------------------
------------------

### FILTRO TEST
| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| aggiunta filtro   | scelta di un filtro da applicare alla ricerca | 1. inserimento del filtro nella barra 2. avvio   | viene visualizzata la lista dei prodotti cercati tenendo conto del filtro applicato            |                   |
| rimozione filtro   | rimozione del filtro applicato | 1. interazione con il bottone del filtro 2. rimozione del filtro 3. filtra         | filtro rimosso e visualizzazione della lista di base         |                   |

------------------
------------------

### CHECKOUT TEST
| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| checkout completato   | l'ordine è confermato correttamente | 1. inserimento dell'indirizzo 2. inserimento del codice paypal 3. ordina   | viene confermato l'ordine e rimandati alla home, rimozione prodotti dal carrello            |                   |
| checkout non completato   | ordine non completato | 1. interazione con il bottone del carrello        | ordine annullato         |                   |
| checkout non conforme  | ordine non completato, mancanza dati | 1. inserimento dell'indirizzo 2. ordina | ordine non effettuato, mancanza del campo paypal         |                   |

------------------
------------------

### RESOCONTO_VENDITE TEST
| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| apri resoconto   | visualizzazione della pagina con i resoconti delle vendite | 1. interazione con il bottone resoconto vendite  |  visualizzazione pagina del resoconto vendite            |                   |
| scelta del filtro   | scelta di un filtro da applicare alla tabella del resoconto vendite | 1. interazione con i filtri 2. scelta del filtro 3. filtra       | filtro applicato correttamente       |                   |
| rimozione filtro   | rimozione del filtro applicato | 1. interazione con il bottone del filtro 2. rimozione del filtro 3. filtra         | filtro rimosso e visualizzazione della lista di base         |                   |

------------------
------------------

### AGGIUNGI_PRODOTTO TEST

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           | Risultati ottenuti |
|---------|-----|------------------|-----------------|-------------------|
| aggiungi nuovo prodotto   | aggiunta di un prodotto non ancora presente  | interazione con il bottone aggiungi prodotto  | prodotto aggiunto e visibile per tutti |                   |
| modifica prodotto   | modificare un prodotto già presente | 1. interazione con il bottone per modificare il prodotto    | cambio delle informazioni del prodotto        |                   |
| rimozione prodotto | rimozione prodotto per tutti | 1. accesso alla home-amministratore 2. interazione con la selezione della modifica del prodotto 3. modificata la quantità del prodotto a 0       | rimozione del prodotto dal carrello |                   |
