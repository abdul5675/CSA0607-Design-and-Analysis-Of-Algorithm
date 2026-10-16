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
