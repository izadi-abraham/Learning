# Valid Anagram. Title

Pattern: | Difficulty: Easy | Date: 21-07-2026

## The problem in my own words

Given 2 strings "s" and "t", retrun true if "t" is an anagram of "s". (if all the characters of "t" exist in "s").

## First idea

What I thought of before writing any code.



## Brute force

Approach, and why it is slow. Time / Space:
After using Map, they ask me to solve this without a Map
```ts
function isAnagram(s: string, t: string): boolean {
    
    if (s.length !== t.length) {
        return false
    }

    const charCount: Record<string, number> = {}

    for (const char of s) {
        const count = charCount[char]
        
        charCount[char] = count === undefined ? 1 : count + 1
    }

    for (const char of t) {
        const count = charCount[char]
        
        if (count === 0 || count === undefined) {
          return false
        }

        charCount[char] = count - 1
    }

    return true
};

```

## Solution No.1

```ts
function isAnagram(s: string, t: string): boolean {
    
    if (s.length !== t.length) {
        return false
    }

    const stringMap = new Map()

    for (const char of s) {
        stringMap.set(char, stringMap.has(char) ? stringMap.get(char) + 1 : 1)
    }

    for (const char of t) {
        if (!stringMap.has(char) || stringMap.get(char) === 0) {
          return false
        }

        stringMap.set(char, stringMap.get(char) - 1)
    }

    return true
};

```

## Solution No.2

Decreased number of the lookup to map and improved naming
What made it click. Time / Space:

```ts
function isAnagram(s: string, t: string): boolean {
    
    if (s.length !== t.length) {
        return false
    }

    const charCount = new Map<string, number>()

    for (const char of s) {
        const count = charCount.get(char)
        
        charCount.set(char, count === undefined ? 1 : count + 1)
    }

    for (const char of t) {
        const count = charCount.get(char)
        
        if (count === 0 || count === undefined) {
          return false
        }

        charCount.set(char, count - 1)
    }

    return true
};
```

## What I learned

- time complexity O(n)
- space complexity O(n)
