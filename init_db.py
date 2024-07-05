import psycopg2

db_params = {
    'dbname': 'crud',
    'user': 'nat',
    'password': '123',
    'host': 'localhost', 
    'port': '5432'  
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE SCHEMA IF NOT EXISTS schema;
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schema.crudTutorial (
        id serial PRIMARY KEY,
        name VARCHAR(50),
        description TEXT
    );
    ''')

    connection.commit()

    print("Table 'crudTutorial' created successfully in schema 'schema'.")

except psycopg2.Error as e:
    print(f"Database error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
