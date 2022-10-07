import random 
from replit import clear
from art import logo 


def deal_card(): 
    """ Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """ Take a list of cards and return the score """
    if sum(cards) == 21 and len(cards) == 2:
        return 0 

    if 11 in cards and sum(cards) > 1:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
    
    if player_score > 21 and dealer_score > 21:
        return " You busted. You lose 😭"
        

    if dealer_score == player_score:
        return "Draw 🤝"
    elif dealer_score == 0: 
        return "Dealer has a Blackjack. You lost 😭"
    elif player_score == 0:
        return "BLACKJACK. You win 🥇 "
    elif player_score > 21:
        return "You busted! Dealer wins 😤"
    elif dealer_score > 21:
        return "Dealers busts. You win 🤩"
    elif player_score > dealer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
     
    print(logo)
    dealer_cards = []
    player_cards = []
    game_over = False

    for x in range(2):
       dealer_cards.append(deal_card())
       player_cards.append(deal_card())



    while not game_over: 
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"  Your cards: {player_cards}, current score: {player_score}")
        print(f"  Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True 
            
        else: 
            player_continues = input("Type 'hit' to get another card, type 'pass' to stay: ")
            
            if player_continues == "hit": 
                player_cards.append(deal_card())
            else: 
                game_over = True 

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print( f" Your final hand: {player_cards}, final score: {player_score}")
    print( f" Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))
        
while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y': 
    clear()
    play_game()




















# dealer_cards = []
# player_cards = []

# while len(dealer_cards) != 2: 
#     dealer_cards = dealer_cards.append(random.randint(1,11))
#     if len(dealer_cards) == 2:
#         print("Dealers has X and a", dealer_cards[1])

# # while len(player_cards) != 2:
# #     player_cards = int(random.choice(cards))
# #     if len(player_cards) == 2:
# #         print("Player has", player_cards)

# # if sum(dealer_cards) == 21: 
# #     print("Dealer wins!")
# # elif sum(dealer_cards) > 21:
# #     print("Dealer Busts")



# # while sum(player_cards) < 21: 
# #     advance = str(input(f"You have {sum(player_cards)}, Type 'hit' or 'pass': "))
# #     # print(advance)
# #     if advance == "hit":
# #         player_cards.append(random.randint(1,11))
# #         print("You now have a total of", str(sum(player_cards)) + " from these cards", player_cards)
# #     else: 
# #         print("The dealer has a total of ", str(sum(dealer_cards)) + " with", dealer_cards)
# #         if sum(dealer_cards) > sum(player_cards):
# #             print("Dealer wins!")
# #         elif sum(dealer_cards) < sum(player_cards):
# #             print("You win")
# #         else: 
# #             print("It's a draw")
# #             break

# # if sum(player_cards) > 21:
# #     print("You busted! Dealer wins")
# # elif sum(player_cards) == 21:
# #     print("You have BLACKJACK! You Win")

    

   