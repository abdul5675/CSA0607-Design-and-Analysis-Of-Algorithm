# Task 3 — Mathematical Complexity

## 3.1 M1
The exact count is C(n) = n(n−1)/2 = (n²−n)/2. The highest-order term is n²/2, so M1 is Θ(n²). If duplicate markers are stored in existing records, auxiliary space can be Θ(1), excluding the input and any output list. A separate list of marked duplicates can require O(n) space.

## 3.2 M2
A(n) = 1 + 2 + ... + 2^k = 2^(k+1)−1, with 2^k < n ≤ 2^(k+1). Thus n ≤ 2^(k+1) < 2n, so A(n) = Θ(n).

## 3.3 M3 searches
- S1 sequential search: best Θ(1); average Θ(n); worst Θ(n); auxiliary space Θ(1).
- S2 binary search: best Θ(1); average Θ(log n); worst Θ(log n); iterative auxiliary space Θ(1); recursive auxiliary space Θ(log n).

## 3.4 M4 current design
T(n) = 4T(n/2) + n.

Master Theorem parameters: a = 4, b = 2, f(n) = n.

n^(log_b a) = n^(log₂4) = n².

Since f(n) = n = O(n^(2−1)), Case 1 applies. Therefore T(n) = Θ(n²).

## 3.5 M4 proposed design
T(n) = 2T(n/2) + n.

Here a = 2, b = 2, f(n) = n, and n^(log₂2) = n. Since f(n) = Θ(n^(log_b a)), Case 2 applies. Therefore T(n) = Θ(n log n).

## 3.6 M5
T(n) = 2T(n/2) + n log₂n.

Here a = 2, b = 2 and n^(log₂2) = n. The extra factor log n means f(n) = Θ(n log n). The standard extended Master Theorem Case 2 gives:

T(n) = Θ(n log²n).

## 3.7 Summary

| Component | Time complexity |
|---|---|
| M1 | Θ(n²) |
| M2 | Θ(n) |
| M3-S1 | Θ(n) worst case |
| M3-S2 | Θ(log n) worst case |
| M4 current | Θ(n²) |
| M4 proposed | Θ(n log n) |
| M5 | Θ(n log²n) |
| Report generator | Θ(n²) |
