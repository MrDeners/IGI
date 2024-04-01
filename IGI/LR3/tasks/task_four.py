def get_max_length(words):
    # This function finds the maximum length of a word in the input list of words
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


def get_amount_longest_word(words):
    # This function calculates the amount of words with the maximum length in the input list of words
    max_length = get_max_length(words)
    counter = 0
    for word in words:
        if len(word) == max_length:
            counter += 1
    return counter


def get_words_before_sign(words):
    # This function returns a list of words that end with a comma or period from the input list of words
    counter = 0
    words_before_sign = []
    for word in words:
        if word[-1] in [',', '.']:
            words_before_sign.append(word)
    return words_before_sign


def get_longest_word_final_e(words):
    # This function finds the longest word in the input list of words that ends with 'e'
    searching_word = ""
    for word in words:
        if word[-1] == 'e':
            if len(word) > len(searching_word):
                searching_word = word
        elif word[-1] in [',', '.', '?', '!']:
            if word[-2] == 'e':
                if len(word) > len(searching_word):
                    searching_word = word

    if searching_word == "":
        return "Not Found"

    return searching_word


def fourth_task():
    # This function processes the input text and prints the results of the other functions
    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy "
            "and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and "
            "picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")
    words = text.split()

    print("Amount of Longest Words: ", get_amount_longest_word(words))

    print("Words before Sign: ", get_words_before_sign(words))

    print("Longest word ending 'e': ", get_longest_word_final_e(words))