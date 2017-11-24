from tkinter import *
from tkinter import messagebox
import random
import drawframe #for create frame
from userDataBase import * #for score database
 
selector = 0 #by default selector is set to zero
gridButtons = {} #creating an empty dictionary of 'gridButtons'
#dictionary 'trackGridPressed' to check all 9 grids is pressed or not. set default as 'False'.
trackGridPressed= {'grid1':False,'grid2':False,'grid3':False,'grid4':False,'grid5':False,'grid6':False,'grid7':False,'grid8':False,'grid9':False}
icons = {} #creating an empty dictonary of 'icons'
#dictionary 'player' for storing each palyer name score and selector. default for score and selector is 0.
player = {'player1':{'id':'','name':'','score':0,'selector':0},'player2':{'id':'','name':'','score':0,'selector':0}}
playerTitle = {} #creating an empty dictionay of 'playerTitle'
 
#function 'center'
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() # width of system screen value
    h = toplevel.winfo_screenheight()# height of system screen value
    
    print("w",w)
    print("h",h)
 
    print("******* WIndow *****",toplevel.geometry())
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))#tk() window object height and width
    print(size)
    x = w/2 - size[0]/2 # calculate value to display window from x axis
    y = h/2 - size[1]/2 # calculate value to display window from y axis
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y))) # Center window position
#function frame    
def frame(player1,player2):
    global selector,gridButtons,icons
   
    player.get('player1')['name'] = player1
    player.get('player2')['name'] = player2
   
    window = Tk()
    window.minsize(width=450, height=550)#setting maximum and minimum height and width for this window
    window.maxsize(width=450, height=550)
    window.title('Tic Tac Toe') #setting title text of main 'window'
    mainTitleText = StringVar() #creating a 'stringVar'
    mainTitleText.set('Welcome!') #setting a text message for this 'stringVar'
    mainTitle = Label(window, text = mainTitleText.get()) #set a Label for the variable
    mainTitle.grid(row = 0, column = 1) #set position for this text message
 
    # Some Variables
    playerName = StringVar() #setting player's name as stringVar();
    player1scoreText = 0 #setting default playerscore with 0
    player2scoreText = 0
   
    #setting icon images to icons dictionary to be used for the game. a default image of white picture
    #a picture to display cross(X) symbol; a picture to display zero(o) symbol is bein uploaded.
    default = PhotoImage(file = 'default.gif')
    xIcon = PhotoImage(file = 'cross.png') #width = 145, height = 155
    oIcon = PhotoImage(file = 'circle.png')
    icons = {'xIcon':xIcon , 'oIcon':oIcon, 'default':default} #updating empty dictionay 'icons'
   
    #Grid Buttons For Tic Tac Toe, with white background
    #Grid Buttons having default image as default.gif and width as 145 and height as 150 then after creating grid object setting  the grid object to gridButtons dict
    #OnClick of grid button call gridPressed function with pass key (e.g 'grid1','grid2'), grid object , icons and window object
    #We need to create 9 grid buttons
    grid1 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid1',grid1,icons,window))
    grid1.grid(row=1, column = 0)
    grid1.config(image = default, width = '145', height = '150')
    gridButtons['grid1'] = grid1
   
    grid2 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid2',grid2,icons,window))
    grid2.grid(row=1, column = 1)
    grid2.config(image = default, width = '145', height = '150')
    gridButtons['grid2'] = grid2
 
    grid3 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid3',grid3,icons,window))
    grid3.grid(row=1, column = 2)
    grid3.config(image = default, width = '145', height = '150')
    gridButtons['grid3'] = grid3
 
    grid4 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid4',grid4,icons,window))
    grid4.grid(row=2, column = 0)
    grid4.config(image = default, width = '145', height = '150')
    gridButtons['grid4'] = grid4
 
    grid5 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid5',grid5,icons,window))
    grid5.grid(row=2, column = 1)
    grid5.config(image = default, width = '145', height = '150')
    gridButtons['grid5'] = grid5
   
  
    grid6 = Button(window, state = NORMAL, bg="white", command = lambda: gridPressed('grid6',grid6,icons,window))
    grid6.grid(row=2, column = 2)
    grid6.config(image = default, width = '145', height = '150')
    gridButtons['grid6'] = grid6
 
    grid7 = Button(window, state = NORMAL,bg="white", command = lambda: gridPressed('grid7',grid7,icons,window))
    grid7.grid(row=3, column = 0)
    grid7.config(image = default, width = '145', height = '150')
    gridButtons['grid7'] = grid7
 
    grid8 = Button(window, state = NORMAL,bg="white", command = lambda: gridPressed('grid8',grid8,icons,window))
    grid8.grid(row=3, column = 1)
    grid8.config(image = default, width = '145', height = '150')
    gridButtons['grid8'] = grid8
 
    grid9 = Button(window, state = NORMAL,bg="white", command = lambda: gridPressed('grid9',grid9,icons,window))
    grid9.grid(row=3, column = 2)
    grid9.config(image = default, width = '145', height = '150')
    gridButtons['grid9'] = grid9
 
    selector = firstPlayer()
    player.get('player1')['selector'] = selector #update player dictionary with player1 selector value
    title = Label(window, text = player.get('player1')['name']+"'s Turn!") #set the title label with this text.
    title.grid(row = 0, column = 1) #setting size and position with 'grid()'
    playerTitle["title"] = title #update dictionary 'playerTitle'
   
    resetNewGame = Button(window, state = NORMAL,text ="Start New Game", command = lambda: newGame(window,resetNewGame))
    resetNewGame.grid(row = 5, column = 1)
    
    if(selector == 0): #ceck condition for 'player2' selector.
        player.get('player2')['selector'] = 1
       
    #showing player 1 name in the window left hand corner at bottom
    playerName.set(player1)
    playe1Info = Label(window, text = playerName.get())
    playe1Info.grid(row = 4, column = 0) #position for player1 name
   
    #showing player 1 Score Label and score below to player 1 name
    score = Label(window, text = 'Score: {}'.format(player1scoreText))
    score.grid(row = 5, column = 0) #position for player1 score display
   
    #showing player 2 name in the window right hand corner at bottom
    playerName.set(player2)
    playe2Info = Label(window, text = playerName.get())
    playe2Info.grid(row = 4, column = 2) #position for player2 name
   
    #showing player 2 Score Label and score below to player 2 name
    score = Label(window, text = 'Score: {}'.format(player2scoreText))
    score.grid(row = 5, column = 2) #position for player2 score display
    player.get('player1')['id'] = insertScore(player1, player1scoreText) #it will generate a id by calling databse, according to the id score will be updated.
    player.get('player2')['id']= insertScore(player2, player2scoreText)
    print(player)# for testing
 
    createMenuItems(window,resetNewGame)   
    center(window)
    window.mainloop()
   
#function 'firstPlayer'; it will randomly choose th first player.
def firstPlayer():
        iconSelector = random.randint(0,1) #generating random number 0 and 1.
        if iconSelector == 0:
            return 0 #0 means the player1 will go first
        else:
            return 1 #1 means the player2 will go first
#function 'gridPressed'. parameter 'gridkey','grid','icons','window' 
def gridPressed(gridKey,grid,icons,window):
       
        global selector,gridButtons
       
        #If grid button not pressed before then it will allow to update values
        if(not trackGridPressed[gridKey]):
           
            playerTitle["title"].destroy() #destroy the old one
            trackGridPressed[gridKey] = True #update trackGridPressed to True it will update only once
           
            #based on selector update player's trun next after grid pressed.position and title is created
            if(selector == player.get('player1')['selector']):
                title = Label(window, text = player.get('player2')['name']+"'s Turn!")
                title.grid(row = 0, column = 1)
            elif(selector == player.get('player2')['selector']):
                title = Label(window, text = player.get('player1')['name']+"'s Turn!")
                title.grid(row = 0, column = 1)
           
            if selector == 1: #condition for 'xIcon' image selection
                grid.config(image = icons['xIcon'], text = 'x') #grid will be filled with that image
            elif selector == 0: #condition for 'oIcon' image selection
                grid.config(image = icons['oIcon'], text = 'o') #grid will be filled with that image
           
            gridButtons[gridKey] = grid #update gridButtons
            playerTitle["title"]= title; #update playerTitle
           
            #updating window according to which player is winning.updating their score showing the winning
            #message in different message box.
            if(userWinConfig()):
                #for 'player1'
                if(selector == player.get('player1')['selector']):
                    player.get('player1')['score'] = player.get('player1')['score']+1
                    score = Label(window, text = 'Score: {}'.format(player.get('player1')['score']))
                    score.grid(row = 5, column = 0)
                    updateScore(player.get('player1')['id'], player.get('player1')['score']) #update player1 score according to that id
                    messagebox.showinfo("Winner!",player.get('player1')['name']+" Win!")
                    resetGridButtonState()
                    selector = firstPlayer()
                #for 'player2'       
                elif(selector == player.get('player2')['selector']):
                    player.get('player2')['score'] = player.get('player2')['score']+1
                    score = Label(window, text = 'Score: {}'.format(player.get('player2')['score']))
                    score.grid(row = 5, column = 2)
                    updateScore(player.get('player2')['id'], player.get('player2')['score']) #update player2 score according to that id
                    messagebox.showinfo("Winner!",player.get('player2')['name']+" Win!")
                    resetGridButtonState()
                    selector = firstPlayer()
               
            #if condition for draw is occured new messagebox will be showing this message.   
            elif(checkAllSelected()):
                messagebox.showinfo("Game Draw!","Game Draw! Try Again!")
                resetGridButtonState()
                selector = firstPlayer()
                   
            else:   #to check the 'x' and 'o' of first player according to it second player's option will change. 
                if(selector==1):
                    selector=0
                elif(selector==0):
                    selector =1
#function 'newGame'. parameter 'window','resetNewGame'                   
def newGame(window,resetNewGame):
    #resetNewGame.destroy() #destroy the old window
    resetGridButtonState()
    player.get('player1')['score'] = 0 #for new game score is set again to 0 for player1
    score = Label(window, text = 'Score: {}'.format(player.get('player1')['score']))
    score.grid(row = 5, column = 0) #position for score
    player.get('player2')['score'] = 0 #for new game score is set again to 0 for player2
    score = Label(window, text = 'Score: {}'.format(player.get('player2')['score']))
    score.grid(row = 5, column = 2) #position for score
   
    
# function 'userWinConfig'               
def userWinConfig():
    global selector,gridButtons
    print(gridButtons['grid1'].config('text'))
    if selector == 1: #winning condition for the player with image option cross 'X'
        if 'x' in gridButtons['grid1'].config('text'): #checking grid 1,2,3
            if 'x' in gridButtons['grid2'].config('text'):
                if 'x' in gridButtons['grid3'].config('text'):
                    return True
            if 'x' in gridButtons['grid4'].config('text'): #checking grid 1,4,7
                if 'x' in gridButtons['grid7'].config('text'):
                    return True
            if 'x' in gridButtons['grid5'].config('text'): #checking grid 1,5,9
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
        if 'x' in gridButtons['grid3'].config('text'): #checking grid 3,6,9
            if 'x' in gridButtons['grid6'].config('text'):
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
            if 'x' in gridButtons['grid5'].config('text'): #checking grid 3,5,7
                if 'x' in gridButtons['grid7'].config('text'):
                    return True
        if 'x' in gridButtons['grid7'].config('text'): #checking grid 7,8,9
            if 'x' in gridButtons['grid8'].config('text'):
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
        if 'x' in gridButtons['grid2'].config('text'): #checking grid 2,5,8
            if 'x' in gridButtons['grid5'].config('text'):
                if 'x' in gridButtons['grid8'].config('text'):
                    return True
        if 'x' in gridButtons['grid4'].config('text'): #checking grid 4,5,6
            if 'x' in gridButtons['grid5'].config('text'):
                if 'x' in gridButtons['grid6'].config('text'):
                    return True
 
#showing all winning combination for player with 'o' image option.
    elif selector == 0:
        if 'o' in gridButtons['grid1'].config('text'): #checking grid 1,2,3
            if 'o' in gridButtons['grid2'].config('text'):
                if 'o' in gridButtons['grid3'].config('text'):
                    return True
            if 'o' in gridButtons['grid4'].config('text'): #checking grid 1,4,7
                if 'o' in gridButtons['grid7'].config('text'):
                    return True
            if 'o' in gridButtons['grid5'].config('text'): #checking grid 1,5,9
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
        if 'o' in gridButtons['grid3'].config('text'): #checking grid 3,6,9
            if 'o' in gridButtons['grid6'].config('text'):
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
            if 'o' in gridButtons['grid5'].config('text'): #checking grid 3,5,7
                if 'o' in gridButtons['grid7'].config('text'):
                    return True
        if 'o' in gridButtons['grid7'].config('text'): #checking grid 7,8,9
            if 'o' in gridButtons['grid8'].config('text'):
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
        if 'o' in gridButtons['grid2'].config('text'): #checking grid 2,5,8
            if 'o' in gridButtons['grid5'].config('text'):
                if 'o' in gridButtons['grid8'].config('text'):
                    return True
        if 'o' in gridButtons['grid4'].config('text'): #checking grid 4,5,6
            if 'o' in gridButtons['grid5'].config('text'):
                if 'o' in gridButtons['grid6'].config('text'):
                    return True
    return False
 
#function 'checkAllSelected()' to check the status of grid is pressed or not.
def checkAllSelected():
    global trackGridPressed
    checkStatus = True #default is True
   
    for key in trackGridPressed: #for loop on dictionay
        if(trackGridPressed[key] == False):
            checkStatus = False #if condition is true update checkStatus to False
            break
       
    return checkStatus #return the value of checkStatus 
 
#Reset the grid buttons objects properties and values
def resetGridButtonState():
        global gridButtons,trackGridPressed
        
        playerTitle["title"].destroy() #destroy each time the older one
       
        for key in gridButtons: #for loop on dictionary gridButton.
            gridButtons[key].config(state = NORMAL, image = icons['default'], text = '')
            trackGridPressed[key]=False #update trackGridPressed
           
#function 'createMenuItems' to create a game menu.      
def createMenuItems(window,resetNewGame):
    menu = Menu(window)#create Menu Tkinter object
    window.config(menu=menu)#adding menu object to window config item
    filemenu = Menu(menu,tearoff=False) #crete filemenu object with menu object with tearoff=False
    menu.add_cascade(label="File", menu=filemenu) #add label to window menu and assign the filemenu object
    filemenu.add_command(label="New Game",command = lambda:StartFromBegin(window)) #add label 'New Game' to filemenu and bind with method 'StartFromBegin'
    filemenu.add_command(label="Reset Game",command = lambda:newGame(window,resetNewGame))#add label 'Reset Game' to filemenu and bind with method 'newGame'
    filemenu.add_separator()#Add separator for filemenu items
    filemenu.add_command(label="Exit", command = lambda:Exit(window))#add label 'Exit' to filemenu and bind with method 'Exit'
   
    helpmenu = Menu(menu,tearoff=False)#crete helpmenu object with menu object with tearoff=False
    menu.add_cascade(label="Help", menu=helpmenu)#add label 'Help' to window menu and assign the helpmenu object
    helpmenu.add_command(label="About...", command=About)#add label 'About' to helpmenu and bind with method 'About'
    helpmenu.add_command(label="Scores",command=TopTenScore)
#function 'StartFromBegin' it will destroy the old game window and start the game from begining   
def StartFromBegin(window):
    window.destroy()
    drawframe.mainframe() #calling mainframe to rebuild the start window
#function 'About' to show information about game.It ia set in menu 
def About():
    messagebox.showinfo("About Game","Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either opponent has three in a row or all nine squares are filled.")
#function to close the game.
def Exit(window):
    print("Exit")
    window.destroy()
#function to 'display' score  
def TopTenScore():
    scores = getTopScores() #it will call this function from 'userDataBase' module
    msg="" #empty string
    for entry in scores:
        msg=msg+str(entry)+"\n" #score messages added each time.
    print(msg)# for testing
    messagebox.showinfo("Top Scores",msg) #it will show scores in the message box
