def number_generator(n):
    # This generator function yields numbers from 0 to n-1
    """
    This generator function yields numbers from 0 to n-1.

    Parameters:
    - n (int): The upper limit for the range of numbers to yield.

    Yields:
    - int: Numbers from 0 to n-1.
    """
    for num in range(n):
        yield num


def second_task():
    # Function for counting the sum of numbers not exceeding 100
    """
    This function counts the sum of numbers not exceeding 100.

    Returns:
    - None
    """
    x = 0
    counter = 0
    numbers = list(number_generator(100))
    # while x < 100:
    #     x += float(input(f"Sum = {x} Input next element: "))
    #     counter += 1
    for i in numbers:
        x += i
        counter += 1
        if x >= 100:
            break
    print(f"Result: {x}  Amount of Elements: {counter}")


