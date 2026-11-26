"""
=========================================================
Topic : collections module - Real World Examples

Author: Mohamed Kalid

Covered:

1. Counter
2. defaultdict
3. deque
4. namedtuple

Real-world use cases:

- Log Analysis
- E-commerce Analytics
- Student Management
- Employee System
- Task Queue
- Browser History
- Inventory Management
- API Response Handling

=========================================================
"""


from collections import Counter, defaultdict, deque, namedtuple



def separator(title):

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)



def main():


    # =====================================================
    # 1. Log Analyzer
    #
    # Counter:
    # Count log levels
    # =====================================================

    separator("1. Log Analyzer using Counter")


    logs = [

        "INFO",

        "ERROR",

        "INFO",

        "WARNING",

        "ERROR",

        "ERROR",

        "INFO"

    ]


    log_counter = Counter(logs)


    print(log_counter)


    print(
        "Most common:",
        log_counter.most_common(1)
    )



    # =====================================================
    # 2. Website Traffic Analyzer
    #
    # Counter:
    # Count page visits
    # =====================================================

    separator("2. Website Traffic Analytics")


    visits = [

        "/home",

        "/login",

        "/home",

        "/products",

        "/home",

        "/login"

    ]


    page_views = Counter(visits)


    print(page_views)


    print(
        "Popular Page:",
        page_views.most_common(1)
    )



    # =====================================================
    # 3. E-Commerce Inventory
    #
    # defaultdict:
    # Group products by category
    # =====================================================

    separator("3. Inventory Management")


    products = [

        ("Laptop", "Electronics"),

        ("Mobile", "Electronics"),

        ("Shoes", "Fashion"),

        ("T-Shirt", "Fashion"),

        ("Book", "Education")

    ]


    inventory = defaultdict(list)


    for product, category in products:

        inventory[category].append(product)



    for category, items in inventory.items():

        print(
            category,
            ":",
            items
        )



    # =====================================================
    # 4. Student Management System
    #
    # defaultdict:
    # Group students by department
    # =====================================================

    separator("4. Student Management")


    students = [

        ("Alice", "Computer Science"),

        ("Bob", "Mechanical"),

        ("Chris", "Computer Science"),

        ("David", "Electrical")

    ]


    departments = defaultdict(list)


    for name, department in students:

        departments[department].append(name)


    print(departments)



    # =====================================================
    # 5. Employee Database
    #
    # namedtuple:
    # Store structured records
    # =====================================================

    separator("5. Employee Database")


    Employee = namedtuple(

        "Employee",

        [

            "id",

            "name",

            "role",

            "salary"

        ]

    )


    employees = [

        Employee(

            1,

            "Alice",

            "Developer",

            90000

        ),

        Employee(

            2,

            "Bob",

            "Tester",

            70000

        )

    ]


    for employee in employees:

        print(

            employee.name,

            employee.role,

            employee.salary

        )



    # =====================================================
    # 6. Task Queue System
    #
    # deque:
    # FIFO processing
    # =====================================================

    separator("6. Task Queue System")


    task_queue = deque()


    task_queue.append(

        "Process Payment"

    )


    task_queue.append(

        "Send Email"

    )


    task_queue.append(

        "Generate Report"

    )


    while task_queue:


        task = task_queue.popleft()


        print(

            "Processing:",

            task

        )



    # =====================================================
    # 7. Browser History
    #
    # deque maxlen
    # =====================================================

    separator("7. Browser History")


    history = deque(maxlen=5)


    pages = [

        "Google",

        "YouTube",

        "GitHub",

        "ChatGPT",

        "StackOverflow",

        "LinkedIn"

    ]


    for page in pages:

        history.append(page)


    print(history)



    # =====================================================
    # 8. LRU Cache Concept
    #
    # deque:
    # Recently used items
    # =====================================================

    separator("8. LRU Cache Concept")


    cache = deque(maxlen=3)


    cache.append("Page1")

    cache.append("Page2")

    cache.append("Page3")


    print(cache)


    cache.append("Page4")


    print(

        "After new item:",

        cache

    )



    # =====================================================
    # 9. Word Frequency Analyzer
    #
    # Counter
    # =====================================================

    separator("9. Word Frequency Analyzer")


    sentence = """

    Python is powerful.

    Python is easy.

    Python is popular.

    """


    words = (

        sentence

        .lower()

        .replace(".", "")

        .split()

    )


    frequency = Counter(words)


    print(frequency)


    print(

        frequency.most_common(3)

    )



    # =====================================================
    # 10. Order Processing System
    #
    # defaultdict + Counter
    # =====================================================

    separator("10. Order Processing System")


    orders = [

        ("Laptop", "Electronics"),

        ("Phone", "Electronics"),

        ("Laptop", "Electronics"),

        ("Shoes", "Fashion")

    ]


    category_orders = defaultdict(int)


    product_count = Counter()


    for product, category in orders:


        category_orders[category] += 1


        product_count[product] += 1



    print(

        "Category Orders:",

        category_orders

    )


    print(

        "Product Count:",

        product_count

    )



    # =====================================================
    # 11. API Response Object
    #
    # namedtuple
    # =====================================================

    separator("11. API Response")


    Response = namedtuple(

        "Response",

        [

            "status",

            "message",

            "data"

        ]

    )


    response = Response(

        200,

        "Success",

        {

            "user": "Kalid"

        }

    )


    print(response)

    print(response.data)



    # =====================================================
    # 12. BFS Queue Example
    #
    # deque
    # =====================================================

    separator("12. BFS Graph Traversal")


    graph = {


        "A": ["B", "C"],

        "B": ["D"],

        "C": ["E"],

        "D": [],

        "E": []

    }


    queue = deque(["A"])


    visited = set()



    while queue:


        node = queue.popleft()


        if node not in visited:


            print(node)


            visited.add(node)


            queue.extend(

                graph[node]

            )



    # =====================================================
    # 13. Combined Mini System
    #
    # All collections together
    # =====================================================

    separator("13. Combined Collection System")


    Employee = namedtuple(

        "Employee",

        [

            "name",

            "department"

        ]

    )


    employees = [

        Employee(

            "Alice",

            "AI"

        ),

        Employee(

            "Bob",

            "Backend"

        ),

        Employee(

            "Chris",

            "AI"

        )

    ]


    department_count = Counter()


    employee_group = defaultdict(list)



    for employee in employees:


        department_count[employee.department] += 1


        employee_group[employee.department].append(

            employee.name

        )



    print(

        department_count

    )


    print(

        employee_group

    )



if __name__ == "__main__":

    main()