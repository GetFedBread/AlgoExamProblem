n = int(input())

L = list(map(int, input().split()))

# lefti:  index of left-most card not yet picked/discarded in L
# righti: index of right-most card not yet picked/discarded in L
# lo: lowest held card by value. None if not yet picked
# hi: highest held card by value. None if not yet picked
def check(lefti, righti, lo, hi):
    # No cards left
    if lefti > righti:
        return 0
    
    global L
    result = 0

    # Take left card
    if lo == None:
        result = check(lefti+1, righti, L[lefti], L[lefti]) + 1
    elif L[lefti] < lo:
        result = check(lefti+1, righti, L[lefti], hi) + 1
    elif L[lefti] > hi:
        result = check(lefti+1, righti, lo, L[lefti]) + 1
    
    # Discard left card
    result = max(check(lefti+1, righti, lo, hi), result)
    
    # Take right card
    if hi == None:
        result = max(check(lefti, righti-1, L[righti], L[righti]) + 1, result)
    elif L[righti] < lo:
        result = max(check(lefti, righti-1, L[righti], hi) + 1, result)
    elif L[righti] > hi:
        result = max(check(lefti, righti-1, lo, L[righti]) + 1, result)
    
    # Discard right card
    result = max(check(lefti, righti-1, lo, hi), result)

    return result


print(check(0, n-1, None, None))