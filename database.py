# File to write database-related code in:

import mysql.connector as conn

db = conn.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')
cursor = db.cursor()

# Returns True if a new user is created, False otherwise:
def createUser(username):
    if userExists(username):
        return False
    cmd = 'INSERT INTO Users(username, movieList) VALUES(\'{}\', NULL)'.format(username) 
    cursor.execute(cmd)
    db.commit()
    return True

# Returns True if user is deleted, False otherwise:
def deleteUser(username):
    if userExists(username) is False:
        return False
    cmd = 'DELETE FROM Users WHERE username=\'{}\''.format(username)
    cursor.execute(cmd)
    return True

# Returns the movie list of the given user. Returns None if the user doesn't exist.
def getMovieList(username):
    if userExists(username) is False:
        return None
    cmd = 'SELECT movieList FROM Users WHERE username=\'{}\''.format(username) #return user's movielist
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

# Adds movie to given user's movie list if the user exists:
def addMovie(username, movieID):
    if userExists() is False:
        return
    ...

# Deletes the given movie from the given user's movie list if the user exists:
def deleteMovie(username, movieID):
    if userExists() is False:
        return
    ...

# Returns True if given user exists, False otherwise:
def userExists(username):
    cmd = 'SELECT EXISTS(SELECT * FROM Users WHERE username = \'{}\')'.format(username)
    cursor.execute(cmd)
    results = cursor.fetchall()
    if results[0][0] == 0: # Username does NOT exist
        return False
    else: # Username exists
        return True

def search_title(text):
    # Code to search database for movies by title:
    cmd = "SELECT Title FROM Movie WHERE Title LIKE \'%{}%\';".format(text)
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

def advanced_query_1():
   cmd = "SELECT actorName, Title, Budget FROM Movie m JOIN Acts a USING(movieID) JOIN CastMember c USING (actorID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Acts a2 USING(movieID) JOIN CastMember c2 USING (actorID) WHERE c2.actorName = c.actorName) AND Budget > 0 ORDER BY Budget DESC;"
   cursor.execute(cmd)
   return list(cursor.fetchall())

def advanced_query_2():
   cmd = "SELECT movieID, Title, Budget, genreName FROM Movie m JOIN Belong b USING(movieID) JOIN Genre g USING (genreID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Belong b2 USING(movieID) JOIN Genre g2 USING (genreID) WHERE g2.genreName = g.genreName) ORDER BY Budget DESC;"
   cursor.execute(cmd)
   return list(cursor.fetchall())



# -------------------------------------------------------------------------------



# Code below is not being used at the moment:

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

#get maxID of movies
def get_maxID_movies():
    cmd = 'SELECT MAX(movieID) FROM Movie';
    cursor.execute(cmd)
    result = cursor.fetchall()
    return result[0][0]

# if __name__ == '__main__':
#     print(get_maxID_movies())