"""
=========================================================
Topic : Deep Copy in Python

Covered:

1. What is Deep Copy?
2. copy.deepcopy()
3. Independent Nested Objects
4. Deep Copy with Lists
5. Deep Copy with Dictionaries
6. Deep Copy with Custom Objects
7. Deep Copy vs Assignment
8. Real-World Applications

=========================================================
"""

import copy


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Deep Copy?
# ---------------------------------------------------------

def deep_copy_definition():
    separator("1. Deep Copy Definition")

    print(
        """
Deep copy creates a completely independent copy
of an object.

Characteristics:

- Creates a new outer object
- Creates copies of nested objects
- No shared references
- Changes do not affect original object
        """
    )


# ---------------------------------------------------------
# 2. Basic Deep Copy Example
# ---------------------------------------------------------

def basic_deep_copy_example():
    separator("2. Basic Deep Copy Example")

    original = [
        [1, 2],
        [3, 4]
    ]

    copied = copy.deepcopy(original)

    copied[0].append(100)

    print("Original:")
    print(original)

    print("\nDeep Copy:")
    print(copied)


# ---------------------------------------------------------
# 3. Checking Object Identity
# ---------------------------------------------------------

def identity_check_example():
    separator("3. Identity Check")

    original = [
        [10, 20],
        [30, 40]
    ]

    copied = copy.deepcopy(original)

    print(
        "Outer Object Same:",
        original is copied
    )

    print(
        "Inner Object Same:",
        original[0] is copied[0]
    )


# ---------------------------------------------------------
# 4. Deep Copy with List of Dictionaries
# ---------------------------------------------------------

def list_dictionary_example():
    separator("4. Deep Copy with List of Dictionaries")

    employees = [
        {
            "name": "John",
            "skills": ["Python", "SQL"]
        },
        {
            "name": "Alice",
            "skills": ["AI", "ML"]
        }
    ]

    backup = copy.deepcopy(employees)

    backup[0]["skills"].append("GenAI")


    print("Original Employees:")
    print(employees)


    print("\nBackup Employees:")
    print(backup)


# ---------------------------------------------------------
# 5. Deep Copy with Dictionary
# ---------------------------------------------------------

def dictionary_example():
    separator("5. Deep Copy Dictionary")

    configuration = {

        "database": {
            "host": "localhost",
            "port": 5432
        },

        "cache": {
            "enabled": True
        }
    }


    copied_config = copy.deepcopy(configuration)


    copied_config["database"]["port"] = 3306


    print("Original Configuration:")

    print(configuration)


    print("\nCopied Configuration:")

    print(copied_config)


# ---------------------------------------------------------
# 6. Deep Copy with Custom Objects
# ---------------------------------------------------------

class Employee:

    def __init__(self, name, skills):

        self.name = name
        self.skills = skills


    def display(self):

        print(
            self.name,
            self.skills
        )


def custom_object_example():
    separator("6. Deep Copy Custom Object")


    employee1 = Employee(
        "Kalid",
        ["Python", "AI"]
    )


    employee2 = copy.deepcopy(employee1)


    employee2.skills.append("LangChain")


    print("Original Employee:")

    employee1.display()


    print("\nCopied Employee:")

    employee2.display()



# ---------------------------------------------------------
# 7. Deep Copy vs Assignment
# ---------------------------------------------------------

def assignment_vs_deep_copy():
    separator("7. Assignment vs Deep Copy")


    original = [
        [1,2],
        [3,4]
    ]


    assignment = original


    deep_copy = copy.deepcopy(original)



    assignment[0].append(99)


    deep_copy[1].append(100)



    print("Original:")

    print(original)


    print("\nAssignment:")

    print(assignment)


    print("\nDeep Copy:")

    print(deep_copy)



# ---------------------------------------------------------
# 8. Memory Comparison
# ---------------------------------------------------------

def memory_comparison():

    separator("8. Reference Comparison")


    data = [
        {
            "value":100
        }
    ]


    copied = copy.deepcopy(data)


    print(
        "Same Object:",
        data is copied
    )


    print(
        "Same Nested Object:",
        data[0] is copied[0]
    )



# ---------------------------------------------------------
# 9. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "9. Real-World Example - AI Model Configuration"
    )


    model_config = {

        "model_name":"GPT",

        "parameters":{

            "temperature":0.7,

            "max_tokens":2048

        },

        "tools":[
            "RAG",
            "Agent"
        ]

    }


    experiment_config = copy.deepcopy(
        model_config
    )


    experiment_config["parameters"]["temperature"] = 0.2

    experiment_config["tools"].append(
        "MCP"
    )


    print("Production Config:")

    print(model_config)


    print("\nExperiment Config:")

    print(experiment_config)



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    deep_copy_definition()

    basic_deep_copy_example()

    identity_check_example()

    list_dictionary_example()

    dictionary_example()

    custom_object_example()

    assignment_vs_deep_copy()

    memory_comparison()

    real_world_example()



if __name__ == "__main__":

    main()