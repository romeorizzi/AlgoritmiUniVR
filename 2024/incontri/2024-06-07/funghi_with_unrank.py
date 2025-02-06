#!/usr/bin/python
from sys import stderr, setrecursionlimit
from functools import lru_cache
setrecursionlimit(10**5)

# MOD = 10**9 + 7   to perform unranking we need the counting to be exact !

indent_cols = 1
def indent():
    global indent_cols
    indent_cols += 2
def deindent():
    global indent_cols
    indent_cols -= 2
def print_stderr(*args,**argv):
    argv["file"] = stderr
    print("|"* indent_cols, *args,**argv)


@lru_cache(maxsize=None)
def num_valid_confs_matching_mask_from(posL,valL):
    """quante sono le configurazioni valide compatibili con una data mask a partire da posL, avendo valore valL in posizione posL.
       Tali configurazioni valide sono sequenze di numeri naturali s_posL,s_(posL+1),...,s_(n-1) dove:
          1. s_posL = valL
          2. s_(n-1) = 0
          3. |s_i - s_(i+1)| <= 1 per i = posL,posL+1,...,n-2
          4. mask[i] in {-1,s_i}  per i = posL,posL+1,...,n-1
    """
    print_stderr(f"called num_valid_confs_matching_mask_from({posL=},{valL=})")
    indent()
    if mask[posL] >= 0 and mask[posL] != valL:
        print_stderr(f"0 <- called num_valid_confs_matching_mask_from({posL=},{valL=}) since  mask[posL] >= 0 and mask[posL] != valL")
        deindent()
        return 0
    if posL == n-1:
        print_stderr(f"1 <- called num_valid_confs_matching_mask_from({posL=},{valL=}) since posL == n-1")
        deindent()
        return 1
    risp = num_valid_confs_matching_mask_from(posL+1,valL) + num_valid_confs_matching_mask_from(posL+1,valL+1)
    if valL > 0:
        risp = risp + num_valid_confs_matching_mask_from(posL+1,valL-1)
    print_stderr(f"{risp=} <- called num_valid_confs_matching_mask_from({posL=},{valL=})")
    deindent()
    return risp

def unrank_matching_mask(rank, posL=0,valL=0):
    """ritorna la configurazione valida di rango r tra quelle compatibili col pattern mask a partire da posL, avendo valore valL in posizione posL. Tali confs avranno lunghezza n-posL. (Si veda il contratto di procedura num_valid_confs_matching_mask_from(posL,valL) per meglio comprendere questo).
    """
    print_stderr(f"called unrank({rank=}, {posL},{valL})")
    indent()
    if mask[posL] >= 0 and mask[posL] != valL:
        print_stderr(f"abort: unrank_matching_mask({rank=}, {posL=},{valL=}) since  mask[posL] >= 0 and mask[posL] != valL")
        assert False, f"abort: unrank_matching_mask({rank=}, {posL=},{valL=}) since  mask[posL] >= 0 and mask[posL] != valL"
    if posL == n-1:
        print_stderr(f"got the required leaf <- called unrank_matching_mask({rank=}, {posL=},{valL=}) since posL == n-1")
        deindent()
        return [valL]
    part_count = num_valid_confs_matching_mask_from(posL+1,valL+1)
    if valL > 0:
        if rank < num_valid_confs_matching_mask_from(posL+1,valL-1):
            ret = [valL] + unrank_matching_mask(rank, posL+1,valL-1)
            print_stderr(f"{ret=} <- called unrank_matching_mask({rank=}, {posL=},{valL=})")
            deindent()
            return ret
        rank -= num_valid_confs_matching_mask_from(posL+1,valL-1)
    if rank < num_valid_confs_matching_mask_from(posL+1,valL):
        ret = [valL] + unrank_matching_mask(rank, posL+1,valL)
        print_stderr(f"{ret=} <- called unrank_matching_mask({rank=}, {posL=},{valL=})")
        deindent()
        return ret
    rank -= num_valid_confs_matching_mask_from(posL+1,valL)
    ret = [valL] + unrank_matching_mask(rank, posL+1,valL+1)
    print_stderr(f"{ret=} <- called unrank_matching_mask({rank=}, {posL=},{valL=})")
    deindent()
    return ret
    
    L = 0; risp = [L]; num_ast = 0
    for pos in range(1,n):
        if mask[pos] != -1:
            Base = num_valid_confs(mask[pos:])
            choice = rank / Base
            rank = rank % Base
            tmp = mask[pos:]
            
    while posL < n - 1:
        posR = posL + 1
        while mask[posR] == -1:
            posR += 1
        risp += unrank(rank,mask[posL:posR])[:-1]
        posL = posR
    risp.append(0)
    print_stderr(f"{risp=} <- called unrank({rank=},{mask=})")
    deindent()
    return risp


mask = list(map(int, input().strip().split()))    
n = len(mask)
if mask[n-1] == -1:
    mask[n-1] = 0
print(num_valid_confs_matching_mask_from(0,0))
for rnk in range(num_valid_confs_matching_mask_from(0,0)):
    print(" ".join(map(str,unrank_matching_mask(rnk))))
