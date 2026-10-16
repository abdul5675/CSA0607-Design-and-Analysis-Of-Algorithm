# Task 11 — Final Recommendation

## Recommended actions
1. **Redesign M1.** Use a hash table keyed by normalized product title and seller ID. Expected processing time can be O(n), assuming effective hashing and manageable collisions. Alternatively, sort by the combined key and compare adjacent records in O(n log n).
2. **Adopt the proposed M4 design.** Removing replicated partitions changes the recurrence from Θ(n²) to Θ(n log n).
3. **Use S2 for repeated catalogue lookups.** Maintain a sorted index or database index. Account for index maintenance as products are inserted or updated.
4. **Retain M2.** Its geometric operation count is Θ(n), and the exact count is less than 2n.
5. **Profile M5 and the report generator.** M5 is Θ(n log²n); the report generator is Θ(n²). Benchmark real data and optimize if they threaten the processing window.

## Conclusion
M1 and the current M4 design are the primary redesign priorities. The M4 redesign, indexed product search, and linear-time M2 provide substantially better scalability. M5 and the report generator should be measured and monitored before production decisions are finalized.
