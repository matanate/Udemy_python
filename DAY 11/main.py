import random
from time import sleep
import os
from blackjack_art import cards_art, title

cards = {"♦":["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♠":["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♥":["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♣":["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]}
card_value = {"A": 11,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "J": 10,
              "Q": 10,
              "K": 10}
def clear():
    os.system('cls')
def pick_card():
    symbol = random.choice(list(cards.keys()))
    number = random.choice(cards[symbol])
    cards[symbol].remove(number)
    if cards[symbol] == []:
        del cards[symbol]
    return [symbol, number]

def score_calc(cards):
    score = 0
    A_number = 0
    for j in [item[1] for item in cards]:
        score += card_value[j]
        if j == "A":
            A_number+= 1
        if score > 21 and A_number > 0:
            score-= 10
            A_number-= 1
    return score
def print_scores(dealer_cards_art, player_cards_art, dealer_score, player_score):
    clear()
    print(title)
    print(f'Dealer Full Cards: {dealer_score}')
    print(dealer_cards_art)      
    print(f'Your cards: {player_score}')
    print(player_cards_art)
    if dealer_score >= 17:
        if player_score > dealer_score or dealer_score > 21:
            print("You Won!")
        elif player_score < dealer_score:
            print("You Lost!")
        else:
            print("It's a Draw!")

def print_current_cards(dealer_cards_art, player_cards_art, player_score = ""):
    clear()
    print(title)
    print('Dealer first Card:')
    print(dealer_cards_art)      
    print(f'Your cards: {player_score}')
    print(player_cards_art)

def blackjack():
    player_cards = [pick_card(), pick_card()]
    player_cards_art = cards_art(player_cards[1][0], player_cards[1][1], cards_art(player_cards[0][0], player_cards[0][1]))
    dealer_cards = [pick_card(), pick_card()]
    dealer_cards_art = cards_art(dealer_cards[0][0], dealer_cards[0][1])
    print_current_cards(dealer_cards_art, player_cards_art)
    player_get_card = True
    i = 1
    player_score = score_calc(player_cards)
    if player_score == 21:
            print ("You Won! Black Jack '21'")
            player_get_card = False
    while player_get_card == True:    
        print_current_cards(dealer_cards_art, player_cards_art)
        if input("Type 'y' to get another card, type'n' to pass: ") == "y":
            i += 1
            player_get_card = True
            player_cards.append(pick_card())
            player_cards_art = cards_art(player_cards[i][0], player_cards[i][1], player_cards_art)
        else:
            player_get_card = False
        player_score = score_calc(player_cards)
        if player_score > 21:
            print_current_cards(dealer_cards_art, player_cards_art, player_score)
            print (f"You lost!")
            player_get_card = False
        elif player_score == 21:
            player_get_card = False

    if player_score < 21:
        dealer_score = score_calc(dealer_cards)
        dealer_cards_art = cards_art(dealer_cards[1][0], dealer_cards[1][1], dealer_cards_art)
        print_scores(dealer_cards_art, player_cards_art, dealer_score, player_score) ; sleep(0.6)    
        i = 1
        while dealer_score < 17:
            i += 1
            dealer_cards.append(pick_card())
            dealer_cards_art = cards_art(dealer_cards[i][0], dealer_cards[i][1], dealer_cards_art)
            dealer_score = score_calc(dealer_cards)
            clear()
            print_scores(dealer_cards_art, player_cards_art, dealer_score, player_score) ; sleep(0.6) 
    if input("Type 'y' to continue playing type 'n' to exit: ") == 'y':
        blackjack()

blackjack()