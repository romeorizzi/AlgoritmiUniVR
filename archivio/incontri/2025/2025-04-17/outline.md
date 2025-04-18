# Incontro 2025-04-17 (aula T.04)

## Oggi un pò di programmazione dinamica a volo di uccello (senza davvero codificare)

Abbiamo visto

### come affrontare il problema Poldo (ricerca di una sottosequenza crescente di lunghezza massima)

- concetto di sottosequenza (ottenuta dalla sequenza rimuovendo degli elementi e mantenendo quelli rimasti nell'ordine originale)
- considerazione: mettere il problema in P non è banale perchè il numero delle soluzioni ammissibili è facilmente esponenziale (anche il sottospazio di quelle ottime) e un approccio greedy fallisce miseramente (non-località)
- ci siamo quindi prefissi di comprendere prima la struttura dello spazio delle soluzioni ammissibile (difficile trovare direttamente un ago in un pagliaio se non sai qualcosa sulla struttura del pagliaio)
- a questo scopo, abbiamo deciso di porci prima il problema del conteggio del numero di soluzioni ammissibili
- abbiamo lavorato su un istanza specifica (per altro lo stesso input su cui ci eravamo posti la questione di Poldo)
- abbiamo adottato un approccio ricorsivo, ossia ci siamo detti:
     calcoliamo (a manina) la risposta corretta (per il problema di conteggio) per ogni prefisso (dai più piccoli ai più grandi)
  lavorando in questo modo, per tentativi ed errori, è infine emersa una famiglia di domande che funzionava (ossia, cadevano come i birilli)

- la famiglia di domande che ci ha consentito di risolvere il problema dei contegi ci ha poi ispirato nell'inventare la famiglia di domande che si sarebbero mangiate il problema Poldo

### come affrontare il problema Massima Sottosequenza Comune

Su questo problema abbiamo deciso di illustrare un altro possibile approccio:

sempre lavorando su un'istanza specifica e prendendone ispirazione, ma ci siamo concentrati sul risolvere prima il problema originale con un elegante e coinciso codice ricorsivo. Abbiamo poi notato che l'interfaccia di fatina era bella compatta e che quindi il problema si poteva portare in P con la memoizzazione, o lavorando su una matrice di programmazione dinamica.

Abbiamo poi gestito a mano la matrice per l'istanza presa in considerazione, per preparaci ad un'eventuale codifica.
