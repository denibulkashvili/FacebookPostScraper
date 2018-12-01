import psycopg2

import login_info as login


try:
    connection = psycopg2.connect(user = login.admin,
                                  password = login.admin_pass,
                                  host = "127.0.0.1",
                                  port = "5434",
                                  database = "postgres")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Create a table
    create_table_query = '''CREATE TABLE cover
          (ID INT PRIMARY KEY     NOT NULL,
          POST_TEXT           TEXT    NOT NULL,
          POST_LINK         TEXT    NOT NULL); '''


    cursor.execute(create_table_query)
    connection.commit()
    print("Created table 'cover' in PostgreSQL.")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
