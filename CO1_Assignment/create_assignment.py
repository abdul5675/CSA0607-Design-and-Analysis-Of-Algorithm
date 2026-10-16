
from pathlib import Path
import math
import csv
import zipfile
import textwrap

ROOT = Path(__file__).resolve().parent

FOLDERS = [
    "Task_1_Algorithm_Design",
    "Task_2_Basic_Operation",
    "Task_3_Mathematical_Complexity",
    "Task_4_Case_Analysis",
    "Task_5_Asymptotic_Analysis",
    "Task_6_Recurrence_Formulation",
    "Task_7_Recurrence_Solution",
    "Task_8_Implementation_Testing/Source_Code",
    "Task_9_Experimental_Performance",
    "Task_10_Theory_vs_Experiment",
    "Task_11_Final_Recommendation",
    "Task_12_Design_Challenge",
    "Report/Source_Code_Screenshots",
    "Report/Output_Screenshots",
    "Report/Analysis",
    "Report/Tables_and_Graphs",
    "Report/Documentation",
]

for folder in FOLDERS:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

answers = {
"Task_1_Algorithm_Design/Answer.md": r"""
# Task 1 — Algorithm Design

## 1.1 Aim
To audit the scalability of ShopSphere, an e-commerce platform growing from 100,000 to 1,000,000 products, by analysing the algorithms used in five backend modules.

## 1.2 Objectives
1. Identify the input size and dominant basic operation of each module.
2. derive operation counts and asymptotic complexity.
3. Solve the given recurrences using substitution and the Master Theorem.
4. Estimate execution time using the specified server rate of 10^8 basic operations per second.
5. Recommend algorithmic redesigns for the 10-minute nightly processing deadline.

## 1.3 Modules and algorithms

### M1 — Duplicate-Listing Detector
The routine compares each product with every later product. Two products are considered duplicates when both title and seller match.

**Pseudocode**
```text
FOR i = 0 TO n - 2
    FOR j = i + 1 TO n - 1
        IF title[i] = title[j] AND seller[i] = seller[j]
            MarkDuplicate(j)
        END IF
    END FOR
END FOR
```

The input size is n products. The dominant operation is the pairwise comparison. The number of pairs grows quadratically.

### M2 — API Rate Limiter
The outer loop doubles i on every iteration, while the inner loop performs i audit operations.

**Pseudocode**
```text
i = 1
WHILE i < n
    FOR j = 0 TO i - 1
        Audit(Request[j])
    END FOR
    i = 2 * i
END WHILE
```

The audit counts are 1, 2, 4, 8, and so on. Their sum is a geometric series and is Θ(n).

### M3 — Product Search
S1 performs sequential search on an unsorted catalogue. S2 performs binary search on a sorted index.

**S1 pseudocode**
```text
FOR i = 0 TO n - 1
    IF catalogue[i] = target
        RETURN i
    END IF
END FOR
RETURN NOT_FOUND
```

**S2 pseudocode**
```text
low = 0
high = n - 1
WHILE low <= high
    mid = floor((low + high) / 2)
    IF index[mid] = target
        RETURN mid
    ELSE IF index[mid] < target
        low = mid + 1
    ELSE
        high = mid - 1
    END IF
END WHILE
RETURN NOT_FOUND
```

Binary search requires a sorted index. Maintaining that index has an update cost that should be considered when new products are added.

### M4 — Recommendation Engine
Current design: T(n) = 4T(n/2) + n. The four recursive calls arise from replicated partitions.

Proposed design: T(n) = 2T(n/2) + n. Removing replicated partitions reduces the number of recursive subproblems.

### M5 — Sales Analytics Engine
The engine splits the data into two halves and performs Θ(n log n) work to sort/process data at each recursive level.

Recurrence: T(n) = 2T(n/2) + n log₂n.

## 1.4 Overall design conclusion
The audit must examine operation counts, time complexity, auxiliary space, and the actual workload. M1 and the current M4 design are the main quadratic bottlenecks.
""",

"Task_2_Basic_Operation/Answer.md": r"""
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
""",

"Task_3_Mathematical_Complexity/Answer.md": r"""
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
""",

"Task_4_Case_Analysis/Answer.md": r"""
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
""",

"Task_5_Asymptotic_Analysis/Answer.md": r"""
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
""",

"Task_6_Recurrence_Formulation/Answer.md": r"""
# Task 6 — Recurrence Formulation

## M4 current design
T(n) = 4T(n/2) + n.

The routine makes four recursive calls, each on half-sized data, and spends linear work combining the results.

## M4 proposed redesign
T(n) = 2T(n/2) + n.

Removing replicated partitions reduces the number of recursive calls from four to two.

## M5 sales analytics
T(n) = 2T(n/2) + n log₂n.

There are two half-sized recursive subproblems and n log₂n work for sorting/processing at the current level.

## S2 binary search
T(n) = T(n/2) + 1, with T(1) = 1 under the assignment's simplified comparison-count model. Each step halves the search range and adds one comparison-level unit.

## Why recurrence relations matter
A recurrence expresses the cost for an input of size n using costs for smaller inputs. It lets us derive the growth rate without running the program for every possible n.
""",

"Task_7_Recurrence_Solution/Answer.md": r"""
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
""",

"Task_8_Implementation_Testing/Answer.md": r"""
# Task 8 — Implementation and Testing

The source code is in `Source_Code/shopsphere_audit.py`. Run it using:

```bash
python Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

The program calculates the exact M1 pair count, M2 geometric sum, S2 halving-level estimate, M4/M5 recurrence-model estimates, and the report-generator operation count.

The program is a transparent operation-count model. It does not execute a real e-commerce database or implement the actual production modules. The recurrence estimates use a stated base case and are not substitutes for production benchmarking.

## Test cases
1. n = 1: no M1 pairs; M2 loop has no iterations.
2. n = 2: M1 performs one pair comparison; M2 performs one audit.
3. n = 1,024: M2 performs 1,023 audits.
4. n = 1,000,000: M1 performs 499,999,500,000 pair comparisons.
5. Search target first/middle/last/absent: used to explain S1 case counts and S2 logarithmic search.
""",

"Task_9_Experimental_Performance/Answer.md": r"""
# Task 9 — Experimental Performance

The supplied Python model generates a CSV operation-count table for n = 100,000 and n = 1,000,000, and calculates estimates for the given server rate.

Assumed rate: 10^8 basic operations per second.

Estimated time = estimated operation count / 10^8.

These times are theoretical estimates based on the assignment's simplified server-rate assumption. They are not measured wall-clock timings. Actual timing requires an implementation and a benchmark environment.

To run:
```bash
python Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

The CSV is saved in `Task_9_Experimental_Performance/operation_estimates.csv`. Graphs are not invented. Add measured benchmark graphs only after implementing and running representative workloads.
""",

"Task_10_Theory_vs_Experiment/Answer.md": r"""
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
""",

"Task_11_Final_Recommendation/Answer.md": r"""
# Task 11 — Final Recommendation

## Recommended actions
1. **Redesign M1.** Use a hash table keyed by normalized product title and seller ID. Expected processing time can be O(n), assuming effective hashing and manageable collisions. Alternatively, sort by the combined key and compare adjacent records in O(n log n).
2. **Adopt the proposed M4 design.** Removing replicated partitions changes the recurrence from Θ(n²) to Θ(n log n).
3. **Use S2 for repeated catalogue lookups.** Maintain a sorted index or database index. Account for index maintenance as products are inserted or updated.
4. **Retain M2.** Its geometric operation count is Θ(n), and the exact count is less than 2n.
5. **Profile M5 and the report generator.** M5 is Θ(n log²n); the report generator is Θ(n²). Benchmark real data and optimize if they threaten the processing window.

## Conclusion
M1 and the current M4 design are the primary redesign priorities. The M4 redesign, indexed product search, and linear-time M2 provide substantially better scalability. M5 and the report generator should be measured and monitored before production decisions are finalized.
""",

"Task_12_Design_Challenge/Answer.md": r"""
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
""",
}

# Write the 12 task answer files.
for relative_path, content in answers.items():
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")

# Runnable operation-count model.
source = r'''
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "Task_9_Experimental_Performance"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SERVER_OPS_PER_SECOND = 100_000_000
SIZES = [100_000, 1_000_000]

def m1_pairs(n):
    return n * (n - 1) // 2

def m2_audits(n):
    if n <= 1:
        return 0
    return 2 ** math.ceil(math.log2(n)) - 1

def s2_levels(n):
    if n <= 0:
        return 0
    return math.ceil(math.log2(n + 1))

def m4_current(n):
    # Exact recurrence count for powers of two, T(1)=1.
    k = round(math.log2(n))
    if n == 2 ** k:
        return 2 * n * n - n
    # Recurrence-level estimate for other n.
    return int(2 * n * n)

def m4_redesign(n):
    # Exact for powers of two, T(1)=1; approximate otherwise.
    k = round(math.log2(n))
    if n == 2 ** k:
        return n * k + n
    return int(n * math.log2(n) + n)

def m5_estimate(n):
    # Recurrence-level estimate; exact formula applies when n is a power of two.
    k = math.log2(n)
    return int(n * (1 + k * (k + 1) / 2))

def report_generator(n):
    return int(3 * n * n + 10 * n * math.log2(n) + 50)

rows = []
for n in SIZES:
    modules = [
        ("M1 Duplicate Listing", m1_pairs(n)),
        ("M2 API Rate Limiter", m2_audits(n)),
        ("M3 S2 Binary Search", s2_levels(n)),
        ("M4 Current", m4_current(n)),
        ("M4 Proposed", m4_redesign(n)),
        ("M5 Sales Analytics", m5_estimate(n)),
        ("Report Generator", report_generator(n)),
    ]
    for module, operations in modules:
        rows.append({
            "module": module,
            "n": n,
            "estimated_operations": operations,
            "estimated_seconds_at_1e8_ops_per_second":
                operations / SERVER_OPS_PER_SECOND,
            "within_600_seconds_under_model":
                operations / SERVER_OPS_PER_SECOND <= 600,
            "measurement_type": "theoretical operation-count estimate, not measured runtime"
        })

csv_path = OUTPUT_DIR / "operation_estimates.csv"
with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("ShopSphere operation-count audit")
print("Assumed server rate:", f"{SERVER_OPS_PER_SECOND:,}", "operations/second")
print("Nightly window: 600 seconds")
print("-" * 90)
for row in rows:
    print(
        f"{row['module']:24s} n={row['n']:>9,} "
        f"ops={row['estimated_operations']:>18,} "
        f"time={row['estimated_seconds_at_1e8_ops_per_second']:>12.6f}s "
        f"within_window={row['within_600_seconds_under_model']}"
    )
print("\nCSV saved to:", csv_path)

try:
    import matplotlib.pyplot as plt
    graph_dir = ROOT / "Report" / "Tables_and_Graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    for module in sorted(set(r["module"] for r in rows)):
        module_rows = [r for r in rows if r["module"] == module]
        xs = [r["n"] for r in module_rows]
        ys = [r["estimated_seconds_at_1e8_ops_per_second"] for r in module_rows]
        plt.plot(xs, ys, marker="o", label=module)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input size n (log scale)")
    plt.ylabel("Estimated time in seconds (log scale)")
    plt.title("ShopSphere theoretical operation-count estimates")
    plt.legend(fontsize="small")
    plt.grid(True, which="both", linestyle=":")
    plt.tight_layout()
    graph_path = graph_dir / "estimated_time_scaling.png"
    plt.savefig(graph_path, dpi=180)
    plt.close()
    print("Graph saved to:", graph_path)
except ImportError:
    print("Matplotlib not installed; skipping graph.")
    print("Install it with: python -m pip install matplotlib")
'''
source_path = ROOT / "Task_8_Implementation_Testing" / "Source_Code" / "shopsphere_audit.py"
source_path.write_text(textwrap.dedent(source).strip() + "\n", encoding="utf-8")

# Build the combined report from all task answers.
report_path = ROOT / "Report" / "Documentation" / "CO1_Assignment_Report.md"
report_parts = [
    "# CO1 Assessment — ShopSphere Scalability Audit\n",
    "**Course:** CSA06 — Design and Analysis of Algorithms  \n",
    "**Student registration number:** 192524358  \n",
    "**Student name:** Shaik Abdul Razak\n\n",
    "## Abstract\n\n"
    "This report analyses ShopSphere's duplicate detection, API rate limiting, "
    "product search, recommendation engine, sales analytics, and report generator. "
    "It applies operation counting, asymptotic notation, recurrence solving, and "
    "the Master Theorem to evaluate scalability as the catalogue reaches one million products.\n",
]
for relative_path, content in answers.items():
    report_parts.append("\n\n---\n\n" + content)
report_parts.append(
    "\n\n---\n\n## References\n\n"
    "1. Cormen, Leiserson, Rivest, and Stein, *Introduction to Algorithms*, MIT Press.\n"
    "2. Python documentation, https://docs.python.org/3/ .\n"
    "3. Assessment brief: DAA CO1-AT1, ShopSphere Scalability Audit.\n"
)
report_path.write_text("".join(report_parts), encoding="utf-8")

# README
readme = """# CO1 Assignment — ShopSphere Scalability Audit

This project analyses the algorithms specified in the ShopSphere assessment.

## Contents
- 12 task folders containing detailed answers.
- Python operation-count model in `Task_8_Implementation_Testing/Source_Code/`.
- Combined report in `Report/Documentation/CO1_Assignment_Report.md`.
- CSV operation estimates in `Task_9_Experimental_Performance/`.
- Optional graph in `Report/Tables_and_Graphs/`.

## Run the program
From the repository root, run:

```powershell
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

If running from inside `CO1_Assignment`, run:

```powershell
python Task_8_Implementation_Testing/Source_Code/shopsphere_audit.py
```

Optional graphs require Matplotlib:

```powershell
python -m pip install matplotlib
```

## Important interpretation
Times in the CSV are operation-count estimates using the assessment's assumption of 10^8 basic operations per second. They are not measured production timings. The model documents assumptions, especially for non-power-of-two recurrence estimates.

## Screenshots
Run the program and capture genuine screenshots of the source code and terminal output. Save them in `Report/Source_Code_Screenshots/` and `Report/Output_Screenshots/`. Do not submit fabricated screenshots.

## GitHub
Review the generated files, then use VS Code Source Control to stage, commit, and push them to the existing repository.
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

for folder in FOLDERS:
    p = ROOT / folder
    if p.is_dir() and not any(p.iterdir()):
        (p / ".gitkeep").touch()

# Create ZIP while excluding temporary Python cache files.
zip_path = ROOT.parent / "CO1_Assignment.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in ROOT.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts:
            zf.write(path, path.relative_to(ROOT.parent))

print("\nSUCCESS: Task answers and report files created.")
print("Project folder:", ROOT)
print("Combined report:", report_path)
print("Python source:", source_path)
print("ZIP file:", zip_path)
print("\nNext: run shopsphere_audit.py and inspect the CSV/graph.")
