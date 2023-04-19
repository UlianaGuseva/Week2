import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'S@mbation1'
DATABASE = 'RestaurantManager' 

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

cursor = connection.cursor()

class Menu_item():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        
    def save(self):
        q = f"insert into menu (name, price) values ('{self.name}', '{self.price}');"
        with connection.cursor() as cursor:
            cursor.execute(q)
            connection.commit()
      
    def delete(self):
        q = f"delete from menu where name = '{self.name}' and price = '{self.price}';"
        with connection.cursor() as cursor:
            cursor.execute(q)
            connection.commit()
            
    def update(self, new_name, new_price):
        q = f"update menu set name = '{new_name}', price = '{new_price}' where name = '{self.name}' and price = '{self.price}';"
        with connection.cursor() as cursor:
            cursor.execute(q)
            connection.commit()
            
    def all():
        q = f"select * from menu"
        with connection.cursor() as cursor:
            cursor.execute(q)
            result = cursor.fetchall()
        print(result)
        
    def get_by_name(name):
        q = f"select * from menu where name = '{name}'"
        with connection.cursor() as cursor:
            cursor.execute(q)
            result = cursor.fetchall()
        if result == []:
            return None
        else:
            print(result)
    
        
# item = Menu_item('Burger', 35)
# item.save()
# item.delete()
# item.save()
# item.update('Veggie Burger', 37)
# item = Menu_item('Beef Stew', 78)
# item.save()
# items = Menu_item.all()
# item2 = Menu_item.get_by_name('Beef Stew')
# print(item2)
# item = Menu_item('Beef Stew', 78) 
# item.delete()