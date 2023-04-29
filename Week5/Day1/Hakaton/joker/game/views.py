from django.shortcuts import render

# Create your views here.
from .models import Deck
from random import shuffle
big_game = 1
num_distribution = 1
player_start = 1
player1hand = []
player2hand = []
player3hand = []
player4hand = []
new_deck = []

def distribution(num):
    for n in Deck.objects.all():
        new_deck.append(n)
    
    shuffle(new_deck)
    print(new_deck)
    for _ in range(distribution):
        player1hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player2hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player3hand.append(new_deck.pop(-1))
    for _ in range(distribution):
        player4hand.append(new_deck.pop(-1))
    return player1hand
        
def Step1(request):
    distribution(num_distribution)
    context = {'hand1' : player1hand}
    return render(request, 'hand1.html', context)
