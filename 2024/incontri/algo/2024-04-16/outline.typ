= Incontro 2024-04-16: in aula I (visita BFS)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== visita BFS

Oggi abbiamo descritto la BFS.
Nata con lo scopo di vedere le componenti connesse di un grafo, nel suo interplay tra linguaggi di si e di no che ne sono usciti abbiamo ottenuto un algoritmo lineare per il computo delle distanze ed una rappresentazione compatta (in O(n) memoria) della famiglia di tutti i cammini minimi da un nodo $s$ dato.
Nell'implementazione dell'idea base sottostante l'algoritmo (un fuoco che si propaga partendo da $s$) ha trovato valorizzazione la coda FIFO, sulla quale lavora l'invariante di "monotona a max 2 livelli successivi".

