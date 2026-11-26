"""
Topic:
List Operations and Methods

Covered:
- append()
- insert()
- extend()
- remove()
- pop()
- clear()
- update elements
"""

def main():

    numbers = [10,20,30]

    print("Original:", numbers)


    # --------------------------------
    # append()
    # Adds element at the end
    # --------------------------------

    numbers.append(40)

    print("\nAfter append:")
    print(numbers)



    # --------------------------------
    # insert()
    # Adds element at specific index
    # --------------------------------

    numbers.insert(1,15)

    print("\nAfter insert:")
    print(numbers)



    # --------------------------------
    # extend()
    # Adds multiple values
    # --------------------------------

    numbers.extend([50,60])

    print("\nAfter extend:")
    print(numbers)



    # --------------------------------
    # remove()
    # Removes first matching value
    # --------------------------------

    numbers.remove(20)

    print("\nAfter remove:")
    print(numbers)



    # --------------------------------
    # pop()
    # Removes by index
    # --------------------------------

    removed = numbers.pop()

    print("\nRemoved value:", removed)
    print(numbers)



    # --------------------------------
    # Update value
    # --------------------------------

    numbers[0] = 100

    print("\nAfter update:")
    print(numbers)



    # --------------------------------
    # clear()
    # Removes everything
    # --------------------------------

    temp = [1,2,3]

    temp.clear()

    print("\nAfter clear:")
    print(temp)



if __name__ == "__main__":
    main()