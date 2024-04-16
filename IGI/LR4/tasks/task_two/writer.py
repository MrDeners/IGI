class Writer:
    @staticmethod
    def write(phones, words, num_consonant_ending_words, average_word_length, words_output, every_seventh_word):
        """
                Write specific information to an output file.

                Args:
                    phones (list): List of phones starting with 29 and 9 digits.
                    words (list): List of words with 2nd consonant and 3rd vowel.
                    num_consonant_ending_words (int): Number of words ending with a consonant.
                    average_word_length (float): Average word length in the text.
                    words_output (list): List of words with average length.
                    every_seventh_word (list): List of every seventh word in the text.
                """
        with open('output.txt', 'w') as file:
            file.write(f'Phones starting with 29 and 9 digits: {phones}\n\n'
                       f'Words with 2nd consonant and 3rd vowel: {words}\n\n'
                       f'Number of words ending with a consonant: {num_consonant_ending_words}\n\n'
                       f'Average word length in text: {average_word_length}\n'
                       f'Words with average length: {words_output}\n\n'
                       f'Every seventh word: {every_seventh_word}')