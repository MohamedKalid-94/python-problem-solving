"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Queue Pattern

Covered:

1. What is Queue?
2. FIFO Concept
3. Enqueue and Dequeue
4. Queue using List
5. Queue using deque
6. BFS Introduction
7. Task Processing
8. Message Queue Concept
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Queue Definition
# ---------------------------------------------------------

def queue_definition():

    separator(
        "1. Queue Pattern Definition"
    )


    print(
        """
Queue is a data structure that follows:

FIFO

First In First Out


Example:

People waiting in a line.


Operations:

Enqueue  -> Add item

Dequeue  -> Remove first item

Front    -> View first item


Common uses:

- Task scheduling
- Message systems
- BFS traversal
- Request handling
- AI agent workflows
        """
    )



# ---------------------------------------------------------
# 2. Basic Queue using List
# ---------------------------------------------------------

def basic_queue_example():

    separator(
        "2. Queue using List"
    )


    queue = []


    queue.append(
        "Task 1"
    )


    queue.append(
        "Task 2"
    )


    queue.append(
        "Task 3"
    )


    print(
        "Queue:",
        queue
    )


    removed = queue.pop(0)


    print(
        "Processed:",
        removed
    )


    print(
        "Remaining:",
        queue
    )



# ---------------------------------------------------------
# 3. Enqueue Operation
# ---------------------------------------------------------

def enqueue_example():

    separator(
        "3. Enqueue Operation"
    )


    queue = []


    tasks = [

        "Email",
        "Report",
        "Meeting"

    ]


    for task in tasks:

        queue.append(task)



    print(
        queue
    )



# ---------------------------------------------------------
# 4. Dequeue Operation
# ---------------------------------------------------------

def dequeue_example():

    separator(
        "4. Dequeue Operation"
    )


    queue = [

        100,
        200,
        300

    ]


    while queue:

        item = queue.pop(0)


        print(
            "Processing:",
            item
        )



# ---------------------------------------------------------
# 5. Queue using deque
# ---------------------------------------------------------

def deque_example():

    separator(
        "5. Queue using collections.deque"
    )


    from collections import deque


    queue = deque()


    queue.append(
        "User Request 1"
    )


    queue.append(
        "User Request 2"
    )


    queue.append(
        "User Request 3"
    )


    print(
        queue
    )


    processed = queue.popleft()


    print(
        "Processed:",
        processed
    )


    print(
        queue
    )



# ---------------------------------------------------------
# 6. Front Element
# ---------------------------------------------------------

def front_element_example():

    separator(
        "6. Front Element"
    )


    from collections import deque


    queue = deque(

        [
            "First",
            "Second",
            "Third"
        ]

    )


    print(
        "Front:",
        queue[0]
    )



# ---------------------------------------------------------
# 7. Customer Service Queue
# ---------------------------------------------------------

def customer_queue_example():

    separator(
        "7. Customer Service Queue"
    )


    from collections import deque


    customers = deque(

        [
            "Customer A",
            "Customer B",
            "Customer C"
        ]

    )


    while customers:

        current = customers.popleft()


        print(
            "Serving:",
            current
        )



# ---------------------------------------------------------
# 8. BFS Introduction
# ---------------------------------------------------------

def bfs_introduction():

    separator(
        "8. Breadth First Search (BFS)"
    )


    print(
        """
BFS uses Queue data structure.


Algorithm:

1. Add starting node to queue

2. Remove first node

3. Visit neighbors

4. Add neighbors to queue


Used in:

- Graph traversal
- Shortest path
- Network search
- Web crawling
        """
    )



# ---------------------------------------------------------
# 9. Simple BFS Example
# ---------------------------------------------------------

def bfs_example():

    separator(
        "9. Simple BFS Example"
    )


    from collections import deque


    graph = {

        "A":["B","C"],

        "B":["D"],

        "C":["E"],

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

            queue.append(neighbor)



    print(
        "BFS Order:",
        visited
    )



# ---------------------------------------------------------
# 10. Message Queue Concept
# ---------------------------------------------------------

def message_queue_example():

    separator(
        "10. Message Queue Concept"
    )


    print(
        """
Real systems use queues between services.


Example:

User Request

      |

API Server

      |

Message Queue

      |

Background Worker


Benefits:

- Asynchronous processing
- Better scalability
- Failure handling
- Load balancing
        """
    )



# ---------------------------------------------------------
# 11. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "11. AI Real-World Example - Agent Task Queue"
    )


    from collections import deque


    tasks = deque(

        [

            "Retrieve documents",

            "Rank results",

            "Generate answer",

            "Validate response"

        ]

    )


    while tasks:


        task = tasks.popleft()


        print(
            "Executing:",
            task
        )



    print(
        """
AI Engineering Usage:

- Agent task execution
- Background jobs
- LLM request queues
- Data pipelines
- Distributed systems
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    queue_definition()

    basic_queue_example()

    enqueue_example()

    dequeue_example()

    deque_example()

    front_element_example()

    customer_queue_example()

    bfs_introduction()

    bfs_example()

    message_queue_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()