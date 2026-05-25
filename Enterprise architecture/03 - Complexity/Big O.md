---
aliases: ["Big O", "Big-O", "O notation"]
---

Set of functions with equivalent asymptotic growth. The ruler that ignores constants and lower order terms.

## Formal
`f(n) ∈ O(g(n))` if `lim(f(n)/g(n)) = c` with `c < ∞`.

Translation:
- limit is finite --> same growth order
- limit --> ∞ --> f grows FASTER than g
- limit --> 0 --> f grows SLOWER than g

## Common collapses
- `2n`, `100n`, `n+1` --> all `O(n)`. Constants gone.
- `4n² + 10n + 1` --> `O(n²)`. Lower terms gone.

## Sibling notations
- **O** - worst case, upper bound
- **Θ** - tight bound, average case
- **Ω** - best case, lower bound

! In job interviews "Big O" almost always means worst case O. In papers Θ is often the right one.

See [[Complexity Classes]] for the menu, [[Time Complexity]] for examples.

## Visual - growth comparison

```mermaid
xychart-beta
    title "operations vs input size"
    x-axis "n" [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y-axis "ops" 0 --> 120
    line "O(1)" [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    line "O(log n)" [0, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    line "O(n)" [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    line "O(n log n)" [0, 2, 5, 8, 12, 16, 20, 24, 29, 33]
    line "O(n^2)" [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Learn more
- Wikipedia: [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - everyone keeps this open during interviews
- MIT OCW: [Introduction to Algorithms (6.006)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- 3Blue1Brown adjacent: search YouTube for "Big O notation visualised"

