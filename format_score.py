from constants import MISS, MISS_OUTPUT, MISPLACED, MISPLACED_OUTPUT, EXACT


def format_score(guess, score):
    """Formats a guess with a given score as output to the terminal.

     Gets user's guess;
    display the score (matching score, with chosen output and position on array of target word).

    MISS => 0 => _

    MISPLACED => 1 => ?

    EXACT => 2 => 're-print letter'

    Prints to screen:
     GUESS

     SCORE(output)

    The following is an example output

    >>> format_score('hello', (0,0,0,0,0))
    H E L L O
    _ _ _ _ _
    >>> format_score('hello', (0,0,0,1,1))
    H E L L O
    _ _ _ ? ?
    >>> format_score('hello', (1,0,0,2,1))
    H E L L O
    ? _ _ L ?
    >>> format_score('hello', (2,2,2,2,2))
    H E L L O
    H E L L O

    Modules used:
        constants:


    :param score: tuple cointaining score of user's guess
    :param guess: input(str)
    :type score: tuple
    :type guess: str

    """
    output_guess = ""
    score_tuple = score

    score = ""
    x = 0
    while x < (len(score_tuple) - 1):
        if score_tuple[x] == MISS:
            score = score + MISS_OUTPUT
            score = score + " "
        if score_tuple[x] == MISPLACED:
            score = score + MISPLACED_OUTPUT
            score = score + " "
        if score_tuple[x] == EXACT:
            score = score + (guess[x].upper())
            score = score + " "
        x = x + 1
    if score_tuple[x] == MISS:
        score = score + "_"
    if score_tuple[x] == MISPLACED:
        score = score + "?"
    if score_tuple[x] == EXACT:
        score = score + (guess[x].upper())

    x = 0
    while x < (len(score_tuple) - 1):
        output_guess = output_guess + guess[x].upper()
        output_guess = output_guess + " "
        x = x + 1
    output_guess = output_guess + guess[x].upper()

    print(output_guess)
    print(score)

