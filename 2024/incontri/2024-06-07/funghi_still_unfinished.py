# WARNING: still under development

#!/usr/bin/python
from sys import stderr

MOD = 10**9 + 7

def num_valid_confs_special_case(L, R, num_ast):
    """quante sono le configurazioni valide compatibili con mask e che iniziano con L e terminano con R.
       Le configurazioni valide sono sequenze di numeri naturali dove |s_i - s_(i+1)| <= 1. 
    """
    print(f"called ")
    if L < 0:
        return 0 
    if R < 0:
        return 0 
    if num_ast == 0:
        if L > R + 1:
            return 0
        if R > L + 1:
            return 0
        return 1
    if L == 0:
        return ( num_valid_confs_special_case(L, R, num_ast - 1) + num_valid_confs_special_case(L + 1, R, num_ast - 1) ) % MOD
    else:
        return ( num_valid_confs_special_case(L - 1, R, num_ast - 1) + num_valid_confs_special_case(L, R, num_ast - 1) + num_valid_confs_special_case(L + 1, R, num_ast - 1) ) % MOD
    

def num_valid_confs(mask):
    """quante sono le configurazioni valide compatibili con una data mask.
       Le configurazioni valide sono sequenze di numeri naturali dove:
          1. s_0 = 0 = s_(n-1)
          2. |s_i - s_(i+1)| <= 1. 
    """
    n = len(mask)
    if mask[0] > 0:
        return 0
    if mask[n-1] > 0:
        return 0
    mask[0] = mask[n-1] = 0
    
    risp = 1
    pos_first_maybe_ast = 1
    while pos_first_maybe_ast < n - 1:
        while mask[pos_first_maybe_ast] != -1:
            if mask[pos_first_maybe_ast] < mask[pos_first_maybe_ast - 1] - 1:
                return 0
            if mask[pos_first_maybe_ast] > mask[pos_first_maybe_ast - 1] + 1:
                return 0
            pos_first_maybe_ast += 1
            if pos_first_maybe_ast == n - 1:
                return risp
        pos_first_ast = pos_first_maybe_ast
        count_ast = 0
        pos_curr = pos_first_ast + 1
        while mask[pos_curr] == -1:
            count_ast += 1
            pos_curr += 1
        risp = (risp * num_valid_confs_special_case(mask[pos_first_ast - 1], mask[pos_curr], count_ast)) % MOD


mask = list(map(int, input().strip().split()))    
print(num_valid_confs(mask))

