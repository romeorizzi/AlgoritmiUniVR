= 2024-03-19: uso di rtal e problema accensione
#text(style:"italic", size:11pt, [Si comincia a comporre il presente documento contestualmente e collaborativamente all'URL:\
#h(6mm) `https://etherpad.wikimedia.org/p/Algoritmi2024-03-19`\
Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

Provate ad affrontare il problema accensione.\
Dove lo trovate?\
```bash
> rtal -s wss://ta.di.univr.it/algo  list
```

Se compare nella lista potete scaricarvi l'archivio dei suoi materiali annessi e decomprimerlo con:
```bash
> rtal -s wss://ta.di.univr.it/algo get accensione
> tar xvf accensione.tar
```

1. leggete il testo (file testo.pdf nell'archivio accensione testè decompresso)
2. prendete contezza della commessa del problema e del protocollo di comunicazione tra quello che sarà il vostro bot risolutore ed rtal (potete anche lanciare il servizio di valutazione senza connettere un vostro eseguibile, interagendo direttamente voi col servizio da tastiera)
3. provate a trovare delle soluzioni al problema nel vostro iperuranio
4. datene un'implementazione in codice
5. verificate la correttezza/qualità delle vostre soluzioni sottoponendole as servizio per una valutazione e feedback immediato:
```bash
> rtal -swss://ta.di.univr.it/algo connect accensione --my_bot_for_accensione
```
6. se scoprite che la vostra soluzione fà solo parte dei punti perchè non abbastanza efficiente (ad esempio, in questo caso, se il suo tempo di computazione è quadrico) provate a individuare delle soluzioni più efficienti asintoticamente (ad esempio, in questo caso, vi serve una soluzione O(n log n) sulla maggior parte delle istanze e per risolverle tutte converrà contenere anche l'uso della memoria. 

== Aspetti focali del problema

Assumendo che lo stato acceso/spento (1/0) dei computer sia inizialmente quello codificato dalla riga
```
   0 1 0 1 0 0
```
ossia che la configurazione iniziale dei computer e dei pulsanti sia la seguente:

#figure(
  image("figs/conf_iniziale.png", width: 60%),
  caption: [
    Configurazione iniziale dei computer e dei pulsanti.
  ],
)

allora potremmo portarci allo stato in cui tutti i computer sono accesi pigiando prima il Pulsante 2, poi il Pulsante 5, e infine il Pulsante 6. Con queste azioni attraverseremo le seguenti configurazioni.

#figure(
  image("figs/mosse.png", width: 80%),
  caption: [
    Configurazioni attraversate per accendere tutti i computer del laboratorio alpha.
  ],
)




== Input

Si legga l'input da `stdin`.
La prima riga contiene $T$, il numero di testcase (istanze) da risolvere. Seguono $T$ istanze del problema, dove ogni istanza presenta un diverso stato iniziale per i computer dell'aula alpha. Ogni istanza è descritta in due righe, dove la prima riga contiene il numero $N$ di computer presenti quel giorno, e la seconda riga specifica quali computer siano inizialmente accesi (1) oppure spenti (0). Le $N$ cifre contenute in questa seconda ed ultima riga sono separate da spazi.

== Output

Per ciascuna istanza, prima di leggere l'istanza successiva, scrivi su `stdout` il tuo output così strutturato:

- la prima riga contiene il numero di diverse configurazioni sui pulsanti con le quali tutti gli $N$ computer siano accesi, e raggiungibili pigiando i pulsanti in ordine strettamente crescente.

- la riga seguente codifica una configurazione dei pulsanti, ossia contiene $N$ numeri interi nell'intervallo $[0, 1]$ separati da spazio con l'$i$-esimo di questi numeri a specificare se Pulsante $i$ è pigiato (1) nella soluzione oppure no $0$. Se nella riga precedente si è stampato uno $0$, si stampino $N$ zeri separati da spazio. Altrimenti si stampi la codifica per una configurazione dei pulsanti con la quale tutti gli $N$ computer siano accesi quando raggiunta pigiando i pulsanti in ordine strettamente crescente. 

Nella descrizione dei subtask è specificato quanti punti si acquisiscono su ciascuna istanza di quel subtask, vuoi per la correttezza del valore riportato nella prima riga, vuoi per la correttezza della configurazione finale dei pulsanti.

== Esempio di Input/Output
Al file example.in.txt corrisponde il file example.out.txt

*Spiegazione:* la prima istanza è l'esempio utilizzato già sopra nel testo. Nella seconda istanza tutti i computer sono inizialmente spenti ed è possibile verificare che l'unica configurazione dei pulsanti con cui tutti i computer sono accesi è quella in cui il Pulsante 3 è l'unico a non essere pressato (posizione di OFF). Nella terza istanza tutti i computer sono inizialmente accesi e non serve fare nulla.

*Nota bene:* Secondo il protocollo rtal proposto da questo problema non dovete scrivere null'altro su stdout e non trovate null'altro in stdin. Vi è concesso fare quello che volete su stderr (logging, monitoring, e scatola nera).
