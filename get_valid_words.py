from constants import ALL_WORDS


def get_valid_words(file_path=ALL_WORDS):
    """returns a list containing all valid words.

    opens file on path (argument);

    read lines and store words in a list.

    Args:
        file_path (str): the path to the file containing the target words

    Returns:
        valid_words (lst)


    :param file_path: location for 'target words' source file
    :type file_path: str


    Modules used:
        constants.


    Note to test that the file is read correctly, use:

    >>> get_valid_words()[0]
    'aahed'
    >>> get_valid_words()[-1]
    'zymic'
    >>> get_valid_words()[10:15]
    ['abamp', 'aband', 'abase', 'abash', 'abask']

    """
    # read words from files and return a list containing all words that can be entered as guesses
    file = open(ALL_WORDS)
    all_words = file.readlines()
    file.close()
    valid_words = list()
    for word in all_words:
        word = word.strip()
        valid_words.append(word)

    return valid_words
