#!/usr/bin/env python3
"""Guess-My-Word is a game where the player has to guess a word.
Project 2
Author: Renato Martins Pereira
Student No.: J196347
Copyright: 2022

"""
# Your code must use PEP8
# Your code must be compatible with Python 3.1x
# You cannot use any libraries outside the python standard library without the explicit permission of your lecturer.

# This code uses terms and symbols adopted from the following source:
# See https://github.com/3b1b/videos/blob/68ca9cfa8cf5a41c965b2015ec8aa5f2aa288f26/_2022/wordle/simulations.py#L104

from play import play


def main(test=False):
    if test:
        import doctest
        return doctest.testmod()
    play()


if __name__ == '__main__':
    print(main(test=False))
