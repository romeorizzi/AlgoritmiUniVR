#  ⚙ Strumenti di lavoro, e la piattaforma `rtal`

Cerchiamo di chiarire da subito il giusto approccio al corso, come necessario quantomeno per superare la sua parte pratica.

## 🎯 metti i problemi al centro

Inutile girarci intorno: la via maestra è affrontare una nutrita collezione di problemi, possibilmente di buona qualità, che vertano sulle competenze trattate ed enfatizzate nel corso, e comparabili come difficoltà a quelli che dovrai affrontare all'esame.

## 🚀 ampia offerta di collezioni di problemi pertinenti

Nella tua preparazione può essere una buona idea avvalerti di problemi presi a tuo criterio da piattaforme di propblemi di altre parti, ce ne sono diverse con problemi interessanti ed altre caratteristiche (materiali, organizzazione, comunità di supporto) che potresti gradire. 
Confermo adatti i problemi al sito per gli [allenamenti alle olimpiadi di informatica italiane (Oii)](https://training.olinfo.it/). Quelli per la fase territoriale sono della difficoltà giusta (inoltre alcuni di loro vengono svolti compitamente nel [Guida alle selezioni territoriali OII (Bugatti)](https://training.olinfo.it/bugatti.pdf)), ma quando vedi che li sai affrontare bene dai un'occhiata anche a qualche problema della fase nazionale. (Se invece sei digiuno e parti da zero considera il percorso [AlgoBadge](https://training.olinfo.it/algobadge) pensato per facilitare l'accesso alla fase territoriale.)
In realtà di piattaforme valide ce ne sono molte, la cosa importante è che ne scegli almeno una per provare ad affrontare autonomamente qualche problema e se incontri delle difficoltà con qualcuno di essi puoi proporlo alla classe (anche attraverso il Gruppo Telegram, così possiamo poi vederlo insieme a lezione dopo aver provato tutti ad affrontarlo).
Un pò tutte queste piattaforme consentono di filtrare i problemi per argomento/tecnica o per evento, o di ordinarli per difficoltà (che viene comunque indicata, ovviamente secondo una qualche metrica solo indicativa).
Nel caso del sito [Oii](https://training.olinfo.it/) le max 5 stelle (o libri) indicano la difficoltà. Per poter sottomettere tue soluzioni e riceve feedback o validazione devi tipicamente registrarti (serve principalmente per fornire una classifica a stimolo dei più agguerriti).

Altre piattaforme/collection di problemi che ci sentiamo di consigliare sia per qualità che per pertinenza sono [CSES Problemset](https://cses.fi/problemset/), [Codeforces Problemset](https://codeforces.com/problemset) e [Leetcode Problemset](https://leetcode.com/problemset). Per il primo di questi tre esiste per altro un [testo gratuito (PDF)] con spiegazioni dettagliate, soluzioni, e riferimento alle strategie generali.

## ⚙ la nostra piattaforma (`rtal`)

Nonostante questa abbondanza di splendide proposte di cui consiglio di avvalersi (quantomeno date una curiosata), per le nostre esercitazioni, homeworks, e per l'esame, noi utilizzaremo un sistema nostro, per quanto un [progetto open source]() cui chi interessato potrà anche contribuire.
Tale sistema si basa su una coppia client/server (`rtal`/`rtald`) che vi consente di far girare le vostre soluzioni in locale, facendole dialogare coi servizi di validazione che girano invece sul server.

Il sistema `rtal` è pensato più per la didattica che per le gare, in quanto vi consente di monitorare cosa stia facendo il vostro programma (vi basta stampare su `stder` invece che su `stdout` per fare print debugging, mentre `stdout` e `stdin` restano riservati alla comunicazione col server) e ci sforziamo di darvi un feedback puntuale non appena il vostro programma fornisca risposte non valide (soluzioni non ammissibili, o non ottime, o comunque non come dovrebbero essere sul piano logico - il server chiude invece subito la comunicazione senza aggiungere alcuna spiegazione non appena non rispettate il protocollo inteso per il particolare problema).     


---
# ⚙ 💻 Guida all'uso di `rtal`

Installati ora e comincia ad utilizzare da subito `rtal`. Ti servirà per le esercitazioni, gli homework, e gli appelli in laboratorio del corso.
 

  - [Come ottenere il client `rtal`](#come-ottenere-il-client-rtal)
  - [Come verificare che `rtal` è installato correttamente](#come-verificare-che-rtal-è-installato-correttamente-e-verificare-la-versione)
  - [L'help interno di `rtal`](#lhelp-interno-di-rtal)
  - [Autenticazione e login](#come-loggarmi-ad-un-server-in-caso-richieda-autenticazione)
  - [Lista dei problemi di un server](#come-vedere-la-lista-dei-problemi-di-una-collectionserver)
  - [Scarica il testo e i materiali pubblici di un problema](#come-scaricarmi-il-testo-e-gli-altri-materiali-pubblici-di-un-problema)
  - [Lista dei servizi attivi di un problema](#come-vedere-la-lista-dei-servizi-attivi-di-un-singolo-problema-e-relativi-argomenti)
  - [Sottometti una tua soluzione o utilizza altri servizi di un problema](#come-sottomettere-la-mia-soluzione-o-avvalermi-di-altri-servizi-disponibili-per-un-problema)

<a id="get_rtal"></a>
## Come ottenere il client `rtal`


Fino a quando non imposteremo le git actions per rendere direttamente accessibili gli eseguibili già compilati, la via più stabile è partire dai sorgenti. (Un'alternativa è farti passare il compilato da un compagno la cui macchina abbia la stessa architettura, ovvero lo stesso genere di sistema operativo e processore grossomodo della stessa casa e numero di bits).

Per **ottenere** i sorgenti di `rtal` clona la repo con un singolo comando dalla CLI:

```bash
git clone https://github.com/Guilucand/rtal-algo-client.git
```

Oppure scarica lo `.zip` (e decomprimilo):
```bash
wget https://github.com/Guilucand/rtal-algo-client/archive/refs/heads/main.zip
```
In alternativa, per scaricare la repo, pigia il tastone verde <img src="../strumenti/stuff/figs/Git_Code_Green_Button.png" width="100" title="" alt=""> labellato "[< > Code]" che trovi nella [pagina su GitHub](https://github.com/Guilucand/rtal-algo-client), in alto. 


Per **compilare** ti serve il compilatore `rust`. Lo puoi facilmente ottenere e configurare automaticamente affidandoti al servizio [`rustup.rs`](https://rustup.rs/) della comunità di Rust.

Una volta installato `rust`, prima della compilazione vera e propria ti consigliamo di lanciare:

```bash
rustup update
```
in modo da assicurarti che l'installazione di Rust sia aggiornata. 

**Compilazione:**
dalla root della repo coi sorgenti di `rtal` già clonata lancia:

```bash
cargo build
```

per ottenere la versione DEBUG del client `rtal`, quella che consigliamo ai problem-solver (ossia agli studenti) in quanto rilascia più informazioni a supporto.

L'eseguibile sarà pertanto prodotto nella sottocartella `/target/debug/`. Ti consigliamo di aggiungere tale percorso alla variabile di ambiente `PATH` in modo che ti sia agevole lanciare l'eseguibile `rtal` indipendentemente da dove ti trovi. 

Per maggiori informazioni sulle opzioni disponibili per la compilazione vai alla [pagina della repo](https://github.com/Guilucand/rtal-algo-client).

<a id="check_rtal"></a>
## Come verificare che `rtal` è installato correttamente

Verifica + controllo di versione:

```bash
rtal -V
```

oppure col comando di primo aiuto discusso next. 


<a id="rtal_help"></a>
## L'help interno di `rtal`

```bash
rtal help
```

Per maggiori dettagli su ogni subcommand (help,list,login,logout,get,connect):

```bash
rtal help connect
```

<a id="rtal_login"></a>
## Come loggarmi ad un server in caso richieda autenticazione

Per i server che richiedono autenticazione(`esame`,`homework`), è abilitata l'autenticazione tramite GIA, quindi prima di poter usare i subcommand `get` o `connect` devi autenticarti con:

```bash
rtal -s <URL-server> login
```

Ad esempio, all'esame lanci:

```bash
rtal -s wss://ta.di.univr.it/esame login
```
inserisci la tua matricola (nel formato VR??????) al prompt e ricopi l'URL che ti viene restituito nel browser dove poi inserire le tue credenziali GIA.

I server principali sono:

| scopo    |     URL del server          | login | allegare sorgenti | attivo |
| :---     | :---                            | ---   |      ---      |  --- | 
| esame    | `wss://ta.di.univr.it/esame`    |  ✅   |  ✅   | solo durante esame |
| homework | `wss://ta.di.univr.it/algo`     |  ✅   |  ✅   | da marzo a febbraio successivo |
| esercizi | `wss://ta.di.univr.it/training` |  ❌   |  ❌   | continuativamente |

In pratica, per effettuare una sottoposizione è richiesto loggarsi preventivamente al server e allegare i sorgenti della propria soluzione (se più file si alleghi un `.tar` del folder che li contiene) ad ogni sottoposizione tramite il servizio `connect`.


<a id="rtal_list"></a>
## Come vedere la lista dei problemi di una collection/server


```bash
rtal -s <URL-server> list
```


<a id="rtal_get"></a>
## Come scaricarmi il testo e gli altri materiali pubblici di un problema

```bash
rtal -s <URL-server> get <nome_problema>
```


<a id="rtal_list_on_problem"></a>
## Come vedere la lista dei servizi attivi di un problema

```bash
rtal -s <URL-server> list <nome_problema>
```

Con il flag di verbose `-v` è possibile visionare le *regexp* dei valori consentiti per i vari argomenti:

```bash
rtal -s <URL-server> list -v <nome_problema>
```

Per questa via, per problemi che non seguano un formato rigido e già conosciuto,  non è comunque possibile ottenere spiegazioni esplicite su quali siano le finalità dei vari servizi elencati e sul ruolo che giocano i loro argomenti. Tutto questo potrebbe infatti dipendere in modo molto libero dal problema specifico; TALight consente infatti molta libertà al problem-maker (il docente).

<a id="rtal_list_on_problem"></a>
 ## Come vedere la lista dei servizi attivi di un singolo problema, e relativi argomenti
Per ottenere questo genere di informazioni devi rivolgerti al servizio `synopsis` del problema di interesse, come segue:

```bash
rtal -s <URL-server> connect <nome_problema> synopsis -a service=<nome_servizio>
```

E' infatti il subcommand `connect`, trattato al prossimo ed ultimo punto, quello utilizzato per invocare i servizi offerti al problem-solver (lo studente) per un problema.

Ad esempio, per conoscere come puoi nel concreto usare il servizio `synopsis` di un problema specifico applicalo a sè stesso come segue:

```bash
rtal -s <URL-server> connect <nome_problema> synopsis -a service=synopsis
```

<a id="rtal_connect"></a>
## Come sottomettere la mia soluzione o avvalermi di altri servizi di un problema

Ci si avvale del subcommand `connect`, più ricco e complesso nell'utilizzo. Ci limitiamo pertanto agli usi principali, vai a [`IT_the-TALight-Problem-Solver-Tutorial1-internet-server.md`](IT_the-TALight-Problem-Solver-Tutorial1-internet-server.md) in questo stesso folder per ulteriori dettagli sia sull'installazione ed uso di `rtal` che sul subcommand `connect`.

L'uso tipico per sottomettere una tua soluzione all'esame oppure come homework (ossia quando vorrai che ti vengano riconosciuti gli eventuali punti totalizzati dalla tua sottoposizione) seguirà grossomodo il seguente formato:

```bash
rtal -s <URL-server> connect -f source=<PATH-TO-SOURCE-FILE> [-e] <nome_problema> [<ARGS>] -- <MY-EXECUTABLE-SOLUTION>
```

Dove:

- `<PATH-TO-SOURCE-FILE>` è il filename completo (relativo od assoluto) del file sorgente della tua soluzione (se i file sorgente sono più di uno allega il `.tar` di un folder che contenga i sorgenti)

- il flag opzionale `-e` può essere aggiunto per monitorare l'interazione tra la tua soluzione e il valutatore che gira sul server

- `<ARGS>` include eventuali argomenti specifici, tra questi quello più comunemente utilizzato è `size` che serve a limitare la sottoposizione a un solo prefisso dei subtask (per evitare rallentamenti del caso la tua soluzione non sia adatta ad affrontare le istanze più grandi).
  - `-a size=esempi_testo`
  - `-a size=small`

- `<MY-EXECUTABLE-SOLUTION>` è una qualsiasi scrittura che, ove immessa anche da sola al prompt della CLI, comporti l'avvio del solver da tè realizzato. Solo alcuni esempi:
  - `./a.out` per un compilato da `C/c++`, eventualmente seguito dagli argomenti che esso, per come lo hai progettato, prevede/consente
  - `./my_solution.py arg1 arg2 ...` se il tuo file `my_solution.py` col codice python ha i permessi di esecuzione e inizia con la riga di shebang
  - `python my_solution.py` o `python3 my_solution.py` per far eseguire il tuo script dall'interprete python effettivamente presente in locale.


> [!NOTE]
> Utile per debuggare come il tuo programma interagisce con il server è comprendere la differenza tra scrivere su `stdout` oppure su `stderr` ed eventualmente anche su file (non essere timido a fare esperimenti). Anche il flag `--echo` del subcommand `connect` può venire molto utile per individuare dove la tua soluzione non rispetti il protocollo di cmunicazione tra la tua soluzione e il validatore del server.

> [!TIP]
> Anche se è solo uno strumento, ti converrà prendere un minimo di dimestichezza nell'uso di `rtal`

> [!TIP]
> Nel caso degli homework, se non disponi di una macchina adeguata da dove svolgerli e sottometterli puoi avvalerti del servizio VirtualLab dell'ateneo (se da casa serve la VPN per fruire di questo servizio)

