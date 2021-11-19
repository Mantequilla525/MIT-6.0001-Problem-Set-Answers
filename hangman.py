# Problem Set 2, hangman.py
# Name: Brandon Davis
# Collaborators: None
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from os import replace, truncate
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    letters = list(secret_word)

    guessed = True

    for letter in letters:
      if letter not in letters_guessed:
        guessed = False
        break

    if guessed == True:
      print('Word is in guessed letters')
      return True
    else:
      return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    letters = list(secret_word)

    printOut = ''

    for letter in letters:
      if letter in letters_guessed:
        printOut += letter
      else:
        printOut += '_ '
    
    return printOut



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    allLetters = string.ascii_lowercase
    availableLetters = ''
    
    for letter in allLetters:
      if letter not in letters_guessed:
        availableLetters += letter
    
    return availableLetters



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    secretWord = secret_word
    secretWordLetters = list(secretWord)
    lettersGuessed = list()

    guesses = 6
    warnings = 3

    vowels = ['a', 'e', 'i', 'o', 'u']

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while True:
      print('-------------------')
      print('You have ' + str(guesses) + ' guesses left.')
      print('Available letters:', get_available_letters(lettersGuessed))
      guess = input('Please guess a letter: ')

      if len(guess) != 1 or guess.isalpha() == False or guess in lettersGuessed:
        print('Invalid input. Please enter one alphabetic letter that has not already been guessed.')
        if warnings > 0:
          warnings -= 1
          print('Warnings remaining:', str(warnings))
        else:
          guesses -= 1
        
        continue

      lettersGuessed.append(guess)

      if guess in secretWordLetters:
        print('Good guess:', get_guessed_word(secretWord, lettersGuessed))
      else:
        print('Oops! That letter is not in my word:', get_guessed_word(secretWord, lettersGuessed))

        if guess in vowels:
          guesses -= 2
        else:
          guesses -= 1
      
      if is_word_guessed(secretWord, lettersGuessed):
        totalScore = guesses * len(secretWord)
        print('-------------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:', totalScore)
        break

      if guesses < 1:
        print('-----------------')
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')
        break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    myWord = my_word.replace(' ', '')
    otherWord = other_word.replace(' ', '')
    
    matching = True

    if len(myWord) == len(otherWord):
      myWordLetters = list(myWord)
      otherWordLetters = list(otherWord)

      letterIndex = -1
      for letter in myWord:
        letterIndex += 1
        if letter == '_':
          continue
        else:
          if letter != otherWordLetters[letterIndex]:
            matching = False
            break
    else:
      matching = False
    
    return matching



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    printStr = ''

    for word in wordlist:
      if match_with_gaps(my_word, word):
        printStr += word + ' '
      else:
        continue
    
    if printStr != '':
      print(printStr)
    else:
      print('No matches found')

show_possible_matches('a_ pl_ ')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    secretWord = secret_word
    secretWordLetters = list(secretWord)
    lettersGuessed = list()

    guesses = 6
    warnings = 3

    vowels = ['a', 'e', 'i', 'o', 'u']

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while True:
      print('-------------------')
      print('You have ' + str(guesses) + ' guesses left.')
      print('Available letters:', get_available_letters(lettersGuessed))
      guess = input('Please guess a letter: ')

      if guess == '*':
        show_possible_matches(get_guessed_word(secretWord, lettersGuessed))
        continue

      if len(guess) != 1 or guess.isalpha() == False or guess in lettersGuessed:
        print('Invalid input. Please enter one alphabetic letter that has not already been guessed.')
        if warnings > 0:
          warnings -= 1
          print('Warnings remaining:', str(warnings))
        else:
          guesses -= 1
        
        continue

      lettersGuessed.append(guess)

      if guess in secretWordLetters:
        print('Good guess:', get_guessed_word(secretWord, lettersGuessed))
      else:
        print('Oops! That letter is not in my word:', get_guessed_word(secretWord, lettersGuessed))

        if guess in vowels:
          guesses -= 2
        else:
          guesses -= 1
      
      if is_word_guessed(secretWord, lettersGuessed):
        totalScore = guesses * len(secretWord)
        print('-------------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:', totalScore)
        break

      if guesses < 1:
        print('-----------------')
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
