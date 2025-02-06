#!/usr/bin/python
from sys import stderr, setrecursionlimit
from functools import lru_cache
setrecursionlimit(10**5)

MOD = 10**9 + 7

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
        print_stderr(f"0 <- called num_valid_confs_matching_mask_from({posL=},{valL=}) since  mask[i] >= 0 and mask[i] != valL")
        deindent()
        return 0
    if posL == n-1:
        print_stderr(f"1 <- called num_valid_confs_matching_mask_from({posL=},{valL=}) since posL == n-1")
        deindent()
        return 1
    risp = (num_valid_confs_matching_mask_from(posL+1,valL) + num_valid_confs_matching_mask_from(posL+1,valL+1)) % MOD
    if valL > 0:
        risp = (risp + num_valid_confs_matching_mask_from(posL+1,valL-1)) % MOD
    print_stderr(f"{risp=} <- called num_valid_confs_matching_mask_from({posL=},{valL=})")
    deindent()
    return risp


mask = list(map(int, input().strip().split()))    
n = len(mask)
print(num_valid_confs_matching_mask_from(0,0))
