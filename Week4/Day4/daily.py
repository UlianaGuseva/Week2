# 
import requests
import json
from random import choice
import psycopg2


# while len(database) < 10:
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_random_instances(data_list, n):
    instances = []
    for _ in range(n):
        random_list = choice(data_list)
        instances.append(random_list)
    return instances

def extract(instance: dict):
    name = instance['name']['common']
    capital = instance['capital'][0]
    flag = instance['flag']
    subregion = instance['subregion']
    population = instance['population']
    return name, capital, flag, subregion, population
    
# i = random.randint(1, 251)
# print(data[0])
# instance = data[0]
# print(instance.keys())

def preprocess(instances: list[dict]):
    preprocessed = []
    for instance in instances:
        preprocessed_inst = extract(instance)
        if preprocessed_inst is None:
            continue
        preprocessed.append(preprocessed_inst)
    return preprocessed

url = "https://restcountries.com/v3.1/all"
data = get_data(url)
random_inst = get_random_instances(data, 10)
clean_inst = preprocess(random_inst)
print(clean_inst)


# ------------------------------
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'S@mbation1'
DATABASE = 'countries' 

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

def insert_query(columns_names: tuple[str], data: tuple, table_name: str):
    columns = ", ".join(columns_names)
    name, capital, flag, subregion, population = data
    query = f"insert into {table_name} ({columns}), values ('{name}', '{capital}', '{flag}', '{subregion}', {population});"
    return query

columns = ['name', 'capital', 'flag', 'subregion', 'population']

q = insert_query(columns_names=columns, data=clean_inst, table_name='countries')
print(q)


def run_change_query(query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    print('success')
        
        
for s in clean_inst:
    q = insert_query(columns_names=columns, data=s, table_name='countries')
    run_change_query(q)
