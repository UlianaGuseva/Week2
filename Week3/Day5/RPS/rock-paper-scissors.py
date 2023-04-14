from game import Game

def get_user_menu_choice():
    choise = input('Menu\n (g) Play a new game \n (x) Show scores and exit \n : ')
    return choise
        
def print_results(all_results):
    print('Game results: \n You won', all_results['win'], 'times \n You lose', all_results['loss'], 'times \n You draw', all_results['draw'], 'times. \n Thank you for playing')
        
def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choise = get_user_menu_choice()
        if choise == 'g':
            my_game = Game()
            one_result = Game.play(my_game)
            if one_result == "win":
                results['win'] += 1
            elif one_result == "loss":
                results['loss'] += 1
            elif one_result == "draw":
                results['draw'] += 1
            choise = ''
        elif choise == 'x':
            print_results(results)
            break
        else:
            print('Wrong choise. Please try again')
        
main()
 
    
    