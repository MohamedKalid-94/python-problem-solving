"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Frequency Map Pattern

Covered:

1. What is Frequency Map?
2. Dictionary Based Counting
3. Character Frequency
4. Word Frequency
5. Duplicate Detection
6. Anagram Checking
7. First Non-Repeating Character
8. Frequency Comparison
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Frequency Map Definition
# ---------------------------------------------------------

def frequency_map_definition():

    separator(
        "1. Frequency Map Definition"
    )


    print(
        """
Frequency Map is a problem-solving pattern
that stores the count of each element.

It uses:

Key   -> Element
Value -> Number of occurrences


Common uses:

- Counting characters
- Finding duplicates
- Anagram problems
- Data analysis
- Searching patterns


Basic Pattern:

frequency = {}

for item in data:

    frequency[item] = frequency.get(item,0)+1
        """
    )



# ---------------------------------------------------------
# 2. Basic Frequency Map
# ---------------------------------------------------------

def basic_frequency_example():

    separator(
        "2. Basic Frequency Map"
    )


    numbers = [

        10,
        20,
        10,
        30,
        20,
        10

    ]


    frequency = {}


    for number in numbers:

        frequency[number] = (
            frequency.get(number,0) + 1
        )


    print(
        frequency
    )



# ---------------------------------------------------------
# 3. Character Frequency
# ---------------------------------------------------------

def character_frequency_example():

    separator(
        "3. Character Frequency"
    )


    text = "programming"


    frequency = {}


    for char in text:

        frequency[char] = (
            frequency.get(char,0) + 1
        )


    print(
        "Character Frequency:"
    )

    print(
        frequency
    )



# ---------------------------------------------------------
# 4. Word Frequency
# ---------------------------------------------------------

def word_frequency_example():

    separator(
        "4. Word Frequency"
    )


    sentence = (
        "python ai python machine learning ai"
    )


    words = sentence.split()


    frequency = {}


    for word in words:

        frequency[word] = (
            frequency.get(word,0) + 1
        )


    print(
        frequency
    )



# ---------------------------------------------------------
# 5. Find Duplicate Elements
# ---------------------------------------------------------

def duplicate_detection_example():

    separator(
        "5. Duplicate Detection"
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


    frequency = {}


    for number in numbers:

        frequency[number] = (
            frequency.get(number,0)+1
        )


    duplicates = []


    for item,count in frequency.items():

        if count > 1:

            duplicates.append(item)


    print(
        "Duplicates:",
        duplicates
    )



# ---------------------------------------------------------
# 6. Find Most Frequent Element
# ---------------------------------------------------------

def most_frequent_element_example():

    separator(
        "6. Most Frequent Element"
    )


    values = [

        "AI",
        "ML",
        "AI",
        "Python",
        "AI",
        "ML"

    ]


    frequency = {}


    for value in values:

        frequency[value] = (
            frequency.get(value,0)+1
        )


    maximum = 0

    result = None


    for key,value in frequency.items():

        if value > maximum:

            maximum = value

            result = key



    print(
        "Most Frequent:",
        result
    )


    print(
        "Count:",
        maximum
    )



# ---------------------------------------------------------
# 7. Anagram Checking
# ---------------------------------------------------------

def anagram_example():

    separator(
        "7. Anagram Checking"
    )


    word1 = "listen"

    word2 = "silent"


    frequency1 = {}

    frequency2 = {}


    for char in word1:

        frequency1[char] = (
            frequency1.get(char,0)+1
        )


    for char in word2:

        frequency2[char] = (
            frequency2.get(char,0)+1
        )


    print(
        "Are Anagrams:",
        frequency1 == frequency2
    )



# ---------------------------------------------------------
# 8. First Non-Repeating Character
# ---------------------------------------------------------

def first_non_repeating_example():

    separator(
        "8. First Non-Repeating Character"
    )


    text = "aabbcddee"


    frequency = {}


    for char in text:

        frequency[char] = (
            frequency.get(char,0)+1
        )


    result = None


    for char in text:

        if frequency[char] == 1:

            result = char

            break



    print(
        "First Unique Character:",
        result
    )



# ---------------------------------------------------------
# 9. Frequency Comparison
# ---------------------------------------------------------

def frequency_comparison_example():

    separator(
        "9. Frequency Comparison"
    )


    list1 = [

        1,
        2,
        2,
        3

    ]


    list2 = [

        1,
        2,
        3,
        2

    ]


    freq1 = {}

    freq2 = {}


    for item in list1:

        freq1[item] = (
            freq1.get(item,0)+1
        )


    for item in list2:

        freq2[item] = (
            freq2.get(item,0)+1
        )


    print(
        "Same Frequency:",
        freq1 == freq2
    )



# ---------------------------------------------------------
# 10. Using collections.Counter
# ---------------------------------------------------------

def collections_counter_example():

    separator(
        "10. collections.Counter"
    )


    from collections import Counter


    data = [

        "Python",
        "AI",
        "Python",
        "ML",
        "AI"

    ]


    result = Counter(data)


    print(
        result
    )


    print(
        result.most_common()
    )



# ---------------------------------------------------------
# 11. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "11. Real-World Example - Document Analysis"
    )


    document = (

        "AI systems use Python "
        "Python is popular for AI"

    )


    words = document.lower().split()


    frequency = {}


    for word in words:

        frequency[word] = (
            frequency.get(word,0)+1
        )


    print(
        "Word Frequency:"
    )

    print(
        frequency
    )


    print(
        """
AI Engineering Usage:

- Document search
- NLP preprocessing
- Chatbot analytics
- Log analysis
- User behavior tracking
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    frequency_map_definition()

    basic_frequency_example()

    character_frequency_example()

    word_frequency_example()

    duplicate_detection_example()

    most_frequent_element_example()

    anagram_example()

    first_non_repeating_example()

    frequency_comparison_example()

    collections_counter_example()

    real_world_example()



if __name__ == "__main__":

    main()