import mysql.connector


db = mysql.connector.connect(host = '35.202.71.75', user = 'root', password = 'movierec', database = 'movierec')

cursor = db.cursor()