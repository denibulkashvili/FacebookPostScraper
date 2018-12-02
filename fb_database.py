import psycopg2

import login_info as login


# SQL Queries
create_table_query = '''CREATE TABLE cover
        (POST_LINK    TEXT    NOT NULL    PRIMARY KEY,
        POST_TEXT     TEXT    NOT NULL,); '''

insert_records_query = """ INSERT INTO cover (POST_LINK, POST_TEXT) VALUES (%s,%s)"""


# Database Operations
def connect_to_database():
    try:
        connection = psycopg2.connect(user = login.admin,
                                    password = login.admin_pass,
                                    host = "127.0.0.1",
                                    port = "5434",
                                    database = "postgres")
        # Print PostgreSQL Connection properties
        cursor = connection.cursor()
        print ( connection.get_dsn_parameters(),"\n")
        return connection, cursor

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def close_connection(connection, cursor):
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

def create_table():
    connection, cursor = connect_to_database()
    
    cursor.execute(create_table_query)
    connection.commit()
    close_connection(connection, cursor)
    print("Created table 'cover' in PostgreSQL.")

def insert_records(text, link):
    """Insert text and link into PostgreSQL table"""
    connection, cursor = connect_to_database()

    records_to_insert = (link, text)
    cursor.execute(insert_records_query, records_to_insert)
    connection.commit()
    close_connection(connection, cursor)
    print(f'Added to database: {text}')