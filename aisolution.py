import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.buffer.readline

n = int(input())
L = list(map(int, input().split()))

mem = {}
greatest = 0
L_local = L
mem_get = mem.get

def check(l, r, lo, hi, current):
    global greatest

    if l > r:
        if current > greatest:
            greatest = current
        return current

    # Admissible upper bounds
    rem = r - l + 1
    if current + rem <= greatest:
        return -1

    # Only safe if values are a permutation of 1..n
    if lo is not None:
        outside = (lo - 1) + (n - hi)
        if current + outside <= greatest:
            return -1

    key = (l, r, lo, hi)
    cached = mem_get(key)
    if cached is not None:
        return cached + current

    best = -1
    left = L_local[l]
    right = L_local[r]

    # Try take moves first
    if lo is None:
        t = check(l + 1, r, left, left, current + 1)
        if t > best: best = t
        t = check(l, r - 1, right, right, current + 1)
        if t > best: best = t
    else:
        if left < lo:
            t = check(l + 1, r, left, hi, current + 1)
            if t > best: best = t
        elif left > hi:
            t = check(l + 1, r, lo, left, current + 1)
            if t > best: best = t

        if right < lo:
            t = check(l, r - 1, right, hi, current + 1)
            if t > best: best = t
        elif right > hi:
            t = check(l, r - 1, lo, right, current + 1)
            if t > best: best = t

    # Then discards
    t = check(l + 1, r, lo, hi, current)
    if t > best: best = t

    t = check(l, r - 1, lo, hi, current)
    if t > best: best = t

    if best != -1:
        mem[key] = best - current
        if best > greatest:
            greatest = best

    return best

print(check(0, n - 1, None, None, 0))