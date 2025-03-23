# Incontro 2025-03-06 (aula T.0.4)

## problema bagno 1xn

* competenza: pensiero ricorsivo

Quanti e quali sono le possibili piastrellature di un bagno 1xn con piastrelle 1x1 e 1x2?

Ovvero: quante e quali sono le possibili tassellazioni di una griglia 1xn con griglie 1x1 e 1x2?

Ad esempio, per n=2 sarebbero le seguenti 2:
```
[][]
[--]
```

e per n=3 sarebbero le seguenti 3:
```
[][][]
[--][]
[][--]
```

## Come si poteva approcciare il problema affinchè sopraggiungesse l'intuizione della strategia ottima

1. analizzare casi/istanze particolari del problema, partendo dai casi piccoli e facili da gestire, ossia partire proprio con n=2 e n=3

2. cercare di darsi un criterio di ordinamento conveniente sulle possibili soluzioni per n fissato, e cercare di essere coerenti sui vari n in modo da aprire ogni via ad una decomposizione ricorsiva, al chiamare in causa le risposte per n più piccoli in seno alla risposta per ogni n dato 


## Esercizio che consiglio
  Scrivere il codice prima per la versione di counting, poi per la versione di listing (partendo dal codice scritto per la versione di counting come prima approssimazione per la struttura del codice per il listing, ridotta all'osso, e da rivestire).

  In realtà è poi interessante anche scrivere un codice iterativo piuttosto che non ricorsivo per il listing. Avrà sia il vantaggio dell'efficienza (soprattutto non necessita della memoria dello stack) e, se impari a scriverlo, è poi anche più semplice.

  Puoi poi provare anche a scrivere codici per le funzioni `next` e `prev`, che data una soluzione per un certo n, restituiscono la soluzione successiva e precedente per lo stesso n, secondo il criterio definito dalla tua decomposizione ricorsiva della struttura del problema.

  Sempre con riferimento allo stesso ordinamento, prova a scrivere codice per il ranking e l'unranking delle possibili piastrellature (anche qui, puoi sperimentare sia la scrittura di un codice iterativo che di un codice ricorsivo e cercare di apprezzare i vantaggi/svantaggi in termini di efficienza e di semplicità)
