= Incontro 2024-03-15: in aula I
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== esempi di uso ricorsione

Abbiamo scritto insieme del codice ricorsivo per la stampa delle piastrellature di un bagno 1xn.
Esempio per n=3:
```
          [][][]
          [--][]
          [][--]
```

La stampa avveniva nei casi base (foglie dell'albero) cui però non bastava la conoscenza della dimensione residua (n=0 oppure n=1 in ogni foglia) ma serviva anche la conoscenza della propria storia.
Per questo abbiamo ideato il seguente contratto:

```
def stampaPiastrellature(n, history=""):
"""stampa le piastrellature di un bagno 1xn, ciascuna prefissata dalla sua history"""
```

Abbiamo affrontanto il problema di contare le piastrellature per un bagno 2xn.
Lo abbiamo risolto in due modi diversi:
    1. allargando la famiglia di problemi che vogliamo risolvere in modo da ottenere chiusura rispetto alle operazioni elementari che abbiamo infine impiegato per ottenere problemi più piccoli. Abbiamo considerato 3 famiglie di problemi (api, vespe e bombi):
        
        f(n) = numero di piastrellature per un bagno 2xn
        g(n) = numero di piastrellature per un bagno 2xn cui è stata rimossa una cella d'angolo
        h(n) = numero di piastrellature per un bagno 2xn cui è stata rimossa una cella d'angolo e quella al suo fianco
        
    2. con una soluzione ricorsiva diretta dove si guessava la posizione della prima piastella verticale


