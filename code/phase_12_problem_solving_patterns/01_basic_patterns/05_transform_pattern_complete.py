"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Transform Pattern

Covered:

1. What is Transform Pattern?
2. Data Transformation
3. Mapping Values
4. String Transformation
5. List Transformation
6. Dictionary Transformation
7. Using map()
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Transform Pattern Definition
# ---------------------------------------------------------

def transform_definition():

    separator(
        "1. Transform Pattern Definition"
    )


    print(
        """
Transform Pattern is a problem-solving technique
used to convert each element into a new form.

Input Data

      |
      ↓

Apply Transformation Rule

      |
      ↓

New Data


Common uses:

- Data conversion
- Feature engineering
- Data cleaning
- Formatting
- API response processing


Pattern:

result = []

for item in data:

    transformed_item = operation(item)

    result.append(transformed_item)
        """
    )



# ---------------------------------------------------------
# 2. Basic Transformation
# ---------------------------------------------------------

def basic_transform_example():

    separator(
        "2. Basic Transformation"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    doubled = []


    for number in numbers:

        doubled.append(
            number * 2
        )


    print(
        "Doubled Values:",
        doubled
    )



# ---------------------------------------------------------
# 3. Square Transformation
# ---------------------------------------------------------

def square_transform_example():

    separator(
        "3. Square Transformation"
    )


    numbers = [

        2,
        4,
        6

    ]


    squares = []


    for number in numbers:

        squares.append(
            number ** 2
        )


    print(
        squares
    )



# ---------------------------------------------------------
# 4. String Transformation
# ---------------------------------------------------------

def string_transform_example():

    separator(
        "4. String Transformation"
    )


    names = [

        "kalid",
        "python",
        "ai"

    ]


    upper_names = []


    for name in names:

        upper_names.append(
            name.upper()
        )


    print(
        upper_names
    )



# ---------------------------------------------------------
# 5. Dictionary Transformation
# ---------------------------------------------------------

def dictionary_transform_example():

    separator(
        "5. Dictionary Transformation"
    )


    users = [

        {
            "name":"Kalid",
            "age":30
        },

        {
            "name":"John",
            "age":25
        }

    ]


    transformed_users = []


    for user in users:

        transformed_users.append(

            {
                "username": user["name"].lower(),

                "is_adult": user["age"] >= 18
            }

        )


    print(
        transformed_users
    )



# ---------------------------------------------------------
# 6. List Comprehension Transformation
# ---------------------------------------------------------

def list_comprehension_transform():

    separator(
        "6. List Comprehension Transformation"
    )


    numbers = [

        10,
        20,
        30

    ]


    result = [

        number / 10

        for number in numbers

    ]


    print(
        result
    )



# ---------------------------------------------------------
# 7. Using map()
# ---------------------------------------------------------

def map_function_example():

    separator(
        "7. map() Transformation"
    )


    numbers = [

        1,
        2,
        3,
        4

    ]


    result = list(

        map(

            lambda x: x * x,

            numbers

        )

    )


    print(
        result
    )



# ---------------------------------------------------------
# 8. Nested Data Transformation
# ---------------------------------------------------------

def nested_data_transform():

    separator(
        "8. Nested Data Transformation"
    )


    products = [

        {
            "name":"Laptop",
            "price":50000
        },

        {
            "name":"Mouse",
            "price":1000
        }

    ]


    updated_products = []


    for product in products:

        updated_products.append(

            {
                "product_name":
                    product["name"],

                "discount_price":
                    product["price"] * 0.9

            }

        )


    print(
        updated_products
    )



# ---------------------------------------------------------
# 9. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "9. Real-World Example - Embedding Transformation"
    )


    documents = [

        "Python programming",

        "Generative AI",

        "Machine Learning"

    ]


    processed_documents = []


    for document in documents:

        processed_documents.append(

            document.lower()

        )


    print(
        "Processed Documents:"
    )


    print(
        processed_documents
    )


    print(
        """
AI Engineering Usage:

- Text preprocessing
- Token normalization
- Feature engineering
- Data pipeline preparation
- API response transformation
- RAG document processing
        """
    )



# ---------------------------------------------------------
# 10. Real-World API Transformation
# ---------------------------------------------------------

def api_response_transform():

    separator(
        "10. API Response Transformation"
    )


    api_users = [

        {
            "first_name":"Mohamed",
            "last_name":"Kalid"
        },

        {
            "first_name":"John",
            "last_name":"Smith"
        }

    ]


    usernames = []


    for user in api_users:

        usernames.append(

            user["first_name"]
            +
            "_"
            +
            user["last_name"]

        )


    print(
        usernames
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    transform_definition()

    basic_transform_example()

    square_transform_example()

    string_transform_example()

    dictionary_transform_example()

    list_comprehension_transform()

    map_function_example()

    nested_data_transform()

    ai_real_world_example()

    api_response_transform()



if __name__ == "__main__":

    main()