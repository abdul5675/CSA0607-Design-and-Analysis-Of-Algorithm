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
