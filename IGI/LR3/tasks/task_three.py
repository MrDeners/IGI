def words_processing(words):
    # This function counts words that start with a consonant
    """
    This function counts words that start with a consonant.

    Parameters:
    - words (List[str]): A list of words to be processed.

    Returns:
    - int: The number of words that start with a consonant.
    """
    counter = 0
    for word in words:
        if word[0] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                       'y', 'z']:
            counter += 1
    return counter


def third_task():
    # This function takes user input, splits it into words, and prints the amount of words starting with a consonant
    """
    This function takes user input, splits it into words, and prints the amount of words starting with a consonant.

    Returns:
    - None
    """
    text = input("Input analyzing text: ")
    words = text.split()
    print(f"Amount of words: {words_processing(words)}")
