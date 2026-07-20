# 0001. Two Sum

Pattern: Hash Map | Difficulty: Easy | Date: 20-07-2026

## The problem in my own words
While scanning the array, find two values that add up to the target and return where they occur.

## First idea - Brute force


```ts
function twoSum(nums: number[], target: number): number[] {
    
    // A Map which saves the numver as key and the index as value

    const membersMap = new Map<number, number[]>();

    // We need to indices - 2 loops 
    // 1- points to the first number of our sum - Ends if nums is finished
    // 2- points to our second number of our sum - Ends if is equal to nums.length - 1

    for (let i = 0; i < nums.length - 1; i++) {

        for (let j = i + 1; j < nums.length; j++) {
            const sum = nums[i] + nums[j];
            const indices = [i, j]
            
            if (sum === target) {
                return indices
            }
            
            membersMap.set(sum, indices)

        }
    }


};
```

## Better solution

What made it click. Time / Space:

The time is not the best, it is using two nested loops, it can use a map to remeber the current first element and then iterate over the array and change the second element. (??)

Time: O(n2)
Space: O(1)

I read a clue - Instead of checking every pair, I have the current number in the array and I konw the target. So now I know what number should I look for to match the target.

Imagine [2, 7, 11, 15] as nums. Now my loop is on 2, and target is 9. So 9 - 2 = 7. I need 7. Now the question can be have I seen 7 before?

### The second version of solution

```ts
function twoSum(nums: number[], target: number): number[] {
    
    // A Map which saves the numver as key and the index as value

    const membersMap = new Map<number, number>();

    // We need to indices  
    // 1- The map keeps the first element and its indice
    // 2- The loop index points to the second number of our sum

    for (let i = 0; i < nums.length; i++) {
        

        const targetInSum = target - nums[i];

        if (membersMap.has(targetInSum)) {
	   // we can add ! to say to TS that I konw this get returns a value and it won't be udnefined
	  // return [membersMap.get(targetInSum)!, i]
            return [membersMap.get(targetInSum), i]
        }

        membersMap.set(nums[i], i)

    }


};
```

### Improve naming and 

```ts
function twoSum(nums: number[], target: number): number[] {
    
    // A Map which saves the numver as key and the index as value

    const membersMap = new Map<number, number>();

    // We need to indices  
    // 1- The map keeps the first element and its indice
    // 2- The loop index points to the second number of our sum

    for (let i = 0; i < nums.length; i++) {


        const complement = target - nums[i];
	const index = memberMap.get(complement)

        if (index !== undefined) {
           
            return [index, i]
        }

        membersMap.set(nums[i], i)

    }


};

```


## What I learned

- Hash Maps let us remember useful information while iterating.
- Sometimes transforming the question makes the solution much simpler.
- Store value → index because the answer requires indices.

## Revisit on

YYYY-MM-DD
