# Task 7 — Recurrence Solution

## S2 by backward substitution
Given T(n) = T(n/2) + 1 and T(1) = 1, assume n is a power of two.

T(n) = T(n/2) + 1

Substitute again:

T(n) = [T(n/4) + 1] + 1
     = T(n/4) + 2.

Substitute again:

T(n) = T(n/8) + 3.

After k substitutions:

T(n) = T(n/2^k) + k.

The recursion reaches the base case when n/2^k = 1. Therefore n = 2^k and k = log₂n.

Using T(1) = 1:

T(n) = 1 + log₂n.

Hence T(n) = Θ(log n).

For arbitrary n, floors/ceilings change the exact integer count, but the asymptotic bound remains Θ(log n).

## M4 current using the Master Theorem
T(n) = 4T(n/2) + n.

a = 4, b = 2, f(n) = n.

n^(log_b a) = n^(log₂4) = n².

Since n = O(n^(2−ε)) for ε = 1, Case 1 applies. Therefore T(n) = Θ(n²).

## M4 proposed redesign
T(n) = 2T(n/2) + n.

a = 2, b = 2, f(n) = n, and n^(log₂2) = n. Case 2 applies, giving T(n) = Θ(n log n).

## M5 using the extended Master Theorem
T(n) = 2T(n/2) + n log n.

a = 2, b = 2, n^(log_b a) = n, and f(n) = Θ(n log n). This is the extended Case 2 form f(n) = Θ(n log^k n) with k = 1. Therefore T(n) = Θ(n log^(k+1)n) = Θ(n log²n).
