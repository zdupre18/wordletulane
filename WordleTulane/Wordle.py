"""
Tulane University, CMPS 1500, Fall 2022

STUDENTS MUST FILL IN BELOW

Student name: Zoe Dupre
Splash card number: 721002552
Student email address: zdupre@tulane.edu
Course section: 1500-01Fa22

Collaborators:
"""
#ella,troy,chris, dave dupre (father)

# NOTE: you mu
# st write your own code. You may discuss the assignment with
#       professors, TAs, other students, or family members. But you MUST
#       list anyone you collaborated with in the space above.

import random


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    solution = random.choice(FIVE_LETTER_WORDS)
    print(solution)

    # Milestone 1: chose a random word from the wordlist here
    def enter_action(guessedword):
        row = gw.get_current_row()
        guessedlower = guessedword.lower()
        #convert guessword to lowercase --- all words are lowercase in dictionary
        for index in range(len(guessedword)):
            #added row to this to define and write in each word
            gw.set_square_letter(row, 0, guessedword[0])
            gw.set_square_letter(row, 1, guessedword[1])
            gw.set_square_letter(row, 2, guessedword[2])
            gw.set_square_letter(row, 3, guessedword[3])
            gw.set_square_letter(row, 4, guessedword[4])
#see if found word is in dicgtinary
        found_word = False
        for w in FIVE_LETTER_WORDS:
            if w == guessedlower:
                found_word = True
                break
        letter_key = guessedword.upper()
        if found_word is False:
            gw.show_message('Not in word list')

        for i,c in enumerate(guessedlower):
            ##enumerate = date set
            if c == solution[i]:
                    #character is in the same positon
                gw.set_square_color(row,i, CORRECT_COLOR)
                gw.set_key_color(letter_key[i],CORRECT_COLOR)
                    #letter key is an array -- not correcrtly named
            else:
                    #is there character present
                character_present = False
                for solution_char in solution:
                    if c == solution_char:
                        gw.set_square_color(row,i,PRESENT_COLOR)
                        gw.set_key_color(letter_key[i],PRESENT_COLOR)
                        character_present = True
                        break
                    if character_present is False:
                        gw.set_square_color(row,i,MISSING_COLOR)
                        gw.set_key_color(letter_key[i],MISSING_COLOR)
        if guessedlower == solution:
            gw.show_message('Congratulations you won!')
            return

        # First, it must check to see whether the user has correctly guessed all five letters, in case you want to
        # If not, your program must moveon to the next row
        # that once you have set the color of a key, itwon’t change back. If, for example, you’ve colored the S key green, it will never get set to yellow orgray even though you may end up using those colors for squares that contain an S. This fact shouldmake your job easier.

        gw.set_current_row(row +1)
        ##enter in a new row to write on it

            #need to check if guess word is a valid word
            #is guess word in list of FIVE_LETTER_WORDS
            #guess word is a one word out of 5,0000 not checking for == (in five letter word)
            ## ex is hello in [in five letter word]

        """ This function is called any time the enter button
        is clicked/typed in the game. guessedword is the player's most
        recent guess which needs to be checked.
        """

        # Milestone 1: put test code here to display
        #              the solution on game board using:








        # also show a message on the gameboard indicating that
        # this is for milestone 1
        # end milestone 1

        # Milestones 2+: put code below here
        #gw.show_message("You need to implement this method.")


    # Students: you do not need to make any changes below here.

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":

    wordle()
#keyboard keys are upper case s.upper so write code to make it that way

#lets see if this is the answer
#if lower == anseer
#resultsfile = open('wordle-results') put it in write mode
#you want to append the file -- open('myfile.txt,'a')
#resultsfile.write('win')
#resultd.fle/close()
#gw.show_message('youwin")