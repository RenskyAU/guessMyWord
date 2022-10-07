import random
from constants import TARGET_WORDS


def get_target_word(file_path=TARGET_WORDS, seed=None):
    """Picks a random word from a file of words...
    Store words from file in a list;
    Generates a random number within the range of the list;
    Picks word located at index/position that matches generated number.

    Args:
        file_path (str): the path to the file containing the words

    Returns:
        str: a random word from the file

    Modules used:
        random;

        constants;

    How do you test that a random word chooser is choosing the correct words??
    Discuss in class!
    # >>> get_target_word()
    # 'aback'
    # >>> get_target_word()
    # 'zonal'


    :type file_path: str
    :type seed: int
    :param file_path: location for 'all words' source file
    :param seed: (int)

    """
    # read words from a file and return a random word (word of the day)
    file = open(TARGET_WORDS)
    all_words = file.readlines()
    file.close()
    target_words = list()
    for word in all_words:
        word = word.strip()
        target_words.append(word)

    target_word = target_words[random.randrange(0, len(target_words) + 1)]

    # word_count = len(target_words)
    return target_word
