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
