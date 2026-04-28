import sys
import time
sys.setrecursionlimit(1_000_000)

start_time = time.time_ns()
n = int(input())

L = list(map(int, input().split()))
s = {}

greatest = 0
mem = {}
# lefti:  index of left-most card not yet picked/discarded in L
# righti: index of right-most card not yet picked/discarded in L
# lo: lowest held card by value. None if not yet picked
# hi: highest held card by value. None if not yet picked
def check(lefti, righti, lo, hi, current):
    global L, mem, greatest
    args = (lefti, righti, lo, hi)
    # No cards left
    if lefti > righti:
        return current
    # Getting a greater value than what is already found is impossible
    if righti - lefti + 1 + current < greatest or (lo != None and lo - 1 + (n - hi) + current  < greatest):
        return -1
    if args in mem:
        return mem[args] + current

    takeres = -1
    # Take left card
    if lo == None:
        takeres = check(lefti+1, righti, L[lefti], L[lefti], current+1)
    elif L[lefti] < lo:
        takeres = check(lefti+1, righti, L[lefti], hi, current+1)
    elif L[lefti] > hi:
        takeres = check(lefti+1, righti, lo, L[lefti], current+1)
    
    # Take right card
    if hi == None:
        takeres = max(check(lefti, righti-1, L[righti], L[righti], current+1), takeres)
    elif L[righti] < lo:
        takeres = max(check(lefti, righti-1, L[righti], hi, current+1), takeres)
    elif L[righti] > hi:
        takeres = max(check(lefti, righti-1, lo, L[righti], current+1), takeres)
    
    discres = -1
    # Discard left card
    discres = check(lefti+1, righti, lo, hi, current)
    # Discard right card
    discres = max(check(lefti, righti-1, lo, hi, current), discres)

    # Max from left & right is the result
    result = max(takeres, discres)
    if result > -1:
        mem[args] = result - current
    else:
        if args in s:
            print("seen before", s[args], "times!")
        print("rejected:", args, "with score", current)
        if args not in s:
            s[args] = 0
        s[args] += 1
    
    if result > greatest:
        greatest = result
    return result


print(check(0, n-1, None, None, 0))

print("time: "+str(time.time_ns() - start_time))