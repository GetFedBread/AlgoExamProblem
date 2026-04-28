import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))

# Compress values
vals = sorted(set(L))
rank = {v: i for i, v in enumerate(vals)}
A = [rank[x] for x in L]

# Positions of each value
pos = [[] for _ in range(n)]
for i, v in enumerate(A):
    pos[v].append(i)

# dp_inc[i][j]: longest increasing sequence starting from i, ending at j
dp_inc = [[0]*n for _ in range(n)]
dp_dec = [[0]*n for _ in range(n)]

# Base: single card
for i in range(n):
    dp_inc[i][i] = 1
    dp_dec[i][i] = 1

# Build by length
for length in range(2, n+1):
    for l in range(n - length + 1):
        r = l + length - 1

        # Increasing
        best = max(dp_inc[l+1][r], dp_inc[l][r-1])

        if A[l] < A[r]:
            best = max(best, 2)
        else:
            best = max(best, 1)

        dp_inc[l][r] = best

        # Decreasing
        best = max(dp_dec[l+1][r], dp_dec[l][r-1])

        if A[l] > A[r]:
            best = max(best, 2)
        else:
            best = max(best, 1)

        dp_dec[l][r] = best

# Combine
print(max(dp_inc[0][n-1], dp_dec[0][n-1]))