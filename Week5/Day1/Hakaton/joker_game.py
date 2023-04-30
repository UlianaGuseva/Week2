
from random import shuffle
class Player():
    def __init__(self, points: int, hand: dict) -> None:
        self.points = points
        self.hand = hand
        self.suits = []
        self.bet = 0
        self.big_points = 0
        
    def get_suits(self):
        for v in self.hand.values():
            self.suits.append(v[0])
            return self.suits
        
    def get_big_points(self):
        if self.bet == self.points:
            self.big_points += self.points*10
        elif self.bet > self.points:
            self.big_points -= self.points*10
        elif self.bet < self.points:
            self.big_points += self.points
        
        
    
# class Game():
#     def __init__(self, num_distribution: int, player_start: int, players_turn: int) -> None:
#         deck = [['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'D'], ['hearts', 'K'], ['hearts', 'A'], 
#         ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'D'], ['diamonds', 'K'], ['diamonds', 'A'], 
#         ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'D'], ['spades', 'K'], ['spades', 'A'], 
#         ['cross', '6'], ['cross', '7'], ['cross', '8'], ['cross', '9'], ['cross', '10'], ['cross', 'J'], ['cross', 'D'], ['cross', 'K'], ['cross', 'A'], 
#         ]
#         self.num_distribution = num_distribution
#         self.player_start = player_start
#         self.players_turn = players_turn
#         self.weight_of_values = {'6': 6, '7': 7, '8':8, '9':9, '10':10, 'J': 11, 'D': 12, 'K':13, 'A': 14}
#         self.current_suit = ''
#         self.table = {}
        
#         def shuffle_deck(self):
#             shuffle_deck = shuffle(self.deck)
#             return shuffle_deck
#         def get_value_of_card(self, card):
#             value = weight_of_values[card[1]]
#             return value
    
    
big_game = 1

player_start = 1

deck = [['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'D'], ['hearts', 'K'], ['hearts', 'A'], 
        ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'D'], ['diamonds', 'K'], ['diamonds', 'A'], 
        ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'D'], ['spades', 'K'], ['spades', 'A'], 
        ['cross', '6'], ['cross', '7'], ['cross', '8'], ['cross', '9'], ['cross', '10'], ['cross', 'J'], ['cross', 'D'], ['cross', 'K'], ['cross', 'A'], 
        ]
new_deck = []
table = {}
players_turn = 1
weight_of_values = {'6': 6, '7': 7, '8':8, '9':9, '10':10, 'J': 11, 'D': 12, 'K':13, 'A': 14}

player1 = Player(points=0, hand={})
player2 = Player(points=0, hand={})
player3 = Player(points=0, hand={})
player4 = Player(points=0, hand={})

players = [player1, player2, player3, player4]



def distribution(num):
    new_deck = deck
    shuffle(new_deck)
    for n in range(num):
        player1.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player2.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player3.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player4.hand[n] = new_deck.pop(-1)
    return player1, player2, player3, player4

def bets():
    turn = 0
    for _ in range(4):
        print(f'Player{turn} turn. your cards: {players[turn].hand}')
        players[turn].bet = int(input('make your bet: '))
        turn += 1
    
        
def step1player(players_turn):
        print(f' Player{players_turn} turn.\n your cards: {players[players_turn-1].hand}.')
        choise = input(' Choose one: ')
        choise = int(choise)
        table[players_turn] = players[players_turn-1].hand[choise]
        current_suit = players[players_turn-1].hand[choise][0]
        print('current suit', current_suit)
        del players[players_turn-1].hand[choise]
        if players_turn !=4:
            players_turn += 1
        else:
            players_turn = 1
        return current_suit, table, player1, players_turn
    
def step_other_players(current_suit, table, players_turn, player1, player2, player3, player4):
        print(f'cards on the table: \n {table} \n')
        print(f' your cards: {players[players_turn-1].hand}.')
        current_player = players[players_turn-1]
        suits=current_player.get_suits()
        print('your suits', suits)
        choise_suit = ''
        if current_suit in suits:
            print('current_suit in suits')
            while choise_suit  != current_suit:
                print(f'Player{players_turn} turn.\n your cards: {current_player.hand}.')
                choise = input(f'Choose one of current suit {current_suit}: ')
                choise =int(choise)
                choise_suit = current_player.hand[choise][0]
        elif 'hearts' in suits:
            print('hearts in suits')
            while choise_suit  != 'hearts':
                print(f'Player{players_turn} turn.\n your cards: {current_player.hand}.')
                choise = input(f'Choose one of trump suit (heart): ')
                choise =int(choise)
                choise_suit = current_player.hand[choise][0]
        else:
            print('no current suit or hearts')
            print(f'Player{players_turn} turn.\n your cards: {current_player.hand}.')
            choise = input(f'Choose any card: ')
            choise = int(choise)
        table[players_turn] = current_player.hand[choise]
        del current_player.hand[choise]
        
        print(f'cards on the table: \n {table}')
        if len(table) == 4:
            table_suits = []
            for v in table.values():
                table_suits.append(v[0])
            winner_choose = {}
            if 'hearts' in table_suits:
                for k, v in table.items():
                    if v[0] == 'hearts':
                        winner_choose[k] = v
                    print(winner_choose)
                if len(winner_choose) == 1:
                    for k in winner_choose.keys():
                        winner = players[k-1]
                    winner.points = winner.points+1
                else:
                    weight = 0 
                    for k, v in winner_choose.items():
                        if weight_of_values[v[1]] > weight:
                            winner = players[k-1]                    
                            weight = weight_of_values[v[1]]
                    winner.points = winner.points+1
                    
            else:
                weight = 0
                for k, v in table.items():
                    if v[0] == current_suit:
                        winner_choose[k] = v
                    print(winner_choose)
                for k, v in winner_choose.items():
                    print(v[1])
                    if weight_of_values[v[1]] > weight:
                        winner = players[k-1]   
                        print(winner)                 
                        weight = weight_of_values[v[1]]
                        print(weight)
                winner.points = winner.points+1
            print(winner)
            print('points', player1.points, player2.points, player3.points, player4.points)
        
        return current_suit, table, players_turn, player1, player2, player3, player4
                    
def delete_points():
    for i in players:
        i.points = 0
        
        
        
        
    
    
    
def game(players_turn): 
    num_distribution = 1   
    for f in range(3):
        player1, player2, player3, player4 = distribution(num_distribution)
        bets()
        for _ in range(num_distribution):
            current_suit, table, player1, players_turn = step1player(players_turn)
            for _ in range(3):
                step_other_players(current_suit, table, players_turn, player1, player2, player3, player4)
                if players_turn !=4:
                    players_turn += 1
                else:
                    players_turn = 1
                table = []
        player1.get_big_points()
        player2.get_big_points()
        player3.get_big_points()
        player4.get_big_points()
        num_distribution += 1
        delete_points()
        print(f'Points: \n Player1: {player1.big_points}\n Player2: {player2.big_points}\n Player3: {player3.big_points}\n Player4: {player4.big_points}')
        

game(players_turn)