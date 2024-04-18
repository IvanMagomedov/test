import psycopg2
from psycopg2 import Error

def insert_record_newvideo(cursor):
    insert_query = """
    INSERT INTO newvideo (id, name_channel, link, number_views, max_views, publication_date, views, likes, comments_count, accompanying_text) 
    VALUES ('e4a93b98-a575-4d81-974e-8ee0ec89a6c5', 'maga', 'video_link', 100, 1000, '2024-04-18', 500, 200, 50, 'some_text')
    """
    cursor.execute(insert_query)

def update_record_newvideo(cursor):
    update_query = """
    UPDATE newvideo SET number_views = 150 WHERE id = 'e4a93b98-a575-4d81-974e-8ee0ec89a6c5'
    """
    cursor.execute(update_query)

def delete_record_newvideo(cursor):
    delete_query = """
    DELETE FROM newvideo WHERE id = 'd2d92c7c-ec73-4fcd-98a8-ad04edd77aa8'
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
                        insert_record_newvideo(cursor)
                        connection.commit()
                        print("1 record successfully inserted")

                    elif action == 'update':
                        # Update a record
                        update_record_newvideo(cursor)
                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record successfully updated")

                    elif action == 'delete':
                        # Delete a record
                        delete_record_newvideo(cursor)
                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record successfully deleted")

                cursor.execute("SELECT * FROM newvideo")
                print("Result", cursor.fetchall())

    except (Exception, Error) as error:
        print("Error while working with PostgreSQL:", error)

# Call the function to perform all operations simultaneously
perform_operations(['delete'])