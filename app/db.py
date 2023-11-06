# You can use a database framework like SQLite to store the data here.
# This example uses a simple text file to store data.
# You can replace this with an actual database connection.

def store_data_to_db(data):
    with open("dates.txt", "a") as file:
        file.write(data)
