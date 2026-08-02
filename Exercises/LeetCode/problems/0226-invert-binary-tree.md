# Invert Binary Tree

Pattern: | Difficulty: Easy | Date: 2026-08-01

## The problem in my own words
We get a binray tree and we need to invert all the left nodes with right nodes in the tree and return the root.

## First idea
What I thought of before writing any code:
I think I only need a stack and a loop.
I iterate over the tree in the loop I put the nodes in the stack in the reverse order,
then while visiting nodes I buil my inverted tree.
Since I sovled the Maximum Depth of binary tree problem and did visit all
the nodes via DFS, currently I can imagine that solution very clearly in my head.

## 1st Version 
- First of all I tried to remember what I was doing in my maximum depth problem. I took a look and remembered all the things.
- I tried to tweak it a bit, since in our new problem I don't need to visit all nodes, I don't need to push when I konw my node is a leaf node.
- So I added 2 more conditions in my if statement to see if the current node's grandchild exist or not. (`root.left.left || root.left.right`)
- Now I should understand how to connect my subtrees to their paretns.

```ts
function invertTree(root: TreeNode | null): TreeNode | null {
    const stack: {root: TreeNode, level: number}[] = []
    let level = 1;

    if(!root) {
        return null
    }

    stack.push({root, level: 1})

    while(stack.length){

        ({ root, level } = stack.pop()!);

        [root.left, root.right] = [root.right, root.left]

        if(root?.right && (root.right?.right || root.right?.left)) {
            stack.push({root: root.right, level: level + 1})
        }

        if(root?.left && (root.left?.right || root.left?.left)) {
            stack.push({root: root.left, level: level + 1})
        }

        console.log("root", root)
        console.log("level", level)
    }

    return root

};
```

- I am thinking if I can only save any node's value when I visit it, then I might be able to attach my inverted subtrees to the node values that are saved in another stack.
- But only saving node values doesn't work, because later if I want to add left/right children then I need to create a TreeNode instance again, so it makes sense to keep
the TreeNode itself in the new array (stack).

## 2nd Version

- I didn't need to do complex operations like saving root nodes then reassigning inverted subtrees to roots and ...
- It was very easy one, I just creat a new variable (`invertedRoot`) and points it to the root node before my loop starts.
- The key insight I learnt here was: At the begining my variables are pointing to the root node - which is an object (let's say it's val is 4):

```
root ───────────────┐
                    │
invertedRoot ───────┘
                    │
                    ▼
                  Node 4
```

- Later when I do `root = stack.pop()`, the object which `root` is pointing changes but the object which `invertedRoot` is pointing is still the `Node 4`.
- Because the above operatin did not change the object itself (the Node object), it just changed the variable `root`.
- Now the picture becomes:

```
invertedRoot ─────────────► Node 4

root ─────────────────────► Node 7
```
- So if at the end I just return the `invertedRoot` that is still pointing to our inverted tree's root node.


```ts
function invertTree(root: TreeNode | null): TreeNode | null {
    const stack: TreeNode[] = []
    const invertedRoot = root;

    if(!root) {
        return null
    }

    stack.push(root)

    while(stack.length){

        root = stack.pop();

        [root.left, root.right] = [root.right, root.left]


        if(root?.right) {
            stack.push(root.right)
        }
        
        if(root?.left) {
            stack.push(root.left)
        }
    }

    return invertedRoot
};
```

Time / Space complexity:

Time: Every node is visited only once. O(n)
Space: In the worst case (skewed tree - h = n) it will be O(n), but average (in a balanced tree) will be O(log n).
