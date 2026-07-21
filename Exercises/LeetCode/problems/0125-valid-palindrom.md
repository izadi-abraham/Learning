# Valid Palindrome. Title

Pattern: Two pointer | Difficulty: Easy | Date: 21-07-1987

## The problem in my own words
Given a string "s", convert all characters to lowercase and remove any non alphanumeric characters.
If it reads from left and right the same, then it is Palindrome.

## First idea

What I thought of before writing any code.

"S"

I can use a REGEX to find any non-alphanumeric characters and replace them with nothing.
I need to convert all characters to lowercase.

Now need to detect if it reads the same. Start 2 index on the staring, one form start and one from end of the string: 
  Iterate over the characters and compare the character in index start with end.
   If they are not the same return false.
   If indexes are equal return true. 

## Brute force

Approach, and why it is slow. Time / Space:

```ts

```

## First Version

The problem is this one doesn't compare the exact characters in the middle.
Example in "raceacar" the "e" and "a" characters in the middle are not checked and it returns true.

Actually everything was correct here, I added console.log() inside my loop and noticed the loop is not iterating at all.
And then noticed that the condition is not true, so i === j will be evaluated to false from begining and it wont run.

```ts
function isPalindrome(s: string): boolean {

    if (s.length === 1) {
        return true
    } 

    s.replace(/[\W_]+/g, "").toLowerCase()

    // raceacar r-r
    // r-r a-a c-c  

    // i === j sould be => i < j
    for (let i = 0, j = s.length - 1; i === j; i++, j++) {
        if (s[i] !== s[j]) {
            return false
        }
    }

    return true

};
```

## Second Version
Can you solve it with space complexity of O(1)
If we adjust the same string it will do the job then.
Improved the Regex readibility and skiped the string adjusting/creating a new one.

```ts
function isPalindrome(s: string): boolean { 
    let i = 0
    let j = s.length - 1

    while (i < j) {

        if (!/[a-zA-z0-9]/.test(s[i])) {
            i++
            continue
        }

        if (!/[a-zA-Z0-9]/.test(s[j])) {
            j--
            continue
        }
        
        if (s[i].toLowerCase() !== s[j].toLowerCase()) {
            return false
        }

        i++
        j--
    }

    return true
    

};

```



## What I learned

-Time complexity:
 - O(n) for cleaning the string
 - O(n) for Two pointer scan
 - Overal time complexity is O(n)

- Space complexity is O(n) because replace makes a new string.
- The improved version skips checking and making a new string.
- Strings are immutable, so there is no method like splice() for arrays that changes the value itself.

## Revisit on

YYYY-MM-DD
