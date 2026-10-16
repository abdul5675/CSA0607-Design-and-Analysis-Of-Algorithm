# Task 2 — Basic Operation

## 2.1 Definition
A basic operation is the repeated operation that most strongly determines how execution time grows as input size n increases.

## 2.2 Basic operations

| Module | Input size | Dominant operation |
|---|---|---|
| M1 | n products | Comparing a product pair's title and seller |
| M2 | n requests | `Audit(Request[j])` |
| M3-S1 | n catalogue entries | Comparing target with each scanned entry |
| M3-S2 | n sorted-index entries | Comparing target with the midpoint key |
| M4 | n customer-product records | Recursive subproblem work and merge work |
| M5 | n sales records | Recursive calls and n log₂n sorting/processing work |
| Report generator | n records | Operations described by 3n² + 10n log₂n + 50 |

## 2.3 M1 exact operation count
For i = 0, the inner loop runs n−1 times. For i = 1, it runs n−2 times. The final outer iteration runs once.

C(n) = (n−1) + (n−2) + ... + 2 + 1

Using the arithmetic-series formula:

C(n) = n(n−1)/2.

At n = 1,000,000:

C(n) = 1,000,000 × 999,999 / 2
     = 499,999,500,000 comparisons.

## 2.4 M2 exact operation count
The inner-loop counts are 1, 2, 4, ..., 2^k, where 2^k is the largest power of two strictly less than n.

A(n) = 1 + 2 + 4 + ... + 2^k
     = 2^(k+1) − 1.

Since k = ceil(log₂n) − 1 for n > 1:

A(n) = 2^ceil(log₂n) − 1.

For n = 1,024:

A(n) = 2^10 − 1 = 1,023.

The operation count is less than 2n and is Θ(n), not Θ(n log n). The team member's claim incorrectly multiplies the number of outer-loop iterations by the maximum inner-loop length instead of summing the actual lengths.

## 2.5 Counting convention
For the theoretical audit, each module uses the operation stated in its definition. In the Python experiment, primitive key comparisons and recursive/loop work must not be confused with wall-clock time. The report distinguishes exact operation counts from estimated times.
