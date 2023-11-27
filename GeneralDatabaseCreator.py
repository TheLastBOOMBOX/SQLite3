import sqlite3, os

file = input("enter DB file you want to open")
while input(f"you wish to open{file}.db? y/n").lower() == "n":
    file = input("enter DB file you want to open")


if not os.path.isfile(f"{file}.db"):
    print("Creating new database")
    DB = sqlite3.connect(f"{file}.db")
    c = DB.cursor()
    Table = input("Name your table")
    numberOfFields = int(input("Enter number 0f fields"))
    fieldNames = []
    for x in range(numberOfFields):
        fieldNames.append(input(f"Enter name for field {x}"))


    c.execute(f'''CREATE TABLE {Table}
    ( filmName text
    , date text
    , genre text
    , IMDBrating text)''')
    DB.commit()
    DB.close()

command = str(input("Enter 1 to view all records \nEnter 2 to specific search data \nEnter 3 to general search data\nEnter 4 to update data\nEnter 5 to delete a field \nEnter 6 to enter data\n"))
DB = sqlite3.connect("DB.db")
c = DB.cursor()

def searchDB():
    print("Search by what?")
    for x in range(len(fieldTuple)):
        print(f"Enter {x} for {fieldTuple[x]}")
    searchField = int(input())
    search = input("Search for what \n")
    return searchField, search



fieldTuple = ("filmName","date","genre","IMDBrating")
if command == "1":
    c.execute('''SELECT * FROM collection''')

elif command == "2":
    searchCriteria = searchDB()
    c.execute(f'''SELECT * FROM collection WHERE {str(fieldTuple[searchCriteria[0]])} = "{searchCriteria[1]}"''')

elif command == "3":
    print("Search by what?")
    for x in range(len(fieldTuple)):
        print(f"Enter {x} for {fieldTuple[x]}")
    searchField = int(input())
    search = input("Search for what \n")
    c.execute(f'''SELECT * FROM collection WHERE {str(fieldTuple[searchField])} LIKE "%{search}%"''')

elif command == "4":
    print("What feild should be updated?")
    for x in range(len(fieldTuple)):
        print(f"Enter {x} for {fieldTuple[x]}")
    updateField = int(input())
    
    print("What should be entered instead")
    update = input()
    
    print("Criteria: When")
    for y in range(len(fieldTuple)):
        print(f"Enter {y} for {fieldTuple[y]}")
    searchField = int(input())
    search = input(F"{fieldTuple[y]} is equal to\n")
    c.execute(F'''UPDATE {fieldTuple[updateField]} SET "{update}" WHERE {fieldTuple[searchField]} = "{search}"''')

elif command == "5":
    print("delete when")
    for y in range(len(fieldTuple)):
        print(f"Enter {y} for {fieldTuple[y]}")
    searchField = int(input())
    search = input(F"{fieldTuple[y]} is equal to\n")
    c.execute(F'''DELETE FROM collection WHERE {fieldTuple[searchField]} = "{search}"''')
    pass

elif command == "6":
    while input("do you want to enter a record? (y/n) \t").lower() == "y":
        filmName = input("filmName \t").lower()
        date = input("date \t\t").lower()
        genre = input("genre \t\t").lower()
        IMDBrating = input("IMDBrating \t").lower()
        c.execute(f'''INSERT INTO collection VALUES ("{filmName}","{date}","{genre}","{IMDBrating}")''')
        DB.commit()
    DB.close()





else:
    print("invalid input")
    DB.commit()
    DB.close()
try:    
    row = c.fetchall()
    nameSpaceValue = 0
    genreSpaceValue = 0
    for x in range(len(row)):
        for y in range(len(row[x])):
            if len(row[x][0]) > nameSpaceValue:
                nameSpaceValue = len(row[x][0])
            if len(row[x][2]) > genreSpaceValue:
                genreSpaceValue = len(row[x][2])
    nameSpaceValue +=2
    genreSpaceValue += 2

    for x in range(len(row)):
        nameSpace = " "*(nameSpaceValue-len(row[x][0]))
        genreSpace = " "*(genreSpaceValue-len(row[x][0]))
        print(F"¦{row[x][0]}{nameSpace} ¦ {row[x][1]}{genreSpace} ¦ {row[x][2]} ¦ {row[x][3]}")

    DB.commit()
    DB.close()
    input()
except:
    print("Done")
