n, m = map(int, input().split()) # cave size
ax, ay, bx, by = map(int, input().split()) # coordinates

def inside(x, y, n, m):
    return (0 <= x < n) and (0 <= y < m)

# my idea: pass x, y to obtuse when run inside of a loop (for x in, for y in,) in an array of sample data that is small for each
def obtuse(ax, ay, bx, by, x, y):
    area2 = (bx - ax) * (y - ay) - (by - ay) * (x - ax) # no degen calc
    if area2 == 0:
        return False
    
    AB = (bx - ax, by - ay)
    AC = (x - ax, y - ay)
    BA = (ax - bx, ay - by)
    BC = (x - bx, y - by)
    CA = (ax - x, ay - y)
    CB = (bx - x, by - y)

    return (
        AB[0] * AC[0] + AB[1] * AC[1] < 0 or 
        BA[0] * BC[0] + BA[1] * BC[1] < 0 or
        CA[0] * CB[0] + CA[1] * CB[1] < 0
    )

xs = {0, 1, n - 1, n - 2, ax, ax + 1, ax - 1, bx, bx + 1, bx - 1}
ys = {0, 1, m - 1, m - 2, ay, ay + 1, ay - 1, by, by + 1, by - 1}

for x in xs:
    for y in ys:
        if inside (x, y, n, m) and (x,y) != (ax, ay) and (x,y) != (bx,by): # extra checks to not place on giants foot
            if obtuse(ax, ay, bx, by, x, y):
                print(x,y) 
                exit()



