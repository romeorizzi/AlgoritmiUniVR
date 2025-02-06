= Incontro 2024-05-17: in aula I (la DFS)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== torniamo sulla DFS

=== grafi non-diretti

DFS come algoritmo di esplorazione di un labirinto (algoritmo di Tremaux)

Proprietà dell'albero DFS (solo tree edges e backward edges, nessun crossing edge).

Invariante di raggiungibilità dal nodo corrente.

Cut-nodes e bridges.

Componenti 2-edge-connesse e componenti biconnesse.

Combinare alla DFS una programmazione dinamica in risalita.

Suggerimento su come ottenere in semplicità un algoritmo performante per matita.

=== grafi diretti

Proprietà dell'albero DFS  (abbiamo ancora i tree edges, mentre i backward edges ora si partizionano in backward edges e forward edges; e compaiono i crossing edges orientati da destra verso sinistra).

Invariante di raggiungibilità dal nodo corrente resta la stessa.

