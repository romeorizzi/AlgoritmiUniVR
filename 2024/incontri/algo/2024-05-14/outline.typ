= Incontro 2024-05-14: in aula I (programmazione dinamica su albero)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== oggi lavoriamo con programmazione dinamica su albero (slalom)

Sito con problemi (e in particolare il problema slalom):

```
https://training.olinfo.it/#/task/slalom/statement
```

Nel caso non-pesato troviamo un punto di frattura del problema nelle foglie:
per ogni foglia v esiste un node cover di minima cardinalità che non include v dato che l'insieme degli archi incidenti a v è sempre sottoinsieme dell'insieme degli archi del nodo adiacente a v.
Questo risolve un bit di non-determinismo ed è già possibile passare la palla a fatina ricorsina.

Abbiamo osservato che mentre nel caso non-pesato abbiamo un semplice algoritmo greedy, nel caso pesato abbiamo dei fenomeni di non-località che ci portano a cercare una soluzione di programmazione dinamica.

Appeso l'albero ad un nodo radice, per ogni nodo v abbiamo il sottoalbero Tv dei nodi che sono discendenti di v (incluso v stesso), chiamato il sottoalbero radicato in v.

Ecco la famiglia (doppia) di problemi chiusa rispetto ad induzione:

```
  Pv = the minimum cost of a min-cover of the subtree Tv rooted at v
  
  Qv = the minimum cost of a min-cover of the subtree Tv rooted at v among those min-covers that are required to include node v
```

Passando all'implementazione, abbiamo osservato come l'albero convenisse sollevarlo dalla radice tramite una DFS.

Abbiamo poi scoperto la convenienza di integrare la computazione dei problemi dentro la DFS stessa.
