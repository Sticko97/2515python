# """
# ACIT2515 Lab

# Week 2 -- complete this file!

# """

# # The number of turns allowed is a global constant
NB_TURNS = 10

import random

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !    
    with open("words.txt", "r") as file:
        selected_word = random.choice(file.readlines())
    return selected_word.strip()

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    # WRITE YOUR CODE HERE
    # pick = pick_random_word()
    # empty_word = ""
    # for word, letters in empty_list:


    new_word = "" #empty string
    for letter in word: 
        if letter in letters:
            new_word += letter
        else:
            new_word += "_"

        new_word += " "

    return new_word.strip()

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""

    if "_" in show_letters_in_word(word, letters):
        return False

def main(turns):
#     """
#     Runs the game. Allows for "turns" loops (attempts).
#     At each turn:
#     1. Ask the user for a letter
#     2. Add the letter to the list of letters already tried by the player
#     3. If the letter was already tried, ask again
#     4. Use the show_letters_in_word function to display hints about the word
#     5. Remove 1 to the number of tries left
#     6. Check if the player
#         - won (= word has been found)
#         - lost (= word has not been found, no tries left)

#     Do not forget to pick a random word first :-)

#     """
#     # WRITE YOUR CODE HERE
    
#     global NB_TURNS #big news we set a global variable
#     # let = input("Enter a Letter: ").upper
    word = pick_random_word()
    wordlist = [*word]
    blanklist = ["_"]
    blanklist = blanklist*len(wordlist)


    print(blanklist)

    used_letters = []

    
    while NB_TURNS > 0:
        # Ask for a letter and check if it was already tried
        letter = input("Enter a letter: ").upper()
        if letter in used_letters:
            print("You've used this letter, try again.")
        
        else:
            used_letters.append(letter)

        for count, item in enumerate(wordlist):
            if letter == item.upper():

                blanklist[count] = letter
                print(blanklist)


        NB_TURNS -= 1


    else:
        full_word = all_letters_found(word, letter) 
        print(f'The word was {word}')
        if full_word is True:
            print("You Win")
        else:
            print("You Lose")

    pass

  

if __name__ == "__main__":
    main(NB_TURNS)