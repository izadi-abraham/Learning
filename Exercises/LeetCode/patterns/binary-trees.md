
# Binary Trees

A binary tree is a tree data structure where each node has **at most two children**,
refered to as the left child and the right child.

## Usage

It is widely used in applications such as **Binary Search Trees** and **heaps**.

# Types of Binary Tree

## On the basis of number of Children

### Full Binary Tree

Every node has either 0 or 2 children. 
(there is no node with 1 child Or all nodes except leaf nodes have 2 children.)
This is also konwn as **proper binary tree.**

### Degenerate Binary Tree

Every node has 1 child (either left child or right child).
Such trees are performance-wise same as linked list.

### Skewed Binary Tree

It's a degenerate binary tree that is either dominated by the left nodes the right nodes.
(Left skewed binary tree / Right skewed binary tree)


## On the basis of level completion

### Complete Binary Tree

All the levels are completely filled except possibly the last level, and the last level
is filled from the left side.
A complete binary tree is a full binary tree but all the leaf nodes must lean toward left.


### Perfect Binary Tree

All nodes have 2 children and all leafs are at the same level.
(number of leaf nodes = number of internal nodes + 1)
Internal nodes are those which are not leaf nodes.

### Balanced Binary Tree

If the height of the tree is O(log n) where n is number of nodes.
For example, the AVL tree maintains O(log n) height by making sure that the difference between the
heights of the left and right subtrees of every node is at most 1.


## Special Types of Binary Trees

#### Binary Search Tree
#### AVl Tree
#### Red Black Tree
#### B - Tree
#### B+ Tree
