# Incontro 2025-04-11 (laboratorio alpha)

## [Il crescione perfetto (cesena)](https://training.olinfo.it/task/itday_cesena) è il problema che avete proposto ed affrontato oggi

(provenienza: dalla Gara della Giornata dell’Informatica 2024 ITT Pascal, Cesena, 14 febbraio 2024) 

Mi sono limitato a darvi i seguenti:

>>Hint: spesso per entrare in un problema conviene prima considerarne dei casi particolari. Nel caso di problemi di competitive programming l'invenzione e scelta di tali casi particolari è spesso suggerita dai subtask.

>>Hint: in particolare: se nessun arco viene mai distrutto, allora la domanda è quanti chiosci siano presenti nella stessa componente connessa del nodo~$0$ da cui decolla l'elicottero (l'istituo Pascal che ospitava la gara). Questo si può risolvere con una singola BFS lanciata dal nodo~0, e la BFS è un ingrediente necessario al risolvere il problema nella sua generalità.

>>Hint: cosa succede quando invece degli archi saltano? Tra i subtask proposti nel testo si suggeriva di affrontare tale questione considerando il caso in cui il grafo era un cammino con un estremo in~0. Abbiamo commentato che questo è un ottimo sottocaso dove andare ad esplorare la questione degli archi che saltano.

Ma ci siamo poi facilitati il lavoro anche ponendoci dapprima l'ambizione di ottenere un primo algoritmo anche solo quadratico (ossia consentendoci di spendere fino ad $n$ BFS).

Ottenuto quello mancava ancora una sola ultima idea per giungere all'algoritmo lineare.

