import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joker.settings')
django.setup()

from game.models import Deck

values = [6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']

if __name__ == '__main__':

    print("Populating database")
    for i in values:
        new_card = Deck(suit = 'cross',
                    value = i,
                    color = 'black',
                    )
    
        new_card.save()