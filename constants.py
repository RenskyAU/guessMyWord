"""
Constants used throughout the program
"""

GAME_NAME = "Guess My Word"

MISS = 0  # _-.: letter not found ⬜
MISS_OUTPUT = "_"
MISPLACED = 1  # O, ?: letter in wrong place 🟨
MISPLACED_OUTPUT = "?"
EXACT = 2  # X, +: right letter, right place 🟩

CORRECT_SCORE = (2, 2, 2, 2, 2)

# TARGET_WORDS = 'c:/Users/renat/Desktop/Wordle/target_words.txt'
TARGET_WORDS = 'target_words.txt'

# ALL_WORDS = 'c:/Users/renat/Desktop/Wordle/all_words.txt'
ALL_WORDS = 'all_words.txt'

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

# Used to be the keyword used to call help function within the game
HELP = "help!"

# Keyboard lines. Used for the special feature
KEYBOARD_LINE1 = ['q', 'w', 'e', 'r', 't', 'y', 'u','i', 'o', 'p']
KEYBOARD_LINE2 = ['a', 's', 'd', 'f', 'g', 'h', 'j' ,'k', 'l']
KEYBOARD_LINE3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

# colours
RED = '\033[91m'
YELLOW = '\033[90m'
GREEN = '\033[102m'
ENDC = '\033[0m' # returns to normal color
