# 02 — Time and Space Efficiency of Algorithms

**Source:** `2 Time and Space Efficiency of Algorithms Slides.pdf` (29 slides)

## Core Question

- **Time complexity**: how does runtime change relative to input size `n`?
- **Space complexity**: how does required memory change relative to `n`?

## Measuring in Python

```python
from timeit import default_timer as timer
start = timer()
# ...
end = timer()
print(end - start)
```

Jupyter magic:
```
%%timeit
find_max(items)
# 4.1 µs ± 606 ns per loop ...

time = %timeit -o find_max(items)  # save result
```

## Comparing Algorithms

For input size `n`:
- Algorithm A: `100n + 1` steps
- Algorithm B: `n² + n + 1` steps

| n       | A          | B       |
|---------|------------|---------|
| 10      | 1 001      | 111     |
| 100     | 10 001     | 10 101  |
| 1 000   | 100 001    | 1 001 001 |
| 10 000  | 1 000 001  | > 10¹⁰  |

**Leading term dominates**. Any `n²` term grows faster than any `n` term. Smaller leading term wins at scale, though a crossover may favor the other for small `n`.

## Order of Growth (Big-O)

Set of functions with equivalent asymptotic growth. Formal:

- `f(n) ∈ O(g(n))` if `lim (f(n)/g(n)) = c` with `c < ∞`.
- Higher order: limit → ∞. Smaller order: limit → 0.

**Linear** — `2n`, `100n`, `n+1` → `O(n)`.
**Quadratic** — `4n² + 10n + 1`, `10n²` → `O(n²)`.

## Big-O Complexity Classes

| Class     | Name         | Example                                   |
|-----------|--------------|-------------------------------------------|
| O(1)      | Constant     | Array index access                        |
| O(log n)  | Logarithmic  | Binary search in sorted array             |
| O(n)      | Linear       | Find element in unsorted array            |
| O(n log n)| Log-linear   | Merge sort                                |
| O(n²)     | Quadratic    | Shortest path between two nodes           |
| O(n³)     | Cubic        | Matrix multiplication                     |
| O(2ⁿ)     | Exponential  | Brute-force password cracking             |
| O(n!)     | Factorial    | All permutations                          |

## Analyzing a Snippet

```python
def calc_mean(items):      # len(items) = n
    n = 0                  # O(1)
    sum_of_items = 0       # O(1)
    for item in items:     # runs n times  → O(n)
        sum_of_items += item   # O(1)
        n += 1                 # O(1)
    return sum_of_items / n    # O(1)
```
Total: **O(n)**.

Replacing the loop with `for i in range(5)` → **O(1)** (fixed iteration count).

## Best / Worst / Average Case

- Worst case: **O** (upper bound)
- Average case: **Θ** (tight bound)
- Best case: **Ω** (lower bound)

## Data Structures

Composition of data + methods + internal organization (= abstract data types).

- **Array** — contiguous, O(1) index access.
- **Dictionary** — key → value.
- **Linked List** — singly / doubly / circular; order from pointers, not memory layout.
- **Stack** — LIFO; `push` / `pop` / `peek`.
- **Queue** — FIFO; `enqueue` (rear) / `dequeue` (front).
- **Binary Search Tree** — keyed nodes; left subtree ≤ node ≤ right subtree.

## Time Complexity in Data Mining

- Iterating over all possible models (patterns) is often infeasible (brute force = test all decision trees / all clusterings).
- Real DM algorithms use **heuristics** — e.g. gradient descent — to find good (low-loss) solutions.
- Typical shape:
  ```
  while not converged:
      do_something()
  ```
- Key questions: **how fast does it converge? what does each iteration cost?**

## Exercise Mentioned

How many decision trees are possible with a dataset of `m` binary attributes? (Answer: very large — motivates heuristic search.)
