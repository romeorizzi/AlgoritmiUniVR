= Incontro 2024-05-07: in aula I
#text(style:"italic", size:11pt, [Gli incontri avvengono sia in presenza che nella stanza Zoom:\
#h(6mm) `https://univr.zoom.us/j/85817283103`\
E, quando disponibile, la loro registrazione è nel folder:\
#h(6mm) `https://univr.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=c4df8587-8f34-4732-8e51-b12d0108ea08`\
])

== approfondimenti di Programmazione Dinamica

Problema arcobaleno/collage (PD su linea, quando i prefissi/suffissi non bastano)

Proposta di contratto ricorsivo:

```python
min_fogli(left,right):
    """ritorna il minimo numero di fogli necessario per costruire l'arcobalemo A[left,right]"""
    assert 0 <= left <= right <= n - 1
```

Quindi, la solozione della domanda originale sarà data da:
```python
print(min_fogli(0,n-1))
```

L'implementazione (bacata) che abbiamo scritto insieme era:

```python
def min_fogli(left,right):
    """ritorna il minimo numero di fogli necessario per costruire l'arcobalemo A[left,right]"""
    assert 0 <= left <= right <= n - 1
    print(f"called min_fogli({left=},{right=})", file=stderr)
    if right <= left + 1:
        return 0
    best_val = 1 + min_fogli(left + 1,right) # il primo colore è servito da un foglio privato
    for next_app_first in range(left+1,right):
        if A[left] == A[next_app_first]:
            best_val = min(best_val, min_fogli(left,next_app_first) + min_fogli(next_app_first,right) - 1 )
    return best_val
    
```

Un problema è nella prima chiamata "fogli(left,next_app_first)" che, in questo momento, potrebbe ancora essere grossa come il problema originale se davvero `next_app_first` fosse fatto variare su tutte le possibili posizioni in cui il primissimo foglio riappare per la prima volta, perchè `right` (anche se a livello di codice è attualmente escluso) potrebbe anche essere il primo punto dove il primo foglio riappare. Quindi bisogna assicurarsi che questo sottoproblema sia più piccolo, e non per una cattiva traduzione in codice ma per una self-reduction (che si porterà via anche il -1). 

Riuscite a fixare il tutto?



