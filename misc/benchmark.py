# AI generated benchmarker

# Used as such:
# pypy benchmark.py --runs 20 --n 52 --cmd pypy solution.py
# pypy benchmark.py --runs 20 --n 52 --cmd java solution

import subprocess
import time
import random
import argparse
import math


def generate_input(n: int) -> str:
    l = [str(i + 1) for i in range(n)]
    random.shuffle(l)

    # match your format exactly
    return f"{n}\n{' '.join(l)}\n"


def run_once(cmd, input_data: str) -> float:
    start = time.perf_counter()

    subprocess.run(
        cmd,
        input=input_data.encode(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    end = time.perf_counter()
    return end - start


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=10, help="number of executions")
    parser.add_argument("--n", type=int, default=1000, help="size of input")
    parser.add_argument("--cmd", nargs="+", required=True,
                        help="solver command, e.g. 'python solver.py' or 'java Solver'")

    args = parser.parse_args()

    total = 0.0
    max_t = 0
    min_t = math.inf

    for i in range(args.runs):
        inp = generate_input(args.n)
        t = run_once(args.cmd, inp)
        total += t
        max_t = max(t, max_t)
        min_t = min(t, min_t)
        print(f"Run {i+1}: {t:.6f}s")

    print("\n--- Summary ---")
    print(f"Runs: {args.runs}")
    print(f"Min time: {min_t:.6f}s")
    print(f"Max time: {max_t:.6f}s")
    print(f"Avg time: {total / args.runs:.6f}s")
    print(f"Total time: {total:.6f}s")


if __name__ == "__main__":
    main()