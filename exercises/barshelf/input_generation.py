import random

def generate_input(n, filename="input.txt"):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        values = [str(random.randint(1, 10**9)) for _ in range(n)]
        f.write(" ".join(values) + "\n")


def generate_all_messy(n, start=1):
    arr = [0]*n
    arr[-1] = start
    for i in range(n-2, -1, -1):
        arr[i] = 2 * arr[i+1]
    return arr

def generate_all_trios_input(n, filename):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        values = generate_all_messy(n)
        f.write(" ".join(map(str, values)) + "\n")

def generate_no_messy(n, filename):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        f.write(" ".join(["1"] * n))

if __name__ == "__main__":
    n = int(input("Enter n: "))
    filename = input("Enter file name: ")
    #generate_input(n, filename)
    #generate_all_trios_input(n, filename)
    generate_no_messy(n, filename)
