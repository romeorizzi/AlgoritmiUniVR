#### Guida Utente - Problem Solver TUTORIAL 1:
# COME ACCEDERE DA UNA CLI AL SERVER TALIGHT IN INTERNET

Questo primo tutorial su come usare TALight presuppone che tu possa avviare il client `rtal` da una `bash` da Command Line Interpreter (CLI). Ecco due metodi con cui puoi eseguire quest'azione:

1. se hai almeno l'installazione parziale di TALight sulla tua macchina: vedere la sezione [Installazione TALight](https://github.com/romeorizzi/TALight/wiki/IT_TALight-Installation) per le istruzioni su come ottenere tale installazione.
2. se per qualche motivo non vuoi o non puoi installare nulla sulla tua macchina: vedere la sezione [TALight da Browser](https://github.com/romeorizzi/TALight/wiki/IT_TALight-from-the-Browser) in cui viene mostrato come ottenere l'accesso da browser con un ambiente CLI `bash` funzionante in cui è installato il client `rtal`.

In entrambi i casi, ora puoi utilizzare i problemi di TALight e accedere ai loro servizi con il ruolo di Problem Solver, purché questi siano distribuiti in Internet e resi disponibili.


## Alcuni comandi per provare le funzionalità disponibili

**Assumiamo che, in un modo o nell'altro ([TALight da browser](https://github.com/romeorizzi/TALight/wiki/IT_TALight-Browser-replit) o [Installazione TALight](https://github.com/romeorizzi/TALight/wiki/IT_TALight-Installation)), ora tu possieda il terminale ed un eseguibile `rtal` posizionati correttamente e funzionanti come spiegato nelle guide precedenti.**

L'approccio previsto all'interno di TALight è l'esplorazione libera, ma, solo per darti un aiuto iniziale, ecco alcuni esempi di comandi che è possibile eseguire per esplorare quali servizi sono offerti dalla raccolta di problemi ospitata su `wss://talight .tk/tutorial`.

Da qui, prova i seguenti comandi.

Per avere un aiuto generale sul comando `rtal` e i sui suoi sottocomandi:

```bash 
rtal -s wss://ta.di.univr.it/esame help
```

Dalla pagina di help visualizzata puoi imparare che l'opzione `--server`, o in breve `-s`, ti permette di specificare l'URL del server a cui il client `rtal` sta inviando la richiesta. Pertanto, la tua richiesta ha navigato attraverso Internet e la pagina di aiuto ti è stata fornita da `wss://ta.di.univr.it/esame`.

Per avere un aiuto più specifico su un sottocomando `rtal` esegui il comando:

```bash 
rtal -s wss://ta.di.univr.it/esame list
```

Pertanto, per vedere l'intero elenco di problemi attualmente disponibili nella nostra raccolta di tutorial come distribuito da `wss://ta.di.univr.it/esame`, è necessario utilizzare il sottocomando `list` del comando `rtal` senza imporre nessun filtro o parametro:

```bash 
rtal -s wss://ta.di.univr.it/esame list
```

Diverse raccolte di problemi possono offrire insiemi di problemi completamente diversi.
Pertanto, l'elenco restituito che contiene i problemi disponibili dipenderà dall'URL specificato dopo l'opzione `-s`. Questa opzione è spiegata quando si esegue `rtal --help`. Se ometti completamente questa opzione, il client `rtal` proverà ad inviare la tua richiesta a un demone `rtald` in esecuzione sul tuo pc in locale. Se nessun demone rtald è in esecuzione sul tuo computer locale, allora otterrai un errore di questo tipo:

```bash
 ERROR rtal > Cannot connect to ws://127.0.0.1:8080/
```

Supponiamo che tu abbia lanciato l'intero comando corretto come riportato sopra, o che tu abbia completamente omesso l'opzione `-s` dopo aver lanciato correttamente il demone `rtald` in locale usando l'opzione `-d` per chiedergli di risolvere i problemi del tutorial (come spiegato nella sezione [Tutorial 2 per Problem Solver - con server locale da CLI](https://github.com/romeorizzi/TALight/wiki/IT_the-TALight-Problem-Solver-Tutorial2-local-server).

In questo caso, l'elenco restituito dei problemi dovrebbe contenere, tra i vari, il problema `sum` che andremo ad esplorare in seguito come esempio.
Con il comando:

```bash 
rtal -s wss://ta.di.univr.it/esame get sum
```

invoca il sottocomando `get` per scaricare il file `.tar`: `sum.tar`. Questo file è l'archivio della cartella pubblica del problema `sum` presente sul server `wss://ta.di.univr.it`. Una volta scompattata questa cartella, al suo interno si può trovare la descrizione del problema `sum` e tutto il materiale relativo ad esso (spiegazioni, video, link, ...) che il problem maker ha raccolto e ha deciso di rendere pubblico (ovvero accessibile a te grazie a questo semplice meccanismo). La cartella `public` può essere un ricco albero di directory, e l'intero albero, insieme a qualsiasi materiale che è collegato simbolicamente all'interno dell'albero (anche se il materiale è posizionato all'esterno) finirà poi nell'archivio scaricato dal problem solver.

<details><summary><b>Come decomprimere un archivio</b></summary>  

Per decomprimere usare il comando:

<code>
tar -xvf sum.tar
```

Se l'archivio è zippato (puoi capirlo in quanto l'estensione sarà `.tgz` o `.tar.zip` invece di `.tar`) puoi eseguire il comando:

<code> 
tar -xvzf sum.tgz
```

Su Windows puoi anche usare alcune utility come 7-Zip o WinZip.

</details>

Il sottocomando list offre anche una funzione di ricerca.
Digitando

```bash 
rtal -s wss://ta.di.univr.it/esame list sum
```

oppure 

```bash 
rtal -s wss://ta.di.univr.it/esame list um
```

ti verrà restituito un elenco contenente solo il problema `sum`, in quanto attualmente è l'unico problema il cui nome contiene la sottostringa `um`.
Questa capacità di filtraggio supporta qualsiasi regular expression.
Ad esempio, con il comando

```bash 
rtal -s wss://ta.di.univr.it/esame list ^p[a-z]*$
```

ottieni l'elenco di tutti quei problemi presenti nella raccolta il cui nome contiene solo lettere minuscole e inizia con `p`. Nelle regular expression i caratteri `^` e `$` sono usati per imporre la corrispondenza di inizio e fine della stringa candidata.

## Esplorare i servizi disponibili per un problema

Usando il flag `-v` del sottocomando `list` come segue:

```bash 
rtal -s wss://ta.di.univr.it/esame list -v
```

oppure

```bash 
rtal -s wss://ta.di.univr.it/esame list -v ^p[a-z]*$
```

si può ottenere un output più dettagliato dove, per ogni problema nella raccolta (il cui nome contiene solo lettere minuscole e inizia con `p`, come nel secondo caso), tutti i servizi disponibili per quel problema sono elencati in un sottoelenco.
Solitamente sei interessato ad esplorare i servizi per il solo problema su cui stai lavorando. Il modo migliore per condurre questo tipo di esplorazione è tramite il servizio di `synopsis` che verrà presentato più avanti. Ad ogni modo, per ora, può essere utilizzato anche il meccanismo di filtraggio:

Digitando:

```bash 
rtal -s wss://ta.di.univr.it/esame list sum
```

oppure, nello specifico:

```bash 
rtal -s wss://ta.di.univr.it/esame list ^sum$
```
otterrai il seguente output:

```
- sum
  * free_sum
    # lang [it]
    # num_questions [10]
    # numbers [twodigits]
    # obj [any]
  * help
    # lang [it]
    # page [help]
  * sum_and_difference
    # lang [it]
    # num_questions [10]
    # numbers [onedigit]
  * sum_and_product
    # lang [it]
    # num_questions [10]
    # numbers [onedigit]
  * synopsis
    # lang [it]
    # service [synopsis]
```

In questo modo puoi facilmente comprendere che, al momento, sono disponibili 5 servizi per il problema `sum`:
`free_sum`, `sum_and_difference`, `sum_and_product`, `help` e `synopsis`.
Per ognuno di questi servizi si ottiene anche la sottolista dei relativi argomenti. Un argomento può avere un valore predefinito (riportato tra parentesi quadre), nel caso in cui l'argomento risulti facoltativo. In caso contrario, l'argomento è obbligatorio. Quando un argomento è facoltativo e non si specifica un valore per esso, viene usato il suo valore di default.

Ma come si conosce l'insieme dei possibili valori per un dato parametro?
Per ottenere in dettaglio tutte le possibili opzioni per gli argomenti, usa:

```bash 
rtal -s wss://ta.di.univr.it/esame list sum -v
```

Con questo comando dovresti ottenere un elenco con la stessa lunghezza e con gli stessi elementi di quello visualizzato sopra, ma la descrizione degli elementi risulta maggiormente estesa e dettagliata.
Ad esempio, guardando solo alle voci relative al servizio `free_sum`:

```bash 
  * free_sum
    # lang [it] ^(hardcoded|en|it)$
    # num_questions [10] ^([1-9]|[1-2][0-9]|30)$
    # numbers [twodigits] ^(onedigit|twodigits|big)$
    # obj [any] ^(any|max_product)$
```
Da notare come vengono specificati i possibili valori di un argomento mediante un'espressione regolare.
Pertanto, i 3 possibili valori per l'argomento `lang` sono `hardcoded`, `en` e `it`; mentre i 30 possibili valori per l'argomento `num_questions` sono gli interi nell'intervallo chiuso [1,30].
Facciamo riferimento alla pagina [regex syntax](https://docs.rs/regex/1.4.3/regex/#syntax) per avere maggiori informazioni riguardanti la sintassi delle espressioni regolari che abbiamo adottato (quelle standard per il linguaggio Rust).

Da questi output potresti dedurre che i tre servizi `sum`, `sum_and_difference` e `sum_and_product` hanno lo scopo di condurre un dialogo in cui a te (o ad un bot che agisce per tuo conto) verranno poste 10 domande (tutte le istanze di un problema definito dal servizio). Infatti, 10 è il valore predefinito per il parametro `num_questions`. Puoi specificare un valore diverso per questo parametro che può accettare solo numeri interi nell'intervallo $[1,30]$ come specificato dalla regexp `^([1-9]|[1-2][0-9]|30)$` come riportato sopra.

Combinando le informazioni specifiche del problema ottenute eseguendo `rtal list sum -v`, con le istruzioni di base di TALight ottenute con `rtal connect --help` potresti, per esempio, decidere di provare il servizio `free_sum` nel seguente modo:

```bash
rtal -s wss://ta.di.univr.it/esame connect sum free_sum
```

E anche provare a richiamarlo con altre combinazioni non standard per i suoi argomenti:
```bash
rtal -s wss://ta.di.univr.it/esame  connect -a num_questions=13 -a numbers=onedigit sum sum_and_product
```

Collegandoti ai servizi in questo modo diretto puoi godere di un'interazione diretta con il server attraverso il terminale. Questo può aiutarti a comprendere il servizio e il protocollo d'interazione.
Sperimenta attivamente i vari argomenti del servizio: sono pensati per aiutarti e talvolta hanno anche lo scopo di offrirti un'escalation su un problema che inizia in modo semplice, ma si avvicina alla tua curiosità e apertura mentale. Prova ad esempio:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a numbers=big sum free_sum
```

oppure

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a obj=max_product sum free_sum
```

### il servizio `synopsis` 

Tutti i problemi offrono un servizio `synopsis`. Questo servizio ha lo scopo di dare un aiuto e trasmettere informazioni sull'uso e sulla sintassi per qualsiasi servizio del problema. 
Per specificare il servizio, utilizzare l'argomento `service` come segue:

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum synopsis -a service=free_sum
```

In questa sintassi `synopsis` è considerato un servizio del problema `sum` ed è stato chiamato con il suo argomento `service` impostato su `free_sum`.
In questo modo l'utente ottiene tutte le informazioni pertinenti al servizio `free_sum` del problema `sum`. In particolare, l'utente ottiene un elenco di tutti gli argomenti del servizio `free_sum`. Il servizio `synopsis` è molto più informativo e di supporto rispetto al sottocomando `list` poiché fornisce anche il significato, uso previsto e vari esempi.

Per saperne di più sul servizio `synopsis` eseguilo in questo modo:

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum synopsis
```

Infatti, l'argomento predefinito per il servizio di synopsis è solitamente `synopsis` stesso.


### il servizio `help`

Il problema `sum` offre anche un servizio di `help` (aiuto)

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum -a page=sum_and_difference help
```

Questo ha lo scopo di esporre delle pagine principali su un determinato problema. Quello che è presente in queste pagine è meno vincolato e segue un formato meno rigido rispetto alle informazioni trasmesse dal servizio `synopsis`.
Tuttavia, attualmente lo abbiamo fatto solo per il problema della `somma` e dobbiamo ancora decidere se e come strutturare e/o organizzare questo ulteriore canale d'informazione.


## Servizi interattivi

Alcuni servizi interagiranno con il problem solver solo per ottenere tutti i dati di input di cui hanno bisogno. Altri servizi richiederanno livelli di interazione più elevati. Il protocollo di interazione viene progettato in piena libertà dal problem maker. I suoi dettagli o l'idea generale potrebbero essere stati descritti nella formulazione del problema, o potrebbero essere rivelati attraverso il servizio di synopsis o man mano che viene sperimentato il servizio stesso. Abbiamo già visto sopra alcuni esempi di servizi basati sull'interazione, come il servizio `free_sum` del problema `sum` che puoi invocare eseguendo:

```bash 
rtal -s wss://ta.di.univr.it/esame connect sum free_sum
```
È abbastanza intuitivo per gli umani comprendere la semplice struttura di questa interazione e il protocollo sottostante.

## Servizi interattivi e bot

Dopo aver capito la competenza che il problema sta cercando di affrontare e il protocollo per l'interazione con esso, puoi creare un bot che mostri quella competenza per conto tuo.

Il plug-in del bot segue questo semplice modello/meccanismo:

```bash
rtal <problem_collection> connect <problem> <service> -- <my_executable_bot>
```

dove si assume che il bot contenente la tua soluzione sia un comando eseguibile sul tuo computer. Inoltre, si presume che il tuo bot comunichi con il mondo esterno attraverso i flussi stdin e stdout (e stderr se vuoi eseguirne il debug).
(L'assunzione standard, ma non obbligatoria, è che si trovi anche sulla tua macchina e che l'abbia forgiato tu stesso.)

Ad esempio, se hai scritto il tuo bot in python (o ne prendi uno già fatto da questo repository, nella cartella `bots` per il problema di tuo interesse), allora un plug-in funzionante potrebbe essere il seguente:


```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- python ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py
```

Il flag `-e` ti consente di vedere l'interazione che si verifica tra il tuo bot e il server di servizio. Prova ad ometterlo per consentire alla chiamata di servizio di procedere senza mostrare particolari informazioni riguardanti la comunicazione.

In realtà, se sei su Linux/Mac e allo script python `free_sum_mysimplebot.py` viene dato il permesso di esecuzione, come nel caso del repository che hai clonato (come già accennato, è meglio la clonazione rispetto al download, ma puoi anche assegnare questi permessi con il comando `chmod` della shell), allora potresti scrivere semplicemente:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py
```

<details><summary><b>Perché la seconda scrittura è migliore e perché non puoi usarla su Windows</b></summary>

Questo perché solo i file `.exe` possono essere eseguiti su Windows, gli script no (anche se la prima riga è la shebang corretta).

Ovviamente puoi anche usare la prima e più lunga forma del comando su Linux e Mac, ma poi è il caso che la versione di python impostata come predefinita nel tuo ambiente attuale sia quella corretta per eseguire il bot.

</details>


Prova alcune altre interazioni, come:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e -a numbers=big sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mysimplebot.py
```

oppure:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a numbers=big -a obj=max_product sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mymaxproductbot.py
```

In tutti questi esempi il bot era stato scritto in python, ma potrebbe essere un qualsiasi binario con i permessi di esecuzione sul tuo sistema locale. Per esempio:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- free_sum_mysimplebot
```

Dove l'eseguibile binario `free_sum_mysimplebot`, che pensavamo si trovasse nella directory corrente, poteva essere ottenuto compilando un codice sorgente scritto in qualsiasi linguaggio di programmazione di tua scelta come ad esempio C, c++, Rust o Java.

### Per riassumere

Con i servizi basati sull'interazione, il problem solver può creare un bot che condurrà quell'interazione per conto suo. Alcuni servizi basati sull'interazione sono pensati solo per i bot.

Ti consigliamo di provare prima un semplice servizio di esempio come:

```bash 
rtal -s wss://ta.di.univr.it/esame connect sum free_sum
```

Dopo aver sperimentato l'interazione offerta da un servizio come `free_sum`, connetti ad esso un bot che hai in locale.

```bash 
./rtal -s wss://ta.di.univr.it/esame connect -e sum free_sum -- python ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mysimplebot.py
```

In questo modo il bot condurrà quella stessa interazione per conto tuo ed esprimerà la tua competenza sul problema. Grazie al flag `-e` puoi osservare il dialogo tra il tuo bot in locale e il server del servizio presente in cloud. Qui, per questo tutorial, potresti trovare il bot `free_sum_mysimplebot.py` tra i file di questo repository, ma l'idea è che il problem solver organizzi e rifletta sulle competenze coinvolte mentre prepara i propri bot. Tale servizio ha lo scopo di offrire un modo semplice per testare il bot e ottenere un feedback completo e informativo sul suo comportamento. Questo aiuterà a sistemare i bug di programmazione in un primo momento, ma ha come scopo principale quello di valutare le competenze stesse e di fornire ulteriore consapevolezza e altre sfide. Infatti, il comportamento della maggior parte dei servizi destinati ai bot può essere regolato attraverso argomenti che consentono al problem solver di stabilire sia i propri obiettivi che il livello di feedback che desidera dal server. L'idea è di lasciare che sia il problem solver a decidere autonomamente quando ha bisogno di maggiore aiuto o quando non vuole spoilerare il problema.

Tuttavia, non tutti i servizi TALight sono pensati per i bot. Infatti, TALight è pensato per essere utilizzato anche dai problem solver che sanno già come programmare; TALight può offrire un ambiente di supporto e divertente anche per loro. Anche i problemi che affrontano esplicitamente le competenze di programmazione possono avere una ricca serie di servizi pensati solo per l'esplorazione umana.

Un bot è un qualsiasi sistema automatico impostato dal problem solver. Può essere scritto in qualsiasi linguaggio e quindi attivare qualsiasi altro componente software o qualsiasi libreria. Il problem solver ha il pieno controllo su di questi purché venga eseguito sulla sua macchina locale.

Supponiamo che il bot `sum_mysimplebot.py` venga eseguito con successo, ottenendo un feedback positivo.
Se lo esegui come segue:

```bash 
rtal -s wss://ta.di.univr.it/esame connect -e -aobj=max_product sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py 
```

allora il feedback che ottieni dovrebbe cambiare drasticamente poiché ciò che è richiesto dal bot è diverso. Ma puoi provare `sum_mymaxproductbot.py` nella stessa directory (di questo repository che hai clonato in locale).

Quando riesci a insegnare una competenza (come quando riesci ad istruire un bot a fare qualcosa) allora ti viene confermato di aver acquisito quella competenza nel profondo. Pertanto, la presentazione di un bot offre un mezzo per valutare la competenza. Quando il servizio ti fornisce una valutazione delle tue soluzioni, convalida i tuoi progressi e può suggerirti nuovi obiettivi e sfide.

