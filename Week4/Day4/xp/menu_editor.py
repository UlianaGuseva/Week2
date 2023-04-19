from xp import Menu_item

def load_manager():
    name = input('input name of menu item: ')
    price = input('input price of menu item: ')
    price = int(price)  
    new_item = Menu_item(name, price)
    print(new_item)
    return new_item

def show_user_menu(program = 0):
    while program != 1 and program != 2 and program !=3 and program != 4 and program != 5:
        program = input("choose an action: \n 1 - save new menu item \n 2 - delete menu item \n 3 - update menu item \n 4 - get all menu \n 5 - get menu item by it name \n : ")
        program = int(program)
    if program == 1:
        Menu_item.save(load_manager())
    elif program == 2:
        Menu_item.delete(load_manager())
    elif program == 3:
        new_name = input('input new_name: ')
        new_price = input('input new_price: ')
        new_price = int(new_price)
        Menu_item.update(load_manager(), new_name, new_price)
    elif program == 4:
        Menu_item.all()
    elif program == 5:
        search_name = input('input a name of item you search: ')
        Menu_item.get_by_name(search_name)
        
            
def add_item_to_menu():
    Menu_item.save(load_manager())
    print('item was added successfully')
    
def remove_item_from_menu():
    item_to_delete = load_manager()
    if Menu_item.get_by_name(item_to_delete.name) != []:
        Menu_item.delete(item_to_delete)
        print('item was deleted successfully')  
    else:
        print('there was an error')
        
def show_restaurant_menu():
    show_user_menu(4)
    
        
    
            


# load_manager()
# show_user_menu()

# add_item_to_menu()
# remove_item_from_menu()
show_restaurant_menu()
