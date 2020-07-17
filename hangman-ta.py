# My variation of MIT60001 OCW's Problem Set 2: Hangman

# TO DO
# Add warnings if user doesn't enter single letters
# Add input filter for letters only
# Add hints
# Add reply if user inputs same letter more than once

import string
import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    '''Opens and loads in words.txt

    Requires words.txt be in the same directory as hangman-ta.py
        Returns: List of words. Words are strings of lowercase letters.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    '''Generates random word from words.txt
    wordlist (list): list of words (strings)

        Returns a word from wordlist at random
    '''
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''Compares guessed letters to all letters in secret word.

    Requires user input of letters in hangman() function. Input letters create
    list "letters_guessed".
        Returns: boolean, True if all the letters of secret_word are in
    letters_guessed; False otherwise. True is Victory, false otherwise.
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''Secret word's letters are "_" until guessed. Replaced by letter upon
    correct guess.

    Requires user input of letters in hangman() function.
        Returns: Correctly guessed letters replace _'s with letter(s).
    '''
    secret_word_to_print = ''
    for char in secret_word:
        if char not in letters_guessed:
            secret_word_to_print += "_ "
        else:
            secret_word_to_print += char

    return secret_word_to_print

def get_available_letters(letters_guessed):
    '''Pulls letters guessed out of alphabet to show user what letters remain.

    Requires import string and for user input of letters in hangman() function.
        Returns: Remaining available/un-guessed letters from alphabet.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char

    return available_letters

def hangman(secret_word):
    '''Starts up an interactive game of Hangman.

    Input single letter guesses when prompted.
        Returns: Whether guess is correct or not. If num_guesses reaches 0, game
    over. If user guesses secret word before num_guesses = 0, victory.
    '''

    letters_guessed = []
    secret_word_to_print = get_guessed_word(secret_word, letters_guessed)
    num_guesses = 6
    # warnings = 3

    print("Welcome to Hangman!\nThe word you have to guess is", len(secret_word), "characters long.")
    print("-- You have -", num_guesses, "- guesses remaining.")
    print("Please enter one single-letter guess per round.")

    while num_guesses > 0:
        letter_guessed = input("Guess a letter! ... : ")
        # while letter_guessed != str:
        #     warnings -= 1
        #     print(f"Please input a single letter only! You have {warnings} left.")
        #     letter_guessed

        #     if warnings <= 0:
        #         print("GAME OVER - You have no more warnings left.")

        if letter_guessed == 'quit':
            return
        else:
            letters_guessed.insert(0, letter_guessed)

        is_word_guessed(secret_word, letters_guessed)
        get_guessed_word(secret_word, letters_guessed)
        secret_word_to_print = get_guessed_word(secret_word, letters_guessed)

        for char in letter_guessed:
            if char not in secret_word:
                num_guesses -= 1
                get_available_letters(letters_guessed)
                secret_word_to_print
                print(f"\nNot quite! Try again.\n-- You have -", num_guesses, "- guesses remaining. ")
                print(f"-- Available letters: {get_available_letters(letters_guessed)}")
                print(f"* * *\nYour guessed word thus far... {secret_word_to_print}")

            else:
                get_available_letters(letters_guessed)
                secret_word_to_print
                print(f"\nGot one!")
                print(f"* * *\nYour guessed word thus far... {secret_word_to_print}")
                print(f"-- Available letters: {get_available_letters(letters_guessed)}")

        if is_word_guessed(secret_word, letters_guessed):
            print("You win!!!")
            print(f"The secret word was '{secret_word}'.")
            return

        if num_guesses <= 0:
            print("\nGAME OVER\n-- No more guesses left.\nYour progress:", secret_word_to_print)
            print(f"The secret word was '{secret_word}'.")
            return

secret_word = choose_word(wordlist)
hangman(secret_word)