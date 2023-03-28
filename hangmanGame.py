ENTER_FILE_PATH_TEXT = "Enter file path: "
ENTER_INDEX_TEXT = "Enter index: "
LETS_START_TEXT = "Let's start!"
GUESS_LETTER_TEXT = "Guess a letter: "

HANGMAN_START_TEXT = """  _    _                                         
 | |  | |                                         
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                      __/ |                      
                     |___/ """

SPACE_CHAR = " "
JUMP_LINE_CHAR = "\n"
EMPTY_CHAR = ""

FILE_READ_MODE = "r"

MAX_TRIES = 6

KEY_PHOTO_1 = 0
KEY_PHOTO_2 = 1
KEY_PHOTO_3 = 2
KEY_PHOTO_4 = 3
KEY_PHOTO_5 = 4
KEY_PHOTO_6 = 5
KEY_PHOTO_7 = 6

PICTURE_1 = """    x-------x"""

PICTURE_2 = """    x-------x
    |
    |
    |
    |
    |"""

PICTURE_3 = """    x-------x
    |       |
    |       0
    |
    |
    |"""

PICTURE_4 = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""

PICTURE_5 = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""

PICTURE_6 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""

PICTURE_7 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

HANGMAN_PHOTOS = {
    KEY_PHOTO_1: PICTURE_1,
    KEY_PHOTO_2: PICTURE_2,
    KEY_PHOTO_3: PICTURE_3,
    KEY_PHOTO_4: PICTURE_4,
    KEY_PHOTO_5: PICTURE_5,
    KEY_PHOTO_6: PICTURE_6,
    KEY_PHOTO_7: PICTURE_7
}

UNDERLINE_CHAR = "_"

ERROR_CHAR = "X"
ARROW_CHAR = " -> "

SAD_FACE_TEXT = ":("

WON_TEXT = "WON"
LOST_TEXT = "LOST"


def main():
    # print the start screen and get secret word
    secret_word = game_start_get_secret_word(MAX_TRIES)

    """
    Till player wins or loses (while num_of_tries<=MAX_TRIES)
    3.
    if the letter is not in the word, print the hanging
    print the curr hanging line
    print the chars with underscores
    Guess a letter: (input)
    check the letter:
    X - invalid
    X + list of already put char: char was already played
    :( - wrong
    check if player won
    """
    old_letters_guessed = []  # list of the already guessed chars
    user_won = False
    num_of_tries = 0

    while num_of_tries < MAX_TRIES and not user_won:

        # ask user to guess a letter (input), check it and act accordingly
        # valid: add to the guessed list, invalid: print
        letter_guessed = input(GUESS_LETTER_TEXT)
        letter_is_valid, old_letters_guessed = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        # if the letter is valid, print the hidden word
        if letter_is_valid:

            # if the letter is not in the word, add to the number of tries and print :( and the current hangman
            if letter_guessed not in secret_word:
                # add one to the tries
                num_of_tries += 1
                print(SAD_FACE_TEXT)
                print_hangman(num_of_tries)

            print(show_hidden_word(secret_word, old_letters_guessed))

            # check if user won
            user_won = check_win(secret_word, old_letters_guessed)

    if user_won:
        print(WON_TEXT)
    else:
        print(LOST_TEXT)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: the letter the user guessed
    :letter_guessed type: str
    :param old_letters_guessed: the list of letters already guessed
    :old_letters_guessed_type: list (str)
    :return: if the guess is valid
    :rtype: boolean
    """
    letter_guessed = letter_guessed.lower()
    has_one_char = False
    has_only_alphabet = False
    havent_guessed = False
    #
    # check if it has only one char
    input_letter_len = len(letter_guessed)
    has_one_char = input_letter_len == 1
    #
    # check if has only alphabet
    has_only_alphabet = letter_guessed.isalpha()
    #
    # check if already guessed this letter
    havent_guessed = old_letters_guessed.count(letter_guessed) == 0
    return has_only_alphabet and has_one_char and havent_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    if the letter is correct and havent been guessed:
        add to the old letters guessed list
        return true and the old letters guessed list
    if the letter is incorrect:
    print X
    under x the list of guessed letters as a small letters list, sorted from smallest to highest
    return false, and the old letters


    :param letter_guessed: user input of the letter guessed
    :param old_letters_guessed: list of the guessed letters so far
    :return:
        if the letter is valid :type: bool
        old_letters_guessed: list with the already guessed letters :typeL list
    """
    print("letter guessed: ", letter_guessed)
    letter_is_valid = check_valid_input(letter_guessed, old_letters_guessed)
    #
    if letter_is_valid:
        old_letters_guessed += letter_guessed
    else:
        old_letters_guessed.sort()

        print(ERROR_CHAR)

        show_hidden_word(letter_guessed, old_letters_guessed)
        #  print the guessed letter with arrows if the char is a repeating letter
        if letter_guessed in old_letters_guessed:
            print((ARROW_CHAR.join(old_letters_guessed)).lower())

    return letter_is_valid, old_letters_guessed


def show_hidden_word(secret_word, old_letters_guessed):
    """
    function returns a string of letters and underscores =
    has the guessed letters in their appropriate position and the rest as underlines
    :param secret_word: the string the player has to guess
    :param old_letters_guessed:  the letters the player has guessed so far
    :return: the string with the guessed letters showing
    :rtype: string
    """
    result_word = ''
    # loops the word and checks if the current letter has been guessed
    # if yes: add it as a letter to the result word
    # if not: add it as an underline to the result word
    for curr_letter in secret_word:
        if curr_letter in old_letters_guessed:
            result_word += curr_letter
        else:
            result_word += UNDERLINE_CHAR
        result_word += ' '
    # erasing the last space
    result_word = result_word[:-1]
    return result_word


def print_hangman(num_of_tries):
    """
    Function recieves the number of tries and prints the according picture
    :param num_of_tries: the number of tries
    :return: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word: the word the user has to guess
    :param old_letters_guessed: the letters that have been guessed
    :return: True - all letters of the secret word have been guessed. if not - False
    """
    user_won = True
    # loops the word, if any of the letters have not been guessed, break and return False
    for curr_letter in secret_word:
        if curr_letter not in old_letters_guessed:
            user_won = False
            break
    return user_won


def choose_word(file_path, index):
    """
    Function receives a file path with words and an index
    Function returns the word in that index in the file

    Obs:
    index starts from 1 and not 0
    If the index is longer then the num of words, go back to the start

    :param file_path: path to a file containing the words (separated by spaces) :type: file
    :param index: the index of a certain wrd in the file :type: int
    :return: the chosen word
    """
    list_words = []

    # 1: file to list of words
    with open(file_path, FILE_READ_MODE) as words_file:
        file_content = words_file.read()
        file_content = file_content.replace(JUMP_LINE_CHAR, EMPTY_CHAR)
        list_words = file_content.split(SPACE_CHAR)

    # 2: check if the index is greater than the amount of words
    #       if so, take out the number of words from the index until it is not greater
    num_words = len(list_words)
    if index > num_words:
        while index > num_words:
            index = index - num_words

    # 3: get the word in that index - 1 (as the index starts from 1 and he list starts from 0)
    chosen_word = list_words[index - 1]

    return chosen_word


def print_start_screen(num_tries):
    print(HANGMAN_START_TEXT)
    print(num_tries)


def game_start_get_secret_word(num_tries):
    """
    function to print the start screen to the user, input the file path and word index and print the 1st hangman and word
    :param num_tries: the max num of tries (to print)
    :return: the secret word
    """

    # input from user file path and index of word
    file_path = input(ENTER_FILE_PATH_TEXT)
    index_secret_word = int(input(ENTER_INDEX_TEXT))
    print(LETS_START_TEXT)

    # call function to get the secret word
    secret_word = choose_word(file_path, index_secret_word)

    # print the 1st hangman and the hidden secret word
    print_hangman(0)
    print(show_hidden_word(secret_word, []))

    return secret_word


if __name__ == '__main__':
    main()
