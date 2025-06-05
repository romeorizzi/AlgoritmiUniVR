# Incontro 2025-06-05 (aula T.0.4)

## i binomial Heaps

i binomial heaps solo la struttura dati per gestire un set si code di priorità (più ospedali distribuiti sul territorio) che possano essere soggette a fusione.
Con essi vogliamo consentire le seguenti operazioni:

1. istituzione di un nuovo ospedale (di una nuova coda di priorità)
2. inserimento di un nuovo paziente in un ospedale, con una data priorità
3. eliminazione di un paziente
4. trova il paziente più urgente in un certo ospedale
5. accorpa due ospedali dati

Abbiamo visto come coi binomial heaps tutte queste operazioni possano essere gestite in $O(log n)$ di delay nel caso peggiore. Per altro il costo per la ricerca del paziente più urgente può ovviamente essere messo a carico delle operazioni di aggiornamento tenendosi annotato l'elemento da ritornare ed aggiornandolo ad  ogni modifica. 
