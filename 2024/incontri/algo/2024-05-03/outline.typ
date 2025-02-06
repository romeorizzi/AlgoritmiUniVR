= Incontro 2024-05-03: approfondimento sul problema Poldo (da remoto)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== oggi abbiamo approfondito sul problema poldo (massima sottosequenza crescente)

La volta scorsa, per il problema poldo, avevamo individuato un "contratto ricorsivo" (famigli di domande che cadono una dopo l'altra come i birilli) di sole $n$ domande, dove $n$ era il numero di panini.

Dove il colesterolo dei panini è memorizzato nel vettore panino, indicizzato da $0$ a $n-1$, la famiglia era:
    
```
per i = 0,1,...,n-1
    max_scorpacciata[i] := numero massimo di panini che riesco a mangiare se il primo panino che mangio è il panino i.
    
    IMPLEMENTAZIONE/COMPUTAZIONE:
    BASE: max_scorpacciata[n-1] = 1  perchè non ci sono altri panini dopo il primo che mangio 
    PASSO:
        per i = n-1, n-2,...,1, 0:
           max_scorpacciata[i] = 1 + max_(j>i) max_scorpacciata[j]

Esempio:
max_scorp:  2  5  1  4  3  4  3  2  2  1
   panino:  7  3  9  4  5  0  1  6  2  8
```

La domanda originale era: quale è il massimo numero di panini che riesco a mangiare rispettando la dieta.

*Nota:* la domanda originale non è una delle domande della famiglia. Ma, fortunatamente, viene molto facile una volta risolti tutti i birilli. La soluzione ottima si mangia almeno un panino, e quindi mangerà un primo panino da qualche parte. Pertanto, `optval`$ = max_(i in [0,n-1]) "max_scorp"[i]$.

Competenza: calcolato optval, come si ricostruisce una soluzione ottima?

Idea: utilizzare la famiglia dei birilli già risposti come road-map (come angioletti compagnetti)

```
max_scorp:  2  5  1  4  3  4  3  2  2  1   <-- max=5
   panino:  7  3  9  4  5  0  1  6  2  8
```

1. con un ciclo for calcolo `optval`$ = max_(i in [0,n-1]) "max_scorp"[i]$.

2. siccome i birilli sono caduti da destra verso sinistra, ora, per costruire una soluzione ottima, li affronto da sinistra verso destra senza paura ad affrontare per primi i problemi più grossi e le domande più arcane.

Ho una promessa di 5, e così di fronte alla prima scelta (il panino 7 me lo magno o è meglio che no?) posso pingare il primo angioletto. Lui mi dice: se parti mangiandoti il panino 7 tu, ben che vada, scorpacci 2. Mh..., pias menga. Non lo mangio (mica sono scemo, dato che angioletto mi predice il futuro).

Come prosegue:

```
max_scorp:   2     5     1      4      3     4     3      2     2     1   <-- max=5
   panino:   7     3     9      4      5     0     1      6     2     8
            no   yep    no    yep    yep  magari  mag   yep   mag   yep
         (5>2) (5->4) (4>1) (4->3) (3->2)             (2->1)       (1->0)    
                             (4>3)  (5>4)  (0<5) (3<5) (6>5) (2<6) (8>6)
```

Una soluzione ottima: 3, 4, 5, 6, 8  (potrebbero essercene anche in numero esponenziale)
Di questo certificato checko che è una sottosequenza della sequenza in input (l'ammissibilità)
```
   panino:  7  3  9  4  5  0  1  6  2  8
               ^     ^  ^        ^     ^ 
```

=== Questione/approfondimento 1:
E se volessi calcolare quante sono le soluzioni ottime? La programmazione dinamica è una tecnica robusta, e non è difficile, sulla stessa struttura ricorsiva (che poi è la linea), definire una famiglia ausiliaria di domande che tenga conto di quante sono le soluzioni ottime per ogni birillo precedentemente introdotto.
Altro esempio di tale robustezza: metti che invece di voler mangiare il numero massimo di panini io voglia riempirmi della massima quantità di colesterolo possibile.


=== Questione/approfondimento 2: nel tirare giù i birilli a mano mi si sono presentati sovente dei birilli che non mi richiedavano poi davvero di controllare tutti i j>1.
Non è che esiste un modo di abbassare la complessità di questo algoritmo (attualmente O(n^2)).

=== Questione/approfondimento 3: abbiamo controllato in tutto l'ammissibilità della nostra soluzione (Yes-certificate), ma possiamo convincerci efficacemente anche del fatto che essa è davvero ottima (No-certificate).


Sulla lavagna abbiamo visto un'implementazione dell'algoritmo che risolve le Questioni 2 e 3. In @tetris riportiamo l'immagine finale (statica) di quanto eleborato insieme:

#figure(
  image("LavagnaALGO2024-05-03_1.png", width: 90%),
  caption: [una partitina a tetris, coi panini di Mr. Poldo],
) <tetris>


Prima di curare questa implementazione abbiamo preferito rovesciare il contratto:
    
vien forse più bello se consideriamo la famiglia di problemi simmetricamente definita:

```
per i = 0,1,...,n-1
    max_scorpacciata[i] := numero massimo di panini che riesco a mangiare se l'ultimo panino che mangio è il panino i.
    
    IMPLEMENTAZIONE/COMPUTAZIONE:
    BASE: max_scorpacciata[0] = 1  perchè non ci sono altri panini prima del panino 0
    PASSO:
        per i = 1, 2,...,n-1:
           max_scorpacciata[i] = 1 + max_(j<i) max_scorpacciata[j]
```

Ci siamo figurati di giocarea tetris, coi panini che ci arrivano come presi da sinistra a destra (ossia prima i problemi piccoli che possono essere risposti subito e via via quelli più grossi che richiedono di aver risolto i problemi precedenti per essere risposti).

Quando arrivava un panino, lo collocavo sul primo bin dove poteva essere collocato, se non poteva essere collocato su nessun bin allora aprivo un nuovo bin apposta per lui, alla immediata destra di tutti gli altri bin già aperti.
Visto che vogliamo trovare una sotto-sequenza strettamente crescente, la regola del tetris è che un panino può essere messo solo sopra panini non più piccoli di lui (quindi dentro un bin verrà a coricarsi una sotto-sequenza non-crescente).
Se un panino finice nel bin b, si tiene memoria del panino del bin b-1 che lo ha calciato.

Si noti che:
    
    1. il panino i finisce nel bin b se e solo se `max_scorpacciata[i] == b`  (il gioco del Tetris è solo un'implementazione)
    
    2. per ricostruire una soluzione ottima ci basta prendere un qualsiasi panino che a termine del Tetris è nell'ultimo bin più a destra, e prendersi anche la sequenza dei suoi calciatori. E' facile vedere che questa sequenza è una sotto-sequenza crescente (ammissibilità, Yes-certificate).
    
*Certificato di NO (di ottimalità):*
    Ho ottenuto optval bins, e, per ogni bin, i panini in esso contenuti costituiscono una sottosequenza non-crescente della sequenza in input. Pertanto, per ogni bin b, ogni soluzione ammissibile potrà prendere al massimo un panino dal bin b. Quindi, nessuna soluzione ammissibile potrà avere più di optval panini.
    
*Complessità:*
    Osservazione: in ogni istante del gioco del Tetris, la sequenza dei paninini che in quel momento sono cime di bin è una sequenza crescente (invariante da dimostrare).
    L'idea è allora di trovare il giusto posto del panino $i$ effettuando una ricerca binaria sugli al più optval bins.
    La complessità diventa quindi $O(n log "optval") = O(n log n)$    

```
Facciamolo a mano:
    7  3  9  4  5  0  1  6  2  8
    
snap 1:
7            7
bins         tops
    
snap 2:
3
7            3
bins         tops
    
snap 3:
3
7 9          3 9
bins         tops
    
snap 4:
3 4
7 9          3 4
bins         tops
    
snap 5:
3 4
7 9 5        3 4 5
bins         tops
    
snap 6:
0
3 4
7 9 5        0 4 5
bins         tops
        
snap 7:
0 1
3 4
7 9 5        0 1 5
bins         tops
        
snap 8:
0 1
3 4
7 9 5 6      0 1 5 6
bins         tops
        
snap 9:
0 1
3 4 2
7 9 5 6      0 1 2 6
bins         tops
        
snap 10:
0 1
3 4 2
7 9 5 6 8    0 1 2 6 8
bins         tops
```