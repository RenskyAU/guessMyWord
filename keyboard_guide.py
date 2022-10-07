from constants import KEYBOARD_LINE1, KEYBOARD_LINE2, KEYBOARD_LINE3, MISS, MISPLACED, EXACT, RED, GREEN, YELLOW, ENDC


def keyboard_guide(guesses, target_word):
    """Prints out a keyboard guide to provide visual
    guidance to user

    Checks if the letters entered by the player have
    already been typed and if not in the target word,
    it is not printed to assist player

    :type target_word: object
    :param target_word: word of the day
    :param guesses:
    list of guesses entered during a
    set of games (uninterrupted play() session)

    :type guesses: list



    """

    all_guessed_letters = list()
    for guess in guesses:
        guess = guess
        for letter in guess:
            all_guessed_letters.append(letter)

    for letter in KEYBOARD_LINE1:
        if (letter in all_guessed_letters) and (letter not in target_word):
            print(f'{RED}{letter.upper()}{ENDC}' + ' ', end='')
            continue
        else:
            print(letter.upper() + ' ', end='')
            continue
    print('  ')
    for letter in KEYBOARD_LINE2:
        if (letter in all_guessed_letters) and (letter not in target_word):
            print(f'{RED}{letter.upper()}{ENDC}' + ' ', end='')
            continue
        else:
            print(letter.upper() + ' ', end='')
            continue
    print('  ')
    for letter in KEYBOARD_LINE3:
        if (letter in all_guessed_letters) and (letter not in target_word):
            print(f'{RED}{letter.upper()}{ENDC}' + ' ', end='')
            continue
        else:
            print(letter.upper() + ' ', end='')
            continue
    print('  ')

    print('\n\n')
