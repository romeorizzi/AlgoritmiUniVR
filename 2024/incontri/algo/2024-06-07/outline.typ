= Incontro 2024-05-31: in aula I
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== oggi

Oggi abbiamo lavorato sul problema funghi.

Abbiamo vissuto insieme come possa essere affrontato e siamo giunti ad una soluzione polinomiale.

Siamo poi passati a scrivere il codice ma non siamo giunti ad una versione corretta.

Nel folder trovate sia la soluzione come a fine lezione che una sequenza di soluzioni corrette che conducono un percorso dal problema di conteggio al problema di unranking.

```
funghi_still_unfinished.py    codice come lasciato a fine versione, contiene ancora dei bug e non gira
funghi.py               prima soluzione corretta, ottenuta per ultimazione del percorso di codifica iniziato assieme
funghi_cleaned.py       pulizia e semplificazione di prima soluzione corretta
funghi_restructured_with_better_contract.py    riduce il numero di sottoproblemi e semplifica il codice (miglioramento interessante ispirato dal desiderio di produrre una versione con l'unranking)
funghi_with_unrank.py   ed ecco come è facile rivedere la procedura di count per ottenere una procedura di unrank. Si noti però come la procedura di unrank debba poggiare sulla procedura di count (e, ATTENZIONE, si consideri perchè il count debba ora essere esatto e non MOD 1000000007)
```

== Esercizio che consiglio
  si scriva ora la procedura di rank dualizzando la procedura di unrank. E' la stessa relazione di dualità che per oglia altra coppia di procedure (unrank,rank) per qualsiasi altra famiglia di strutture. E si può sempre trovare ispirazione nelle procedure di cambio base dei numeri.


Nota: se si vuole lanciare una soluzione senza che compaiano a schermo le righe di debugging si rediriga lo stderr su /dev/null
Ad esempio:
```
./funghi_with_unrank.py < input.txt 2> /dev/null
```
