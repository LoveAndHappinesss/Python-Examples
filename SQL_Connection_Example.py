import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, database_name):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        )
        
        print('MySQL Database connection successful')
    
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        connection.commit()
        print('Successful Query')
    except Error as err:
        print(f'Error: {err}')


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f'Error: {err}')


remove_name = '''
DELETE FROM employee
WHERE last_name = 'Beasly';
'''

add_name = '''
INSERT INTO employee
VALUES(111, 'Pam', 'Beasly', '1988-02-19', 'F', 69000, 106, 3);
'''

basic_select = '''
SELECT first_name, last_name
FROM employee;
'''

connection = create_server_connection('localhost', 'root', 'Deutschemark1998', 'exampledb')
execute_query(connection, add_name)
execute_query(connection, remove_name)
results = read_query(connection, basic_select)


from_db = []

for result in results:
    result = list(result)
    from_db.append(result)

print(from_db)
