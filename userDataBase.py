import sqlite3 #for creating database
#function to create database
def createDbAndTable():
    conn = sqlite3.connect("tictactoe.db") #open database for game
    print("Opened database successfully") #for testing
    
    #conn.execute('''DROP TABLE TIC_TAC_SCORES''')
    #table with id, player name, score, date time wil be created
    conn.execute('''CREATE TABLE IF NOT EXISTS TIC_TAC_SCORES
             (ID INTEGER  PRIMARY KEY     AUTOINCREMENT,
             NAME           TEXT    NOT NULL,
             SCORE            INT     NOT NULL,
             scoredate  DATETIME DEFAULT CURRENT_TIMESTAMP);''')
    
    print("Table created successfully")
    conn.close()
#function to insert score; parameter 'name','score'
def insertScore(name,score):
    conn = sqlite3.connect('tictactoe.db') #open database
    print("Opened database successfully")

    cursor = conn.execute("INSERT INTO TIC_TAC_SCORES (NAME,SCORE) \
      VALUES (?,?)",(name,score)) #insert name and score in the database
    
    print(cursor.lastrowid) #for testing
    conn.commit() #commit it
    print("Records created successfully")
    conn.close()
    return cursor.lastrowid #return the generated id. score will be added according to the id
# function 'updateScore'; parameter 'userId','score'    
def updateScore(userId,score):
    conn = sqlite3.connect('tictactoe.db') #open database
    print("Opened database successfully")
    
    sql = ''' UPDATE TIC_TAC_SCORES SET SCORE = ? WHERE id = ?''' #query to update score in a id
    cur = conn.cursor() 
    cur.execute(sql, (score,userId)) #execute the query
     
    conn.commit() #commit it
    print("Records update successfully for user "+str(userId)+" and updated score "+str(score))
    
    conn.close()
#function 'getTopScores'    
def getTopScores():
    conn = sqlite3.connect('tictactoe.db') #open database
    print("Opened database successfully")
    scoreData=[] #empty list
    #top 20 score will be showing in descending order in the database
    cursor = conn.execute("SELECT name, SCORE, scoredate from TIC_TAC_SCORES ORDER BY SCORE desc LIMIT 20")
    for row in cursor:
        #print(row)
        scoreData.append(row) #scoredata is appended row wise to display all player's score.
        """print("ID = ", row[0])
        print("NAME = ", row[1])
        print("SCORE = ", row[2], "\n")"""
    
    conn.close()
    print(scoreData)
    return scoreData #return scoreData

#updateScore(7,99)
#getTopScores()

