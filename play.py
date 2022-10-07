from get_target_word import get_target_word
from get_valid_words import get_valid_words
from ask_for_guess import ask_for_guess
from score_guess import score_guess
from is_correct import is_correct
from format_score import format_score
from constants import MAX_ATTEMPTS, HELP
from keyboard_guide import keyboard_guide


def play():
    """Code that controls the interactive game play...

    Takes no parameters or arguments;

    Gets word of the day and valid words;

    Takes user guesses until game is won or user runs
    out of attempts (6);

    Makes use of multiple modules + constants as it
    only executes a simple loop in its own code.

    Modules used:
        get_target_word;

        get_valid_words;

        ask_for_guess;

        score_guess;

        is_correct;

        format_score;

        keyboard_guide;

        constants;


    Methods called:
        get_valid_words()

        get_target_word()

        ask_for_guess(valid_words)

        score_guess(guess, word_of_the_day)

        format_score(guess, score)

        is_correct(score)


    """
    # select a word of the day:
    word_of_the_day = get_target_word()

    # build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()

    attempts = 0
    game_won = False
    guesses = list()

    print("Welcome to Guess My Word\n" + "\n"
          + f"Type '{HELP}' at any time to obtain assistance about the game.\n")

    while attempts < MAX_ATTEMPTS:
        guess = ask_for_guess(valid_words)
        # keyboard_guide(guesses, word_of_the_day)
        guesses.append(guess)
        keyboard_guide(guesses, word_of_the_day)
        score = score_guess(guess, word_of_the_day)
        if is_correct(score):
            format_score(guess, score)
            print("Winner Winner, Chicken dinner!!")
            game_won = True
            break
        else:
            format_score(guess, score)
            attempts = attempts + 1
            continue

    if game_won:
        print("Congratulations ! - You have Won the game")
    else:
        print(f"The word of the day was: {word_of_the_day}")
        print("Better luck next time!\n")

    while True:
        print("Would you like to play another game ? [Y/N] ")
        play_another_game = input()

        if play_another_game.lower() == "y":
            play()
        if play_another_game.lower() == "n":
            exit()
        else:
            print("Your choice could not be processed. [Valid answers are 'Y' or 'N']")
