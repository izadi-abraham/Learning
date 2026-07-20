# 0217. Contains Duplicate

Pattern: Hash Set | Difficulty: Easy | Date: 2026-07-19

## The problem in my own words

Given an array of numbers, say whether any value shows up more than once.

## First idea

Use an object as a hash map to remember numbers already seen.

## Brute force

Compare every number with every other one. Time O(n²) / Space O(1).

## Better solution

Use a JavaScript Set, because the value itself isn't important — only whether it
has been seen before. Time O(n) / Space O(n).

## What I learned

- A Set is the right data structure when only existence matters.
- JavaScript object keys are strings.
- Set expresses the intent better than an object used as a map.
- Return early as soon as the duplicate is found.

Clues that suggest a Set: detect duplicates, check if something already exists,
fast lookup, "have I seen this before?".

## Revisit on

2026-07-26
