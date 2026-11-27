"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Tree Traversal Introduction

Covered:

1. What is Tree?
2. Tree Terminology
3. Binary Tree
4. Tree Representation
5. DFS Traversal
6. Preorder Traversal
7. Inorder Traversal
8. Postorder Traversal
9. BFS Level Order Traversal
10. Binary Search Tree Concept
11. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Tree Definition
# ---------------------------------------------------------

def tree_definition():

    separator(
        "1. Tree Definition"
    )


    print(
        """
A Tree is a hierarchical
non-linear data structure.


Example:


             A

          /     \\

         B       C

        / \\

       D   E


A = Root

B,C = Children

D,E = Leaf Nodes


Used in:

- File systems
- Databases
- AI decision systems
- HTML DOM
- Search algorithms
        """
    )



# ---------------------------------------------------------
# 2. Tree Terminology
# ---------------------------------------------------------

def tree_terms():

    separator(
        "2. Tree Terminology"
    )


    print(
        """
Root:

Top node of tree.


Parent:

Node having children.


Child:

Node connected below parent.


Leaf:

Node without children.


Height:

Longest path from root
to leaf.


Depth:

Distance from root.
        """
    )



# ---------------------------------------------------------
# 3. Binary Tree Node Creation
# ---------------------------------------------------------

def binary_tree_creation():

    separator(
        "3. Binary Tree Creation"
    )


    class Node:

        def __init__(self,value):

            self.value = value

            self.left = None

            self.right = None



    root = Node("A")


    root.left = Node("B")

    root.right = Node("C")


    root.left.left = Node("D")

    root.left.right = Node("E")



    print(
        "Root:",
        root.value
    )


    print(
        "Left Child:",
        root.left.value
    )


    print(
        "Right Child:",
        root.right.value
    )



# ---------------------------------------------------------
# 4. Preorder Traversal
# ---------------------------------------------------------

def preorder_example():

    separator(
        "4. Preorder Traversal"
    )


    print(
        """
Order:

Root

Left

Right


Example:


       A

      / \\

     B   C


Output:

A B C


Used for:

- Copying trees
- Serialization
        """
    )



    class Node:

        def __init__(self,value):

            self.value = value

            self.left = None

            self.right = None



    root = Node("A")

    root.left = Node("B")

    root.right = Node("C")



    result = []



    def preorder(node):

        if node:

            result.append(node.value)

            preorder(node.left)

            preorder(node.right)



    preorder(root)



    print(
        result
    )



# ---------------------------------------------------------
# 5. Inorder Traversal
# ---------------------------------------------------------

def inorder_example():

    separator(
        "5. Inorder Traversal"
    )


    print(
        """
Order:

Left

Root

Right


Example:


       A

      / \\

     B   C


Output:

B A C


Used in:

- Binary Search Trees
- Sorted output
        """
    )



# ---------------------------------------------------------
# 6. Postorder Traversal
# ---------------------------------------------------------

def postorder_example():

    separator(
        "6. Postorder Traversal"
    )


    print(
        """
Order:

Left

Right

Root


Example:


       A

      / \\

     B   C


Output:

B C A


Used in:

- Delete operations
- Bottom-up processing
        """
    )



# ---------------------------------------------------------
# 7. Implement DFS Traversal
# ---------------------------------------------------------

def dfs_tree_example():

    separator(
        "7. DFS Tree Traversal"
    )


    class Node:

        def __init__(self,value):

            self.value = value

            self.left = None

            self.right = None



    root = Node(1)


    root.left = Node(2)

    root.right = Node(3)

    root.left.left = Node(4)

    root.left.right = Node(5)



    result = []



    def dfs(node):

        if node is None:

            return


        result.append(
            node.value
        )


        dfs(node.left)

        dfs(node.right)



    dfs(root)


    print(
        "DFS:",
        result
    )



# ---------------------------------------------------------
# 8. Level Order Traversal BFS
# ---------------------------------------------------------

def level_order_example():

    separator(
        "8. Level Order Traversal (BFS)"
    )


    from collections import deque


    tree = {

        1:[2,3],

        2:[4,5],

        3:[],

        4:[],

        5:[]

    }


    queue = deque()


    queue.append(1)


    result = []



    while queue:


        node = queue.popleft()


        result.append(node)


        for child in tree[node]:

            queue.append(child)



    print(
        "Level Order:",
        result
    )


    print(
        """
BFS uses Queue.

Used for:

- Level processing
- Shortest path
- Tree width calculation
        """
    )



# ---------------------------------------------------------
# 9. Binary Search Tree
# ---------------------------------------------------------

def bst_example():

    separator(
        "9. Binary Search Tree Concept"
    )


    print(
        """
Binary Search Tree Rule:


Left child

<

Parent

<

Right child



Example:


          50

       /      \\

     30        70

    / \\       / \\

   20 40     60 80


Benefits:

- Fast searching
- Ordered data
- Efficient insertion
        """
    )



# ---------------------------------------------------------
# 10. Tree Complexity
# ---------------------------------------------------------

def complexity_example():

    separator(
        "10. Tree Complexity"
    )


    print(
        """
Traversal:

Time:

O(n)


Because every node
is visited once.


Space:

O(height)


Due to recursion stack.
        """
    )



# ---------------------------------------------------------
# 11. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "11. AI Engineering Example - Decision Tree"
    )


    print(
        """
Decision Tree:


              Start

                |

          Is user premium?

             /      \\

           Yes       No

            |         |

        Special    Normal

        Response   Response



AI Usage:

- Machine Learning trees
- Rule engines
- Agent decision paths
- Knowledge hierarchies
- Document structures
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    tree_definition()

    tree_terms()

    binary_tree_creation()

    preorder_example()

    inorder_example()

    postorder_example()

    dfs_tree_example()

    level_order_example()

    bst_example()

    complexity_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()