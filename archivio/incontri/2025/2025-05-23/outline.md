# Incontro 2025-05-09 (laboratorio alfa)

## I binary heaps, implementazione pratica delle code di priorità

Il progetto di strutture dati efficienti spesso si basa sulla ricerca di un giusto compromesso. 
Nel caso delle priority queue ciò si traduce nel proporre e gestire una via di mezzo tra un'ordinamento totale e il disordine totale tra gli oggetti in coda.

Nell'implementazione della struttura dati astratta "coda di priorità" data dai binary heaps gli elementi in coda vengono di fatto (the hard reality word) collocate nel prefisso di un array, anche se su un piano concettuali ce li figuriamo come nodi di un albero binario, radicato, ordinato e completo.
Se gli indici del vettore partono da 0, allora 0 è la radice dell'albero e vale:

```
   inline int padre(int i) { return (i-1)/2; }
   inline int left_child(int i) { return 2*i+1; }
   inline int right_child(int i) { return 2*(i+1); }
```

Viviamo quindi in Fantasilandia (vediamo e guardiamo ad un albero) quando vogliamo comprendere l'idea e funzionamento sottostante dei binary heap, ma siamo poi chiamati all'Hard Reality World quando dobbiamo scrivere il codice che lo realizza in pratica.

Nei binary heaps, le due invarianti cardine sono:

1. buon ordinamento dello heap. Nessun nodo ha chiave minore di quello di babbo suo (no-Edipo property). Questa proprietà è chiara e semplice agli occhi di chi vive in fantasilandia, ma più caotica e misteriosa se uno la considerasse sull'array. 

2. buon riempimento dello heap. In Fantasilandia reciterebbe: se un nodo dell'albero binario infinito contiene un elemento allora sono pieni anche tutti i nodi dei livelli superiori, così come anche tutti i nodi dello stesso livello disposti alla sua sinistra.
   Nell'Hard Reality World è più chiara: le posizioni piene dell'array sono un prefisso dell'array.

La no-Edipo property ci garantisce che quando la coda non è vuota allora la radice è sempre abitata da un elemento di minimo.

Dobbiamo verificare se sia possibile gestire la `Insert` e poi anche la `ExtractMin` in $O(log n)$ operazioni, mantenendo le due invarianti.

Sistemando prima l'invariante fisica e procedendo di scambio di ruoli per risolvere i nostri problemi di relazione padre-figlio in Fantasilandia abbiamo ultimato il progetto della struttura dati pervenendo al risultato desiderato.


## Problema Stalom

```
https://training.olinfo.it/task/slalom
```

- greedy: ogni albero garantisce di avere almeno una foglia
- programmazione dinamica: una volta radicato un albero, ad ogni nodo resta associato il sottoalbero dei suoi discendenti. Le famiglie di sottoproblemi potrebbero essere in corrispondenza coi nodi: un sottoproblema per ogni tale sottoalbero. Ma magari di famiglie ne servono due: le api col miele e una famiglia di bombi a supporto.

