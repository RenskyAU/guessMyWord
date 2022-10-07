from constants import CORRECT_SCORE


def is_correct(score):
    """Checks if the score is entirely correct and returns True if it is

     Examples:
    >>> is_correct((1,1,1,1,1))
    False
    >>> is_correct((2,2,2,2,1))
    False
    >>> is_correct((0,0,0,0,0))
    False
    >>> is_correct((2,2,2,2,2))
    True"""

    return score == CORRECT_SCORE
