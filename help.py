from constants import GAME_NAME, WORD_LENGTH, MAX_ATTEMPTS, MISS, MISS_OUTPUT, MISPLACED, MISPLACED_OUTPUT


def game_help():
    """Provides help for the game

    Called by user input ('help!').

    Not case-sensitive.(input is converted previously to lower)



    """

    print(f"Welcome to {GAME_NAME}\n" + '\n'
          + f"{GAME_NAME} is a word guessing game.\n"
          + f"A {WORD_LENGTH} letter word is randomly chosen from a repository.\n" + "\n"
          + "< < GAMEPLAY > >\n" + "\n"
          + f"The user is given {MAX_ATTEMPTS} attempts to guess the right word.\n" + "\n"
          + "When scoring the guess, the game goes as follow:\n"
          + "\tLetter in guess is on the same position as in the chosen word: Shows the letter;\n"
          + f"\t> Letter in guess is in different position as in the chosen word: Shows {MISPLACED_OUTPUT}\n"
          + f"\t> Letter in guess is nor present in the chosen word: Shows {MISS_OUTPUT}\n" + "\n"
          + f"The player is given {MAX_ATTEMPTS} attempts on guessing the word.\n"
          + f"The guesses will only be considered as a valid attempt if:\n"
          + f"\t> The guess word has {WORD_LENGTH} letters;\n"
          + "\t> The guess word is a valid word (part of a word repository);\n" + "\n"
          + "A guess letter will only be scored the number of times it appears on the target word.\n" + "\n")


