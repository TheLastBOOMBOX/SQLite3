import sqlite3, os
if not os.path.isfile("filmDB.db"):
    filmDB = sqlite3.connect("filmDB.db")
    c = filmDB.cursor()
    c.execute('''CREATE TABLE collection
    ( filmName text
    , date text
    , genre text
    , IMDBrating text)''')
    filmDB.commit()
    filmDB.close()

filmDB = sqlite3.connect("filmDB.db")
c = filmDB.cursor()
while input("do you want to enter a record? (y/n) \t").lower() == "y":
    filmName = input("filmName \t").lower()
    date = input("date \t\t").lower()
    genre = input("genre \t\t").lower()
    IMDBrating = input("IMDBrating \t").lower()
    c.execute(f'''INSERT INTO collection VALUES ("{filmName}","{date}","{genre}","{IMDBrating}")''')
    filmDB.commit()
filmDB.close()
input()
