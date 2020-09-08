# My variation of MIT60001 OCW's Problem Set 2: Hangman

import string
import random
import sys

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
    letters_guessed; False otherwise. True is "Beating the game".
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

    Input: Requires import string and for user input of letters in hangman() function.
        Returns: Remaining available/un-guessed letters from alphabet.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char

    return available_letters

def hangman(secret_word):
    '''Starts up an interactive game of Hangman.

    Input: single letter guesses when prompted.
        Returns: Whether guess is correct or not. If num_guesses reaches 0, game
        over. If user guesses secret word before num_guesses = 0, victory.
    '''

    # initializers
    letters_guessed = []
    duplicate_letters = []
    secret_word_to_print = get_guessed_word(secret_word, letters_guessed)
    num_guesses = 6
    strikes = 0

    # title screen
    print(f"\nWelcome to Hangman!\n* * * * * * * * * *\n\nThe word you have to guess is {len(secret_word)} characters long.")
    print(f"-- You have - {num_guesses} - guesses remaining.")
    print("Please enter one single-letter guess per round.")
    print("\n------------------------------------")

    # loop to begin guessing letters
    while num_guesses > 0:
        letter_guessed = input("Guess a letter! ... : ")
        letter_guessed = letter_guessed.casefold() # forces guesses to be lower case

        if letter_guessed == 'quit':
            sys.exit()
        elif len(letter_guessed) != 1:
            print("Reminder: Please enter one single-letter guess per round.")
            continue
        elif letter_guessed in letters_guessed:
            duplicate_letters.insert(0, letter_guessed)
        else:
            letters_guessed.insert(0, letter_guessed)

        is_word_guessed(secret_word, letters_guessed) # Compares guessed letters to all letters in secret word.
        get_guessed_word(secret_word, letters_guessed) # Secret word's letters are "_" until guessed.
        secret_word_to_print = get_guessed_word(secret_word, letters_guessed)

        for char in letter_guessed:
            if char in duplicate_letters:
                strikes += 1
                if strikes < 3:
                    print(f"\nYou already tried that character! You have {strikes} strike(s).")
                    print(f"-- You still have - {num_guesses} - guesses remaining. ")

            elif not letter_guessed.isalpha():
                strikes += 1
                if strikes < 3:
                    print(f"\nPlease input single letters only! You have {strikes} strike(s).")
                    print(f"-- You still have - {num_guesses} - guesses remaining. ")

            elif char not in secret_word:
                if char not in duplicate_letters:
                    num_guesses -= 1
                    get_available_letters(letters_guessed)
                    secret_word_to_print
                    print(f"\nNot quite! Try again.\n-- You have - {num_guesses} - guesses remaining. ")
                    print(f"-- Available letters: {get_available_letters(letters_guessed)}")
                    print(f"\nYour guessed word thus far... {secret_word_to_print}")
                    print("\n------------------------------------")

            else:
                get_available_letters(letters_guessed)
                secret_word_to_print
                print("\nGot one!")
                print(f"* * * * *\nYour guessed word thus far... {secret_word_to_print}")
                print(f"-- You still have - {num_guesses} - guesses remaining. ")
                print(f"-- Available letters: {get_available_letters(letters_guessed)}")
                print("\n------------------------------------")

        if strikes >= 3:
            num_guesses -= 1
            print("3 strikes! You lose a guess...")
            print(f"-- You now have - {num_guesses} - guesses remaining. ")
            strikes = 0

        if is_word_guessed(secret_word, letters_guessed):
            print("\n\n\n* * YOU WIN * *")
            print(f"\nThe secret word was '{secret_word}'.")
            print(f"\nScore: {num_guesses * len(set(secret_word))}")
            try_again = input("\nWould you like to play again? Type 'yes' or 'no' ... : ").lower()
            if try_again in ['y', 'ye', 'yes']:
                print("--Good luck!\n")
                print("\n------------------------------------\n")
                secret_word = choose_word(wordlist)
                hangman(secret_word)
            elif try_again in ['n', 'no']:
                print("--Until next time!")
                sys.exit()
            else:
                print("--Until next time!")
                sys.exit()

        if num_guesses <= 0:
            print("\n\n\nGAME OVER\n-- No more guesses left.")
            print(f"\nThe secret word was '{secret_word}'.")
            print(f"\nYour progress: {secret_word_to_print}")

            try_again = input("\nWould you like to play again? Type 'yes' or 'no' ... : ").lower()
            if try_again in ['y', 'ye', 'yes']:
                print("--Good luck!\n")
                print("\n------------------------------------\n")
                secret_word = choose_word(wordlist)
                hangman(secret_word)
            elif try_again in ['n', 'no']:
                print("--Until next time!")
                sys.exit()
            else:
                print("--Until next time!")
                sys.exit()

secret_word = choose_word(wordlist)
hangman(secret_word)
