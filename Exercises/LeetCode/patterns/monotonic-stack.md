# Monotonic Stack

A stack whose values stay sorted (increasing or decreasing). You push indices and pop them the moment the current element breaks the order — the pop is where the answer gets resolved.

## Use when

- "Next / previous greater (or smaller) element"
- You need, for each item, the distance to something bigger/smaller ahead
- A brute force compares every item with everything after it (O(n²))

## Complexity

Time: O(n) — each index is pushed once and popped at most once

Space: O(n) — the stack

## Problems

- [0739 Daily Temperatures](../problems/0739-daily-temprature.md)

## Related patterns

- Two Pointers
- Sliding Window

## Real-world examples

- Stock span (days until a higher price)
- Largest rectangle in a histogram
