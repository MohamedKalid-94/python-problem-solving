"""
=========================================================
Topic : Python Internals - Real World Problems

Covered:

1. Memory Optimization
2. Reference Management
3. Copy Problems
4. Mutable Object Bugs
5. Immutable Object Usage
6. Hashing Based Cache System
7. Identity Debugging
8. Namespace Management
9. AI/Backend Real-World Scenarios

=========================================================
"""

import copy
import sys


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Problem 1: Memory Optimization using Generator
# ---------------------------------------------------------

def memory_optimization_problem():

    separator(
        "1. Memory Optimization - Large Data Processing"
    )

    print(
        """
Problem:

Loading millions of records into a list
consumes large memory.

Solution:

Use generator for lazy evaluation.
        """
    )


    # Bad approach
    data = [
        x for x in range(100000)
    ]


    print(
        "List Memory Count:",
        len(data)
    )


    # Better approach
    generator = (
        x for x in range(100000)
    )


    print(
        "Generator First Value:",
        next(generator)
    )


# ---------------------------------------------------------
# Problem 2: Reference Sharing Bug
# ---------------------------------------------------------

def reference_bug_problem():

    separator(
        "2. Reference Sharing Bug"
    )


    user_profile = {

        "name":"Kalid",

        "skills":[
            "Python",
            "AI"
        ]

    }


    backup_profile = user_profile


    backup_profile["skills"].append(
        "GenAI"
    )


    print(
        "Original Profile:"
    )

    print(user_profile)


    print(
        """
Problem:

Both variables point to the same object.
        """
    )



# ---------------------------------------------------------
# Problem 3: Fix Reference Sharing using Copy
# ---------------------------------------------------------

def copy_solution_problem():

    separator(
        "3. Fix Reference Problem"
    )


    user_profile = {

        "name":"Kalid",

        "skills":[
            "Python",
            "AI"
        ]

    }


    backup_profile = copy.deepcopy(
        user_profile
    )


    backup_profile["skills"].append(
        "LangChain"
    )


    print(
        "Original:"
    )

    print(user_profile)


    print(
        "\nBackup:"
    )

    print(backup_profile)



# ---------------------------------------------------------
# Problem 4: Mutable Default Argument
# ---------------------------------------------------------

def add_document(
        document,
        documents=[]
):

    documents.append(
        document
    )

    return documents



def mutable_default_problem():

    separator(
        "4. Mutable Default Argument Problem"
    )


    print(
        add_document(
            "doc1.pdf"
        )
    )


    print(
        add_document(
            "doc2.pdf"
        )
    )


    print(
        """
Problem:

Default list is shared between calls.
        """
    )



# ---------------------------------------------------------
# Problem 5: Safe Mutable Handling
# ---------------------------------------------------------

def safe_add_document(
        document,
        documents=None
):

    if documents is None:

        documents = []


    documents.append(
        document
    )

    return documents



def safe_mutable_solution():

    separator(
        "5. Safe Mutable Handling"
    )


    print(
        safe_add_document(
            "resume.pdf"
        )
    )


    print(
        safe_add_document(
            "invoice.pdf"
        )
    )



# ---------------------------------------------------------
# Problem 6: AI Configuration Copy
# ---------------------------------------------------------

def ai_configuration_problem():

    separator(
        "6. AI Model Configuration Management"
    )


    production_config = {

        "model":"LLM",

        "parameters":{

            "temperature":0.7,

            "max_tokens":2000

        }

    }


    experiment_config = copy.deepcopy(
        production_config
    )


    experiment_config["parameters"]["temperature"] = 0.2


    print(
        "Production:"
    )

    print(
        production_config
    )


    print(
        "\nExperiment:"
    )

    print(
        experiment_config
    )



# ---------------------------------------------------------
# Problem 7: Hash Based Cache
# ---------------------------------------------------------

def hash_cache_problem():

    separator(
        "7. Hash Based Cache System"
    )


    cache = {}


    prompt = (
        "Explain machine learning"
    )


    prompt_key = hash(
        prompt
    )


    cache[prompt_key] = (
        "Generated AI Response"
    )


    print(
        "Cache Key:"
    )

    print(
        prompt_key
    )


    print(
        "\nCached Result:"
    )

    print(
        cache[prompt_key]
    )



# ---------------------------------------------------------
# Problem 8: Identity Debugging
# ---------------------------------------------------------

def identity_debugging_problem():

    separator(
        "8. Identity Debugging"
    )


    data1 = [

        "AI",
        "ML"

    ]


    data2 = data1


    print(
        "Data1 ID:",
        id(data1)
    )


    print(
        "Data2 ID:",
        id(data2)
    )


    print(
        "Same Object:",
        data1 is data2
    )


    print(
        """
Useful when debugging
unexpected data changes.
        """
    )



# ---------------------------------------------------------
# Problem 9: Namespace Management
# ---------------------------------------------------------

def namespace_management_problem():

    separator(
        "9. Namespace Management"
    )


    model_name = "GPT"


    def generate():

        prompt = "Explain AI"


        print(
            "Model:",
            model_name
        )


        print(
            "Prompt:",
            prompt
        )


    generate()



# ---------------------------------------------------------
# Problem 10: RAG Pipeline State Management
# ---------------------------------------------------------

def rag_pipeline_problem():

    separator(
        "10. RAG Pipeline State Management"
    )


    state = {

        "documents":[
            "python.pdf",
            "ai.pdf"
        ],

        "chunks":[],


        "status":"loading"

    }


    processing_state = copy.deepcopy(
        state
    )


    processing_state["chunks"].extend(
        [
            "chunk1",
            "chunk2"
        ]
    )


    processing_state["status"] = (
        "completed"
    )


    print(
        "Original State:"
    )

    print(state)


    print(
        "\nProcessing State:"
    )

    print(processing_state)



# ---------------------------------------------------------
# Problem 11: Memory Usage Monitoring
# ---------------------------------------------------------

def memory_monitoring_problem():

    separator(
        "11. Memory Monitoring"
    )


    large_object = [

        x for x in range(10000)

    ]


    print(
        "Object Size:",
        sys.getsizeof(large_object),
        "bytes"
    )


    print(
        """
Useful for:

- Large datasets
- ML pipelines
- Batch processing
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    memory_optimization_problem()

    reference_bug_problem()

    copy_solution_problem()

    mutable_default_problem()

    safe_mutable_solution()

    ai_configuration_problem()

    hash_cache_problem()

    identity_debugging_problem()

    namespace_management_problem()

    rag_pipeline_problem()

    memory_monitoring_problem()



if __name__ == "__main__":

    main()