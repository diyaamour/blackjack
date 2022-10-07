import random 
from replit import clear 
from art import logo 

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0 

    if 11 in cards and sum(cards) > 1:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def compare(player_score, dealer_score):

    if player_score > 21 or dealer_score > 21: 
        return "You went over. you lose."

    if player_score == dealer_score: 
        return "It's a draw."
    elif player_score > dealer_score:
        retrun "You win"
    elif dealer_score == 0:
        return "Dealer has a blackjack. You lose"
    elif player_score == 0:
        return " You have a blackjack. you win"
    elif dealer_score > 21:
        return "Dealer busted. You win"
    elif player_score > 21:
        return "You busted. You lose"
    else: 
        return "You lose."
    


while input("Do you want to play a game of Blackjack? Type 'y' to play, 'n' to exit: ") == 'y':
    clear()
    play_game()
