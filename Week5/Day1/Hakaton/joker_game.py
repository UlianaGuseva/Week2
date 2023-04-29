
from random import shuffle
# class Player(self, hand):
#     hand = {}
    
    
big_game = 1
num_distribution = 1
player_start = 1
player1hand = {}
player2hand = {}
player3hand = {}
player4hand = {}
players = [player1hand, player2hand, player3hand, player4hand]
deck = [['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'D'], ['hearts', 'K'], ['hearts', 'A'], 
        ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'D'], ['diamonds', 'K'], ['diamonds', 'A'], 
        ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'D'], ['spades', 'K'], ['spades', 'A'], 
        ['cross', '6'], ['cross', '7'], ['cross', '8'], ['cross', '9'], ['cross', '10'], ['cross', 'J'], ['cross', 'D'], ['cross', 'K'], ['cross', 'A'], 
        ]
new_deck = []
table = {}
players_turn = 1
points = {1: 0, 2: 0, 3: 0, 4: 0}
weight_of_values = {'6': 6, '7': 7, '8':8, '9':9, '10':10, 'J': 11, 'D': 12, 'K':13, 'A': 14}

def distribution(num):
    new_deck = deck
    shuffle(new_deck)
    for n in range(num):
        player1hand[n] = new_deck.pop(-1)
    for _ in range(num):
        player2hand[n] = new_deck.pop(-1)
    for _ in range(num):
        player3hand[n] = new_deck.pop(-1)
    for _ in range(num):
        player4hand[n] = new_deck.pop(-1)
    return player1hand, player2hand, player3hand, player4hand
        
def step1player(players_turn):
        print(f' Player{players_turn} turn.\n your cards: {players[players_turn-1]}.')
        choise = input(' Choose one:')
        choise = int(choise)
        table[players_turn] = players[players_turn-1][choise]
        current_suit = players[players_turn-1][choise][0]
        del players[players_turn-1][choise]
        if players_turn !=4:
            players_turn += 1
        else:
            players_turn = 1
        return current_suit, table, player1hand, players_turn
    
def step_other_players(current_suit, table, players_turn, player1hand, player2hand, player3hand, player4hand ):
        print(f'cards on the table: \n {table} \n')
        suits=[]
        for v in players[players_turn-1].values():
            suits.append(v[0])
        choise_suit = ''
        if current_suit in suits:
            while choise_suit  != current_suit:
                print(f'Player{players_turn} turn.\n your cards: {players[players_turn-1]}.')
                choise = input(f'Choose one of current suit {current_suit}: ')
                choise =int(choise)
                choise_suit = players[players_turn-1][choise][0]
        elif 'hearts' in suits:
            while choise_suit  != 'hearts':
                print(f'Player{players_turn} turn.\n your cards: {players[players_turn-1]}.')
                choise = input(f'Choose one of trump suit (heart): ')
                choise =int(choise)
                choise_suit = players[players_turn-1][choise][0]
        else:
            print(f'Player{players_turn} turn.\n your cards: {players[players_turn-1]}.')
            choise = input(f'Choose any card: ')
            choise = int(choise)
        table[players_turn] = players[players_turn-1][choise]
        del players[players_turn-1][choise]
        
        print(f'cards on the table: \n {table}')
        if len(table) == 4:
            table_suits = []
            for v in table.values():
                table_suits.append(v[0])
            winner_choose = {}
            if 'hearts' in table_suits:
                for k, v in table.items():
                    if v[0] == 'hearts':
                        winner_choose[k] = [v]
                if len(winner_choose) == 1:
                    for k in winner_choose.keys():
                        points[k] = points[k]+1
                else:
                    weight = 0 
                    for k, v in winner_choose.items():
                        if weight_of_values[v[1]] > weight:
                            winner = players[k-1]                    
                            weight = weight_of_values[v[1]]
                        points[winner] = points[winner]+1
                    
            else:
                weight = 0
                for k, v in table.items():
                    if v[0] == current_suit:
                        winner_choose[k] = [v]
                for k, v in winner_choose.items():
                    if weight_of_values[v[1]] > weight:
                        winner = players[k-1]                    
                        weight = weight_of_values[v[1]]
                    points[winner] = points[winner]+1
            print(winner_choose)
            print('points', points)
        
        return current_suit, table, players_turn, player1hand, player2hand, player3hand, player4hand
                    
  
        
        
        
        
    
    
    
def game(players_turn):    
    player1hand, player2hand, player3hand, player4hand = distribution(num_distribution)
    print(player1hand, player2hand, player3hand, player4hand)
    current_suit, table, player1hand, players_turn = step1player(players_turn)
    for _ in range(3):
        step_other_players(current_suit, table, players_turn, player1hand, player2hand, player3hand, player4hand)
        if players_turn !=4:
            players_turn += 1
        else:
            players_turn = 1
        

game(players_turn)