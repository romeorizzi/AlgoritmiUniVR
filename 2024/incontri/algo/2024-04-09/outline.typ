= Incontro 2024-04-09: in aula alpha (problema `prima_PD_su_linea`)
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== recap su problemi già precedentemente assegnati

Riguardo ai problemi:

+ Flotta di aerei kamikaze in viaggio

+ Ponti di tessere

abbiamo deciso di lasciarveli ancora a voi per non spoilerarli, ma abbiamo chiarito il senso del primo dei due:

1. a serbatoio pieno, gli aerei riescono a percorrere distanza 1

2. partono in $n$ dalla base

3. mi basta che uno arrivi

4. gestiscili in modo da massimizzare la distanza del target.

Una volta risolto questo puoi poi porti la seguente domanda (problema inverso):

- quanti aerei ti servono per riuscire a raggiungere un target a distanza $D$?


== problema proposto oggi e su cui abbiamo lavorato

oggi eravamo in laboratorio alpha e abbiamo proposto di lavorare su:

```
rtal -s wss://ta.di.univr.it/algo get prima_PD_su_linea
```

l'idea è di comiciare a lavorare su problemi di programmazione dinamica (precedentemente avevamo solo dato una prima ambientazione a tale tecnica di problem solving col percorso ricorsione #sym.arrow  memoizzazione #sym.arrow  PD illustrato sul problema piastrelle).

