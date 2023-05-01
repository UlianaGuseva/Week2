from random import shuffle
class Player():
    def __init__(self, name: str, points: int, hand: dict, serial_num: int) -> None:
        self.name = name
        self.serial_num = serial_num
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
            self.big_points = self.big_points - (self.bet-self.points)*10
        elif self.bet < self.points:
            self.big_points += self.points      
    
class Game():
    def __init__(self, num_distribution: int, player_start: int, players_turn: int) -> None:
        self.deck = [['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'D'], ['hearts', 'K'], ['hearts', 'A'], 
        ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'D'], ['diamonds', 'K'], ['diamonds', 'A'], 
        ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'D'], ['spades', 'K'], ['spades', 'A'], 
        ['cross', '6'], ['cross', '7'], ['cross', '8'], ['cross', '9'], ['cross', '10'], ['cross', 'J'], ['cross', 'D'], ['cross', 'K'], ['cross', 'A'], 
        ]
        self.num_distribution = num_distribution
        self.player_start = player_start
        self.players_turn = players_turn
        self.weight_of_values = {'6': 6, '7': 7, '8':8, '9':9, '10':10, 'J': 11, 'D': 12, 'K':13, 'A': 14}
        self.current_suit = ''
        self.table = {}
        self.diller = 1
        self.first_after_distribution = 'y'
        
    def shuffle_deck(self):
        shuffle(self.deck)
        return self.deck
    def get_value_of_card(self, card):
        value = self.weight_of_values[card[1]]
        return value


deck = [['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'D'], ['hearts', 'K'], ['hearts', 'A'], 
        ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'D'], ['diamonds', 'K'], ['diamonds', 'A'], 
        ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'D'], ['spades', 'K'], ['spades', 'A'], 
        ['cross', '6'], ['cross', '7'], ['cross', '8'], ['cross', '9'], ['cross', '10'], ['cross', 'J'], ['cross', 'D'], ['cross', 'K'], ['cross', 'A'], 
        ]

player1 = Player(name='Player1', serial_num=1, points=0, hand={})
player2 = Player(name='Player2', serial_num=2, points=0, hand={})
player3 = Player(name='Player3', serial_num=3, points=0, hand={})
player4 = Player(name='Player4', serial_num=4, points=0, hand={})
my_game = Game(num_distribution=1, player_start=1, players_turn=1)
players = {1: player1, 2: player2, 3: player3, 4: player4}


def distribution(num):
    new_deck = my_game.shuffle_deck()
    print(new_deck)
    for n in range(num):
        player1.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player2.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player3.hand[n] = new_deck.pop(-1)
    for n in range(num):
        player4.hand[n] = new_deck.pop(-1)
    return player1, player2, player3, player4

def bets(my_game):
    turn = my_game.diller
    for _ in range(3):
        print(f'Player{turn} turn. Your cards: {players[turn].hand}')
        players[turn].bet = int(input('make your bet: '))
        if turn != 4:
            turn += 1
        else:
            turn = 1
    if my_game.num_distribution-(player1.bet+player2.bet+player3.bet+player4.bet) >= 0:
        print(f'Player{turn} turn. Your cards: {players[turn].hand}')
        banned_bet = my_game.num_distribution - (player1.bet+player2.bet+player3.bet+player4.bet)
        players[turn].bet = banned_bet
        while players[turn].bet == banned_bet:
            players[turn].bet = int(input(f'Make your bet. You cant make bet of {banned_bet}: '))
    else:
        print(f'Player{turn} turn. Your cards: {players[turn].hand}')
        players[turn].bet = int(input('make your bet: '))  
    
        
def step1player(my_game, player1, player2, player3, player4):
        my_game.table = {}
        if my_game.first_after_distribution == 'y':
            my_game.players_turn = my_game.diller
            current_player = players[my_game.players_turn]
        else:
            current_player = players[my_game.players_turn]
        print(f'{current_player.name} turn.\n your cards: {current_player.hand}.')
        choise = int(input('Choose one: '))
        my_game.table[my_game.players_turn] = current_player.hand[choise]
        my_game.current_suit = current_player.hand[choise][0]
        del current_player.hand[choise]
        if my_game.players_turn !=4:
            my_game.players_turn += 1
        else:
            my_game.players_turn = 1
        my_game.first_after_distribution = 'n'
        return my_game, player1, player2, player3, player4 
    
def step_other_players(my_game, player1, player2, player3, player4):
        print(f'cards on the table: \n {my_game.table} \n')
        print('current suit', my_game.current_suit)
        current_player = players[my_game.players_turn]
        current_player.suits=current_player.get_suits()
        choise_suit = ''
        if my_game.current_suit in current_player.suits:
            while choise_suit != my_game.current_suit:
                print(f'{current_player.name} turn.\n Your cards: {current_player.hand}.')
                choise = int(input(f'Choose one card of current suit ({my_game.current_suit}): '))
                choise_suit = current_player.hand[choise][0]
        elif 'hearts' in current_player.suits:
            while choise_suit  != 'hearts':
                print(f'{current_player.name} turn.\n your cards: {current_player.hand}.')
                choise = int(input(f'Choose one card of trump suit (heart): '))
                choise_suit = current_player.hand[choise][0]
        else:
            print(f'{current_player.name} turn.\n your cards: {current_player.hand}.')
            choise = int(input(f'Choose any card: '))
        current_player.suits = []
        my_game.table[my_game.players_turn] = current_player.hand[choise]
        del current_player.hand[choise]
        
        if len(my_game.table) == 4:
            print(f'cards on the table: \n {my_game.table} \n')
            table_suits = []
            for v in my_game.table.values():
                table_suits.append(v[0])
            winner_choose = {}
            if 'hearts' in table_suits:
                for k, v in my_game.table.items():
                    if v[0] == 'hearts':
                        winner_choose[k] = v
                if len(winner_choose) == 1:
                    for k in winner_choose.keys():
                        winner = players[k]
                    print(f'winner is {winner.name}')
                    my_game.players_turn = winner.serial_num
                    winner.points = winner.points+1
                else:
                    weight = 0 
                    for k, v in winner_choose.items():
                        if my_game.get_value_of_card(v) > weight:
                            winner = players[k]                    
                            weight = my_game.get_value_of_card(v)
                    print(f'winner is {winner.name}')
                    my_game.players_turn = winner.serial_num
                    winner.points = winner.points+1
                    
            else:
                weight = 0
                for k, v in my_game.table.items():
                    if v[0] == my_game.current_suit:
                        winner_choose[k] = v
                for k, v in winner_choose.items():
                    if my_game.get_value_of_card(v) > weight:
                        winner = players[k]                  
                        weight = my_game.get_value_of_card(v)
                print(f'winner is {winner.name}')
                my_game.players_turn = winner.serial_num
                winner.points = winner.points+1
            print(f'Bets:\n Player1 - {player1.bet} {player1.points}\n Player2 - {player2.bet} {player2.points}\n Player3 - {player3.bet} {player3.points}\n Player4 - {player4.bet} {player4.points}')
        return my_game, player1, player2, player3, player4
                    
def delete_points_bets():
    for i in players.values():
        i.points = 0
        i.bet = 0     
    
def game(my_game):    
    
    for f in range(9):
        my_game.first_after_distribution = 'y'
        print(f'GAME {f+1}')
        player1, player2, player3, player4 = distribution(my_game.num_distribution)
        bets(my_game)
        for _ in range(my_game.num_distribution):
            my_game, player1, player2, player3, player4 = step1player(my_game, player1, player2, player3, player4)
            for _ in range(2):
                my_game, player1, player2, player3, player4 = step_other_players(my_game, player1, player2, player3, player4)
                if my_game.players_turn !=4:
                    my_game.players_turn += 1
                else:
                    my_game.players_turn = 1
            my_game, player1, player2, player3, player4 = step_other_players(my_game, player1, player2, player3, player4)
        if my_game.diller != 4:
            my_game.diller += 1
        else:
            my_game.diller = 1        
        player1.get_big_points()
        player2.get_big_points()
        player3.get_big_points()
        player4.get_big_points()
        my_game.num_distribution += 1
        delete_points_bets()
        print(f'Points: \n Player1: {player1.big_points}\n Player2: {player2.big_points}\n Player3: {player3.big_points}\n Player4: {player4.big_points}')
    winner = player1
    for p in players:
        if p.big_points > winner.points:
            winner = p
    print(f'The WINNER is {winner.name}')
        
game(my_game)