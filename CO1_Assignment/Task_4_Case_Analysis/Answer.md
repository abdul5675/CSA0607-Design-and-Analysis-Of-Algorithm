# Task 4 — Best, Average and Worst Cases

## M3-S1: Sequential search
- **Best case:** target is the first entry; 1 comparison.
- **Worst case:** target is the last entry or absent; n comparisons.
- **Average successful case:** if every position is equally likely, the average is (1 + 2 + ... + n)/n = (n+1)/2 comparisons.

If the target exists with probability p and its position is uniformly distributed, while an unsuccessful search checks all n entries:

E[C] = p(n+1)/2 + (1−p)n.

For n = 1,000,000 and p = 0.5:

E[C] = 0.5 × 500,000.5 + 0.5 × 1,000,000
     = 750,000.25 comparisons.

## M3-S2: Binary search
- **Best case:** target equals the first midpoint; one midpoint check.
- **Average case:** Θ(log₂n) comparisons under ordinary balanced-search assumptions.
- **Worst case:** the algorithm continues until the target is found or the interval becomes empty; Θ(log₂n) comparisons.

For n = 1,000,000, log₂n ≈ 19.93. The search needs about 20 halving levels; the exact number of key comparisons depends on the target and counting convention.

## Other modules
M1's pairwise nested loops perform the same number of pair comparisons regardless of whether duplicates are found. M2's audit count depends on n and the doubling schedule. M4 and M5 are recurrence-based and are analysed using their specified recurrences rather than search-position cases.
