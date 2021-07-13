import mysql.connector 
import pandas as pd
import numpy as np
import math
import json
db = mysql.connector.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')

cursor = db.cursor()

movies_metadata = pd.read_csv('movies_metadata.csv')
keyword = pd.read_csv('keywords.csv')
credits = pd.read_csv('credits.csv')

class Movie:
    def __init__(self, movieID, Title, Overview, Keywords, Lang, isAdultFilm, Budget, collection_dict = None):
        self.movieID = movieID
        self.Title = Title
        self.Overview = Overview
        self.Keywords = Keywords
        self.Lang = Lang
        self.isAdultFilm = isAdultFilm
        self.Budget = Budget
        self.collection_id = self.collection_name = None
        if collection_dict is not None:
            self.collection_id = collection_dict['id']
            self.collection_name = collection_dict['name']
    def insert(self):
        cmd = None
        if self.collection_id:
            col_cmd = 'INSERT INTO Collection VALUES({}, \'{}\')'.format(self.collection_id, self.collection_name)
            try:
                cursor.execute(col_cmd)
            except:
                pass
            db.commit()
            cmd = 'INSERT INTO Movie VALUES({}, \'{}\', \'{}\', \'{}\', \'{}\', {}, {}, {})'.format(self.movieID, self.Title, self.Overview, self.Keywords, self.Lang, self.isAdultFilm, self.Budget, self.collection_id)
            try:
                cursor.execute(cmd)
            except:
                pass
            db.commit()
        else:
            cmd = 'INSERT INTO Movie(movieID, Title, Overview, Keywords, Lang, isAdultFilm, Budget) VALUES({}, \'{}\', \'{}\', \'{}\', \'{}\', {}, {})'.format(self.movieID, self.Title, self.Overview, self.Keywords, self.Lang, self.isAdultFilm, self.Budget)
            try:
                cursor.execute(cmd)
            except:
                pass
            db.commit()


def parse_movie_metadata():

    for index, row in movies_metadata.iterrows():
        collection = row['belongs_to_collection']
        collection_dict = None
        try:
            val = math.isnan(collection)          
        except:
            collection_dict = eval(collection)
            
        adult = (bool)(row['adult'])
        try:
            budget = (int)(row['budget'])
        except:
            budget = 0
        try:
            id = (int)(row['id'])
            lang = (str)(row['original_language'])
            title = (str)(row['original_title'])
            overview = (str)(row['overview'])
            kw = keyword.loc[keyword.id == id, 'keywords'].values[0]
            kw = eval(kw)
        except:
            continue

        keyword_list = []
        for item in kw:
            keyword_list.append(item['name'])
        keyword_list = json.dumps(keyword_list)

        m = Movie(id, title, overview, keyword_list, lang, adult, budget, collection_dict)
        m.insert()

def parse_genre():
    for index, row in movies_metadata.iterrows():
        try:
            id = (int)(row['id'])
            genres = row['genres']
            genres = eval(genres)

            for item in genres:
                genreID = item['id']
                cmd = 'INSERT INTO Genre VALUES ({}, \'{}\')'.format(genreID, item['name'])
                try:
                    cursor.execute(cmd)
                except:
                    pass
                db.commit()
                cmd = 'INSERT INTO Belong VALUES ({}, {})'.format(id, genreID)
                try:
                    cursor.execute(cmd)
                except:
                    pass
                db.commit()
        except:
            continue
def parse_cast():
    for index, row in credits.iterrows():
        try:    
            cast = eval(row['cast'])
            id = (int)(row['id'])
        except:
            continue

        for item in cast:
            gender = 'other'
            if item['gender'] == 1:
                gender = 'female'
            elif item['gender'] == 2:
                gender = 'male'
            cmd = 'INSERT INTO CastMember VALUES({}, \'{}\', \'{}\')'.format((int)(item['cast_id']), item['name'], gender)
            try:    
                cursor.execute(cmd)
            except:
                pass
            db.commit()
            cmd = 'INSERT INTO Acts VALUES({}, {}, \'{}\')'.format(id, (int)(item['cast_id']), item['character'])
            try:    
                cursor.execute(cmd)
            except:
                pass
            db.commit()

def parse_crew():
    for index, row in credits.iterrows():
        try:
            crew = eval(row['crew'])
            id = (int)(row['id'])
        except:
            continue
        #print(crew)
        for item in crew:
            cmd = 'INSERT INTO CrewMember(crewMemberID, crewName) VALUES(\'{}\', \'{}\')'.format(item['credit_id'], item['name'])
            try:
                cursor.execute(cmd)
            except:
                pass
            db.commit()
            cmd = 'INSERT INTO WorksOn(movieID, crewMemberID, Job) VALUES({}, \'{}\', \'{}\')'.format(id, item['credit_id'], item['job'])
            try:
                cursor.execute(cmd)
            except:
                pass
            db.commit()
if __name__ == '__main__':
    #parse_movie_metadata()
    #parse_genre()
    #parse_cast()
    #parse_crew()
    pass