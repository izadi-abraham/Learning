# Linked List Cycle

Pattern: | Difficulty: Easy | Date: 2026-08-04

## The problem in my own words
- We are given the head of a linked list. We need to figure out if there is a cycle or not.
- A node in the linked list has a next property, can be a ListNode or null.
- If next is null it means that's end of the list (so there is no cycle).
- If next is a ListNode we can move to next member in the list.
- `pos` is the index of the next node where `tail` is connected to.
- `pos` is the key variable here. If it exist and its value is `-1` then it shows that tail is not connected
to any other listNode, so there is no cycle.
- If `pos` exist and its value is something other than `-1` then for suer there is a cycle.
- My first idea is iterate over the linked list's nodes, if a node's next is null then that's end of list
and there is no cycle.
- If there is a node which `pos` exist and it has any value other than `-1` then there is cycle.
- I was thinking to use the cycle detction condition as:

```
if(head?.pos && head?.pos !== -1) {
            return true
        }
```
- But TS is not happy and it throws this erro:

```
Line 6: Char 18: error TS2339: Property 'pos' does not exist on type 'ListNode'.
```

- If I can not use/check the `pos` property, I was thinking to create a map,
when visiting any node, save the node's value and index in the map.
- So when I visit a new node then I can check and see if I already saw this value before with the samy position.
- But still something is not clear here, I can only increase my index when there is a `next`,
but I can not understand if I am cycling around my list.
- Question: "what is the indicator of knowing as an example value `2` which exist in my map, is a new value
 and it's not the same one I already visited?"
- Maybe if it's next value is also the same as the one which existed :thinking
- We can save the node itslef in a set, and then compare if we already had visited the node by `set.has()`



## First idea
What I thought of before writing any code:


## 1st Version 


```ts

function hasCycle(head: ListNode | null): boolean {
    const listMembers = new Set<ListNode>()

    if(!head) {
        return false
    }

    while(head?.next !== null) {

        if (listMembers.has(head)) {
            return true
        }

        listMembers.add(head)
        head = head.next
    }

    return false;
};

```

Time / Space complexity:

## 2nd Version


```ts

```

Time / Space complexity:

## 3rd Version

```ts

```
