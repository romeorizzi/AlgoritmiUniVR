= 2024-03-26: questioni di efficienza (problema accensione)
#text(style:"italic", size:11pt, [Talvolta si comincia a comporre il presente documento contestualmente e collaborativamente all'URL:\
#h(6mm) `https://etherpad.wikimedia.org/p/Algoritmi2024-03-26`\
Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

Dopo che gli studenti ci avevano lavorato anche per conto loro, siamo tornati  sul problema accensione introdotto la volta scorsa (2024-03-19).

Gli studenti avevano già prodotto una soluzione ricorsiva che però era quadratica e pertanto non riusciva a risolvere tutti i subtask nemmeno implementata in c++ (non è una questione di costante moltiplicativa ma di complessità asintotica).

Abbiamo quindi discusso in più aspetti l'importanza del punto di vista offerto dalla complessità asintotica.

Abbiamo poi intuito, analizzando la nostra prima soluzione/codice, che la strada maestra per ridurre la complessità asintotica per questo problema richiedesse di dare un upper-bound sub-quadratico a $sum_{i=1}^n "#DIVISORS_OF"(i)$.

Lavorando anche con le mani abbiamo raccolto l'opinione che potesse esserci un upper-bound asintotico del tipo O(n log n), che in effetti sarebbe stato quanto necessario e bastante per poter risolvere tutti i subtask.

Per dimostrare un tale upper-bound abbiamo osservato che
$
    sum_{i=1}^n "#DIVISORS_OF"(i) = sum_{j=1}^n "#MULTIPLES_OF"(j) = n(1+1/2+1/3+ ... + 1/n) = O(n log n)
$

Dove l'ultimo passaggio può venire da conoscenza pregressa della serie armonica, o con la classica approssimazione con un integrale, o anche con una dimostrazione induttiva diretta. Vedi come andrebbe organizzata?

Un compagno ha concluso che a questo punto la cosa migliore era riscrivere la soluzione alla luce della struttura di questa dimostrazione, ossia pivotando il nostro punto di vista dagli interruttori ai PC almeno quando si compia l'aggiornamento di quali PC siano accesi.


*due problemi per approfondire meglio uno dei tanti modelli concettuali incontrati nell'affrontare il problema accensione:*

+ Flotta di aerei kamikaze in viaggio

+ Ponti di tessere