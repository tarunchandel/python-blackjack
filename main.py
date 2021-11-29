import art
import random
from replit import clear 

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Function to draw a card
def draw(user):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user.append(random.choice(cards))
  return user

#function to check the sum of cards for the given user
def cards_total(user):
  if sum(user) > 21 and 11 in user:
    user.remove(11)
    user.append(1)
  return sum(user)

#Function to check if it is a blackjack
def is_blackjack(user):
  if sum(user) == 21 and len(user) == 2:
    return True
  else:
    return False
    
#function to decide the winner
def find_winner(player, dealer):
  if (is_blackjack(player) and is_blackjack(dealer)) or (cards_total(dealer) == cards_total(player)):
    print("It is a draw.")
  elif is_blackjack(dealer):
    print("It's a Blackjack for the dealer! Dealer wins!")
  elif is_blackjack(player):
    print("It's a Blackjack! You win!")
  elif cards_total(dealer) > 21 or cards_total(dealer) < cards_total(player):
    print("You Win!")
  else:
    print("Dealer wins!")

#function for the game, to make it recursive
def play_game():
  clear()
  print(art.logo)
  player = []
  dealer = []

  #initiating the game by drawing 2 cards for both the players
  in_play_flag = True
  
  for _ in range(2):
    dealer = draw(dealer)
    player = draw(player)

  if not is_blackjack(player):
    print(f"Dealer: {dealer[0]}.\nYour Cards: {player}. Your total: {cards_total(player)}")
    while in_play_flag:
      play_flag = input("Type 'y' to get another card, type 'n' to pass: ")
      if play_flag == 'y':
        player = draw(player)
        print(f"Dealer: {dealer[0]}.\nYour Cards: {player}. Your total: {cards_total(player)}")
        if cards_total(player) > 21:
          print("You lost.")
          in_play_flag = False
      
      else:
        in_play_flag = False
        #checking dealer's cards and their total
        
        if not is_blackjack(dealer):
          while cards_total(dealer) < 17:
            dealer = draw(dealer)
          print(f"Dealer Cards: {dealer}. Dealer's total: {cards_total(dealer)}.\nYour Cards: {player}. Your total: {cards_total(player)}")
              
      #checking and declaring the winner
        find_winner(player, dealer)

  else:
    find_winner(player, dealer)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()