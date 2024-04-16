import re


class TextProcessor:
    @staticmethod
    def find_phone(text):
        """
        Find phone numbers in the given text.

        Args:
            text (str): The input text.

        Returns:
            list: List of phone numbers found in the text.
        """
        return re.findall(r'\b29\d{7}\b', text)

    @staticmethod
    def words_with_letter(text):
        """
        Find words with a specific letter pattern in the given text.

        Args:
            text (str): The input text.

        Returns:
            list: List of words matching the specified letter pattern.
        """
        return re.findall(r'\b\w(?=[^aeiouy])([aeiouy])(?=\w)\w+\b', text, flags=re.IGNORECASE)

    @staticmethod
    def words_consonant_ending(text):
        """
        Count the number of words ending with a consonant in the given text.

        Args:
            text (str): The input text.

        Returns:
            int: Number of words ending with a consonant.
        """
        consonant_ending_words = re.findall(r'\b\w+[^aeiouy\W]\b', text, flags=re.IGNORECASE)
        return len(consonant_ending_words)

    @staticmethod
    def words_length_median(text):
        """
        Calculate the median length of words in the given text.

        Args:
            text (str): The input text.

        Returns:
            int: The median length of words.
        """
        word_lengths = [len(word) for word in re.findall(r'\b\w+\b', text)]
        return round(sum(word_lengths) / len(word_lengths))

    @staticmethod
    def filter_length(text):
        """
        Filter words with the same length as the median length of words in the given text.

        Args:
            text (str): The input text.

        Returns:
            str: List of words with the same length as the median length, or a message indicating no such words were found.
        """
        average_word_length = TextProcessor.words_length_median(text);
        words_with_avg_length = [word for word in re.findall(r'\b\w+\b', text) if len(word) == average_word_length]
        if words_with_avg_length:
            return ', '.join(words_with_avg_length)
        else:
            return f'There are no {average_word_length}-symbols words'

    @staticmethod
    def every_seventh(text):
        """
        Extract every seventh word from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: Every seventh word from the text.
        """
        return ' '.join(re.findall(r'\b\w+\b', text)[6::7])
