# Task 12 — Design Challenge: ShopSphere Scalability Decision

## Scenario
The catalogue grows from 100,000 to 1,000,000 products. The nightly processing window is 10 minutes (600 seconds), and the server is assumed to execute 10^8 basic operations per second.

## Estimated operation counts at n = 1,000,000

### M1
C(n) = n(n−1)/2
     = 499,999,500,000 operations.

Estimated time = 499,999,500,000 / 100,000,000
              = 4,999.995 seconds
              ≈ 83.33 minutes.

M1 fails the 10-minute window under the given model.

### M2
A(n) = 2^ceil(log₂n) − 1
     = 2^20 − 1
     = 1,048,575 audit operations.

Estimated time ≈ 0.01049 seconds.

M2 passes the simplified model.

### S2
log₂(1,000,000) ≈ 19.93, so about 20 halving levels are required. At roughly 20–21 key comparisons, the model estimates approximately 0.0000002 seconds at 10^8 operations/second. This is an algorithmic estimate, not a realistic end-to-end database latency guarantee.

### M4 current
T(n) = 4T(n/2) + n has Θ(n²) complexity. Under a simplified recurrence model with T(1) = 1, the exact count for powers of two is T(n) = 2n² − n. For n = 1,000,000, this model gives 1,999,999,000,000 operations, or approximately 19,999.99 seconds (about 333.33 minutes). It fails.

### M4 redesign
T(n) = 2T(n/2) + n. For powers of two and T(1) = 1, the recurrence gives T(n) = n log₂n + n. At n = 1,000,000, the approximate estimate using log₂n is 20,931,569 operations, or about 0.2093 seconds. This is a recurrence-model estimate.

### M5
T(n) = 2T(n/2) + n log₂n. For n = 2^k and T(1) = 1, the recurrence gives approximately T(n) = n[1 + k(k+1)/2]. For n = 1,000,000, k ≈ log₂n ≈ 19.93; using this approximation gives about 2.09 × 10^8 operations, or about 2.1 seconds. Since 1,000,000 is not a power of two, treat this as an estimate, not an exact count.

## Decision table

| Module | Estimated operations | Estimated time | 10-minute window |
|---|---:|---:|---|
| M1 | 499,999,500,000 | 83.33 min | Fail |
| M2 | 1,048,575 | 0.0105 s | Pass |
| S2 | About 20–21 comparisons | About 0.0000002 s | Pass in model |
| M4 current | About 2.0 × 10^12 | About 333 min | Fail |
| M4 redesign | About 2.09 × 10^7 | About 0.21 s | Pass in model |
| M5 | About 2.1 × 10^8 | About 2.1 s | Pass in model |

## Recommended redesign
- Replace M1 pairwise comparisons with a hash table on a normalized title + seller identifier; sorting and adjacent comparison is an alternative.
- Remove replication in M4 and use the proposed Θ(n log n) recurrence.
- Use an indexed lookup for S2 and maintain index consistency as products are added daily.
- Keep M2, since its count is linear.
- Profile M5 and the report generator on representative workloads. The report generator's Θ(n²) growth means it can also become a bottleneck.

## Production considerations
The server's stated operation rate is an idealized assumption. Real deployment must account for disk and network I/O, database indexing, locks, cache behavior, concurrency, memory, and data skew. Use monitoring and production-like load tests before guaranteeing the deadline.

## Final defense
The redesign priorities are M1 and current M4 because their quadratic operation counts exceed the 600-second budget in the supplied model. The proposed M4 design, indexed search, and linear M2 have better growth rates. M5 and the report generator require benchmarking and optimization if measured runtime approaches the deadline.
