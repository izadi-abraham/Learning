# Sliding Window

Keep a window `[left, right]` over a sequence. `right` always moves forward; `left` only moves when the window breaks a rule. You track the answer as the window grows and shrinks instead of recomputing from scratch.

## Use when

- Longest / shortest / count of substrings or subarrays meeting a condition
- The answer is a contiguous run
- Brute force re-scans overlapping ranges (O(n²))

## Complexity

Time: O(n) — each element enters and leaves the window once

Space: O(k) — usually a map/count of what is inside the window

## Problems

- [0003 Longest Substring Without Repeating Characters](../problems/0003-longest-substring-without-repeating-characters.md)
- [0424 Longest Repeating Character Replacement](../problems/0424-longest-repeating-character-replacement.md)

## Related patterns

- Two Pointers
- Hash Map

## Real-world examples

- Rate limiting (requests in the last N seconds)
- Rolling averages over a stream
