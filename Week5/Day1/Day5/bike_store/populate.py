import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import Customer, Rental, Vehicle, Vehicle_Size, Vehicle_Type
from faker import Faker
from datetime import date, timedelta
import random


faker = Faker()

# for _ in range(20):
#     if __name__ == '__main__':

#         print("Populating database")
    
#         new_cust = Customer(first_name = faker.first_name(),
#                     last_name = faker.last_name(),
#                     email = faker.email(),
#                     phone_number = faker.phone_number(),
#                     address = faker.address(),
#                     city = 'Tel Aviv',
#                     country = 'Israel')
    
#         new_cust.save()

    # if __name__ == '__main__':

    #     print("Populating database")
    
    #     new_cust = Vehicle(vehicle_type =  Vehicle_Type.objects.get(id=random.randint(1, 4)),
    #     date_created = '2019-01-02',
    #     real_cost = random.randint(250, 1500),
    #     size = Vehicle_Size.objects.get(id=random.randint(1, 4)))
    
    #     new_cust.save()

if __name__ == '__main__':
    for i in range(13):
        print("Populating database")
        date = faker.date_between(start_date='-7d', end_date='now')

    
        new_rent = Rental(rental_date = date,
        return_date = date+timedelta(days=6),
        customer = Customer.objects.get(id=random.randint(1, 54)),
        vehicle = Vehicle.objects.get(id=random.randint(1, 22)))
    
        new_rent.save()