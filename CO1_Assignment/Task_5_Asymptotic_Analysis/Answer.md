# Task 5 — Asymptotic Analysis

## Big-O
f(n) = O(g(n)) means that there are positive constants c and n₀ such that 0 ≤ f(n) ≤ c g(n) for every n ≥ n₀. It describes an asymptotic upper bound.

## Big-Ω
f(n) = Ω(g(n)) means there are positive constants c and n₀ such that f(n) ≥ c g(n) for every n ≥ n₀. It describes an asymptotic lower bound.

## Big-Θ
f(n) = Θ(g(n)) means f(n) is both O(g(n)) and Ω(g(n)). It gives a tight asymptotic bound.

## Application to ShopSphere
- M1: n(n−1)/2 is Θ(n²).
- M2: the geometric sum is Θ(n).
- S1: worst-case sequential search is Θ(n).
- S2: binary search is Θ(log n).
- M4 current: Θ(n²).
- M4 proposed: Θ(n log n).
- M5: Θ(n log² n).

Logarithmic growth is much slower than linear growth; linear growth is much slower than quadratic growth. At one million records, reducing a quadratic routine to n log n or n can change whether a nightly processing deadline is achievable.

## Report-generator proof
Let f(n) = 3n² + 10n log₂n + 50.

For n ≥ 1, log₂n ≤ n, so n log₂n ≤ n². Also 50 ≤ 50n². Therefore:

f(n) ≤ 3n² + 10n² + 50n² = 63n².

Thus f(n) = O(n²), with c₂ = 63 and n₀ = 1.

Also, f(n) ≥ 3n² for every n ≥ 1. Hence f(n) ≥ 3n², so f(n) = Ω(n²), with c₁ = 3 and n₀ = 1.

Combining the bounds:

3n² ≤ f(n) ≤ 63n² for n ≥ 1.

Therefore f(n) = Θ(n²).

## Prove that f(n) is not O(n)
Assume, for contradiction, that f(n) ≤ c n for all n ≥ n₀, for some constant c > 0. Since f(n) ≥ 3n², this implies 3n² ≤ cn, or n ≤ c/3. But n can be arbitrarily large, so this inequality eventually fails. The assumption is false; therefore f(n) is not O(n).
