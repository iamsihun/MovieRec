# File to write database-related code in:
import mysql.connector as conn
import redis
import json
r_conn = redis.Redis()

db = conn.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')
cursor = db.cursor()

# Returns True if a new user is created, False otherwise:
def createUser(username):
    if userExists(username):
        return False
    cmd = 'INSERT INTO Users(username, favorite_movie) VALUES(\'{}\', NULL)'.format(username) 
    cursor.execute(cmd)
    db.commit()
    return True

# Returns True if user is deleted, False otherwise:
def deleteUser(username):
    if userExists(username) is False:
        return False
    cmd = 'DELETE FROM Users WHERE username=\'{}\''.format(username)
    cursor.execute(cmd)
    db.commit()
    return True

# Returns favorite movie of given user:
def getFavoriteMovie(username):
    cmd = "SELECT Title from Users u JOIN Movie m ON u.favorite_movie = m.movieID where username = \'{}\'".format(username)
    try:
        cached = r_conn.get(username)
        if cached is not None:
            return json.loads(cached)
        cursor.execute(cmd)
        results = cursor.fetchall()
        #return list(results)
        r_conn.set(json.dumps(list(results)))
        return list(results)

    except:
        return None

#Updates User's favorite Movie_id
#args: username, new favorite movie_id
def updateUserFavoriteMovie(username, new_favorite_movie):
    cmd = "UPDATE Users SET favorite_movie = {} WHERE username = \'{}\'".format(new_favorite_movie, username)
    try:
        cursor.execute(cmd)
        db.commit()
        return True
    except:
        return False

# Returns the movie list of the given user. Returns None if the user doesn't exist.
def getMovieList(username):
    if userExists(username) is False:
        return None
    cmd = 'SELECT movieID, Title FROM Movie NATURAL JOIN SavedMovies WHERE username=\'{}\''.format(username) #return user's movielist
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

# Returns True if the movie was added to the given user's movie list, False otherwise:
def addMovie(username, movieID):
    if userExists(username) is False:
        return False
    cmd = 'INSERT INTO SavedMovies(username, movieID) VALUES(\'{}\', \'{}\')'.format(username, movieID) 
    cursor.execute(cmd)
    db.commit()
    return True

# Returns True if the movie was deleted from the given user's movie list, False otherwise:
def deleteMovie(username, movieID):
    if userExists(username) is False:
        return False
    cmd = 'DELETE FROM SavedMovies WHERE username=\'{}\' AND movieID=\'{}\''.format(username, movieID)
    cursor.execute(cmd)
    db.commit()
    return True

# Returns True if given user exists, False otherwise:
def userExists(username):
    cmd = 'SELECT EXISTS(SELECT * FROM Users WHERE username = \'{}\')'.format(username)
    cursor.execute(cmd)
    results = cursor.fetchall()
    if results[0][0] == 0: # Username does NOT exist
        return False
    else: # Username exists
        return True

# Code to search database for movies by title:
def search(text):
    cmd = "SELECT movieID, Title FROM Movie WHERE Title LIKE '%{}%' UNION SELECT movieID, Title FROM Movie NATURAL JOIN Acts NATURAL JOIN CastMember WHERE actorName LIKE '%{}%'".format(text, text)
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

def getMovieData(movieID):
    data = {}
    
    cmd = "SELECT Title FROM Movie WHERE movieID = \'{}\';".format(movieID)
    cursor.execute(cmd)
    results = cursor.fetchall()

    movieData = list(results)
    genres = getGenres(movieID)
    director = getDirector(movieID)
    cast = getCast(movieID)

    data['MovieData'] = movieData
    data['Genres'] = genres
    data['Director'] = director
    data['Cast'] = cast

    return data

# Find the genres for a movie using movieID
def getGenres(movieID):
    cmd = "SELECT genreName FROM Movie NATURAL JOIN Belong NATURAL JOIN Genre WHERE movieID = {};".format(movieID)
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

# Find the director for a movie using movieID
def getDirector(movieID):
    cmd = "SELECT crewName FROM Movie NATURAL JOIN WorksOn NATURAL JOIN CrewMember WHERE movieID = {} AND Job = \'Director\';".format(movieID)
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

# Find actors for a movie using movieID
def getCast(movieID):
    cmd = "SELECT actorName FROM Movie NATURAL JOIN Acts NATURAL JOIN CastMember WHERE movieID = {};".format(movieID)
    cursor.execute(cmd)
    results = cursor.fetchall()
    return list(results)

# Call the stored procedure
def actor_tiers():
    cursor.callproc('actor_tiers')
    results = []
    for result in cursor.stored_results():
        results = result.fetchall()
    return results

def advanced_query_1():
   cmd = "SELECT actorName, Title, Budget FROM Movie m JOIN Acts a USING(movieID) JOIN CastMember c USING (actorID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Acts a2 USING(movieID) JOIN CastMember c2 USING (actorID) WHERE c2.actorName = c.actorName) AND Budget > 0 ORDER BY Budget DESC;"
   cursor.execute(cmd)
   return list(cursor.fetchall())

def advanced_query_2():
   cmd = "SELECT genreName, Title, Budget FROM Movie m JOIN Belong b USING(movieID) JOIN Genre g USING (genreID) WHERE Budget >= ALL(SELECT Budget FROM Movie m2 JOIN Belong b2 USING(movieID) JOIN Genre g2 USING (genreID) WHERE g2.genreName = g.genreName) ORDER BY Budget DESC;"
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
#     updateUserFavoriteMovie('abc', 20)
    