# Incontro 2025-03-21 (laboratorio alpha)

## problema muro ([training.olinfo.it/task/terry/muro](training.olinfo.it/task/terry/muro))

* proposto da: un compagno

* sorgente: preso dal [sito per allenarsi alle olimpiadi di informatica](training.olinfo.it), dove puoi sottometere soluzioni per ottenere feedback

* competenze richieste: ingenuity

* tecnica algoritmica: greedy

* altre competenze che aiuterebbero (ad esempio se uno volesse poi dimostrare la correttezza della propria intuizione risolutiva):
    - induzione matematica
    - buona caratterizzazione nella forma di una formula max-min

## Come si poteva approcciare il problema affinchè sopraggiungesse l'intuizione della strategia ottima
  analizzando casi particolari del problema, come ad esempio:
  1. se tutti i rettangoli sono larghi L=1
  2. se tutti i rettangoli hanno la stessa larghezza
  3. se le larghezze dei rettangoli sono non-crescenti
  4. se le larghezze dei rettangoli sono non-decrescenti
    
## Politica greedy intuita/congetturata ottima
  strutturata in:
  - colloca un rettangolo alla volta senza preoccuparti del futuro (greedy)
  - piazza quindi il rettangolo attuale in modo da massimizzare la funzione obiettivo (ossia la varietà di colori esposti), e, a parità di funzione obiettivo, mettilo il più a sinistra possibile per mantenere una struttura opportuna che non comprometta il futuro.

## Esercizio che consiglio
  produrre dimostrazione che la politica intuita produce sempre una soluzione ottima

## un ulteriore commento (che spesi solo ad incontro successivo 2025-03-27) su come accorgersi che un problema si presta ad un approccio greedy

Il problema muro ci ha consegnato (anche a mè) la seguente lesson learned

**La spia delle brise per il greedy** risolvendo a manina e per benino piccole istanze del problema muro ci si rendeva conto che esistevano soluzioni ottime in cui ogni prefisso delle scelte spese dalla soluzione era soluzione ottima per il rispettivo prefisso dello stream di colori che arrivavano in input.

