# Incontro 2025-04-03 (aula T.04)

## Oggi DFS (su grafi non-diretto)

### abbiamo visto
- come si svolge la visita DFS
- `open`, `close`, `dad`
- tree edges e back edges
- l'albero DFS e le sue proprietà, come è vestito dai co-tree edges
- bridges a cutnodes
- relazione di equivalenza sui nodi: u <--> v se e solo se esistono due u,v-cammini edge-disjoint. Le componenti 2-edge-connesse
- relazione sui nodi: u <--> v se e solo se esiste un ciclo che contiene sia u che v, ossia se e solo se esistion due u,v-cammini internally node disjoint. Esempio che non gode della proprietà transitiva. Lo stesso esempìo mostra che le componenti 2-connesse (definite come quei sottoinsiemi massimali di nodi che inducono un grafo connesso e privo di cutnodes) non sono disgiunte.
- `backval[v] := min {open[x] : yx in E with y a desendant of v}`
  1. questi valori cadono come i birilli (al momento di chiudere il nodo v)
  2. il tree-edge `dad[v]v` è un bridge se e solo se `backval[v] > open[dad[v]]`
  3. il nodo `v` è un cutnode se e solo se è la radice e ha almeno due figli oppure `backval[v] == open[v]`
- le componenti 2-edge-connesse e le componenti 2-connesse (e i rispettivi alberi) possono essere calcolati facilmente affiancando alla DFS uno stack esterno.

In questo stesso folder puoi trovare il codice che avevamo scritto su `https://www.onlinegdb.com/`

