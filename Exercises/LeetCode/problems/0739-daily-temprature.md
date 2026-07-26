# Daily Tempreture

Pattern: Stack | Difficulty: Medium | Date: 26-07-2026

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

```

Time / Space complexity:

## 3rd Version

```ts

```
