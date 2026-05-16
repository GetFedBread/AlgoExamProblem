import random
from collections import deque

pattern_length = 20

state = int(input())

def is_sub(sub, arr):
    n, m = len(arr), len(sub)
    
    for i in range(n - m + 1):
        if arr[i:i+m] == sub:
            return True
    return False

def move_right():
    global state
    print("? right")
    state = int(input())

def move_left():
    global state
    print("? left")
    state = int(input())

def flip():
    global state
    print("? flip")
    state = int(input())

pattern = [1]+[random.choice([0, 1]) for _ in range(pattern_length-1)]

for _ in range(pattern_length):
    if state != 0:
        flip()
    move_right()

for _ in range(pattern_length):
    move_left()

for i in range(pattern_length):
    if state != 0:
        print("!", (i))
        exit(0)
    if pattern[i] == 1:
        flip()
    move_right()

steps = 1
seen = deque(maxlen=pattern_length)
for _ in range(5000):
    seen.append(state)
    if len(seen) == pattern_length and list(seen) == pattern:
        print("!", steps)
        exit(0)
    move_right()
    steps += 1