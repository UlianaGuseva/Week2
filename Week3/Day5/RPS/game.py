import random
class Game:
    def __init__(self) -> None:
        self.list_select = ['r', 's', 'p']
        self.user_item = ''
        self.computer_item = ''
        self.result = ''
        
    
    def get_user_item(self):
        while True:
            self.user_item = input('Select (r)ock, (p)aper, or (s)cissors: ')
            if self.user_item in self.list_select:
                break
            else:
                print('Wrong choise. Please try again')
        return self.user_item
    
    def get_computer_item(self):
        comp_random = random.randint(0, 2)
        self.computer_item = self.list_select[comp_random]
        return self.computer_item
    
    def get_game_result(self):
        if self.computer_item == self.user_item:
            self.result = 'draw'
        elif self.computer_item == 'r':
            if self.user_item == 's':
                self.result = 'loss'
            else:
                self.result = 'win'
        elif self.computer_item == 's':
            if self.user_item == 'p':
                self.result = 'loss'
            else:
                self.result = 'win'
        elif self.computer_item == 'p':
            if self.user_item == 'r':
                self.result = 'loss'
            else:
                self.result = 'win'
        return self.result
    def play(self):
        Game.get_user_item(self)
        Game.get_computer_item(self)
        Game.get_game_result(self)
        print('You choise:', self.user_item, 'The computer choise:', self.computer_item, '. Result:', self.result)
        return self.result
        
        
            
            
        
        
    
      

                