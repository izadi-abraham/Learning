# Merge Intervals

Pattern: Intervals | Difficulty: Medium | Date: 22-07-2026

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
- Iterate over the intervals
- The first key question: "What property would make it much easier to detect overlapping intervals?"
- I am thinking if either index1 or index2 of an interval is biiger than another interval's index1 and smaller
it's index2 then that's an interval.
- So each interval I iterate I need to keep the start and end of that interval, so in the next interval I can
compare with previous ones. Maybe a map of "index of interval => interval" like "0": [1,3] and "1": [2,6].
- Now when iterating index 2 which is [8, 10] I can compare if  1 < 8 < 3, 2 < 8 < 6, 1 < 10 < 8, ...

---

1-Sort by interval start.
2-Put the first interval into result.
3-Iterate from the second interval onward.
4-Compare only with the last interval in result.
5-If they overlap:
 5.1-update the last interval's end.
 5.2-Otherwise:push the current interval into result

## First Version
I have this first version after some help but I noticed the sorting doesn't work always.
Let's see this case "[[4,5],[1,4],[0,1]]", that doesn't move [0,1] to the first index, it only moves that once.
In the ideal sort algorithm if you find a must change the position element, you need to compare again,
the just changed position with before element as well and continue to the begining if it keeps need changing position.
A recursive can solve this easily.

```ts
function merge(intervals: number[][]): number[][] {
    
    console.log("input:", intervals)

    // sort the input interval
    for (let i = 0; i < intervals.length - 1; i++) {
        if(intervals[i][0] > intervals[i + 1][0]) {
            const temp = intervals[i]
            intervals[i] = intervals[i + 1]
            intervals[i + 1] = temp
        }
    }

    console.log("sorted:", intervals)
    
    const result = [intervals[0]]
    let i = 1;

    while(i < intervals.length) {
        const lastInterval = result[result.length - 1]
        // detect overlap & merge
        if(lastInterval[1] >= intervals[i][0]) {
            result[result.length - 1] = [lastInterval[0], Math.max(lastInterval[1], intervals[i][1])]
        } else {
            result.push(intervals[i])
        }
        
        i++
    }

    return result
};
```

## Better solution

What made it click. Time / Space:
This is an improved version. The sort part is replaced by JS Array.sort() and the mergin is improved for readability.

Time complexity = sort (depends on the engine implementation but can be concidered as O(n log n)),
and the mergin part is O(n). Putting them together the O(n log n) will dominate so that's the answer.

Space complexity = result array is O(n), and the sort again depends on the implementation algorithm and it might be
O(n) or O(n log n). Those algorithms use temporary memory.

```ts
function merge(intervals: number[][]): number[][] {
    intervals.sort((a, b) => a[0] - b[0])
    
    const result = [intervals[0]]
    let i = 1;

    while(i < intervals.length) {
        const lastInterval = result[result.length - 1]
        if(lastInterval[1] >= intervals[i][0]) {
            lastInterval[1] = Math.max(lastInterval[1], intervals[i][1])
        } else {
            result.push(intervals[i])
        }
        
        i++
    }

    return result
};
```

## What I learned

-

## Revisit on

YYYY-MM-DD
