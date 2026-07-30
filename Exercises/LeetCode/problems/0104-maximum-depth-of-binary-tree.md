# Maximum Depth Of Binary Tree

Pattern:  | Difficulty: Easy | Date: 2026-07-28

## The problem in my own words
Given the root of a binary tree, we need to return its maximum depth.
Maximum depth of a binary tree is the number of nodes along the longest path
from the root node down to the farthest leaf node.

## First idea
What I thought of before writing any code:
- I tried to ignore what I remember from the recursive approach from before.
- I remembered we can use an array of stack, to push any node that we are not traversing its right child,
And traverse the left child instead.
- This way we continue traversing up to the fartheset left leef and then we pop from the stack afterwards.
So we can visit all nodes this way.
- I suppose this is DFS.
- I also tried to keep a depth variable, any time that there is a child on a node, then increment the depth.
- It took me a long time to get to this point because I tried different combination of what I remembered:
- For example I remembered we can do as below to move from one node to another:
```
if(root.left) {
  root = root.left
}
```
- Or I need to check the length of my stack and continue pop() on my stack so I can visit all nodes.

- Or I can use while loop to move to farthest node in left/right child. (but I think in this algorithm that is 
not needed. It took me time to trace and discover that.)

- Now at this point there are some test cases that fail, and the algorithm has bug.
- I also tried some ideas like when we visit a leaf, then we need to decrese our depth.
- Or we need a separate variable (let's name it max), and we need to compare and assign to max whenever we
want to decrement the depth.

## 1st Version 


```ts
function maxDepth(root: TreeNode | null): number {
    const stack = []
    let depth = 1
    let max = 1
    
    if (!root) {
        return 0
    }

    stack.push(root)

    while(stack.length) {
        root = stack.pop()
        
        if(root?.right) {
            stack.push(root.right)
        }
        
        if(root?.left) {
            stack.push(root.left)
        }

        if (root?.left || root?.right) {
            depth++
        }
    }

    return depth
};
```

Time / Space complexity:

## 2nd Version
I fixed the bug in this version. The idea is the stack in previous version only saved the TreeNode entity.
I need to save the depth next to each node, so later when processing the node I know which depth does this node belong.

```ts
function maxDepth(root: TreeNode | null): number {
    const stack = []
    let depth = 1
    let max = 1
    
    if (!root) {
        return 0
    }

    stack.push({ root, depth: 1})

    while(stack.length) {
        ({ root, depth } = stack.pop())

        if (root?.left || root?.right) {
            depth++
        }
        
        if(root?.right) {
            stack.push({root: root.right, depth})
        }
        
        if(root?.left) {
            stack.push({ root: root.left, depth})
        }

        if(!root?.left && !root?.right) {
            max = Math.max(max, depth)
        }
    }

    return max
};

```


## 3rd Version
In this version there is a slight improvement.
Instead of increamenting the depth inside an if condition like:

```
if (root?.left || root?.right) {
            depth++
        }

```
I could just save the depth of each node in the stack when pushing.
The depth of each child will be depth of parent + 1.
We don't need to handle incrementing the depth value manually, because we read the depth of each node,
when poping from the stack and it is already incremented when it was saving while processing the parent.

```
 if(root?.right) {
            stack.push({root: root.right, depth: depth + 1})
        }

        if(root?.left) {
            stack.push({ root: root.left, depth: depth + 1})
        }

```

The final iterative version:

```ts
function maxDepth(root: TreeNode | null): number {
    const stack = []
    let depth = 1
    let max = 1
    
    if (!root) {
        return 0
    }

    stack.push({ root, depth: 1})

    while(stack.length) {
        ({ root, depth } = stack.pop())
        
        if(root?.right) {
            stack.push({root: root.right, depth: depth + 1})
        }
        
        if(root?.left) {
            stack.push({ root: root.left, depth: depth + 1})
        }

        // leaf node
        if(!root?.left && !root?.right) {
            max = Math.max(max, depth)
        }
    }

    return max
};

```

Time / Space complexity:
Time complexity must be O(n), since we traverse(visit) all the nodes only once.
Space Complexity: O(h), where h is the height of the tree, due to the explicit DFS stack. In the worst case (a skewed tree), h = n, so the worst-case space complexity is O(n).
