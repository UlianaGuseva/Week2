import random
class Card:
    def __init__(self) -> None:
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self) -> None:
        pass
    def shuffle(suit, value):
        my_deck = []
        for i in suit:
            for n in value:
                my_deck.append(i+' '+n)
        random.shuffle(my_deck)
        return my_deck
            
    def deal(suit, value):
        deck = Deck.shuffle(suit, value)
        print(deck)
        your_card = deck[0]
        del deck[0]
        print('your card: ', your_card)
        print('deck: ', deck)
   
        
my_cards = Card()
# Deck.shuffle(my_cards.suit, my_cards.value)
Deck.deal(my_cards.suit, my_cards.value)

