"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Problem Solving Real World Problems

Covered:

1. Problem Solving Approach
2. Array Processing
3. Frequency Counting
4. Data Filtering
5. Searching
6. Sorting
7. Stack Based Problems
8. Queue Based Problems
9. Sliding Window Analytics
10. AI Engineering Use Cases

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Problem Solving Approach
# ---------------------------------------------------------

def problem_solving_approach():

    separator(
        "1. Problem Solving Approach"
    )


    print(
        """
Professional Problem Solving Steps:


Step 1:

Understand the problem

        ↓

Step 2:

Identify input and output

        ↓

Step 3:

Choose data structure

        ↓

Step 4:

Select algorithm pattern

        ↓

Step 5:

Optimize complexity

        ↓

Step 6:

Test edge cases


Common Patterns:

- Hash Map
- Two Pointer
- Sliding Window
- Stack
- Queue
- Binary Search
- Recursion
- Dynamic Programming
        """
    )



# ---------------------------------------------------------
# 2. Find Duplicate Values
# ---------------------------------------------------------

def duplicate_detection_example():

    separator(
        "2. Duplicate Detection using Hash Map"
    )


    numbers = [

        10,
        20,
        30,
        20,
        40,
        10

    ]


    frequency = {}


    duplicates = []


    for number in numbers:


        frequency[number] = (

            frequency.get(
                number,
                0
            )
            +
            1

        )



    for key,value in frequency.items():

        if value > 1:

            duplicates.append(key)



    print(
        "Duplicates:",
        duplicates
    )


    print(
        """
Pattern Used:

Frequency Map


Real Usage:

- Duplicate documents
- User records
- Data cleaning
        """
    )



# ---------------------------------------------------------
# 3. Log Analysis
# ---------------------------------------------------------

def log_analysis_example():

    separator(
        "3. Log Analysis Problem"
    )


    logs = [

        "ERROR",

        "INFO",

        "ERROR",

        "WARNING",

        "ERROR"

    ]


    count = {}


    for log in logs:

        count[log] = (

            count.get(
                log,
                0
            )
            +
            1

        )



    print(
        count
    )


    print(
        """
Pattern:

Counter


Used in:

- Application monitoring
- Error tracking
- Observability systems
        """
    )



# ---------------------------------------------------------
# 4. Find Maximum Transaction
# ---------------------------------------------------------

def maximum_transaction_example():

    separator(
        "4. Maximum Value Problem"
    )


    transactions = [

        1200,
        5000,
        2300,
        9000,
        4500

    ]


    maximum = transactions[0]


    for amount in transactions:

        if amount > maximum:

            maximum = amount



    print(
        "Maximum Transaction:",
        maximum
    )


    print(
        """
Pattern:

Maximum/Minimum Pattern
        """
    )



# ---------------------------------------------------------
# 5. Two Sum Problem
# ---------------------------------------------------------

def two_sum_example():

    separator(
        "5. Two Sum Problem"
    )


    numbers = [

        2,
        7,
        11,
        15

    ]


    target = 9


    seen = {}


    result = None



    for index,value in enumerate(numbers):


        required = target - value


        if required in seen:

            result = (

                seen[required],

                index

            )

            break



        seen[value] = index



    print(
        "Indexes:",
        result
    )


    print(
        """
Pattern:

Hash Map


Used in:

- Searching
- Recommendation matching
        """
    )



# ---------------------------------------------------------
# 6. API Rate Monitoring
# ---------------------------------------------------------

def sliding_window_api_example():

    separator(
        "6. API Rate Monitoring"
    )


    requests = [

        100,
        120,
        150,
        200,
        180

    ]


    window = 3


    for i in range(

        len(requests)-window+1

    ):

        current = requests[

            i:i+window

        ]


        average = sum(current)/window


        print(
            "Average:",
            average
        )


    print(
        """
Pattern:

Sliding Window


Used in:

- API monitoring
- Traffic analysis
- Real-time metrics
        """
    )



# ---------------------------------------------------------
# 7. Browser History
# ---------------------------------------------------------

def browser_history_example():

    separator(
        "7. Browser History"
    )


    history = []


    history.append(
        "google.com"
    )


    history.append(
        "github.com"
    )


    history.append(
        "chat.openai.com"
    )


    print(
        "History:",
        history
    )


    previous = history.pop()


    print(
        "Back:",
        previous
    )


    print(
        """
Pattern:

Stack


Used in:

- Undo systems
- Navigation
        """
    )



# ---------------------------------------------------------
# 8. Task Processing System
# ---------------------------------------------------------

def task_queue_example():

    separator(
        "8. Task Processing Queue"
    )


    from collections import deque


    tasks = deque(

        [

            "Process Resume",

            "Generate Report",

            "Send Email"

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
Pattern:

Queue


Used in:

- Background workers
- AI pipelines
- Distributed systems
        """
    )



# ---------------------------------------------------------
# 9. Document Search
# ---------------------------------------------------------

def document_search_example():

    separator(
        "9. Document Search"
    )


    documents = [

        "python ai",

        "machine learning",

        "python programming"

    ]


    keyword = "python"


    results = []



    for document in documents:


        if keyword in document:

            results.append(document)



    print(
        "Results:",
        results
    )


    print(
        """
Pattern:

Search Pattern


Used in:

- Search engines
- RAG systems
- Document retrieval
        """
    )



# ---------------------------------------------------------
# 10. AI Engineering Pipeline Example
# ---------------------------------------------------------

def ai_pipeline_example():

    separator(
        "10. AI Engineering Problem Solving"
    )


    print(
        """
Real RAG Pipeline:


User Query

    |

Retrieve Documents

    |

Rank Results

    |

Generate Response

    |

Validate Answer



Patterns Used:


1. Hash Map

Metadata lookup


2. Priority Queue

Ranking


3. Graph

Knowledge relationships


4. Sliding Window

Context management


5. Dynamic Programming

Optimization


6. Stack

Agent history


7. Queue

Task processing
        """
    )



# ---------------------------------------------------------
# 11. Interview Problem Checklist
# ---------------------------------------------------------

def interview_checklist():

    separator(
        "11. Interview Problem Checklist"
    )


    print(
        """
Before coding:


1. Understand problem


2. Identify pattern


3. Select data structure


4. Write simple solution


5. Optimize


6. Analyze:

Time Complexity

Space Complexity


7. Test:

Empty input

Single value

Large input

Duplicate values
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    problem_solving_approach()

    duplicate_detection_example()

    log_analysis_example()

    maximum_transaction_example()

    two_sum_example()

    sliding_window_api_example()

    browser_history_example()

    task_queue_example()

    document_search_example()

    ai_pipeline_example()

    interview_checklist()



if __name__ == "__main__":

    main()