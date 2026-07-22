# Longest Substring Without Repeating Characters.

Pattern: | Difficulty: Medium | Date: 22-07-2026

## The problem in my own words
string s is input, return the length of the longest substring without duplicate characters.

## First idea

What I thought of before writing any code.

I need to iterate over my string s.
 - save iterated characters, whenever you hit a duplicate, then you have your substring so far. Count the length of current substring, 
 - save it in the longestLength variable, if it is bigger than the current variable's value. 

## Brute force

Approach, and why it is slow. Time / Space:

Time complexity = O(n^2) - because if we are throwing away all the characters in the set and start from the begining.
consider this case:
`abcdefga` 
- We build a set of size 7, then you clear it when get to the last a and you almost build the whole thing again.
- Notice that we visited some characters twice. In longer strings this repeated building can happen many times,
- In worst case runtime is O(n^2).



Space complexity = O(n)

```ts
function lengthOfLongestSubstring(s: string): number {
  const sub = new Set<string>()
  const chars = new Map<string, number>()
  let longest = 0
  let i = 0

  while(i < s.length) {

    if(sub.has(s[i])) {
        sub.clear()
        i = chars.get(s[i])
    } else {
        sub.add(s[i])
        chars.set(s[i], i)
        const size = sub.size
        longest = size > longest ? size : longest
    }
    i++
  }

  return longest
};
```

## Better solution

What made it click. Time / Space:
- Time and Space are improved.
- For loop can make this a bit cleaner. Because right always increases by 1.


```ts
function lengthOfLongestSubstring(s: string): number {
  const chars = new Map<string, number>()
  let longest = 0
  let right = 0
  let left = 0

  while(right < s.length) {
    const charIndex = chars.get(s[right])
    
    if(charIndex !== undefined && charIndex >= left) {
        left = charIndex + 1
    }

    chars.set(s[right], right)
    const size = (right + 1) - left
    longest = Math.max(longest, size)
    right++
  }

  return longest
};
```

## What I learned

-

## Revisit on

YYYY-MM-DD
