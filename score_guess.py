from constants import MISS, MISPLACED, EXACT


def score_guess(guess, target_word):
    """Given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (MISS, MISPLACED, or EXACT)

    > letter count of both guess and target_word (dict);

    > *each letter in guess (also present in target word) is checked if index position in array is the same;

    > If matched: scores 2 (EXACT)

    > if not matched...:
       if letter count at guess > target_word: Scores 0 (MISS)

       else: Scores 1 (MISPLACED)
    > each time a letter in guess scores 1 or 2, the letter count on both guess and targe_word are deducted.

    > score is stored one by in a list.

    > *list is reversed and converted to a tuple

    * letters are checked back to front to ensure that when a letter count is higher
      in guess than in target, the last letter will be the one scored as MISS.

    * list is reversed to match the word.

    Returns:
        score : tuple of integers

    Modules used:
        constants;



    Programers note:

    The golden rule is that only valid letters score. Given each letter count of (guess, target word),
    a letter is only valid if it can be matched in both words (1 to 1). Therefore, if a letter count is
    higher on the guess, the letter is either an Exact match or a Miss(as only the matching/valid letters score).
    The count of letters is deducted at each scoring (pairing) of letters. Count of letters in the taget
    word is only decreased when letter is paired (letter in guess is Misplaced or Exact match).

    Here are some example (will run as doctest):

    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)

    Try and pass the first few tests in the doctest before passing these tests.
    >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    >>> score_guess('train', 'tenor')
    (2, 1, 0, 0, 1)
    >>> score_guess('moody', 'rhino')
    (0, 1, 0, 0, 0)
    >>> score_guess('duded', 'caddy')
    (1, 0, 2, 0, 0)


    :type guess: str
    :param guess: input(guess)
    :type target_word: str
    :param target_word: target_words[random]

        """
    # You must use this convention as test automation will be validating your scorer
    count_guess = dict()
    count_target = dict()
    guess_score = list()

    # Letter count of 'guess' and 'target_word' stored in dictionaries
    for letter in guess:
        count_guess[letter] = count_guess.get(letter, 0) + 1
    for letter in target_word:
        count_target[letter] = count_target.get(letter, 0) + 1

    index = len(guess) - 1
    while index >= 0:
        if guess[index] in target_word:
            while count_guess[guess[index]] >= 0:
                if guess[index] == target_word[index]:  # Score 2 (right place)
                    count_guess[guess[index]] = count_guess[guess[index]] - 1
                    count_target[guess[index]] = count_target[guess[index]] - 1
                    guess_score.insert(0, EXACT)
                    break
                else:
                    if count_guess[guess[index]] > count_target[guess[index]]:
                        # Score 0 (miss)
                        count_guess[guess[index]] = count_guess[guess[index]] - 1
                        guess_score.insert(0, MISS)
                        break
                    # Scores 1 (misplaced)
                    count_guess[guess[index]] = count_guess[guess[index]] - 1
                    count_target[guess[index]] = count_target[guess[index]] - 1
                    guess_score.insert(0, MISPLACED)
                    break

        else:
            # Score 0 (miss)
            guess_score.insert(0, MISS)

        index = index - 1

    score = tuple(guess_score)

    return score
