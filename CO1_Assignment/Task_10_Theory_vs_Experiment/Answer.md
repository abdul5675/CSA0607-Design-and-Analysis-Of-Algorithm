# Task 10 — Theory versus Estimated Performance

Theoretical analysis predicts how costs grow as n increases. The assignment's server model converts operation estimates into approximate time, but actual execution depends on constants, data structures, memory, I/O, concurrency, and implementation details.

| Module | Theoretical complexity | Scaling interpretation |
|---|---|---|
| M1 | Θ(n²) | Doubling n roughly quadruples pair comparisons |
| M2 | Θ(n) | Doubling n roughly doubles audit operations |
| S1 worst case | Θ(n) | Doubles the maximum scan length |
| S2 | Θ(log n) | Adds about one halving level when n doubles |
| M4 current | Θ(n²) | Doubling n roughly quadruples dominant work |
| M4 proposed | Θ(n log n) | Growth is much lower than quadratic |
| M5 | Θ(n log²n) | Superlinear; benchmark with realistic data |
| Report generator | Θ(n²) | Quadratic term dominates |

Estimated operation counts and times are written to CSV by the Python model. These estimates must not be described as measured experimental timings. A real experiment should time actual implementations repeatedly on the same machine and report the mean/median, dataset size, and test conditions.
