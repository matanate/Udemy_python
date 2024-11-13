from random import randint
import os
from guessing_game_art import TITLE

#setting constant variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check the difficulty and return the number of turns
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return  EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS

#Function to check user's guess against the answer
def check_answer(guess, answer, turns):
    """check user's guess against the answer, returns the number of turns remaining"""
    if int(guess) > answer:
        print("Too High.")
        return turns -1
    elif int(guess) < answer:
        print("Too Low.")
        return turns -1
    elif int(guess) == answer:
        print(f"You got it! The answer was {answer}")

def game():
    #clear the screen at the start of the game
    os.system('cls')

    #print the game title
    print(TITLE)

    #generate a randome number between 1 and 100.
    answer = randint(1, 100)
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')

    #choose difficulty
    turns = set_difficulty()

    #repeat the guessing if they get it wrong
    guess = 0
    while int(guess) != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        #let the user guess a number
        guess = input("Make a Guess: ")
        
        #track the number of turns
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, You Loose")
            return

game()
