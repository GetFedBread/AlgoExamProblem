from random import shuffle

n = int(input())

l = [str(i+1) for i in range(n)]
shuffle(l)

print(n)
print(" ".join(l))