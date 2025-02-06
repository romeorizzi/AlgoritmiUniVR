== Flotta di aerei kamikaze in viaggio

Una flotta di aerei deve decidere quale target colpire.
In questo momento tutti gli aerei si trovano alla base, tutti col serbatoio pieno e pronti a partire. Gli aerei sono tutti uguali, a serbatoio pieno riescono a percorrere una singola unità di distanza ed il loro consumo è lineare nella distanza percorsa.
Per colpire un certo target ci basta che anche uno solo degli aerei lo raggiunga.

*Domanda~1:* Quale è la massima distanza dalla base di un target che possiamo colpire se la nostra flotta dispone di $n$ aerei?

Chiameremo $D(n)$ la risposta a tale domanda, cerchiamo di spiegare perchè sia funzione di $n$ ma lasceremo a tè di meglio comprenderla.

\ $D(1) = 1$: un singolo aereo riesce certamente ad attraversare una distanza di $D=1$ unità se viaggia diritto senza indugi. Non potrà mai portarsi ad una distanza maggiore di $1$ dalla base poichè ogni volta che lascia la base ha autonomia per allontanarsi di al più $1$ dalla base stessa non trovando alcun luogo dove rifornirsi al di fuori della base.

\ $D(2) = 3/2$: ecco come una flotta di $2$ aerei può raggiungere un punto a distanza $3/2$ dalla base:
entrambi gli aerei percorreranno un viaggio di sola andata su una semiretta che parte dalla base. Inizialmente i due aerei viaggiano insieme (la semiretta è la stessa) ma un aereo si ferma dopo aver percorso distanza 1/2. A quel punto entrambi gli aerei avranno il proprio serbatoio mezzo pieno. Uno dei due aerei decide che il suo viaggio termina a quel punto e consegna il suo mezzo serbatoio di carburante all'altro aereo, che da lì riesce a percorrere un ulteriore unità di distanza.

*Obiettivo~1:* individuare una definizione ricorsiva per la funzione $D(n)$.

*Obiettivo~2:* studiare l'ordine di crescita asintotico della funzione $D(n)$.

Ed ora poniamoci la questione pratica di progettare l'attacco kamikaze:  

*Domanda~2:* Quale è il minimo numero di aerei che consenta alla flotta di attraversare l'intera distanza $D$?

Chiamiamo $n(D)$ la risposta a tale domanda e cerchiamo di comprendere tale funzione.

*Obiettivo~3:* studiare l'ordine di crescita asintotico della funzione $n(D)$.

*Obiettivo~4:* riusciamo a fornire una forma chiusa?

