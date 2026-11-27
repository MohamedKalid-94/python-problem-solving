"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Sliding Window Pattern

Covered:

1. What is Sliding Window?
2. Fixed Size Window
3. Variable Size Window
4. Maximum Sum Subarray
5. Average Calculation
6. Longest Substring
7. Frequency Window
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Sliding Window Definition
# ---------------------------------------------------------

def sliding_window_definition():

    separator(
        "1. Sliding Window Pattern Definition"
    )


    print(
        """
Sliding Window is an optimization pattern
used for problems involving continuous
segments of data.

Instead of recalculating every window:

Brute Force:

O(n*k)


Sliding Window:

O(n)


Concept:

Create a window

        ↓

Process elements

        ↓

Move window forward


Used in:

- Arrays
- Strings
- Data streams
- Time series
- Log analysis
        """
    )



# ---------------------------------------------------------
# 2. Fixed Size Window
# ---------------------------------------------------------

def fixed_window_example():

    separator(
        "2. Fixed Size Sliding Window"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    window_size = 3


    window_sum = sum(
        numbers[:window_size]
    )


    maximum = window_sum


    for i in range(
        window_size,
        len(numbers)
    ):


        window_sum += numbers[i]


        window_sum -= numbers[i-window_size]


        maximum = max(
            maximum,
            window_sum
        )



    print(
        "Maximum Window Sum:",
        maximum
    )



# ---------------------------------------------------------
# 3. Window Movement
# ---------------------------------------------------------

def window_movement_example():

    separator(
        "3. Window Movement"
    )


    data = [

        10,
        20,
        30,
        40,
        50

    ]


    size = 2


    for i in range(
        len(data)-size+1
    ):

        window = data[
            i:i+size
        ]

        print(
            "Window:",
            window
        )



# ---------------------------------------------------------
# 4. Maximum Average Subarray
# ---------------------------------------------------------

def maximum_average_example():

    separator(
        "4. Maximum Average Subarray"
    )


    scores = [

        80,
        90,
        70,
        100,
        95

    ]


    k = 3


    current_sum = sum(
        scores[:k]
    )


    maximum = current_sum


    for i in range(
        k,
        len(scores)
    ):

        current_sum += scores[i]

        current_sum -= scores[i-k]


        maximum = max(
            maximum,
            current_sum
        )


    average = maximum / k


    print(
        "Maximum Average:",
        average
    )



# ---------------------------------------------------------
# 5. Longest Substring Without Duplicate
# ---------------------------------------------------------

def longest_unique_substring_example():

    separator(
        "5. Longest Unique Substring"
    )


    text = "abcabcbb"


    window = set()


    left = 0


    maximum_length = 0


    for right in range(
        len(text)
    ):


        while text[right] in window:

            window.remove(
                text[left]
            )

            left += 1



        window.add(
            text[right]
        )


        maximum_length = max(

            maximum_length,

            right-left+1

        )



    print(
        "Longest Length:",
        maximum_length
    )



# ---------------------------------------------------------
# 6. Frequency Window
# ---------------------------------------------------------

def frequency_window_example():

    separator(
        "6. Frequency Based Window"
    )


    text = "aabbcc"


    window_size = 2


    for i in range(

        len(text)-window_size+1

    ):

        window = text[
            i:i+window_size
        ]


        frequency = {}


        for char in window:

            frequency[char] = (

                frequency.get(
                    char,
                    0
                )
                +
                1

            )


        print(
            window,
            frequency
        )



# ---------------------------------------------------------
# 7. Minimum Window Concept
# ---------------------------------------------------------

def minimum_window_example():

    separator(
        "7. Minimum Window Concept"
    )


    print(
        """
Problem:

Find smallest section of data
containing required values.


Example:

Text:
ADOBECODEBANC


Required:
ABC


Answer:

BANC


Used in:

- Search engines
- NLP
- Document retrieval
        """
    )



# ---------------------------------------------------------
# 8. Data Stream Window
# ---------------------------------------------------------

def data_stream_window_example():

    separator(
        "8. Data Stream Processing"
    )


    api_response_times = [

        100,
        120,
        110,
        200,
        150

    ]


    window_size = 3


    for i in range(

        len(api_response_times)
        -
        window_size
        +
        1

    ):

        window = api_response_times[
            i:i+window_size
        ]


        average = sum(window) / window_size


        print(
            "Average Response:",
            average
        )



# ---------------------------------------------------------
# 9. Sliding Window with Queue
# ---------------------------------------------------------

def queue_window_example():

    separator(
        "9. Sliding Window Queue"
    )


    from collections import deque


    stream = [

        5,
        10,
        15,
        20

    ]


    window = deque()

    size = 3


    for value in stream:

        window.append(value)


        if len(window) > size:

            window.popleft()



        print(
            list(window)
        )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - LLM Monitoring"
    )


    token_usage = [

        1000,
        1500,
        2000,
        1200,
        1800

    ]


    window_size = 3


    for i in range(

        len(token_usage)
        -
        window_size
        +
        1

    ):

        window = token_usage[
            i:i+window_size
        ]


        average = (
            sum(window)
            /
            window_size
        )


        print(
            "Average Token Usage:",
            average
        )


    print(
        """
AI Engineering Usage:

- LLM token monitoring
- Streaming analytics
- Moving averages
- Rate limiting
- Real-time metrics
- Log processing
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    sliding_window_definition()

    fixed_window_example()

    window_movement_example()

    maximum_average_example()

    longest_unique_substring_example()

    frequency_window_example()

    minimum_window_example()

    data_stream_window_example()

    queue_window_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()