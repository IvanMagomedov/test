import psycopg2
from psycopg2 import Error

def insert_record_promo(cursor):
    insert_query = """
    INSERT INTO promo (id, name, number_views, max_views, name_channel, accompanying_text) 
    VALUES ('2bc3eea4-c48f-4f12-9878-e314c407677f', 'maga', 100, 1000, 'Djafar', 'some_text')
    """
    cursor.execute(insert_query)

def update_record_promo(cursor):
    update_query = """
    UPDATE promo SET number_views = 150 WHERE id = '2bc3eea4-c48f-4f12-9878-e314c407677f'
    """
    cursor.execute(update_query)

def delete_record_promo(cursor):
    delete_query = """
    DELETE FROM promo WHERE id = '2bc3eea4-c48f-4f12-9878-e314c407677f'
    """
    cursor.execute(delete_query)

def perform_operations(actions):
    try:
        # Connect to an existing database
        with psycopg2.connect(user="postgres",
                              password="385645",
                              host="127.0.0.1",
                              port="5432",
                              database="new_shorts") as connection:

            with connection.cursor() as cursor:
                for action in actions:
                    if action == 'insert':
                        # Insert a record
                        insert_record_promo(cursor)
                        connection.commit()
                        print("1 record successfully inserted")

                    elif action == 'update':
                        # Update a record
                        update_record_promo(cursor)
                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record successfully updated")

                    elif action == 'delete':
                        # Delete a record
                        delete_record_promo(cursor)
                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record successfully deleted")

                cursor.execute("SELECT * FROM promo")
                print("Result", cursor.fetchall())

    except (Exception, Error) as error:
        print("Error while working with PostgreSQL:", error)

# Call the function to perform all operations simultaneously
perform_operations(['insert', 'update'])