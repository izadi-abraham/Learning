# Two Pointers

Walk two indices through the data at the same time — often one from each end moving toward the middle, or one slow and one fast. Lets you skip work a nested loop would repeat.

## Use when

- The array is sorted, or symmetry matters (palindrome)
- "Find a pair that sums to X", compare front against back
- Brute force uses two nested loops (O(n²))

## Complexity

Time: O(n) — the pointers only ever move toward each other

Space: O(1) — just the two indices

## Problems

- [0125 Valid Palindrome](../problems/0125-valid-palindrom.md)
- [0167 Two Sum II - Input Array Is Sorted](../problems/0167-two-sum-2-sorted-array.md)

## Related patterns

- Sliding Window
- Binary Search

## Real-world examples

- Merging two sorted lists
- Removing duplicates from a sorted array in place
