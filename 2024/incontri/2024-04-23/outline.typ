= Incontro 2024-04-23: in aula I (i linguaggi di SI e di NO della BFS)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])


Siamo partiti da un'analisi dei linguaggi di SI e di NO della BFS:

-SI: i nodi di questa classe sono tutti parte di una stessa componente connessa in quanto ti offro un albero radicato nel rappresentante di classe che li tiene tutti insieme. Ogni nodo a parte il rappresentante di classe indica un padre di distanza inferiore dal rappresentante di classe.
-NO: le classi di questa partizione dei nodi sono in componenti diverse poichè puoi controllare che nessun arco ha estremi in classi diverse.

di fatto, l'albero radicato nel rappresentante di classe è anche albero dei cammini minimi.

Partendo da questo, abbiamo generalizzato il problema al caso pesato.

Il caso pesato piò essere ridotto al caso non pesato e poi risolto con la BFS semplicemente suddividendo gli archi così come comanda la loro lunghezza. Purtroppo questa riduzione non è polinomiale ma solo pseudo-polinomiale, ma basta a comprendere che esiste ancora un albero dei cammini minimi.

Abbiamo dimostrato in modo più esistenziale che esiste sempre un albero dei cammini minimi se $d >= 0$. E abbiamo preso questa come ipotesi base per l'algoritmo di Dijkstra.

Abbiamo visto Dijkstra in 3 modi diversi:

1. una event driven simulation

2. un gioco di morose con uno che fà proposte sul mercato non appena conosce il fatto suo e può fare proposte serie e, almeno da parte sua, definitive

3. un esperimento sotto l'effetto della gravità


Abbiamo scritto un primo codice per la DFS da ananalizzare la prossima volta.