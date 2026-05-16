import subprocess
import time
import sys

def measure_runtime(program, input_file):
    with open(input_file, "r") as f:
        start = time.perf_counter()
        subprocess.run(["python", program], stdin=f, stdout=subprocess.DEVNULL)
        end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python measure.py <program.py> <input.txt>")
        sys.exit(1)

    program = sys.argv[1]
    input_file = sys.argv[2]

    t = measure_runtime(program, input_file)
    print(f"Execution time: {t:.6f} seconds")