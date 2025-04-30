# Incontro Tutor 2025-04-23 (aula Alfa)

## Soluzione del problema Mexican Standoff (dessert)

### abbiamo visto

- come invertire la direzione degli archi in un grafo rappresentato come lista di adiacenza
- come modificare l'algoritmo bfs per adattarsi al problema, mantenendo una complessita' lineare e visitando i nodi solo quando raggiungono la soglia di attivazione
- implementazione in python della soluzione

## Soluzione del problema cioccolato (`https://training.olinfo.it/task/terry/cioccolato`)

### abbiamo visto

- come funziona la soluzione lineare in M+N, e perche' non e' sufficiente per risolvere il problema (visti i limiti N, M <= 10\*\*12)
- come ottimizzare la soluzione lineare osservando che la strategia ottima conduce sempre ad un quadrato (o rettangolo con |N-M| = 1)
- implementazione in python della soluzione in O(1)

## Soluzione del problema triangolo (`https://training.olinfo.it/task/triangolo`)

### abbiamo visto

- come affrontare il problema in modo intuitivo (soluzione esponenziale)
- come usare la programmazione dinamica per scomporre il problema su ogni livello del triangolo,
  salvandosi per ogni numero la migliore somma che si riesce ad ottenere partendo dalla cima e arrivando a quel numero
- come indicizzare il triangolo nella sua rappresentazione come matrice
- implementazione in python di tre modi diversi di codificare la soluzione
  - bottom-up, partendo dalla cima del triangolo (`triangolo.py`)
    - soluzione derivata dal ragionamento iniziale
    - complessa gestione degli indici per evitare di leggere celle al di fuori del triangolo
  - bottom-up, partendo dal fondo del triangolo (`triangolo2.py`)
    - soluzione meno intuitiva
    - risolve il problema della gestione degli indici, ogni cella letta e' garantito che esista
  - top-down, partendo dalla cima del triangolo (`triangolo_ric.py`)
    - soluzione piu' semplice da ideare, derivata dalla soluzione ricorsiva del problema
    - necessita' di implementare la memoizzazione, altrimenti la soluzione non termina per input grandi (`input_triangolo_big.txt`, generato con `gen_triangolo.py`)
    - leggermente piu' lenta delle versioni bottom-up, ma comunque sufficiente per ottenere il massimo punteggio

## Proposto problema Big Stonks

Link: `https://training.olinfo.it/task/stonks`
