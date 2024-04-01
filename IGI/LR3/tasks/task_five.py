def input_list():
    # This function using for get users number list
    number_list = []
    amount = 1
    while True:
        try:
            string = input(f"Input {amount} element. Input 's' if ypu want to stop: ")
            if string == "s":
                break
            number_list.append(float(string))
            amount += 1
        except ValueError:
            print("ERROR: Not a number entered")
    return number_list


def fifth_task():
    # This function realize tasks exercises
    number_list = input_list()
    print("Amount of '0' elements", number_list.count(0))
    print("Sum of elements after min: ", sum(number_list[number_list.index(min(number_list)):]))
    print("List: ", number_list)
