# Piano di Test

### LOGIN TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           |
|---------|-----|------------------|-----------------|
| successo   | login va a buon fine  | 1. inserimento username 2. inserimento password 3. invio    | Reindirizzamento alla home            |
| username sbagliato    | username non presente o non conforme alle regole |          | errore: inserisci nuovamente          |
| password sbagliata   | La password non segue le regole o non è collegata a quell'account  |         | errore: inserisci nuovamente         |
------------------
------------------

### REGISTRAZIONE TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           |
|---------|-----|------------------|-----------------|
| successo   | La registrazione va a buon fine  | 1. (inserimento di tutte le altre informazioni) 2. inserimento username 3. inserimento password 4. invio    | Reindirizzamento al Login            |
| password non conforme   | La password non segue le regole  |         | errore: inserisci nuovamente         |
| controllo ripetizione password   | le due password inserite non sono uguali  |      | errore: inserisci nuovamente          |
| controllo username   | username già presente |      | errore: inserisci nuovamente          |

------------
------------

### ADMIN LOGIN TEST:

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           |
|---------|-----|------------------|-----------------|
| successo   | login va a buon fine  | 1. inserimento username 2. inserimento password 3. invio    | Reindirizzamento alla home_amministratore            |
| username sbagliato    | username non presente o non conforme alle regole |          | errore: inserisci nuovamente          |
| password sbagliata   | La password non segue le regole o non è collegata a quell'account  |         | errore: inserisci nuovamente         |
------------------
------------------

### CARRELLO TEST

| Nome    | Descrizione | Passi       | Cosa ci aspettiamo           |
|---------|-----|------------------|-----------------|
| aggiungi nuovo prodotto   | aggiunta di un prodotto non ancora presente nel carrello  | interazione con il bottone aggiungi al carrello  | prodotto aggiunto nel carrello
| aggiungi prodotto   | aggiungere un prodotto già presente nel carrello |          |        |
| visualizza carrello  | collegamento con la pagina carrello.html | interazione con il bottone carrello        | accesso al carrello         |
| modifica quantità | cambio della quantità di un prodotto del carrello | 1. accesso al carrello 2. interazione con la selezione delle unità del prodotto       | aggiornamento del numero relativo alle unità del prodotto        |
| rimozione prodotto | rimozione prodotto dal carrello | 1. accesso al carrello 2. interazione con la selezione delle unità del prodotto       | rimozione del prodotto dal carrello 
------------------
------------------


