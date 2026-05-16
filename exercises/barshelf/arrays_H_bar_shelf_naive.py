n = int(input())

bottles = list(map(int, input().split()))

big_diff = [False]* (n-1)

rows = [0]* (n)
cols = [0]* (n)

for i in range(n-1):
    for j in range (i+1, n):
        ratio = bottles[i]/bottles[j]
        if ratio >= 2:
            rows[i] += 1
            cols[j] += 1

#print(rows)
#print(cols)

total_count = 0

for middle in range(1, n-1):
    count = rows[middle] * cols[middle]
    total_count += count

print(total_count)