# Incontro 2025-03-20 (aula T.0.4)

## problema minato

* competenza chiave: programmazione dinamica
* competenza ausiliaria: pensiero ricorsivo

* tecnica algoritmica: programmazione dinamica
* tecnica algoritmica alternativa: ricorsione con memoizzazione

## Come si poteva approcciare il problema affinchè sopraggiungesse l'intuizione della strategia ottima
  analizzando casi particolari del problema, come ad esempio:
  1. ragionare su un'istanza specifica (noi abbiamo lavorato su una specifica matrice booleana 5x6)
  2. pur continuando a riferirci a quella specifica matrice (come scritta sulla pietra a riferimento per l'intero sciame di fatine ricorsine, non vorrei infatti passarmi l'intera descrizione dell'istanza ad ogni ricorsione perchè le possibili chiamate sarebbero allora in numero esponenziale) ci siamo cercati di auto-porre delle domande comunque più piccole di quella originariamente posta dal problema
  3. ad esempio, invece di limitarci ad affrontare la domanda originale:
   
    * quanti sono i percorsi dalla cella (0,0) alla cella (m-1,n-1) ?
  
    ci siamo chiesti:

    * quanti sono quelli da (?,?) a (m-1,n-1) ?
  
    ma sempre con riferimento alla matrice originaria scritta sulla pietra (tenuta come variabile globale, in questo modo a fatina bastava passare un numero limitato di informazioni)

  4. questa famiglia di (sotto)problemi/domande che ci siamo auto-inventati noi aveva le seguenti caratteristiche appealing:
   
    * aveva un numero poi solo polinomiale di domande (premessa alla ricorsione con memoizzazione e alla programmazione dinamica)
    * la domanda originale è una delle domande nella famiglia (non sempre deve essere così, in generale ci basta che sia facile da evadere una volta che si conoscano le risposte ad ogni domanda nella famiglia)
    * conteneva delle domande così piccine da essere ovvie (e, per altro, in un certo senso, la domanda originale era la più grossa di tutte)
    * cadevano tutte per effetto domino
Si noti che all'invenzione ed esplorazione della famiglia di domande si può giungere in modo anche naturale esplorando il problema, eventualmente ragionando anche con le mani (in qualche modo, per poterlo risolvere, il problema andrà pur toccato e palpato, perchè la soluzione è lui che la conosce, non possiamo imporgliela noi). 
  
    
## Ulteriori lezioni

  1. il concetto di sentinella ci ha fatto aggiungere una riga ed una colonna per rendere più uniforme e leggero il meccanismo di propagazione di caduta dei birilli (passo induttivo) ed anche per semplificare la regola per il computo sui casi base.
  2. abbiamo notato come tenere fisso lo sguardo alla complessità asintotica più che non alle costanti additive o moltiplicative rimanga una risorsa in ogni fase della gestione del problema (anche dopo aver visto la famiglia, supporta l'introduzione delle sentinelle, e poi ci ha supportati anche in scelte sull'approccio alla codifica)
  3. non c'è un unico modo di fare le cose, e non c'è limite al meglio: ad esempio, ci siamo posti la domanda di come ridurre l'utilizzo di memoria interna da quadratico a lineare, ossia a produrre una soluzione efficace entro una cornice di streaming (più stringente/restrittiva). Fare questo ci ha costretti a reinventarci una seconda famiglia di problemi, per altro assai simmetrica alla prima:
     quanti sono i percorsi da (0,0) a (?,?), piuttosto che non da (?,?) a (m-1,n-1)
  4. prendersi il giusto tempo per pensare anche prima (e durante) la fase finale, quella della codifica, verifica e debug. Procedere in modo organizzato e disciplinato può fare una grande differenza, sempre che non si cada nell'errore di credere che si possa fare tutto abbandonandosi a degli automatismi e teorie scritte una volta per tutte
   
  >Nota: noi abbiamo lavorato su una stessa specifica matrice 5x6, dalla definizione del problema, all'intuizione ed affinamento della soluzione, al progetto della codifica, fino al debug

## Esercizio che consiglio
  Il problema triangolo fu assegnato ad una delle prime iOi, poi anni dopo lo riproponemmo alle territoriali solo con un nuovo nome (Discesa massima): [https://training.olinfo.it/task/discesa](https://training.olinfo.it/task/discesa)

  Da questo si può intendere come attraverso le gare si sia riusciti a promuovere in modo anche ampio una cultura del Computational Thinking.
  I problemi sono cibo.
  