# 0020. Valid Parantheses

Pattern: Stack | Difficulty: Easy | Date: 2026-07-25 – 2026-07-26

## The problem in my own words
Sting s contains '(', ')', '[', ']', '{', '}'.
Return true if our string s is valid.
Retrun false if it's not a valid string.

Valid means:
- Open brackets must be closed with the same type.
- Open bracets must be closed in the correct oreder.
- Every close bracket has a corresponding open bracket of the same type. 

## First idea

- I need to have a map of each character and it's type, whether it is close or open. (can be a simple object)
- I need an array to be my stack. To know whether I have something waiting (open bracket) to be closed, and if yes what type is it.
- Iterating over the string and trying to see what do we have in our array (stack data structure)
- When iterating I check my current char:
 - If this is a close and my array is empty, it's wrong for sure.
 - If this is a close and 
 - If this is open just push it to array.
- If s is finished now I need to match everything I have.

## 1st Version

Approach, and why it is slow. Time / Space:

```ts
const stack = []

  const bracketType = new Map([
      ['(', {
        'shape': 'open',
        'type': 1
      }],
      [')', {
        'shape': 'close',
        'type': 1
      }],
      ['[', {
        'shape': 'open',
        'type': 2
      }],
      [']', {
        'shape': 'close',
        'type': 2
      }],
      ['{', {
        'shape': 'open',
        'type': 3
      }],
      ['}', {
        'shape': 'close',
        'type': 3
      }]
  ])

  let i = 0

  while(i < s.length && stack.length) {
    const stringChar = bracketType.get(s[i])
    const stackChar = bracketType.get(stack[stack.length - 1])

    if(stringChar.shape === 'close' && !stack.length) {
      console.log("false")
      return false
    }

    if(
      stringChar.shape === 'close' &&
      stackChar.shape === 'open' &&
      stringChar.type === stackChar.type
    ) {
      stack.pop()
    }

    if(stringChar.shape === stackChar.shape) {
      stack.push()
    }

    i++
  }

  console.log("true")

  return !stack.length

```

## 2nd Version
There is a bug in the version 1.
I need to think more and trace further to understand it.
It fails on this input "(]".

- I found the bug and fixed it. This version works but for sure now it needs improvements.

```ts
function isValid(s: string): boolean {

  const stack = []

  const bracketType = new Map([
      ['(', {
        'shape': 'open',
        'type': 1
      }],
      [')', {
        'shape': 'close',
        'type': 1
      }],
      ['[', {
        'shape': 'open',
        'type': 2
      }],
      [']', {
        'shape': 'close',
        'type': 2
      }],
      ['{', {
        'shape': 'open',
        'type': 3
      }],
      ['}', {
        'shape': 'close',
        'type': 3
      }]
  ])

  let i = 0

  while(i < s.length) {
    const stringChar = bracketType.get(s[i])
    const stackChar = bracketType.get(stack[stack.length - 1])

    if(stringChar.shape === 'close' && !stack.length) {
      return false
    }

    if(
      stringChar.shape === 'close' &&
      stackChar?.shape === 'open' &&
      stringChar.type === stackChar?.type
    ) {
      stack.pop()
    } else {
      stack.push(s[i])
    }

    i++
  }

  return !stack.length
};
```

## 3rd Version
And the 3rd version. In this one the map is simplifed, the metadata is removed.
The confusion for me was, how can I check if my current s[i] is the same type of the top of stack.
I tried to use the map in all my conditions, so I was thinking if I want to implement this condition which exist in my previous impelentation:

```ts
stringChar.shape === 'close' &&
stackChar?.shape === 'open' &&
stringChar.type === stackChar?.type
```
Then for the last check, how can I get the type of my bracket on top of my stack. It should be an opening one,
and opening in the map will be undefined.

But later I noticed if I get the s[i] from map and check with current top of stack (note that I don't get the top of stack from map, I check with it's raw value),
then if they are equal it means they are the same type :)


```ts
function isValid(s: string): boolean {
    const stack = []

  const pairs = new Map([
      [')', '('],
      [']', '['],
      ['}', '{'],
  ])

  let i = 0

  while(i < s.length) {

    if(pairs.get(s[i])) {
      if(!stack.length || pairs.get(s[i]) !== stack[stack.length - 1]) {
        return false
      }

      stack.pop()
    }

    if(pairs.get(s[i]) === undefined) {
      stack.push(s[i])
    }

    i++
  }

  return !stack.length
};
```

- Time complexity would be O(n). Since we iterate over s once.
- Space is also O(n) since we create a stack in the worst case scenarion as long as a string.

And better wording of above explanation:

"We process each character once, and each character can be pushed onto and popped from the stack at most one time."

That wording demonstrates that you're thinking about the algorithm's operations, not just the while loop.
