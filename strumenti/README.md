# 🎯 ⚙ Strumenti per la tua preparazione

Inutile girarci intorno: il principale strumento è affrontare una nutrita collezione di problemi, possibilmente di buona qualità, che vertano sulle competenze trattate ed enfatizzate nel corso, e comparabili come difficoltà a quelli che dovrai affrontare all'esame.

Confermo adatti i problemi al sito per gli [allenamenti alle olimpiadi di informatica italiane (Oii)](https://training.olinfo.it/). Quelli per la fase territoriale sono della difficoltà giusta (inoltre alcuni di loro vengono svolti compitamente nel [Guida alle selezioni territoriali OII (Bugatti)](https://training.olinfo.it/bugatti.pdf)), ma quando vedi che li sai affrontare bene dai un'occhiata anche a qualche problema della fase nazionale. (Se invece sei digiuno e parti da zero considera il percorso [AlgoBadge](https://training.olinfo.it/algobadge) pensato per facilitare l'accesso alla fase territoriale.)
In realtà di piattaforme valide ce ne sono molte, la cosa importante è che ne scegli almeno una per provare ad affrontare autonomamente qualche problema e se incontri delle difficoltà con qualcuno di essi puoi proporlo alla classe (anche attraverso il Gruppo Telegram, così possiamo poi vederlo insieme a lezione dopo aver provato tutti ad affrontarlo).
Un pò tutte queste piattaforme consentono di filtrare i problemi per argomento/tecnica o per evento, o di ordinarli per difficoltà (che viene comunque indicata, ovviamente secondo una qualche metrica solo indicativa).
Nel caso del sito [Oii](https://training.olinfo.it/) le max 5 stelle (o libri) indicano la difficoltà. Per poter sottomettere tue soluzioni e riceve feedback o validazione devi tipicamente registrarti (serve principalmente per fornire una classifica a stimolo dei più agguerriti).

Altre piattaforme/collection di problemi che ci sentiamo di consigliare sia per qualità che per pertinenza sono [CSES Problemset](https://cses.fi/problemset/), [Codeforces Problemset](https://codeforces.com/problemset) e [Leetcode Problemset](https://leetcode.com/problemset). Per il primo di questi tre esiste per altro un [testo gratuito (PDF)] con spiegazioni dettagliate, soluzioni, e riferimento alle strategie generali.

Nonostante questa abbondanza di splendide proposte di cui consiglio di avvalersi (quantomeno date una curiosata), per le nostre esercitazioni, homeworks, e per l'esame, noi utilizzaremo un sistema nostro, per quanto un [progetto open source]() cui chi interessato potrà anche contribuire.
Tale sistema si basa su una coppia client/server (`rtal`/`rtald`) che vi consente di far girare le vostre soluzioni in locale, facendole dialogare coi servizi di validazione che girano invece sul server.
Il sistema è pensato più per la didattica che per le gare, in quanto vi consente di monitorare cosa stia facendo il vostro programma (vi basta stampare su `stder` invece che su `stdout` per fare print debugging, mentre `stdout` e `stdin` restano riservati alla comunicazione col server) e ci sforziamo di darvi un feedback puntuale non appena il vostro programma fornisca risposte non valide (soluzioni non ammissibili, o non ottime, o comunque non come dovrebbero essere sul piano logico - il server chiude invece subito la comunicazione senza aggiungere alcuna spiegazione non appena non rispettate il protocollo inteso per il particolare problema).     

---

1. [Come ottenere il client `rtal`](get_rtal)
2. [Come verificare che `rtal` è installato correttamente, e verificare la versione](check_rtal)
3. [L'help interno di `rtal`](rtal_help)
4. [Come loggarmi ad un server in caso richieda autenticazione](rtal_login)
5. [Come vedere la lista dei problemi offerti di una collection/server](rtal_list)
6. [Come scaricarmi il testo e gli altri materiali pubblici di un problema](rtal_get)
7. [Come vedere la lista dei servizi attivi di un singolo problema, e relativi argomenti](rtal_list_on_problem)
8. [Ottenere le informazioni specifiche a un problema, ai suoi servizi e relativi argomenti](synopsis)
9. [Come sottomettere la mia soluzione o avvalermi di altri servizi disponibili per un problema](rtal_connect)

[get_rtal]: ## Come ottenere il client `rtal`

Dal repo di rtal puoi forse scaricarti l'eseguibile già compilato per la tua architettura. In caso contrario clona il repo in locale e, dopo esserti installato Rust, potrai compilarlo.

[check_rtal]: ## Come verificare che `rtal` è installato correttamente, e verificare la versione

```bash
rtal -V
```

o puoi anche provare direttamente a chiedere aiuto


[rtal_help]: ## L'help interno di `rtal`

```bash
rtal help
```

Oltre a questa schermata di riepilogo dei subcommands risulta possibile chiedere maggiori informazioni su ogni singolo subcommand (help,list,login,logout,get,connect) ad esempio con:

```bash
rtal connect
```

[rtal_login]: ## Come loggarmi ad un server in caso richieda autenticazione

I server per esame o per homework richiedono autenticazione, che dal lato docente può essere gestita senza particolari difficoltà avvalendosi del meccanismo degli argomenti per il subcommand `connect`.
Per i nostri corsi in Verona abbiamo integrato l'autenticazione GIA, e quindi prima di poter accedere a subcommands quali `get` e `connect` dovrai lanciare:

```bash
rtal -s <URL-server> login
```

Ad esempio, all'esame dovrai come prima cosa lanciare:

```bash
rtal -s wss://ta.di.univr.it/esame login
```

I server di vostro interesse sono:

| scopo    |     URL del server            | login | allegare sorgenti | attivo |
|:---------|:------------------------------|-------|-------------------|
| esame    | wss://ta.di.univr.it/esame    |  ✅   |  ✅   | solo durante esame |
| homework | wss://ta.di.univr.it/algo     |  ✅   |  ✅   | da marzo a febbraio successivo |
| esercizi | wss://ta.di.univr.it/training |  ❌   |  ❌   | continuativamente |

In pratica, per effettuare una sottoposizione è richiesto loggarsi preventivamente al server e allegare i sorgenti della propria soluzione (se più file si alleghi un `.tar` del folder che li contiene) ad ogni sottoposizione tramite il servizio `connect`.


[rtal_list]: ## Come vedere la lista dei problemi di una collection/server

Per visionare la lista dei problemi attivi:

```bash
rtal -s <URL-server> list
```


[rtal_get]: ## Come scaricarmi il testo e gli altri materiali pubblici di un problema

```bash
rtal -s <URL-server> get <nome_problema>
```


[rtal_list_on_problem]: ## Come vedere la lista dei servizi attivi di un singolo problema, e relativi argomenti

```bash
rtal -s <URL-server> list <nome_problema>
```

E' inoltre possibile visionare le `regexp` che definiscono i valori consentiti per i vari argomenti utilizzando il comando col flag di verbose

```bash
rtal -s <URL-server> list -v <nome_problema>
```

Per questa via, per problemi che non seguano un formato rigido e già conosciuto,  non è comunque possibile ottenere spiegazioni esplicite su quali siano le finalità dei vari servizi elencati e sul ruolo che giocano i loro argomenti. Tutto questo potrebbe infatti dipendere in modo molto libero dal problema specifico; TALight consente infatti molta libertà al problem-maker (il docente).

[rtal_list_on_problem]: 
Per ottenere questo genere di informazioni devi rivolgerti al servizio `synopsis` del problema di interesse, come segue:

```bash
rtal -s <URL-server> connect <nome_problema> synopsis -a service=<nome_servizio>
```

E' infatti il subcommand `connect`, trattato al prossimo ed ultimo punto, quello utilizzato per invocare i servizi offerti al problem-solver (lo studente) per un problema.

Ad esempio, per conoscere come puoi nel concreto usare il servizio `synopsis` di un problema specifico applicalo a sè stesso come segue:

```bash
rtal -s <URL-server> connect <nome_problema> synopsis -a service=synopsis
```

[rtal_connect]: ## Come sottomettere la mia soluzione o avvalermi di altri servizi disponibili per un problema

Questo è il servizio più ricco e complesso. Ci limitiamo quì agli esempi di utilizzo principali, come di tuo interesse, rimandando al file `IT_the-TALight-Problem-Solver-Tutorial1-internet-server.md` in questo stesso folder per informazioni più dettagliate sull'installazione ed uso di `rtal` in generale e sul servizio `connect` in particolare.


> [!TIP]
> Anche se è solo uno strumento, ti converrà prendere un minimo di dimestichezza nell'uso di `rtal`

> [!NOTE]
> Utile per debuggare come il tuo programma interagisce con il server è comprendere la differenza tra scrivere su `stdout` oppure su `stderr` ed eventualmente anche su file (non essere timido a fare esperimenti). Anche il flag `--echo` del subcommand `connect` può venire molto utile per individuare dove la tua soluzione non rispetti il protocollo di cmunicazione tra la tua soluzione e il validatore del server.
