# Incontro 2025-04-09 (aula T.04)

## Oggi DFS (su grafi diretti) + DAGs + strongly connected components

### abbiamo visto
- la struttura del grafo (diretto) come messa a nudo dalla DFS
- un problema di scheduling
- come si procede nell'analisi di un problema (per buone domande/congetture)
- problema duale: trovare cicli diretti in un grafo
- come le buone-congetture sono profezie che si auto-realizzano: pozzi e sorgenti
- trovare un ciclo diretto in un grafo senza pozzi, e in il gioco dei certificati ai vari meta-livelli
- un primo algoritmo lineare a lingua biforcuta
- algoritmo basato sulla DFS
- calcolo di un topological-sort dalla DFS - ragionare con le mani e per deduzione da quanto già in realtà si sà
- concetto di strong-connectivity per grafi diretti e il DAG delle strongly-connected-components
- trovare il cammino più lungo in grafi diretti è NP-hard
- ma in DAGs è in P grazie alla programmazione dinamica

### Challenge

come potremo fare per identificare il DAG delle strongly-connected components?