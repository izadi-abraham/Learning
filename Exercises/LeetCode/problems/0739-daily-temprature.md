# 0739. Daily Temperatures

Pattern: Monotonic Stack | Difficulty: Medium | Date: 2026-07-26

## The problem in my own words
We have an input array of temperatures. At any index we should return an array of answer which it's corresponding index
will tesll us how many days that input index should wait until the temperature will be warmer. Basically this question (temp[i] < temp[i + j]).


## First idea
What I thought of before writing any code:
Keep 2 pointers in the temperature array move the second one until you find the waremer temeprature or the array is finished. Then move to next temperature.
This won't be the most optimal one for sure, it seems O(n^2). For each member of the array we need to check in the worst case n-1 other members.
n * n - 1 = n ^ 2

## 1st Version 
First I tried my loop and did console log to make sure my loop is as inteded.
Actually this helped me to identify a bug early.

```ts
const _ = require('lodash');

function sayHello(temperatures) {
  
  for(let i = 0; i < temperatures.length; i++) {
    console.log("i", i)
    for(let j = i + 1; j < temperatures.length; j++){
      console.log("j", j)
    }
  }
}

_.times(1, sayHello([1, 2, 4, 4]));


```


```ts
const answer = []
  
  for(let i = 0; i < temperatures.length; i++) {
    for(let j = i + 1; j <= temperatures.length; j++){
      if(temperatures[i] < temperatures[j]) {
        answer[i] = j - i
        break
      }
      answer[i] = 0
    } 
  }
  return answer
```




Time / Space complexity:

this is O(n^2) and we need to improve this version.

## 2nd Version
I am still stuck.

I can see some patterns but can't figure out exactly how to do that.

For example I was thinking if I iterate with one loop,



I only check the temp[i] < temp[i+1] and if it is not smaller then push temp[i] to an array like stack.

Move to next until you find a temp[i+1] which is bigger than temp[i] and in this case you can also compare tmep[i+1] again with top of the stack if it is bigger than
top of stack then we can fill in the distance between index of top of stack element in temp array with the distance. but I don't know what is it.


```ts

function sayHello(temperatures) {
  const answer = []
  const stack = []

  for(let i = 0; i < temperatures.length; i++) {
    
    // check if last stack item is smaller than current one
    while(stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
      answer[stack[stack.length - 1]] = i - stack.pop()
    }

    // end of temperatures
    if(temperatures[i + 1] === undefined) {
      answer[i] = 0
      break
    }
    
    // simple case - 1 day
    if(temperatures[i] < temperatures[i + 1]) {
      answer[i] = 1
    } else {
      stack.push(i)
    }
  }

  // emptying stack and put 0 - ther was no higher number than these
  while(stack.length) {
    answer[stack.pop()] = 0
  }

  return answer

}

```

This versino is improved time complexity wise.
Now we visit each item in the tem array once in the input array, and in the worst case we have to
visit all members once more in our stack array. So the time complexity is n * 2 = O(n).
The sapce complexity is O(n) as well with the same situation as the time.

## 3rd Version
We need to simplify our code a bit.

This part is extra, because the loop itself handles this case,
as this condition alwasy returns false "number < undefined => false"

```ts
 // end of temperatures
 if(temperatures[i + 1] === undefined) {
    answer[i] = 0
    break
 }
```

Also this part is not needed. Look what our while loop is doing. As long as there is something in the stack,
and the number which is resolved based on the index in the stack is smaller than current temp,
it resolves it and place the 1 in the corresponding index in answer array.
It handles waiting 1 day, 2 day, ...
So if we just push any index we visit in our temp array into stack then the while does the job for us.
No need for this part:

```ts
 // simple case - 1 day
    if(temperatures[i] < temperatures[i + 1]) {
      answer[i] = 1
    } else {
      stack.push(i)
    }
```

And the full simplified version:

```ts
const answer = []
  const stack = []

  for(let i = 0; i < temperatures.length; i++) {
    
    // check if last stack item is smaller than current one
    while(stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]){
      const previousIndex = stack.pop()
      answer[previousIndex] = i - previousIndex
    }

    stack.push(i)
  }

  // emptying stack and put 0 - ther was no higher number than these
  while(stack.length) {
    answer[stack.pop()] = 0
  }

  return answer
```

And better wording for the complexity:

Each index is pushed onto the stack exactly once and popped at most once.
Although there is a nested while loop in our for loop but the total number of 
stack operation across the entire algorithm is at most "2n" and therefore 
the overal time complexity is O(n).

