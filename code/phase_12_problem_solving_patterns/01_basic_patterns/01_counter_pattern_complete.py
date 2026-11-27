"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Counter Pattern

Covered:

1. What is Counter Pattern?
2. Counting Frequency
3. Counting with Dictionary
4. Counting with get()
5. Counting Characters
6. Counting Numbers
7. Counting Conditions
8. Real-World Examples

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Counter Pattern?
# ---------------------------------------------------------

def counter_definition():

    separator(
        "1. Counter Pattern Definition"
    )

    print(
        """
Counter Pattern is a problem-solving technique
used to count occurrences of elements.

Common uses:

- Frequency counting
- Duplicate detection
- Finding most common elements
- Data analysis
- Log processing

Basic idea:

Create a counter variable and
increase it whenever an element appears.
        """
    )


# ---------------------------------------------------------
# 2. Basic Counter
# ---------------------------------------------------------

def basic_counter_example():

    separator(
        "2. Basic Counter Example"
    )


    count = 0


    for number in range(1, 6):

        count += 1


    print(
        "Count:",
        count
    )



# ---------------------------------------------------------
# 3. Counting List Elements
# ---------------------------------------------------------

def list_counter_example():

    separator(
        "3. Counting List Elements"
    )


    numbers = [
        10,
        20,
        10,
        30,
        20,
        10
    ]


    counter = {}


    for number in numbers:

        if number in counter:

            counter[number] += 1

        else:

            counter[number] = 1



    print(
        "Frequency:"
    )

    print(counter)



# ---------------------------------------------------------
# 4. Counter using get()
# ---------------------------------------------------------

def get_counter_example():

    separator(
        "4. Counter using get()"
    )


    numbers = [
        1,
        2,
        3,
        1,
        2,
        1
    ]


    frequency = {}


    for number in numbers:

        frequency[number] = (
            frequency.get(number, 0) + 1
        )


    print(
        frequency
    )



# ---------------------------------------------------------
# 5. Character Frequency
# ---------------------------------------------------------

def character_frequency_example():

    separator(
        "5. Character Frequency"
    )


    text = "pythonprogramming"


    frequency = {}


    for char in text:

        frequency[char] = (
            frequency.get(char, 0) + 1
        )


    print(
        "Character Count:"
    )

    print(frequency)



# ---------------------------------------------------------
# 6. Find Duplicate Elements
# ---------------------------------------------------------

def duplicate_detection_example():

    separator(
        "6. Duplicate Detection"
    )


    numbers = [

        1,
        2,
        3,
        2,
        4,
        5,
        1

    ]


    counter = {}


    for number in numbers:

        counter[number] = (
            counter.get(number, 0) + 1
        )


    duplicates = []


    for key, value in counter.items():

        if value > 1:

            duplicates.append(key)


    print(
        "Duplicates:",
        duplicates
    )



# ---------------------------------------------------------
# 7. Find Most Frequent Element
# ---------------------------------------------------------

def most_frequent_example():

    separator(
        "7. Most Frequent Element"
    )


    votes = [

        "Python",
        "AI",
        "Python",
        "ML",
        "Python",
        "AI"

    ]


    counter = {}


    for vote in votes:

        counter[vote] = (
            counter.get(vote, 0) + 1
        )


    maximum = 0

    result = None


    for item, count in counter.items():

        if count > maximum:

            maximum = count

            result = item


    print(
        "Most Frequent:",
        result
    )

    print(
        "Count:",
        maximum
    )



# ---------------------------------------------------------
# 8. Counting Conditions
# ---------------------------------------------------------

def condition_counter_example():

    separator(
        "8. Condition Counter"
    )


    numbers = [

        10,
        25,
        40,
        55,
        70

    ]


    even_count = 0

    odd_count = 0


    for number in numbers:

        if number % 2 == 0:

            even_count += 1

        else:

            odd_count += 1



    print(
        "Even:",
        even_count
    )

    print(
        "Odd:",
        odd_count
    )



# ---------------------------------------------------------
# 9. Using collections.Counter
# ---------------------------------------------------------

def collections_counter_example():

    separator(
        "9. collections.Counter"
    )


    from collections import Counter


    skills = [

        "Python",
        "AI",
        "Python",
        "ML",
        "AI"

    ]


    result = Counter(skills)


    print(
        result
    )


    print(
        "Most Common:"
    )


    print(
        result.most_common(1)
    )



# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "10. Real-World Example - Log Analysis"
    )


    logs = [

        "ERROR",
        "INFO",
        "WARNING",
        "ERROR",
        "INFO",
        "ERROR"

    ]


    error_count = {}


    for log in logs:

        error_count[log] = (
            error_count.get(log, 0) + 1
        )


    print(
        "Log Frequency:"
    )

    print(
        error_count
    )


    print(
        """
AI/Backend Usage:

- API request counting
- Error monitoring
- User activity tracking
- Word frequency analysis
- Document analysis
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    counter_definition()

    basic_counter_example()

    list_counter_example()

    get_counter_example()

    character_frequency_example()

    duplicate_detection_example()

    most_frequent_example()

    condition_counter_example()

    collections_counter_example()

    real_world_example()



if __name__ == "__main__":

    main()