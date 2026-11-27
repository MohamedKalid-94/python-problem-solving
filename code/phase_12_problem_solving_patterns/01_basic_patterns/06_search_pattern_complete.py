"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Search Pattern

Covered:

1. What is Search Pattern?
2. Linear Search
3. Searching in Strings
4. Searching Objects
5. Multiple Match Search
6. Binary Search Introduction
7. Search Optimization
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Search Pattern Definition
# ---------------------------------------------------------

def search_definition():

    separator(
        "1. Search Pattern Definition"
    )


    print(
        """
Search Pattern is a technique used to
find required data from a collection.

Basic idea:

Input Data

      |
      ↓

Compare each element

      |
      ↓

Return matching result


Common uses:

- Finding records
- Searching documents
- Database queries
- AI retrieval systems
- User lookup


Types:

1. Linear Search
2. Binary Search
3. Hash Based Search
        """
    )



# ---------------------------------------------------------
# 2. Basic Linear Search
# ---------------------------------------------------------

def linear_search_example():

    separator(
        "2. Linear Search"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50

    ]


    target = 30


    found = False


    for number in numbers:

        if number == target:

            found = True

            break



    print(
        "Found:",
        found
    )



# ---------------------------------------------------------
# 3. Linear Search with Index
# ---------------------------------------------------------

def search_with_index():

    separator(
        "3. Search With Index"
    )


    names = [

        "Python",
        "Java",
        "AI",
        "ML"

    ]


    target = "AI"


    index = -1


    for i in range(len(names)):

        if names[i] == target:

            index = i

            break



    print(
        "Index:",
        index
    )



# ---------------------------------------------------------
# 4. Search String
# ---------------------------------------------------------

def string_search_example():

    separator(
        "4. String Search"
    )


    sentence = (
        "Python is popular for AI development"
    )


    keyword = "AI"


    if keyword in sentence:

        print(
            "Keyword Found"
        )

    else:

        print(
            "Keyword Not Found"
        )



# ---------------------------------------------------------
# 5. Search Multiple Values
# ---------------------------------------------------------

def multiple_search_example():

    separator(
        "5. Multiple Search"
    )


    numbers = [

        10,
        20,
        30,
        20,
        40

    ]


    target = 20


    positions = []


    for index, value in enumerate(numbers):

        if value == target:

            positions.append(index)



    print(
        "Positions:",
        positions
    )



# ---------------------------------------------------------
# 6. Search Dictionary
# ---------------------------------------------------------

def dictionary_search_example():

    separator(
        "6. Dictionary Search"
    )


    users = {

        101:"Kalid",

        102:"John",

        103:"Alice"

    }


    user_id = 102


    if user_id in users:

        print(
            users[user_id]
        )

    else:

        print(
            "User Not Found"
        )



# ---------------------------------------------------------
# 7. Search Objects
# ---------------------------------------------------------

def object_search_example():

    separator(
        "7. Object Search"
    )


    employees = [

        {
            "id":1,
            "name":"Kalid",
            "role":"AI Engineer"
        },

        {
            "id":2,
            "name":"John",
            "role":"Developer"
        }

    ]


    search_id = 2


    result = None


    for employee in employees:

        if employee["id"] == search_id:

            result = employee

            break



    print(
        result
    )



# ---------------------------------------------------------
# 8. Binary Search Introduction
# ---------------------------------------------------------

def binary_search_intro():

    separator(
        "8. Binary Search Introduction"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50,
        60

    ]


    target = 40


    left = 0

    right = len(numbers)-1


    found = False


    while left <= right:


        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            found = True

            break


        elif numbers[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "Found:",
        found
    )



# ---------------------------------------------------------
# 9. Search Optimization
# ---------------------------------------------------------

def search_comparison():

    separator(
        "9. Search Comparison"
    )


    print(
        """
Linear Search:

Time Complexity:
O(n)

Checks every element.


Binary Search:

Time Complexity:
O(log n)

Requires sorted data.


Hash Search:

Average:
O(1)

Example:
Dictionary lookup
        """
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - Document Search"
    )


    documents = [

        "Python programming guide",

        "Machine learning basics",

        "Generative AI tutorial",

        "Database concepts"

    ]


    keyword = "AI"


    results = []


    for document in documents:

        if keyword.lower() in document.lower():

            results.append(document)



    print(
        "Search Results:"
    )


    print(
        results
    )


    print(
        """
AI Engineering Usage:

- RAG document retrieval
- Vector database search
- User search
- Log analysis
- Recommendation systems
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    search_definition()

    linear_search_example()

    search_with_index()

    string_search_example()

    multiple_search_example()

    dictionary_search_example()

    object_search_example()

    binary_search_intro()

    search_comparison()

    ai_real_world_example()



if __name__ == "__main__":

    main()