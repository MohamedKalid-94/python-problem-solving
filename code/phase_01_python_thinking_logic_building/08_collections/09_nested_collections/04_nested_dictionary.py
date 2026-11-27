"""
Topic: Nested Dictionary

Problem:
Store employee details.
"""

employees = {
    "emp1": {
        "name": "Alice",
        "salary": 50000
    },
    "emp2": {
        "name": "Bob",
        "salary": 60000
    }
}

print(employees["emp1"]["name"])
print(employees["emp2"]["salary"])