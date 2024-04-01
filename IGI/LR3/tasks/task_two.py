def second_task():
    # Function for counting the sum of numbers not exceeding 100
    x = 0
    counter = 0
    while x < 100:
        x += float(input(f"Sum = {x} Input next element: "))
        counter += 1
    print(f"Result: {x}  Amount of Elements: {counter}")
