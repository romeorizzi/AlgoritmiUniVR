# Incontro 2025-03-14 (laboratorio alpha)

## percorso di introduzione alla programmazione dinamica partendo dall'approccio di ricorsione pura e passando per la ricorsione con memoizzazione

Con riferimento al problema `Borse di studio` ([https://training.olinfo.it/task/oii_borse](https://training.olinfo.it/task/oii_borse)) ampiamente trattato la volta scorsa, ci siamo posti la domanda se non fosse possibile limitarsi a stampare il solo numero delle soluzioni (piuttosto che listarle tutte una ad una) ma in un tempo ora polinomiale nel valore dell'input $b=$`numero di dobloni da distribuire`.

Abbiamo osservato come l'implementazione naturale del template ricorsivo di scomposizione del problema vista la vota scorsa conduceva ad un algoritmo esponenziale.

Abbiamo indagato le cause del problema (anche se le diverse domande erano solo in numero polinomiale, le singole domande, specie quelle per i casi piccoli, venivano poste un numero esagerato di volte).

La comprensione del problema ci ha condotti ad un semplice espediente per risolverlo:
> *ricorsione con memoizzazione:* tenere memoria delle risposte già precedentemente ottenute e restituite da altre chiamate ricorsive e, quando chiamati su quella stessa domanda, ritornare immediatamente la risposta per come memorizzata prima di filiare come i conigli.

Abbiamo analizzato sia empiricamente che concettualmente quanto fosse efficace questa tecnica.

Abbiamo poi rovesciato il calzino per ottenere una soluzione iterativa (e bottom-up, pushed) piuttosto che ricorsiva (e top-down, pulled) basata sul seguente approccio:
> *approccio PD:* riempire direttamente, in buon ordine e pilotati da semplici cicli for, la matrice delle risposte memorizzate (comunque avvalendosi della stessa formula ricorsiva).

Impiegando questo approccio abbiamo ottenuto il nostro primo esempio di
> *programmazione dinamica:* quando devi rispondere ad una domanda, progetta una famiglia di domande (in numero però al più polinomiale) che contenga la domanda in questione ma cadano poi tutte facili come i birilli per effetto domino partendo da casi base/elementari. Ovviamente la singola domanda di interesse è bene sia una delle domande della famiglia, o quantomeno sia ad esse collegata in modo che sia poi possibile evaderla una volta che le risposte a queste siano tutte note.


>Note: in un linguaggio moderno come `python` l'impiego dei decorator offre un modo molto rapido per aggiungere la memoizzazione ad una procedura di risocrione pura (ma ovviamente è necessario che essa si presti, ossia che il numero di problemi diversi effettivamente chiamati sia ragionevolmente contenute; la competenza oggetto di questa lezione non è quindi cosa da cui si possa quindi prescindere). 

## Esercizio che consiglio
  Cercate dalle piattaforme o collection di problemi che preferire vari problemi che siano taggati richiedere la tecnica della programmazione dinamica (o direttamente listati/proposti sotto tale voce), e vedete se riuscite ad individuare come risolverli. Partite da quelli più semplici e, seguendo anche la vostra curiosità e gusto personali, regolatevi in modo da bilanciare la difficoltà per introdurvi a nuovi trucchi, tecniche, e competenze in modo graduale.
  Condividete e discutiamo anche in classe problemi che non vi vengono o che comunque reputate interessanti e meritevoli di rivedere insieme.
  
>Hint: ecco un espediente efficace di automiglioramento (come anche consigliata dal tuo oculista): se siete già bravi a vedere la soluzione PD, sforzatevi di cucinare anche una ricorsione con memoizzazione (almeno su un piano concettuale, come organizzarla). Se invece ti è ancora difficile vedere direttamente una soluzione di PD, imposta ed affronta il percorso più graduale che abbiamo seguito in questa lezione: parti da una prima soluzione ricorsiva anche inefficiente, vedi se puoi darle efficienza riducendo la quantità di informazione che deve essere passata ad ogni chiamata ricorsiva, produci uno speed-up esponenziale tramite la memoizzazione, e infine chiediti come puoi ribaltare il calzino e vedi se ti riesce ed ha senso visualizzarsi una famiglia di sottoproblemi che cadano come i birilli. 