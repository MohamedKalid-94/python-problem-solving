"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Stack Pattern

Covered:

1. What is Stack?
2. LIFO Concept
3. Push and Pop Operations
4. Stack using List
5. Balanced Parentheses
6. Expression Evaluation Concept
7. Undo / Redo Pattern
8. Monotonic Stack Introduction
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Stack Definition
# ---------------------------------------------------------

def stack_definition():

    separator(
        "1. Stack Pattern Definition"
    )


    print(
        """
Stack is a data structure that follows:

LIFO

Last In First Out


Example:

Stack of Plates:

Last plate placed
is removed first.


Operations:

Push  -> Add element

Pop   -> Remove top element

Peek  -> View top element


Common uses:

- Function calls
- Undo operations
- Expression checking
- Browser history
- Backtracking
        """
    )



# ---------------------------------------------------------
# 2. Basic Stack using List
# ---------------------------------------------------------

def basic_stack_example():

    separator(
        "2. Basic Stack using List"
    )


    stack = []


    stack.append(
        "Python"
    )


    stack.append(
        "AI"
    )


    stack.append(
        "LLM"
    )


    print(
        "Stack:",
        stack
    )


    removed = stack.pop()


    print(
        "Removed:",
        removed
    )


    print(
        "After Pop:",
        stack
    )



# ---------------------------------------------------------
# 3. Stack Push Operation
# ---------------------------------------------------------

def push_operation():

    separator(
        "3. Push Operation"
    )


    stack = []


    items = [

        10,
        20,
        30

    ]


    for item in items:

        stack.append(item)



    print(
        stack
    )



# ---------------------------------------------------------
# 4. Stack Pop Operation
# ---------------------------------------------------------

def pop_operation():

    separator(
        "4. Pop Operation"
    )


    stack = [

        10,
        20,
        30

    ]


    while stack:

        print(
            "Removed:",
            stack.pop()
        )



# ---------------------------------------------------------
# 5. Peek Operation
# ---------------------------------------------------------

def peek_operation():

    separator(
        "5. Peek Operation"
    )


    stack = [

        "Login",
        "Dashboard",
        "Profile"

    ]


    top = stack[-1]


    print(
        "Top Element:",
        top
    )



# ---------------------------------------------------------
# 6. Reverse String using Stack
# ---------------------------------------------------------

def reverse_string_example():

    separator(
        "6. Reverse String using Stack"
    )


    text = "Python"


    stack = []


    for char in text:

        stack.append(char)



    reversed_text = ""


    while stack:

        reversed_text += stack.pop()



    print(
        "Reverse:",
        reversed_text
    )



# ---------------------------------------------------------
# 7. Balanced Parentheses
# ---------------------------------------------------------

def balanced_parentheses_example():

    separator(
        "7. Balanced Parentheses"
    )


    expression = "(a+b)*(c+d)"


    stack = []


    pairs = {

        ")":"(",

        "]":"[",

        "}":"{"

    }


    balanced = True


    for char in expression:


        if char in "([{":

            stack.append(char)


        elif char in ")]}":


            if (
                not stack
                or
                stack.pop()
                !=
                pairs[char]
            ):

                balanced = False

                break



    if stack:

        balanced = False



    print(
        "Balanced:",
        balanced
    )



# ---------------------------------------------------------
# 8. Undo Operation Pattern
# ---------------------------------------------------------

def undo_pattern_example():

    separator(
        "8. Undo Operation Pattern"
    )


    actions = []


    actions.append(
        "Write Python"
    )


    actions.append(
        "Add Function"
    )


    actions.append(
        "Save File"
    )


    print(
        "Actions:",
        actions
    )


    undo = actions.pop()


    print(
        "Undo:",
        undo
    )


# ---------------------------------------------------------
# 9. Monotonic Stack Introduction
# ---------------------------------------------------------

def monotonic_stack_example():

    separator(
        "9. Monotonic Stack Introduction"
    )


    numbers = [

        2,
        1,
        5,
        3,
        4

    ]


    stack = []


    for number in numbers:


        while (
            stack
            and
            stack[-1] < number
        ):

            stack.pop()


        stack.append(number)



    print(
        "Monotonic Stack:",
        stack
    )



# ---------------------------------------------------------
# 10. Function Call Stack
# ---------------------------------------------------------

def function_call_stack_example():

    separator(
        "10. Function Call Stack"
    )


    print(
        """
When functions call other functions,
Python internally uses a call stack.


Example:

main()

  calls

function_a()

  calls

function_b()


function_b finishes first,
then function_a,
then main.


This follows:

LIFO principle.
        """
    )



# ---------------------------------------------------------
# 11. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "11. Real-World Example - Agent History"
    )


    agent_steps = []


    agent_steps.append(
        "User Query"
    )


    agent_steps.append(
        "Retrieve Documents"
    )


    agent_steps.append(
        "Generate Answer"
    )


    print(
        "Agent Steps:",
        agent_steps
    )


    last_step = agent_steps.pop()


    print(
        "Rollback Step:",
        last_step
    )


    print(
        """
AI Engineering Usage:

- Agent workflow rollback
- Conversation history
- Tool execution tracking
- Backtracking algorithms
- Parsing LLM outputs
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    stack_definition()

    basic_stack_example()

    push_operation()

    pop_operation()

    peek_operation()

    reverse_string_example()

    balanced_parentheses_example()

    undo_pattern_example()

    monotonic_stack_example()

    function_call_stack_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()