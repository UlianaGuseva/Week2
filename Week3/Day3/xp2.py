import string
import random
import datetime
from faker import Faker




def random_module(num):
    if num == random.randint(1, 100):
        print('Success!')
        
random_module(2)
    
def string_module():
    letters = string.ascii_letters
    print ( ''.join(random.choice(letters) for i in range(5)))
    
string_module()

def current_date():
    today = datetime.date.today()
    print(today.strftime('%d.%m.%Y'))
    
current_date()

def new_year():
    now = datetime.datetime.today()
    ny = datetime.datetime(2024,1,1)
    time = ny-now
    mm, ss = divmod(time.seconds, 60)
    hh, mm = divmod(mm, 60)
    print('the 1st of January is in {} days and {}:{}:{} hours'.format(time.days, hh, mm, ss))
    
new_year()

def minutes_life(dd_mm_yyyy):
    dt = datetime.datetime.strptime(dd_mm_yyyy, ("%d/%m/%Y"))
    now = datetime.datetime.today()
    minutes = now - dt
    print('yoy lived', int(minutes.total_seconds()// 60), 'minutes')
    
minutes_life('12/3/1994')
    
def holiday():
    pesah = datetime.datetime(2023,4,5)
    today = datetime.datetime.today()
    time = pesah-today
    mm, ss = divmod(time.seconds, 60)
    hh, mm = divmod(mm, 60)
    print('today is', today.strftime('%d.%m.%Y'), 'the next holiday is in {} days and {}:{}:{} hours'.format(time.days, hh, mm, ss))
    
holiday()
    
def jupiter(age_sec):
    print('your age on Earth', round(age_sec/31557600, 2), 'years')
    print('your age on Mercury', round(age_sec/31557600/0.2408467, 2), 'years')
    print('your age on Venus', round(age_sec/31557600/0.61519726, 2), 'years')
    print('your age on Mars', round(age_sec/31557600/1.8808158, 2), 'years')
    print('your age on Jupiter', round(age_sec/31557600/11.862615, 2), 'years')
    print('your age on Saturn', round(age_sec/31557600/29.447498 , 2), 'years')
    print('your age on Uranus', round(age_sec/31557600/84.016846 , 2), 'years')
    print('your age on Neptune', round(age_sec/31557600/164.79132, 2), 'years')


jupiter(1000000000)


def faker_func():
    fake = Faker()
    fake_data = {}
    fake_data = {'name': fake.name(), 'adress': fake.address(), 'language code': fake.language_code()}    
    users.append(fake_data)
    

users = []
faker_func()
faker_func()
faker_func()
faker_func()
print(users)


