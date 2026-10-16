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
