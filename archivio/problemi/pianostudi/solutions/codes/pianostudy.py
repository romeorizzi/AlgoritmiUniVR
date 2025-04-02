#!/usr/bin/env python3
from sys import stderr,stdout, argv

def pianifica(lista_corsi):
    n = len(lista_corsi)
    """ogni corso della lista è una quadrupla:
        - i: nome del corso (first 1 a n)
        - first: primo giorno del corso
        - last: ultimo giorno del corso
        - val: numero crediti del corso
    """
    lista_corsi = sorted(lista_corsi, key=lambda x: x["last"])
    best_with_last_course = [(-1,0,None)] # contiene una tripla (last_day,max_val,pos_corso_sorted) che esprimono il massimo valore ottenibile se l'ultimo corso frequentato è proprio lista_corsi[pos_corso_sorted]. Memorizzeremo le sole triple con max_val maggiore che per ogni last_day più piccolo. Inizializzato per contenere una sentinella di valore zero e compatibile con ogni altro corso. 

    curr_max_val = 0
    for pos_corso_sorted,corso in enumerate(lista_corsi):
        # Trova l'indice del corso che finisce immediatamente prima dell'inizio del corso corrente
        left, right = 0, len(best_with_last_course)
        while left < right - 1:
            mid = (left + right) // 2
            if best_with_last_course[mid][0] < corso["first"]:
                left = mid
            else:
                right = mid

        potential_value = corso["val"] + best_with_last_course[left][1]
        if potential_value > curr_max_val:
            curr_max_val = potential_value
            best_with_last_course.append((corso["last"],curr_max_val,pos_corso_sorted))
    opt_val = curr_max_val
    opt_sol1 = [{"nome_corso":None,"pos_corso_sorted":None,"first_day":lista_corsi[-1]["last"] + 1}]
    while curr_max_val > 0:
        last_day,max_val,pos_corso_sorted = best_with_last_course.pop()
        if last_day < opt_sol1[-1]["first_day"] and max_val == curr_max_val:
            opt_sol1.append({"nome_corso": lista_corsi[pos_corso_sorted]["name"], "pos_corso_sorted":pos_corso_sorted, "first_day":lista_corsi[pos_corso_sorted]["first"]})
            curr_max_val -= lista_corsi[pos_corso_sorted]["val"]
            
    opt_sol = [ _["nome_corso"] for _ in reversed(opt_sol1[1:]) ]    
    return opt_val, opt_sol


T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    lista_corsi = []
    for i in range(n):
        da, a, crediti = map(int, input().strip().split())
        lista_corsi.append({"name": i+1, "first": da, "last": a, "val": crediti})
    opt_val, opt_sol = pianifica(lista_corsi)
    print(opt_val)
    print(" ".join(map(str,opt_sol)))

