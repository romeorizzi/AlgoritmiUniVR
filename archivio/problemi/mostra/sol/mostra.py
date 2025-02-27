#!/usr/bin/env python3
from sys import stderr,stdout, argv

T = int(input())
for t in range(1, 1 + T):
    n,m = map(int, input().strip().split())
    V = list(map(int, input().strip().split()))
    G = list(map(int, input().strip().split()))

    prev_i_bigger_than_j = [ [None] * n for _ in range(m) ]
    prev_j_smaller_than_i = [ [None] * n for _ in range(m) ]
    for i in range(m):
        for j in range(n):
            if i > 0 and G[i-1] > V[j]:
                prev_i_bigger_than_j[i][j] = i-1
            else:
                prev_i_bigger_than_j[i][j] = prev_i_bigger_than_j[i-1][j]
            if j > 0 and G[i] > V[j-1]:
                prev_j_smaller_than_i[i][j] = j-1
            else:
                prev_j_smaller_than_i[i][j] = prev_j_smaller_than_i[i][j-1]
    """ #print debugging:
    for i in range(m):
        print(f" prev_i_bigger_than_j[{i=}] = " + " ".join(map(str, prev_i_bigger_than_j[i])))
    for i in range(m):
        print(f" prev_j_smaller_than_i[{i=}] = " + " ".join(map(str, prev_j_smaller_than_i[i])))
    """            
        
    overflow_sols = False
    overflow_sets = False
    max_match = [ [0] * (n+1) for _ in range(m+1) ]
    num_opt_sols = [ [1] * (n+1) for _ in range(m+1) ]
    num_opt_sets = [ [1] * (n+1) for _ in range(m+1) ]
    for mm in range(1,m+1):
        for nn in range(1,n+1):
            i = mm - 1
            j = nn - 1
            prev_i_ok_with_j = prev_i_bigger_than_j[i][j]
            prev_j_ok_with_i = prev_j_smaller_than_i[i][j]
            if G[i] > V[j]:
                max_match[mm][nn] = 1 + max_match[mm-1][nn-1]
                if not overflow_sols:
                    num_opt_sols[mm][nn] = num_opt_sols[mm-1][nn-1]
                    if max_match[mm-1][nn] == max_match[mm][nn]:
                        num_opt_sols[mm][nn] += num_opt_sols[mm-1][nn]
                    if max_match[mm][nn-1] == max_match[mm][nn]:
                        num_opt_sols[mm][nn] += num_opt_sols[mm][nn-1]
                if not overflow_sets:
                    num_opt_sets[mm][nn] = num_opt_sets[mm-1][nn-1]
                    if max_match[mm-1][nn] == max_match[mm][nn]:
                        num_opt_sets[mm][nn] += num_opt_sets[mm-1][nn]
            else:
                max_match[mm][nn] = max(max_match[mm][nn-1], max_match[mm-1][nn])
                if not overflow_sets:
                    if max_match[mm-1][nn] == max_match[mm][nn]:
                        num_opt_sets[mm][nn] = num_opt_sets[mm-1][nn]
                        if prev_j_ok_with_i is not None:
                            if max_match[mm-1][prev_j_ok_with_i] + 1 == max_match[mm][nn]:
                                num_opt_sets[mm][nn] += num_opt_sets[mm-1][prev_j_ok_with_i]
                    else:
                        assert max_match[mm][nn-1] == max_match[mm][nn] == 1 + max_match[mm-1][nn]
                        num_opt_sets[mm][nn] = num_opt_sets[mm][nn-1]
                if not overflow_sols:
                    if max_match[mm-1][nn] == max_match[mm][nn-1]:
                        if max_match[mm-1][nn-1] == max_match[mm][nn]:
                            num_opt_sols[mm][nn] = num_opt_sols[mm][nn-1] + num_opt_sols[mm-1][nn] - num_opt_sols[mm-1][nn-1]
                        else:
                            num_opt_sols[mm][nn] = num_opt_sols[mm][nn-1] + num_opt_sols[mm-1][nn]
                    elif max_match[mm-1][nn] < max_match[mm][nn-1]:
                        num_opt_sols[mm][nn] = num_opt_sols[mm][nn-1]
                        if prev_i_ok_with_j is not None:
                            if max_match[prev_i_ok_with_j][nn] == max_match[mm][nn]:
                                if max_match[prev_i_ok_with_j][nn-1] == max_match[mm][nn]:
                                    num_opt_sols[mm][nn] += num_opt_sols[prev_i_ok_with_j][nn] - num_opt_sols[prev_i_ok_with_j][nn-1]
                                else:
                                    num_opt_sols[mm][nn] += num_opt_sols[mmfirst][nn]
                    else:
                        num_opt_sols[mm][nn] = num_opt_sols[mm-1][nn]
                        if prev_j_ok_with_i is not None:
                            if max_match[mm][prev_j_ok_with_i] == max_match[mm][nn]:
                                if max_match[mm-1][prev_j_ok_with_i] == max_match[mm][nn]:
                                    num_opt_sols[mm][nn] += num_opt_sols[mm][prev_j_ok_with_i] - num_opt_sols[mm-1][prev_j_ok_with_i]
                                else:
                                    num_opt_sols[mm][nn] += num_opt_sols[mm][nnfirst]
            
            if num_opt_sols[mm][nn] > 10**9 + 7:  
                overflow_sols = True
            if num_opt_sets[mm][nn] > 10**9 + 7:  
                overflow_sets = True
                
    print(n + max_match[m][n])
    optS = ["0"] * m; optT = ["0"] * n
    i = m; j = n
    promise = max_match[i][j]
    while promise > 0:
        while max_match[i][j-1] == promise:
            j -= 1
        while G[i-1] <= V[j-1]:
            i -= 1
        i -= 1; j -= 1
        optS[i] = "1"
        optT[j] = "1"
        promise = max_match[i][j]
    print(" ".join(optT))
    print(" ".join(optS))
    
    """ #print debugging:
    for i in range(m+1):
        print(f" num_opt_sols[{i=}] = " + " ".join(map(str, num_opt_sols[i])))
    for i in range(m+1):
        print(f" num_opt_sets[{i=}] = " + " ".join(map(str, num_opt_sets[i])))
    """
    print(num_opt_sols[m][n])
    print(num_opt_sets[m][n])
