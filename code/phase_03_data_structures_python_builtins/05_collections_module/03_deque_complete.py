"""
=========================================================
Topic : collections.deque

Author: Mohamed Kalid

deque = Double Ended Queue

It allows insertion and deletion from both ends.

Normal List:

append()        -> Fast
appendleft()    -> Slow (O(n))

deque:

append()        -> O(1)
appendleft()    -> O(1)

Common Uses:

1. Queue implementation
2. Stack implementation
3. Sliding Window
4. BFS traversal
5. Undo/Redo systems
6. Browser history

=========================================================
"""

from collections import deque


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Creating deque
    # =====================================================

    separator("1. Creating deque")


    numbers = deque([10, 20, 30])


    print(numbers)

    print(type(numbers))



    # =====================================================
    # 2. append()
    # Add element at right side
    # =====================================================

    separator("2. append()")


    queue = deque([1, 2, 3])


    print("Before")

    print(queue)


    queue.append(4)


    print("After append")

    print(queue)



    # =====================================================
    # 3. appendleft()
    # Add element at left side
    # =====================================================

    separator("3. appendleft()")


    queue = deque([2, 3, 4])


    queue.appendleft(1)


    print(queue)



    # =====================================================
    # 4. pop()
    # Remove from right
    # =====================================================

    separator("4. pop()")


    numbers = deque([10, 20, 30])


    removed = numbers.pop()


    print("Removed:")

    print(removed)


    print("Remaining")

    print(numbers)



    # =====================================================
    # 5. popleft()
    # Remove from left
    # =====================================================

    separator("5. popleft()")


    numbers = deque([10, 20, 30])


    removed = numbers.popleft()


    print("Removed:")

    print(removed)


    print("Remaining")

    print(numbers)



    # =====================================================
    # 6. extend()
    # =====================================================

    separator("6. extend()")


    data = deque([1, 2, 3])


    data.extend([4, 5, 6])


    print(data)



    # =====================================================
    # 7. extendleft()
    # =====================================================

    separator("7. extendleft()")


    data = deque([4, 5, 6])


    data.extendleft([1, 2, 3])


    print(data)


    print(
        "Note: extendleft inserts elements "
        "one by one from left"
    )



    # =====================================================
    # 8. rotate()
    # =====================================================

    separator("8. rotate()")


    numbers = deque([1, 2, 3, 4, 5])


    numbers.rotate(2)


    print("Rotate right")

    print(numbers)



    numbers.rotate(-2)


    print("Rotate left")

    print(numbers)



    # =====================================================
    # 9. reverse()
    # =====================================================

    separator("9. reverse()")


    numbers = deque([1, 2, 3, 4])


    numbers.reverse()


    print(numbers)



    # =====================================================
    # 10. maxlen
    # =====================================================

    separator("10. maxlen")


    history = deque(
        maxlen=3
    )


    history.append("Page1")

    history.append("Page2")

    history.append("Page3")

    history.append("Page4")


    print(history)


    print(
        "Oldest item removed automatically"
    )



    # =====================================================
    # 11. Queue Implementation
    # FIFO
    # =====================================================

    separator("11. Queue using deque")


    queue = deque()


    queue.append("Customer 1")

    queue.append("Customer 2")

    queue.append("Customer 3")


    print(queue)


    print(
        "Serving:",
        queue.popleft()
    )


    print(queue)



    # =====================================================
    # 12. Stack Implementation
    # LIFO
    # =====================================================

    separator("12. Stack using deque")


    stack = deque()


    stack.append("Page 1")

    stack.append("Page 2")

    stack.append("Page 3")


    print(stack)


    print(
        "Remove:",
        stack.pop()
    )


    print(stack)



    # =====================================================
    # 13. Sliding Window
    # =====================================================

    separator("13. Sliding Window Example")


    numbers = [

        10,

        20,

        30,

        40,

        50

    ]


    window = deque(maxlen=3)


    for number in numbers:

        window.append(number)

        print(
            list(window)
        )



    # =====================================================
    # 14. Moving Average
    # =====================================================

    separator("14. Moving Average")


    values = [

        10,

        20,

        30,

        40,

        50

    ]


    window = deque(maxlen=3)


    for value in values:

        window.append(value)


        if len(window) == 3:

            average = sum(window) / 3

            print(
                "Window:",
                list(window),
                "Average:",
                average
            )



    # =====================================================
    # 15. Browser History Example
    # =====================================================

    separator("15. Browser History")


    browser = deque(maxlen=5)


    browser.append("Google")

    browser.append("YouTube")

    browser.append("GitHub")

    browser.append("ChatGPT")


    print(browser)


    browser.pop()


    print(
        "After Back:",
        browser
    )



    # =====================================================
    # 16. BFS Example
    # =====================================================

    separator("16. BFS Traversal")


    graph = {


        "A": ["B", "C"],

        "B": ["D"],

        "C": ["E"],

        "D": [],

        "E": []

    }


    queue = deque(["A"])

    visited = set()


    while queue:


        node = queue.popleft()


        if node not in visited:


            print(node)


            visited.add(node)


            queue.extend(
                graph[node]
            )



    # =====================================================
    # 17. Complexity
    # =====================================================

    separator("17. Time Complexity")


    print(
        """
        append()        : O(1)

        appendleft()    : O(1)

        pop()           : O(1)

        popleft()       : O(1)

        rotate()        : O(k)

        Searching       : O(n)

        """
    )



if __name__ == "__main__":

    main()