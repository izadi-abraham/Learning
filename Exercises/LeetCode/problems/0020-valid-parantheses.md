# Valid Parantheses

Pattern: Stack | Difficulty: Easy | Date: 25-07-2026 - 26-07-2026

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

## Brute force

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

## Version 2
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

## Version 3

-

## Revisit on

YYYY-MM-DD
