"""
=========================================================
Topic : Namespaces in Python

Covered:

1. What is Namespace?
2. Built-in Namespace
3. Global Namespace
4. Local Namespace
5. Enclosing Namespace
6. LEGB Rule
7. Namespace Dictionary
8. Variable Scope
9. Global Keyword
10. Nonlocal Keyword
11. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Namespace?
# ---------------------------------------------------------

def namespace_definition():
    separator("1. Namespace Definition")

    print(
        """
A namespace is a container that stores
names and their object references.

Python uses namespaces to avoid
name conflicts.

Types of namespaces:

1. Built-in Namespace
2. Global Namespace
3. Local Namespace
4. Enclosing Namespace
        """
    )


# ---------------------------------------------------------
# 2. Built-in Namespace
# ---------------------------------------------------------

def builtin_namespace_example():

    separator(
        "2. Built-in Namespace"
    )


    print(
        len("Python")
    )


    print(
        type(100)
    )


    print(
        """
Examples of built-in names:

print()
len()
type()
sum()
max()
min()
        """
    )



# ---------------------------------------------------------
# 3. Global Namespace
# ---------------------------------------------------------

company = "AI Solutions"

employee_count = 100


def global_namespace_example():

    separator(
        "3. Global Namespace"
    )


    print(
        "Company:",
        company
    )


    print(
        "Employee Count:",
        employee_count
    )


    print(
        """
Variables created outside functions
belong to global namespace.
        """
    )



# ---------------------------------------------------------
# 4. Local Namespace
# ---------------------------------------------------------

def local_namespace_example():

    separator(
        "4. Local Namespace"
    )


    role = "AI Engineer"


    experience = 8


    print(
        "Role:",
        role
    )


    print(
        "Experience:",
        experience
    )


    print(
        """
Variables inside functions
belong to local namespace.
        """
    )



# ---------------------------------------------------------
# 5. Enclosing Namespace
# ---------------------------------------------------------

def enclosing_namespace_example():

    separator(
        "5. Enclosing Namespace"
    )


    message = "Outer Function"


    def inner_function():

        print(
            message
        )


    inner_function()



# ---------------------------------------------------------
# 6. LEGB Rule
# ---------------------------------------------------------

def legb_rule_example():

    separator(
        "6. LEGB Rule"
    )


    print(
        """
Python searches variables in this order:

L - Local
E - Enclosing
G - Global
B - Built-in

Example:

Local variable is checked first,
then enclosing,
then global,
then built-in.
        """
    )



# ---------------------------------------------------------
# 7. Namespace Dictionary
# ---------------------------------------------------------

def namespace_dictionary_example():

    separator(
        "7. Namespace Dictionary"
    )


    username = "Kalid"


    print(
        globals()
    )


    print(
        "\nLocal Namespace:"
    )


    print(
        locals()
    )



# ---------------------------------------------------------
# 8. Variable Scope Example
# ---------------------------------------------------------

value = "Global Value"


def scope_example():

    value = "Local Value"


    print(
        "Inside Function:",
        value
    )



def variable_scope_example():

    separator(
        "8. Variable Scope"
    )


    print(
        "Outside Function:",
        value
    )


    scope_example()



# ---------------------------------------------------------
# 9. Global Keyword
# ---------------------------------------------------------

counter = 0


def increase_counter():

    global counter


    counter += 1



def global_keyword_example():

    separator(
        "9. Global Keyword"
    )


    print(
        "Before:",
        counter
    )


    increase_counter()


    print(
        "After:",
        counter
    )


    print(
        """
global keyword allows modifying
global variables inside functions.
        """
    )



# ---------------------------------------------------------
# 10. Nonlocal Keyword
# ---------------------------------------------------------

def nonlocal_keyword_example():

    separator(
        "10. Nonlocal Keyword"
    )


    count = 0


    def inner():

        nonlocal count


        count += 1


        print(
            count
        )


    inner()

    inner()



# ---------------------------------------------------------
# 11. Namespace Conflict Example
# ---------------------------------------------------------

def namespace_conflict_example():

    separator(
        "11. Namespace Conflict"
    )


    name = "Local Name"


    print(
        name
    )


    print(
        """
Same variable name can exist
in different namespaces.
        """
    )



# ---------------------------------------------------------
# 12. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "12. Real-World Example - AI Application"
    )


    model_name = "GPT"

    temperature = 0.7


    def generate_response():

        prompt = "Explain AI"


        print(
            "Model:",
            model_name
        )


        print(
            "Prompt:",
            prompt
        )


    generate_response()


    print(
        """
Namespaces help manage:

- Configuration values
- API clients
- Database connections
- AI pipeline states
- Application modules
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    namespace_definition()

    builtin_namespace_example()

    global_namespace_example()

    local_namespace_example()

    enclosing_namespace_example()

    legb_rule_example()

    namespace_dictionary_example()

    variable_scope_example()

    global_keyword_example()

    nonlocal_keyword_example()

    namespace_conflict_example()

    real_world_example()



if __name__ == "__main__":

    main()