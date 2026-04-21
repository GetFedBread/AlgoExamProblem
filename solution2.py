import sys
import time
sys.setrecursionlimit(1_000_000)

start_time = time.time_ns()
n = int(input())

L = list(map(int, input().split()))

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
        return current
    if args in mem:
        return mem[args] + current

    result = 0

    # Take left card
    if lo == None:
        result = check(lefti+1, righti, L[lefti], L[lefti], current+1)
    elif L[lefti] < lo:
        result = check(lefti+1, righti, L[lefti], hi, current+1)
    elif L[lefti] > hi:
        result = check(lefti+1, righti, lo, L[lefti], current+1)
    
    # Discard left card
    result = max(check(lefti+1, righti, lo, hi, current), result)
    
    # Take right card
    if hi == None:
        result = max(check(lefti, righti-1, L[righti], L[righti], current+1), result)
    elif L[righti] < lo:
        result = max(check(lefti, righti-1, L[righti], hi, current+1), result)
    elif L[righti] > hi:
        result = max(check(lefti, righti-1, lo, L[righti], current+1), result)
    
    # Discard right card
    result = max(check(lefti, righti-1, lo, hi, current), result)

    mem[args] = result - current
    if result > greatest:
        greatest = result
    return result


print(check(0, n-1, None, None, 0))

print("time: "+str(time.time_ns() - start_time))