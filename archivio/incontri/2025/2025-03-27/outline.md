# Incontro 2025-03-27 (aula T.04)

## un commento su come accorgersi che un problems (il problema [muro](training.olinfo.it/task/terry/muro) di volta scorsa) si presta ad un approccio greedy

risolvendo a mano piccole istanze ci si rendeva conto che esistevano soluzioni ottime in cui ogni prefisso delle scelte spese dalla soluzione era soluzione ottima per il rispettivo prefisso dello stream di colori che arrivavano in input.  

## Grafi

### alcune nozioni
- la relazione di equivalenza sui nodi (u <--> v se e solo se esiste un cammino di etrremi u e v) e la nozione di componenti connesse
- le nozioni di sottografo e sottografo indotto

### la BFS

- BFS e DFS multistart identificano le componenti connesse in tempo lineare
- come succede che un algoritmo finisce col risolvere più problemi di quelli per cui era stato pensato, e perchè concentrarsi sulle domande più fondamentali
- l'idea algoritmica della BFS quando la domanda base è capire se il grafo è connesso o meno (ossia la genesi delle idee algoritmiche)
- i linguaggi di si e di no traspaiono già dall'idea algoritmica
- se ciascun nodo parla una solo volta (a tutti i suoi vicini) allora si ottiene un algoritmo lineare
- come la coda FIFO evita fughe in avanti nella frontiera dei nodi visitati 
- albero dei cammini minimi

### calcolo dei cammini minimi
- la BFS calcola anche i cammini minimi

### e se agli archi è associata una lunghezza?

- NP-hardness del problema se le lunghezze possono essere anche negative
- riduzioni ed algoritmi pseudopolinomiali
- progetto di un algoritmo ispirati dalla sua struttura portante

### l'algoritmo di Dijkstra

- algoritmo di Dijkstra come event-driven simulation (con coda di priorità a regolare l'ordine degli eventi)
- monovariante su cui poggia la correttezza dell'algoritmo di Dijkrtra

