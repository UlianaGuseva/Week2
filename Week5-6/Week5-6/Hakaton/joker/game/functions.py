from .models import Deck
from random import shuffle
big_game = 1
distribution = 1
player_start = 1
player1hand = []
player2hand = []
player3hand = []
player4hand = []

def distribution(distribution):
    new_deck = Deck.objects.all()
    shuffle(new_deck)
    for _ in range(distribution):
        player1hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player2hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player3hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player4hand.append(new_deck.pop(-1))
        

             