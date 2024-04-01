from tasks.task_one import first_task as first
from tasks.task_two import second_task as second
from tasks.task_three import third_task as third
from tasks.task_four import fourth_task as fourth
from tasks.task_five import fifth_task as fifth


def working(task):
    # This function processes user decisions about tasks
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
    while True:
        print("\n|------------------------------------------------------|")
        print("Tasks:")
        print("1: Function Calculating via Power Series")
        print("2: Sum of Sequence")
        print("3: Text Analyzer")
        print("4: Advanced Text Analyzer")
        print("5: Lists Processing")
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
