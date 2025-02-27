#!/usr/bin/env python3
from sys import stderr, stdout, argv
from random import randrange, randint

usage = f"""
   Call as follows:
      {argv[0]} optval_ok optsol_ok debug_level efficiency_level

   where the arguments hold the following meaning:
   - optval_ok:
        0 means that optval in the first output line is always correct
        1 means that optval is often ok, but not always
        2 first output line is never correct
   - optsol_ok
        0 means that optsol in the second output line is always correct
        1 means that optsol is often ok, but not always
        2 second output line is never correct
   - debug_level
        0 print no debug info on stderr
        1 print checkpoint testcase number to help debugging
        2 print also the received instance
        3 echo on stderr also the output on stdout
        4 print also most significant internal data exchanges
   - efficiency_level
        0 greedy at its best
        1 one coin at the time
        2 exp"""

pieces = [1,2,5,10,20,50,100,200,500,1000]

def greedy_at_its_best(S):
    optsol = []
    for piece in reversed(pieces):
        optsol.append(S//piece)
        S %= piece
    return sum(optsol), optsol[::-1]

def greedy_one_coin_at_the_time(S):
    optsol = []
    for piece in reversed(pieces):
        optsol += [0]
        while piece <= S:
            S -= piece
            optsol[-1] += 1
    return sum(optsol), optsol[::-1]

def exp(S, pos_max_piece = len(pieces) - 1):
    if pos_max_piece == 0:
        return S,[S]
    bestval, bestsol = exp(S, pos_max_piece - 1)
    num_max_pieces = 1
    while num_max_pieces * pieces[pos_max_piece] <= S:
        fairyval,fairysol = exp(S -num_max_pieces * pieces[pos_max_piece], pos_max_piece - 1)
        if fairyval + num_max_pieces < bestval:
            bestval = fairyval + num_max_pieces
            bestsol = fairysol + [num_max_pieces]
    return bestval, bestsol

optimize = [greedy_at_its_best, greedy_one_coin_at_the_time, exp]    

  
if __name__ == "__main__":
    if len(argv) != 5:
        print(f"Error: program {argv[0]} called with {len(argv)-1} arguments rather than 5.")
        print(usage)
        exit(1)
    optval_ok, optsol_ok, debug_level, efficiency_level = map(int, argv[1:])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        S = int(input())
        if debug_level > 1:
            print(f"{S=}", file=stderr)
        optval, optsol = optimize[efficiency_level](S)
        if debug_level > 2:
            print(f"{optval=},{optsol=}", flush=True, file=stderr)
        fouts = [stderr, stdout] if debug_level > 3 else [stdout]
        spoil_optval = optval_ok==2 or (optval_ok==1 and randrange(4)==0)
        spoil_optsol = optsol_ok==2 or (optsol_ok==1 and randrange(4)==0)
        if spoil_optval and spoil_optsol:
            for i,piece in enumerate(pieces[1:],start=1):
                if optsol[i]>0:
                    optsol[i] -= 1
                    optsol[0] += piece
                    optval += piece - 1
                    break
        else:
            if spoil_optval:
                optval += 2*randint(0,1) - 1
            if spoil_optsol:
                optsol[-1] += 2*randint(0,1) - 1
        for fout in fouts:
            print(optval, file=fout)
            print(" ".join(map(str,optsol)), file=fout)
        fout.flush()
