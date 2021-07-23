# File to write database-related code in:

import mysql.connector as conn


db = conn.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')

cursor = db.cursor()



def search_title(text):
    # Code to search database for movies by title:
    cmd = "SELECT Title FROM Movie WHERE Title LIKE \'{}\';".format(text)
    print(cmd)
    cursor.execute(cmd)
    results = cursor.fetchall()
    print(results)
    return list(results)