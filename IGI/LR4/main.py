# Author - Malush Denis BSUIR IaPT 253501
# Created - 01.04.2024
# Laboratory Work - #3
# Python Studying   Version - 1.0.0 (Release)
# The Best program for Python Studying


from tasks.task_one.task_one import first_task as first
from tasks.task_two.task_two import second_task as second
from tasks.task_three.task_three import third_task as third
from tasks.task_four.task_four import fourth_task as fourth
from tasks.task_five.task_five import fifth_task as fifth


def working(task):
    # This function processes user decisions about tasks
    """
    This function processes user decisions about tasks by calling the corresponding task function.

    Parameters:
    - task (int): The task number the user has selected.

    Returns:
    - None
    """
    if task == 1:
        first()
    elif task == 2:
        second()
    elif task == 3:
        third()
    elif task == 4:
        fourth()
    elif task == 5:
        fifth()


def main_menu():
    # This function display user interface
    """
    This function displays the user interface for selecting tasks and handles user input.

    Returns:
    - None
    """
    while True:
        print("\n|------------------------------------------------------|")
        print("Tasks:")
        print("1: First Task")
        print("2: Second Task")
        print("3: Third Task")
        print("4: Fourth Task")
        print("5: Fifth Task")
        print("6: Close program")
        print("\n")
        operation = int(input("Your choice: "))

        if operation < 1 or operation > 6:
            print("Please choose an existing operation (1, 2, 3, 4, 5 or 6).")
            continue

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        if operation == 6:
            print("\n")
            return
        working(operation)
        main_menu()


if __name__ == "__main__":
    main_menu()
