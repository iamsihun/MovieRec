# File to write database-related code in:

import mysql.connector as conn

db = conn.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')
cursor = db.cursor()

def search_title(text):
    # Code to search database for movies by title:
    cmd = "SELECT Title FROM Movie WHERE Title LIKE \'%{}%\';".format(text)
    # print(cmd)
    cursor.execute(cmd)
    results = cursor.fetchall()
    # print(results)
    return list(results)

#get maxID of movies
def get_maxID_movies():
    cmd = 'SELECT MAX(movieID) FROM Movie';
    cursor.execute(cmd)
    result = cursor.fetchall()
    return result[0][0]

#add a movie record, id will automatically be set to 1+max
#args: title, overview, language
def insert_movie(title, overview, language):
    max_idx = get_maxID_movies()
    cmd = "INSERT INTO Movie (movieID, Title, Overview, Lang) VALUES {}, \'{}\', \'{}\', \'{}\'".format(max_idx+1, title, overview, language)
    cursor.execute(cmd)
    db.commit()

#update movie_title, takes newtitle and id of movie
def update_movie_title(id, new_title):
    try:
        cmd = "UPDATE Movie SET Title = \'{}\' WHERE movieID = {}".format(new_title, id)
    except:
        pass
    cursor.execute(cmd)
    db.commit()

def delete_movie(id):
    try:
        cmd = "DELETE FROM Movie WHERE movieID = {}".format(id)
    except:
        pass
    cursor.execute(cmd)
    db.commit()

def advanced_query_1():
   cmd = "SELECT actorName, Title, Budget FROM Movie m JOIN Acts a USING(movieID) JOIN CastMember c USING (actorID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Acts a2 USING(movieID) JOIN CastMember c2 USING (actorID) WHERE c2.actorName = c.actorName) AND Budget > 0 ORDER BY Budget DESC;"
   cursor.execute(cmd)
   return list(cursor.fetchall())

def advanced_query_2():
   cmd = "SELECT movieID, Title, Budget, genreName FROM Movie m JOIN Belong b USING(movieID) JOIN Genre g USING (genreID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Belong b2 USING(movieID) JOIN Genre g2 USING (genreID) WHERE g2.genreName = g.genreName) ORDER BY Budget DESC;"
   cursor.execute(cmd)
   return list(cursor.fetchall())

# Check if user exists. Add entry to 'Users' if they don't exist
def userExists(username):
    cmd = 'SELECT EXISTS(SELECT * FROM Users WHERE username = \'{}\')'.format(username)
    print(cmd)
    cursor.execute(cmd)
    results = cursor.fetchall()
    if results[0][0] == 0: #username does NOT exist
        cmd = 'INSERT INTO Users(username, movieList) VALUES(\'{}\', NULL)'.format(username) 
        print(cmd)
        cursor.execute(cmd)
        db.commit()
        return False
    else:   #username exists
        return True

#returns movie list of user (ASSUMING USER EXISTS)
def movieList(username):
    cmd = 'SELECT movieList FROM Users WHERE username=\'{}\''.format(username) #return user's movielist
    cursor.execute(cmd)
    results = cursor.fetchall()
    return results

# if __name__ == '__main__':
#     print(get_maxID_movies())