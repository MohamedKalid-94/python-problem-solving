"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Graph Traversal Introduction

Covered:

1. What is Graph?
2. Graph Terminology
3. Graph Representation
4. Adjacency List
5. Adjacency Matrix
6. Breadth First Search (BFS)
7. Depth First Search (DFS)
8. Connected Components
9. Cycle Detection Concept
10. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Graph Definition
# ---------------------------------------------------------

def graph_definition():

    separator(
        "1. Graph Definition"
    )


    print(
        """
A Graph is a non-linear data structure
containing:

1. Nodes (Vertices)

2. Connections (Edges)


Example:

    A ----- B

    |

    C


A, B, C = Nodes

Lines = Edges


Types:

1. Directed Graph

A → B


2. Undirected Graph

A — B


3. Weighted Graph

Connection has cost.


Used in:

- Social networks
- Maps
- Recommendation systems
- Knowledge graphs
        """
    )



# ---------------------------------------------------------
# 2. Graph Terminology
# ---------------------------------------------------------

def graph_terms():

    separator(
        "2. Graph Terminology"
    )


    print(
        """
Vertex:

A single node.


Edge:

Connection between nodes.


Degree:

Number of connections.


Path:

Sequence of connected nodes.


Cycle:

Path that returns to starting node.


Neighbor:

Connected node.
        """
    )



# ---------------------------------------------------------
# 3. Adjacency List
# ---------------------------------------------------------

def adjacency_list_example():

    separator(
        "3. Graph Representation - Adjacency List"
    )


    graph = {

        "A":[

            "B",
            "C"

        ],

        "B":[

            "A",
            "D"

        ],

        "C":[

            "A"

        ],

        "D":[

            "B"

        ]

    }


    print(
        graph
    )



# ---------------------------------------------------------
# 4. Adjacency Matrix
# ---------------------------------------------------------

def adjacency_matrix_example():

    separator(
        "4. Graph Representation - Adjacency Matrix"
    )


    matrix = [

        [0,1,1,0],

        [1,0,0,1],

        [1,0,0,0],

        [0,1,0,0]

    ]


    print(
        matrix
    )


    print(
        """
Matrix value:

1 = Connection exists

0 = No connection
        """
    )



# ---------------------------------------------------------
# 5. Breadth First Search
# ---------------------------------------------------------

def bfs_example():

    separator(
        "5. Breadth First Search (BFS)"
    )


    from collections import deque


    graph = {

        "A":[

            "B",
            "C"

        ],

        "B":[

            "D"

        ],

        "C":[

            "E"

        ],

        "D":[],

        "E":[]

    }



    queue = deque()


    visited = []


    queue.append(
        "A"
    )


    while queue:


        node = queue.popleft()


        visited.append(node)


        for neighbor in graph[node]:

            if neighbor not in visited:

                queue.append(
                    neighbor
                )



    print(
        "BFS:",
        visited
    )


    print(
        """
BFS uses:

Queue

FIFO


Applications:

- Shortest path
- Level traversal
- Network search
        """
    )



# ---------------------------------------------------------
# 6. Depth First Search
# ---------------------------------------------------------

def dfs_example():

    separator(
        "6. Depth First Search (DFS)"
    )


    graph = {

        "A":[

            "B",
            "C"

        ],

        "B":[

            "D"

        ],

        "C":[

            "E"

        ],

        "D":[],

        "E":[]

    }


    visited = []


    def dfs(node):

        if node in visited:

            return


        visited.append(node)


        for neighbor in graph[node]:

            dfs(neighbor)



    dfs("A")


    print(
        "DFS:",
        visited
    )


    print(
        """
DFS uses:

Recursion / Stack


Applications:

- Backtracking
- Path finding
- Tree traversal
        """
    )



# ---------------------------------------------------------
# 7. Connected Components
# ---------------------------------------------------------

def connected_components_example():

    separator(
        "7. Connected Components"
    )


    graph = {

        1:[2],

        2:[1],

        3:[4],

        4:[3]

    }


    visited = set()


    components = 0



    def explore(node):

        visited.add(node)


        for neighbor in graph[node]:

            if neighbor not in visited:

                explore(neighbor)



    for node in graph:


        if node not in visited:

            explore(node)

            components += 1



    print(
        "Components:",
        components
    )



# ---------------------------------------------------------
# 8. Cycle Detection Concept
# ---------------------------------------------------------

def cycle_detection_example():

    separator(
        "8. Cycle Detection Concept"
    )


    print(
        """
Cycle:

A path that comes back
to the starting node.


Example:


A → B → C → A


Detection methods:

- DFS visited tracking
- BFS parent tracking


Used in:

- Dependency checking
- Workflow validation
- Network analysis
        """
    )



# ---------------------------------------------------------
# 9. Graph Complexity
# ---------------------------------------------------------

def complexity_example():

    separator(
        "9. Graph Algorithm Complexity"
    )


    print(
        """
For graph:

V = Number of vertices

E = Number of edges


BFS:

Time:
O(V + E)


DFS:

Time:
O(V + E)


Used for large networks.
        """
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. AI Engineering Example - Knowledge Graph"
    )


    knowledge_graph = {

        "Python":[

            "Programming",

            "AI"

        ],

        "AI":[

            "Machine Learning",

            "LLM"

        ]

    }


    print(
        knowledge_graph
    )


    print(
        """
AI Engineering Usage:

1. Knowledge Graphs

Entity relationships.


2. Recommendation Systems

User-item connections.


3. RAG Systems

Document relationship graphs.


4. Agent Planning

State transition graphs.


5. Social Network Analysis
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    graph_definition()

    graph_terms()

    adjacency_list_example()

    adjacency_matrix_example()

    bfs_example()

    dfs_example()

    connected_components_example()

    cycle_detection_example()

    complexity_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()