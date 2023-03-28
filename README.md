# HangmanPython

Guidelines:

Program recieves from player:
    path to the words file  - str
    int representing a particular word in the file

The word in the specific index the player choose will be the words to guess

functions:
check_win(secret_word, old_letters_guessed)
type: boolean function
Returns:
    true:  all the letters in the secret word are  in the list of letters guessed.\

show_hidden_word(secret_word, old_letters_guessed)
Returns:
     string that shows the letters from the old_letters_guessed list that are in the secret_word string
     in their appropriate position, and the other letters in the string (which the player has not yet guessed) as underlines.

check_valid_input(letter_guessed, old_letters_guessed)
Checks:
 1. correctness of the input
 2. whether it is legal to guess this letter (that is, the player has not guessed this letter before)
Returns:
     true or false accordingly.

try_update_letter_guessed(letter_guessed, old_letters_guessed)
Function uses the check_valid_input function to know if the character is correct and has not been guessed before
or the character is not correct and/or is already in the list of guesses.
Return + print:
If the character is incorrect or the character has already been guessed before: X + below it the list of letters that have already been guessed and returns false.
If the character is correct and it was not guessed before: the function adds the character to the list of guesses and returns true.


TO-DO:

-> change this fun to return only the word
choose_word(file_path, index)
Returns:
    the secret word in the received index - str]


-> group the printout of the opening page

variables:

secret_word - str:  the word that the user needs to guess, passed as an argument to the hangman function.

old_letters_guessed - str :  letters the player has guessed so far.

MAX_TRIES - int;  maximum number of failed attempts allowed in the game, which is 6.

num_of_tries - int: number of failed attempts by the user so far.

HANGMAN_PHOTOS - dict: the pictures of the hanging man in each of the positions.

THE GAME:

1. print the opening screen:
    HANGMAN TEXT
    num of tries: MAX_NUM_TRIES

2. input file path and index of word
    Enter file path:
    Enter index:
    Print Let's start!
    Select secret word

Till player wins or loses (while num_of_tries<=MAX_TRIES)
3. check if player won
    print the curr hanging line
   print the chars with underscores
   Guess a letter: (input)
   check the letter:
    X - invalid
    X + list of already put char: char was already played
    :( - wrong

    right letter:
    show word
    tries++

4.  win: WIN
    passed max attempt:
    LOSE


