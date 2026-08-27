# Reverse Linked List

Pattern:  | Difficulty: Easy| Date: 26-08-2026

## The problem in my own words
We need to reverse the order of a linked list.


## First idea
What I thought of before writing any code:

First I thought if I can keep a pointer to the current node, then move to the next node and then change the next pointer of the next node the pointer I kept. But when I suspect
if I move to the next node, does the pointer moves as well.

Another idea is to change the pointer of the next node's next to the current node `node.next.next = node`
And then move to next node, and now change the pointer of the previous node (in the first iteration, change the previous's node's next to null.
This doesn't work. If I change the `node.next.next`, then node.next is out of the list :)

I am thinking it makes sense to move to the end of the list and then start chagning the next pointers.


## 1st Version 


```ts

```

Time / Space complexity:

## 2nd Version


```ts

```

Time / Space complexity:

## 3rd Version

```ts

```
