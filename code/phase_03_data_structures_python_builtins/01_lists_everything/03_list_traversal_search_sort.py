"""
Topic:
List Traversal, Searching and Sorting

Covered:
- for loop
- enumerate()
- while loop
- in operator
- index()
- count()
- sort()
- sorted()
- reverse()
"""

def main():

    numbers = [50,20,40,10,30]


    # --------------------------------
    # Traversal using for loop
    # --------------------------------

    print("For Loop Traversal:")

    for number in numbers:
        print(number)



    # --------------------------------
    # enumerate()
    # Gives index and value
    # --------------------------------

    print("\nUsing enumerate:")

    for index,value in enumerate(numbers):

        print(index,value)



    # --------------------------------
    # Searching
    # --------------------------------

    print("\nSearching:")


    if 40 in numbers:
        print("40 exists")



    # index()

    position = numbers.index(20)

    print("20 position:",position)



    # count()

    count = numbers.count(10)

    print("10 count:",count)



    # --------------------------------
    # Sorting
    # --------------------------------

    print("\nBefore sorting:")
    print(numbers)


    numbers.sort()

    print("Ascending:")
    print(numbers)



    numbers.sort(reverse=True)

    print("Descending:")
    print(numbers)



    # sorted creates new list

    values = [5,2,8,1]

    new_values = sorted(values)

    print("\nOriginal:",values)
    print("Sorted copy:",new_values)



    # Reverse

    values.reverse()

    print("Reverse:",values)



if __name__ == "__main__":
    main()