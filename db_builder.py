# creates tables for database stored in DB_FILE: blogs.db
# field names created; no records
import sqlite3   #enable control of an sqlite database

DB_FILE="blogs.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()

def createTable(tableName, fieldNames):
	'''creates new table with list of parameters to be taken in'''
              #facilitate db ops
	commandArgs = "("
	colTypes = []
	for name in fieldNames:
		commandArgs += name + " " + fieldNames[name] + ","
		colTypes.append(fieldNames[name])
	commandArgs = commandArgs[:-1]
	# print(colTypes)
	commandArgs += ")"
	# print ("CREATE TABLE " + tableName + " "+ commandArgs)
	c.execute("CREATE TABLE " + tableName + " "+ commandArgs)

def closeDB():
	db.commit() #save changes
	db.close()  #close database

usersHeader = {"UserID":"INTEGER PRIMARY KEY","PFP":"TEXT","Username":"TEXT UNIQUE", "Password":"TEXT", "LikedPosts" : "TEXT"}
createTable("users", usersHeader)

postsHeader = {"PostID": "INTEGER PRIMARY KEY", "BlogId": "INTEGER", "AuthorID": "INTEGER", "Content":"TEXT", "Timestamp":"DATETIME", "VOTES":"INTEGER", "Heading":"TEXT"}
createTable( "posts", postsHeader)

blogsHeader = {"BlogID":"INTEGER PRIMARY KEY", "OwnerID":"INTEGER", "CollaboratorIDs":"TEXT","BlogTitle":"TEXT", "BlogDes":"TEXT","Category":"TEXT"}
createTable("blogs", blogsHeader)

closeDB()
