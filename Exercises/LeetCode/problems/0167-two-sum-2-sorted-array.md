# Two Sum || - Input Array Is Sorted. Title

Pattern: Two pointers | Difficulty: Medium | Date: 22-07-2026

## The problem in my own words
We have a sorted (increasing order) integer array.
We need to find indices of the 2 numbers which add up to the target.
Return indices + 1, like [index1 + 1, index2 + 2]


## First idea

What I thought of before writing any code.
I am thinking of iterating the array sum the 2 numbers next to each other,
check if they match the target, return the indices, if not continue.
This is the brute force.
The time complexity will be O(n)
But I think since the array is sorted we can improve it by O(n/2).

First I was thinking of only comparing `if(number[i] + number[i + 1] === target)` but we need to indices.
We need to compare the first element with all others. So it will be 2 nested loops.
Ofcourse the brute force version. Which will be O(n^2).

## Brute force

Approach, and why it is slow. Time / Space:
Time complexity is O(n^2)
Since we need to iterate over the array with 2 nested loops

```ts
function twoSum(numbers: number[], target: number): number[] {
    
    for (let i = 0; i < numbers.length; i++) {
        for(let j = i + 1; j < numbers.length; j++) {
            if(numbers[i] + numbers[j] === target) {
                return [i + 1, j + 1]
            }
        }
    }
};
```

## Better solution

What made it click. Time / Space:
I think since the array is sorted, we can just find the middle index,
sum the first index with the middle one, if it less than target, continue with the upper part and find the middle and so one.

I had an idea like this but it's not gonna work:
Because if index 0 and 6 are smaller than target we can not forget about index 0 up to 6.
Answer might be index 1 + index 8.

It's not binary search neither recursive.
It should be two pointer.

```
// target 59
    // [1, 3, 5, 6, 7, 8, 12, 22, 33, 34, 54, 63] - Length 12
    // 12 / 2 = 6
    // Start comparing index 0 with index 6 and see if it smaller than target or not.
```

```ts
function twoSum(numbers: number[], target: number): number[] {
    let i = 0
    let j = numbers.length - 1

    while (i < j) {
	const sum = numbers[i] + numbers[j]
        if(sum === target) {

            return [i + 1, j + 1]

        } else if(sum < target) {
            i++
            continue
        } else {
            j--
            continue
        }

        i++
        j--
    }

};
```

## What I learned

 - 

## Revisit on

YYYY-MM-DD
