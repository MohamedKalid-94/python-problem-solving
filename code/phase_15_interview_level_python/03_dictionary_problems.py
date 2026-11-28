"""
Phase 15 - Interview-Level Python
03 Dictionary Problems
"""


def frequency_count(text):
    result = {}
    for ch in text:
        result[ch] = result.get(ch, 0) + 1
    return result


def word_count(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


def merge_dicts(a, b):
    # If both have the same key, the value from b wins
    return {**a, **b}


def find_duplicates(values):
    result = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    # Keep only the items that appear more than once
    return {k: v for k, v in result.items() if v > 1}


def main():
    print("Frequency:", frequency_count("python"))
    print("Words:", word_count(["ai", "python", "ai"]))
    print("Merge:", merge_dicts({"a": 1}, {"b": 2}))
    print("Duplicates:", find_duplicates([1, 2, 2, 3, 3, 3]))


if __name__ == "__main__":
    main()