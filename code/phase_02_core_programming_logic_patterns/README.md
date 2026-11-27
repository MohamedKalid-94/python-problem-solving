# Programming Patterns

A comprehensive collection of Python programs demonstrating the most common programming patterns used in software development, coding interviews, competitive programming, data processing, and AI engineering.

This module focuses on **how to think while solving problems**, rather than memorizing solutions. By mastering these patterns, you can solve hundreds of different programming problems using reusable approaches.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand common programming patterns
- Choose the right pattern for a problem
- Write efficient and readable code
- Analyze time and space complexity
- Improve problem-solving skills
- Prepare for Python coding interviews
- Build a strong foundation for Data Structures and Algorithms

---

# Folder Structure

```
programming_patterns/

│
├── 01_counter_pattern/
│   ├── 01_count_positive_numbers.py
│   ├── 02_count_vowels.py
│   ├── 03_count_words.py
│   └── 04_count_even_numbers.py
│
├── 02_accumulator_pattern/
│   ├── 01_sum_numbers.py
│   ├── 02_product_numbers.py
│   ├── 03_calculate_average.py
│   └── 04_running_total.py
│
├── 03_max_min_pattern/
│   ├── 01_find_largest.py
│   ├── 02_find_smallest.py
│   ├── 03_highest_salary.py
│   └── 04_longest_word.py
│
├── 04_search_pattern/
│   ├── 01_find_element.py
│   ├── 02_contains_check.py
│   ├── 03_linear_search.py
│   ├── 04_first_occurrence.py
│   └── 05_last_occurrence.py
│
├── 05_filter_pattern/
│   ├── 01_filter_valid_values.py
│   ├── 02_remove_duplicates.py
│   ├── 03_filter_positive_numbers.py
│   └── 04_filter_even_numbers.py
│
├── 06_transform_pattern/
│   ├── 01_map_values.py
│   ├── 02_square_numbers.py
│   ├── 03_uppercase_strings.py
│   └── 04_currency_conversion.py
│
├── 07_frequency_map_pattern/
│   ├── 01_count_occurrences.py
│   ├── 02_character_frequency.py
│   ├── 03_word_frequency.py
│   ├── 04_most_repeated_item.py
│   └── 05_histogram.py
│
├── 08_grouping_pattern/
│   ├── 01_group_students.py
│   ├── 02_group_employees.py
│   ├── 03_group_products.py
│   └── 04_group_by_category.py
│
├── 09_two_pointer_pattern/
│   ├── 01_palindrome_check.py
│   ├── 02_reverse_array.py
│   ├── 03_merge_sorted_arrays.py
│   ├── 04_remove_duplicates.py
│   └── 05_sorted_array_operations.py
│
├── 10_sliding_window_pattern/
│   ├── 01_maximum_sum_subarray.py
│   ├── 02_longest_substring.py
│   ├── 03_moving_average.py
│   └── 04_window_optimization.py
│
├── 11_prefix_sum_pattern/
│   ├── 01_range_sum.py
│   ├── 02_cumulative_total.py
│   └── 03_fast_range_calculation.py
│
├── 12_hash_map_thinking/
│   ├── 01_fast_lookup.py
│   ├── 02_cache_example.py
│   ├── 03_index_mapping.py
│   └── 04_duplicate_detection.py
│
├── 13_nested_loop_thinking/
│   ├── 01_matrix_operations.py
│   ├── 02_grid_traversal.py
│   ├── 03_pattern_printing.py
│   └── 04_compare_elements.py
│
├── 14_state_tracking_pattern/
│   ├── 01_previous_current.py
│   ├── 02_value_transition.py
│   ├── 03_flag_tracking.py
│   └── 04_status_changes.py
│
├── 15_simulation_pattern/
│   ├── 01_atm_simulation.py
│   ├── 02_traffic_light.py
│   ├── 03_game_simulation.py
│   ├── 04_robot_movement.py
│   └── 05_bank_account.py
│
├── interview_qanda.md
├── notes.md
├── practice.md
└── README.md
```

---

# Programming Patterns Covered

## 1. Counter Pattern

Counts elements that satisfy a condition.

**Examples:**

- Count vowels
- Count words
- Count positive numbers
- Count even numbers

**Complexity:** `O(n)`

---

## 2. Accumulator Pattern

Accumulates a running value while iterating.

**Examples:**

- Sum
- Product
- Average
- Running total

**Complexity:** `O(n)`

---

## 3. Max / Min Pattern

Finds the largest or smallest element.

**Examples:**

- Highest salary
- Lowest temperature
- Longest word

**Complexity:** `O(n)`

---

## 4. Search Pattern

Searches for an element in a collection.

**Examples:**

- Linear search
- First occurrence
- Last occurrence
- Contains check

**Complexity:** `O(n)`

---

## 5. Filter Pattern

Creates a new collection containing only matching elements.

**Examples:**

- Positive numbers
- Even numbers
- Valid records
- Remove duplicates

**Complexity:** `O(n)`

---

## 6. Transform Pattern

Converts each element into another value.

**Examples:**

- Square numbers
- Currency conversion
- Uppercase strings

**Complexity:** `O(n)`

---

## 7. Frequency Map Pattern

Uses dictionaries to count occurrences efficiently.

**Examples:**

- Character frequency
- Word frequency
- Histograms
- Duplicate detection

**Complexity:** `O(n)`

---

## 8. Grouping Pattern

Groups related data together.

**Examples:**

- Students by grade
- Employees by department
- Products by category

**Complexity:** `O(n)`

---

## 9. Two Pointer Pattern

Uses two indices moving through a collection.

**Examples:**

- Palindrome check
- Reverse array
- Pair sum
- Merge sorted arrays

**Complexity:** `O(n)`

---

## 10. Sliding Window Pattern

Processes a fixed-size or variable-size window efficiently.

**Examples:**

- Maximum subarray sum
- Longest substring
- Moving average

**Complexity:** `O(n)`

---

## 11. Prefix Sum Pattern

Precomputes cumulative sums for fast range queries.

**Examples:**

- Range sum
- Cumulative totals
- Query optimization

**Complexity:**

- Build: `O(n)`
- Query: `O(1)`

---

## 12. Hash Map Thinking

Uses dictionaries for fast lookups.

**Examples:**

- Fast lookup
- Duplicate detection
- Caching
- Index mapping

**Complexity:** `O(1)` average lookup

---

## 13. Nested Loop Thinking

Processes multidimensional data or pairwise comparisons.

**Examples:**

- Matrix traversal
- Grid operations
- Pattern printing

**Complexity:** Typically `O(n²)`

---

## 14. State Tracking Pattern

Tracks changes in values while processing data.

**Examples:**

- Status changes
- Previous/current comparisons
- Sensor monitoring

**Complexity:** `O(n)`

---

## 15. Simulation Pattern

Models real-world systems by updating state step by step.

**Examples:**

- ATM
- Banking
- Traffic lights
- Robot movement

---

# Real-World Applications

These programming patterns are widely used in:

- Backend Development
- Web Applications
- Data Engineering
- Machine Learning
- Artificial Intelligence
- Database Systems
- Financial Software
- Inventory Management
- Analytics Dashboards
- Game Development

---

# Skills You Will Gain

After completing this module, you will be able to:

- Solve common coding interview problems
- Recognize reusable problem-solving patterns
- Analyze algorithm efficiency
- Optimize brute-force solutions
- Write cleaner, maintainable Python code
- Build confidence in algorithmic thinking

---

# Complexity Summary

| Pattern | Time Complexity | Space Complexity |
|----------|----------------:|-----------------:|
| Counter | O(n) | O(1) |
| Accumulator | O(n) | O(1) |
| Max / Min | O(n) | O(1) |
| Search | O(n) | O(1) |
| Filter | O(n) | O(n) |
| Transform | O(n) | O(n) |
| Frequency Map | O(n) | O(n) |
| Grouping | O(n) | O(n) |
| Two Pointer | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Prefix Sum | O(n) Build / O(1) Query | O(n) |
| Hash Map | O(1) Average Lookup | O(n) |
| Nested Loop | O(n²) | O(1) |
| State Tracking | O(n) | O(1) |
| Simulation | Depends on Input | Depends on State |

---

# Recommended Learning Order

1. Counter Pattern
2. Accumulator Pattern
3. Max / Min Pattern
4. Search Pattern
5. Filter Pattern
6. Transform Pattern
7. Frequency Map Pattern
8. Grouping Pattern
9. Two Pointer Pattern
10. Sliding Window Pattern
11. Prefix Sum Pattern
12. Hash Map Thinking
13. Nested Loop Thinking
14. State Tracking Pattern
15. Simulation Pattern

---

# Included Resources

This module also includes:

- **`notes.md`** – Detailed explanations of every pattern
- **`practice.md`** – 160+ practice exercises and mini projects
- **`interview_qanda.md`** – Frequently asked interview questions with answers

---

# Prerequisites

Before starting this module, you should be familiar with:

- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Strings
- Collections (Lists, Tuples, Sets, Dictionaries)

---

# Next Step

After mastering these programming patterns, continue with:

- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- Data Structures
- Algorithms
- SQL
- Python for AI and Machine Learning

These patterns provide the foundation for advanced software development and technical interviews.