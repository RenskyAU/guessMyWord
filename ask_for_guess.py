from constants import WORD_LENGTH, HELP
from help import game_help


def ask_for_guess(valid_words):
    """Requests a guess from the user directly from stdout/in

    User input (guess) is converted to lower case (matching source file);

    <Loop until valid guess is entered:>

    Uses help module (if input == HELP constant);

    If guess is a valid word (in valid_words (lst) ) => returns guess (str)

    :type valid_words : list
    :param valid_words: list containing all words

    Modules used:
        help;

        constants;

    Returns: Guess
        str: the guess chosen by the user in lowercase.



    """
    while True:
        print("Please type in your 5 letter word")
        user_guess = input().lower()
        if user_guess == HELP:
            game_help()
        else:
            if len(user_guess) == WORD_LENGTH:
                if user_guess in valid_words:
                    guess = user_guess
                    break
                else:
                    print("Invalid word!")
                    continue
            else:
                print("Your word does not have 5 letters")
                continue

    return guess
