from .reader import *
from .writer import *
from .zipper import *
from .text_processor import *


def second_task():
    """
        Perform a series of operations on text data and write the results to a file.

        This function reads text data from a file, performs several text processing operations using the `TextProcessor` class,
        and writes the results to an output file using the `Writer` class. It also zips the output file using the `Zipper` class.

        Returns:
            None
        """
    text = AdvancedReader.read("input")

    phones = TextProcessor.find_phone(text)

    words = TextProcessor.words_with_letter(text)

    num_consonant_ending_words = TextProcessor.words_consonant_ending(text)

    average_word_length = TextProcessor.words_length_median(text)

    words_output = TextProcessor.filter_length(text)

    every_seventh_word = TextProcessor.every_seventh(text)

    Writer.write(phones, words, num_consonant_ending_words, average_word_length, words_output, every_seventh_word)

    Zipper.zip("output", "results")
