
# 0217. Contains Duplicate

## Pattern

Hash Set

## Difficulty

Easy

## Time Complexity

O(n)

## Space Complexity

O(n)

## My first idea

Use an object as a hash map to remember numbers already seen.

## Final solution

Use a JavaScript Set because the value itself isn't important - only whether it has been seen before.

## What I learned

- A Set is the right Data structure when only existence matters.
- JavaScript object keys are string.
- Set expresses the intent better than an object used as a map.
- Return early as soon as the duplicate is found.

## Interview notes

Typical clues that suggest using a Set:


- Detect duplicates
- Check if something already exist.
- Fast lookup.
- "Have I seen this before?"

## Review

Review againg in one week.

