import psycopg2
from datetime import date

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'S@mbation1'
DATABASE = 'actors' 

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

# cursor = connection.cursor()

# query = 'select * from actors'

# cursor.execute(query)

# result = cursor.fetchall()

# print(result)

# connection.close()


# with connection.cursor() as cursor:
#     cursor.execute(query)
#     result = cursor.fetchall()
    
# print(result)
    
# def select_column(column_name: str, table_name: str):
#     query = f'select {column_name} from {table_name}'
#     return query

    

def run_query(query:str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result
    
# print(result)

# query1 = select_column('first_name', 'actors')
# query2 = select_column('last_name', 'actors')

# result1 = run_query(query1)
# result2 = run_query(query2)

# print('First names: ', result1)
# print('Last names: ', result2)

# def select_columns(columns: list[str], table_name: str):
#     for s in columns:
#         query = f'select {s} from {table_name}'
#         result = []
#         with connection.cursor() as cursor:     
#             cursor.execute(query)
#             result.append(cursor.fetchall())
#     return result

def select_columns(columns: list[str], table_name: str):
    start = 'select '
    columms_str = ''
    for idx, column in enumerate(columns):
        columms_str += column
        if idx < len(columns) - 1:
            columms_str += ', '
    end = f' from {table_name}'

    query = start + columms_str + end
    return query


result = select_columns(['first_name', 'last_name'], 'actors')    
print(result)
columns = ['first_name', 'last_name', 'age', 'number_oscars']
q = select_columns(columns, 'actors')

print(q)

output = run_query(q)
print(output)


f_name = 'merlin'
l_name = 'monroe'
birthday = date(1970,1,1)
num_oscars = 2

q = f"insert into actors (first_name, last_name, age, number_oscars) values ('{f_name}', '{l_name}', '{birthday}', {num_oscars});"

def run_change_query(query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        
run_change_query(q)

print(q)

