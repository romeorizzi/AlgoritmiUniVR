# Incontro 2025-03-13 (aula T.0.4)

## problema `Borse di studio` ([https://training.olinfo.it/task/oii_borse](https://training.olinfo.it/task/oii_borse))

* richiesta in senso lato: saper listare efficacemente gli oggetti entro un determinato spazio di interesse 
* competenza chiave: pensiero ricorsivo


## Cosa abbiamo scoperto

La responsabilità di determinare noi l'opportuno contratto ricorsivo, generalizzando utilmente la definizione del problema assegnato, spetta a noi. Dobbiamo infatti metterci nelle condizioni di "poter chiudere/rispettare il contratto".
In questo problema la chiusura del contratto è una mera questione di disporre effettivamente delle informazioni necessarie, sia che lo  si veda nella versione di conteggio (che in generale consiglio di porsi per prima), che poi nel progetto dell'interfaccia per la procedura ricorsiva per il listing (visto che abbiamo voluto scriverla ricorsiva).

In realtà era possibile, dopo aver comunque compiuto il percorso necessario a cogliere la struttura ricorsiva del problema stesso, scrivere un codice iterativo forse anche più efficace. E, se in un linguaggio moderno come `python`, era anche possibile evitare di dover ampliare per una seconda volta il contratto ricorsivo semplicemente avvalendosi dei generatori.


    
## Ulteriori lezioni

Quando siamo passati alla codifica abbiamo scoperto quanto convenga codificare prima una funzione ricorsiva che affronti il solo problema del conteggio (ci va benissimo che sia una ricorsione pura, esponenziale, la cosa importante è avere una prima struttura chiara e magari anche testata da poi successivamente con gli ulteriroi orpelli vestire come un albero di natale con le bocce).
