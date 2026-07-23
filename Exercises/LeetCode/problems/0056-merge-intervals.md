# Merge Intervals

Pattern: | Difficulty: Medium | Date: 22-07-2026

## The problem in my own words
We have an array of intervals. array of sub arrays (sub arrays are exactly length of 2 and index 0 is laways smaller than index 1).
Find all the onew which have overlaps and merge them into 1. Return an array of non-overlap intervals.

## First idea

What I thought of before writing any code.
- I see that we can find all intervals.
- Then from all the members the Math.min() is the index 0 and Math.max() is the index 1 of our new merged interval.
- We can get all inteval[0] s and find mind + all intervals[1] s and find max.
- I am thinking how can I determine overlaps :thinking
- Maybe that's a good idea to write the algorithm in a high level model first.
- 
- Iterate over the intervals
- 


## Brute force

Approach, and why it is slow. Time / Space:

```ts

```

## Better solution

What made it click. Time / Space:

```ts

```

## What I learned

-

## Revisit on

YYYY-MM-DD
