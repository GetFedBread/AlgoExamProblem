class FenwickTree():
    """A Fenwick tree (binary indexed tree) implementation; update and query run in O(log n)."""

    def __init__(self, n):
        self.A = [0 for _ in range(n + 1)]

    def add(self, i, k):
        """Add k to the i-th element."""
        while i < len(self.A):
            self.A[i] += k
            i += i & -i

    def prefix_sum(self, i):
        """Return the sum of elements from index 1 to i."""
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s
    
    def suffix_sum(self, i):
        """Return the sum of elements from index i to end."""
        return self.prefix_sum(len(self.A)-1) - self.prefix_sum(i - 1)


def create_mapping(arr):
    """ 
    Creates mapping 
        from: union of all relevant values (arr, their doubles and halves)
        to: unique indexes [1...M]
    while preserving order.
    To be used in Fenwick tree.
    """
    x = (set(arr))
    x_twice = {a*2 for a in x}
    x_half = {a//2 for a in x}

    all_values = sorted(set(x | x_twice | x_half))

    dict = {}
    for i in range(len(all_values)):
        dict[all_values[i]] = i+1 # one-indexed to match fenwick tree
    return dict


def process_left(arr, mapping):
    """Computes, for each position i, how many elements to the left are at least twice as large as arr[i]."""
    bigger_left_counts = [0]*len(arr)
    tree = FenwickTree(len(mapping))

    for i in range(len(arr)):
        double_idx = mapping[arr[i]*2]
        bigger_left_counts[i] = tree.suffix_sum(double_idx)
        tree.add(mapping[arr[i]], 1)

    return bigger_left_counts


def process_right(arr, mapping):
    """Computes, for each position i, how many elements to the right are at most half of arr[i]."""
    smaller_right_counts = [0]*len(arr)
    tree = FenwickTree(len(mapping))

    for i in reversed(range(len(arr))):
        half_idx = mapping[arr[i]//2]
        smaller_right_counts[i] = tree.prefix_sum(half_idx)
        tree.add(mapping[arr[i]], 1)

    return smaller_right_counts


def count_messy_trios(bottles):
    """
    Return the number of “messy trios” in the list of bottle heights.
    A messy trio (i, j, k) satisfies: i < j < k,  a[i] ≥ 2*a[j],  and  a[j] ≥ 2*a[k]
    """
    mapping = create_mapping(bottles)
    left = process_left(bottles, mapping)
    right = process_right(bottles, mapping)

    total_count = 0

    for middle in range(1, len(bottles)-1):
        count = left[middle] * right[middle]
        total_count += count

    return total_count


def main():
    _ = int(input())
    bottles = list(map(int, input().split()))

    print(count_messy_trios(bottles))    


if __name__ == "__main__":
    main()
