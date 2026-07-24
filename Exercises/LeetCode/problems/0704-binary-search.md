# Binary Search

Pattern: Binary Search | Difficulty: Easy | Date: 23-07-2026

## The problem in my own words
Given a sorted array of integers and a target, return the index of the array element which is equal to our target.
If doesn't exist, return -1.

## First idea
If the array is sorted, so we can just find the middle index. length / 2.
compare the target with middle element, if it's bigger continue with second half,
if smaller continue with first half and so on...
This will be recursive for sure. I mean recursive is cleaner version.


## First Version

Approach, and why it is slow. Time / Space:

```ts
function search(nums: number[], target: number): number {


    return (function binSearch(left: number, right: number) {
        
        if(left > right) {
            return -1
        }
        
        const middleIdx = Math.floor((right + left) / 2)

        if (target === nums[middleIdx]) {
            return middleIdx
        } else if(target > nums[middleIdx]) {
            return binSearch(nums, target, middleIdx + 1, right)
        } else {
            return binSearch(nums, target, left, middleIdx - 1)
        }
    })(0, nums.length - 1)
};
```

## Better solution

What made it click. Time / Space:
The recursion was a tail recursion, the stacked function calls in the call stack,
were waiting for nothing, they just simply returning what was the answer in the last call.
In such cases recursion is not doing anything specific. That might be even better to not use it,
In order to simply the function call overheads.
This is the loop version (non-recursive).

Time complexity is O(log n) on both recursion and iterative
Space complexity on the iterative version is O(1) but on the recursive version,
it will be O(log n), since we push to our stack half of the length so in the worst case,
we will have log n items in our stack.

```ts
function search(nums: number[], target: number): number {

    let left = 0
    let right = nums.length - 1

    while(left <= right) {   
        const midIdx = Math.floor((right + left) / 2)

        if (target === nums[midIdx]) {
            return midIdx
        } else if(target > nums[midIdx]) {
            left = midIdx + 1
        } else {
            right = midIdx - 1
        }
    }

    return -1
};
```

## What I learned

-

## Revisit on

YYYY-MM-DD
