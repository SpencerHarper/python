#!/usr/bin/env python
# ocw13-hangman.py

# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "ocw14-words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []
list1 = []

def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    if set(secret_word) < set(letters_guessed):
	return True
    else:
	return False

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    list = []
    guessed = []
    for i in secret_word:
	list.append(i)
    for i in secret_word:
	if i in letters_guessed:
		guessed.append(i)
   	else:
		guessed.append('-')
    return join(guessed, '')

#    pass # This tells your code to skip this function; delete it when you

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    mistakes_made = 0
    incorrect_letters = []

    secret_word = get_word()
    
    while mistakes_made < 6:
	print '\n'*50
	print print_hangman_image(mistakes_made)
	print 'guesses left:', 6 - mistakes_made
	print 'letters guessed:', join(letters_guessed, '')
	print 'incorrect letters:', join(incorrect_letters, '')
	print print_guessed()
	input = raw_input('Enter letter: ')
	print '------------------------'
	lower(input)
	if input in secret_word:
		letters_guessed.append(input)
		if set(secret_word) < set(letters_guessed):
			print '\n'*50
		        print_hangman_image(mistakes_made)
			print '------------------------'
                        return secret_word
	else:
		incorrect_letters.append(input)
		mistakes_made = mistakes_made + 1
		while mistakes_made == 6:
                        print '\n'*50
			print_hangman_image(mistakes_made)
			print '------------------------'
			return secret_word

    print '\n'*50
    print_hangman_image(mistakes_made)
    print '------------------------'
    return secret_word

print play_hangman()
print '------------------------'
