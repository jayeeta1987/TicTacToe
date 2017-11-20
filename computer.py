from tkinter import *
from tkinter import messagebox
import random
import drawframe

selector = 0 #by default selector is set to zero
gridButtons = {} #creating an empty dictionary of 'gridButtons'
#dictionary 'trackGridPressed' to check all 9 grids is pressed or not. set default as 'False'.
trackGridPressed= {'grid1':False,'grid2':False,'grid3':False,'grid4':False,'grid5':False,'grid6':False,'grid7':False,'grid8':False,'grid9':False}
icons = {} #creating an empty dictonary of 'icons'
#dictionary 'player' for storing each palyer name score and selector. default for score and selector is 0.
player = {'player1':{'name':'','score':0,'selector':0},'player2':{'name':'','score':0,'selector':0}}
playerTitle = {} #creating an empty dictionay of 'playerTitle'

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
    title = Label(window, text = player.get('player1')['name']+"'s Turn!") #set the title label with this text
    title.grid(row = 0, column = 1) #setting size and position with 'grid()'
    playerTitle["title"] = title #update dictionary 'playerTitle'
    
    resetNewGame = Button(window, state = NORMAL,text ="Start New Game", command = lambda: newGame(window,resetNewGame))
    resetNewGame.grid(row = 5, column = 1) 
    
    if(selector == 0): #ceck condition for 'player2' selector.
        player.get('player2')['selector'] = 1
        
    #showing player 1 name in the window left hand corner at bottom
    playerName.set(player1)
    playe1Info = Label(window, text = playerName.get())
    playe1Info.grid(row = 4, column = 0)  #position for player1 name
    
    #showing player 1 Score Label and score below to player 1 name
    score = Label(window, text = 'Score: {}'.format(player1scoreText))
    score.grid(row = 5, column = 0) #position for player1 score display
    #showing computer's position in the window right hand corner at bottom
    playerName.set(player2)
    playe2Info = Label(window, text = playerName.get())
    playe2Info.grid(row = 4, column = 2)
    
    #computer's score position
    score = Label(window, text = 'Score: {}'.format(player2scoreText))
    score.grid(row = 5, column = 2)
    createMenuItems(window,resetNewGame)    
    center(window) #calling center to open the game window in middle of system screen
    window.mainloop()

#function 'firstPlayer'; it will randomly choose th first player.
def firstPlayer():
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            return 0 #0 means the computer will go first
        else:
            return 1 #1 means the player will go first

#function 'gridPressed'. parameter 'gridkey','grid','icons','window'     
def gridPressed(gridKey,grid,icons,window):
    
        global selector,gridButtons
    #If grid button not pressed before then it will allow to update values 
        if(not trackGridPressed[gridKey]):
            playerTitle["title"].destroy()  #destroy the old one
            trackGridPressed[gridKey] = True #update trackGridPressed to True it will update only once
            
            title = Label(window, text = player.get('player2')['name']+"'s Turn!")
            title.grid(row = 0, column = 1) #position for player's turn message 
            
            if selector == 1: #condition for 'xIcon' image selection
                grid.config(image = icons['xIcon'], text = 'x') #grid will be filled with that image
            elif selector == 0:   #condition for 'oIcon' image selection
                grid.config(image = icons['oIcon'], text = 'o')  #grid will be filled with that image
            
            gridButtons[gridKey] = grid #update gridButtons
            playerTitle["title"]= title #update playerTitle
            #if human wins the game the new message box score winning message will be updated with following code.
            if(userWinConfig()):
                print("Human Win!")
                player.get('player1')['score'] = player.get('player1')['score']+1
                score = Label(window, text = 'Score: {}'.format(player.get('player1')['score']))
                score.grid(row = 5, column = 0)
                messagebox.showinfo("Winner!",player.get('player1')['name']+" Win!")
                resetGridButtonState()
                selector = firstPlayer()
            elif(checkAllSelected()): #if game draw update the message box information by following code
                messagebox.showinfo("Game Draw!","Game Draw! Try Again!")
                resetGridButtonState()
                selector = firstPlayer()
            else: #to check the 'x' and 'o' option for human according to computers options will be changed
                if(selector==1):
                    selector=0
                elif(selector==0):
                    selector =1
                computerTurn(window,player.get('player1')['score']) #basis human player's score computer will develop the strategy. 
#function 'computerTurn'; parameter 'window','score'; (score of humnan )
def computerTurn(window,score):
    global selector,trackGridPressed,gridButtons
    
    d = {k: v for k, v in trackGridPressed.items() if v == False} #get the values which are avialabe for AI
    print(d)
    randomKey = random.choice(list(d)) #random grid choice for computer initially
    print(randomKey)
    
    if(score > 2):
        key = ruleStrategy(score) #based on this score of human it will call rulestrategy
        
        if(key == "nothing match"): #if nothing match with our strategy of human position it will return random
            key = randomKey         #like 4th grid  and 9th grid is occupied by human 
    else:
        key = randomKey #if human score is less than 2 computer will return random position only.
            
    trackGridPressed[key] = True
    print("key",key)
    if selector == 1: #condition for 'x' icon selection
        gridButtons[key].config(image = icons['xIcon'], text = 'x')   
    elif selector == 0:  #condition for 'y' icon selection
        gridButtons[key].config(image = icons['oIcon'], text = 'o')
        
    playerTitle["title"].destroy()# destroy the old title.
    
    title = Label(window, text = player.get('player1')['name']+"'s Turn!")
    title.grid(row = 0, column = 1) #position for computer turn's message
    
    playerTitle["title"]= title #update the palyer title.
    
    if(userWinConfig()): #if computer wins it will update the messagebox with wiining message. label,score will be updated also.
        print("computer win!")
        player.get('player2')['score'] = player.get('player2')['score']+1
        score = Label(window, text = 'Score: {}'.format(player.get('player2')['score']))
        score.grid(row = 5, column = 2) #set position
        messagebox.showinfo("Winner!",player.get('player2')['name']+" Win!")
        resetGridButtonState()
        selector = firstPlayer()
    elif(checkAllSelected()): #if game draw update the label
        label = Label(window,text = "Game Draw!", font = ('Comic Sans MS',10),bg = 'Red', fg = 'yellow')
        label.grid(row = 0, column = 1) #set position
        
        resetGridButtonState()
        selector = firstPlayer()
            
    else:    
        if(selector==1):
            selector=0
        elif(selector==0):
            selector =1
def ruleStrategy(score):
    checkVal='x' #variable 'checkVal'default value is set to option 'x'
    isAdvance=False #variable 'isAdvance' is used to check score status, by default is set to False
    print("Human Score:-"+str(score)) #for testing purpose
    
    if(score > 5): #if human score is more than 5 it will change value of 'setValue'
        isAdvance=True
    
    if selector == 0: #condition for option 'o'
        checkVal='o'   #value of it is changed 
    #key = checkAdvanceStrategy(checkVal)
    #according to 'checkVal' computer will check its winning combination present or not. 
    #details on function 'checkVal' 
    key = checkAdvanceStrategy(checkVal) if isAdvance else checkSimpleStrategy(checkVal)
    print("rule Str",key)
    if(key == "nothing match"): #if no winning combination for computer then it will check human's move and try to block it.
        if(checkVal=='x'):      #'o' and 'x' will be depend on selector.
            key = checkAdvanceStrategy('o') if isAdvance else checkSimpleStrategy('o') 
        else:
            key = checkAdvanceStrategy('x') if isAdvance else checkSimpleStrategy('x') 
        print("if rule Str",key)
        return key #key is reffering to that grid to block or for computer's move.
    else:
        print("else rule Str",key)
        return key #else computer will check its winning combination
#function 'checkSimpleStrategy' parameter val('o' or 'x')               
def checkSimpleStrategy(val):
    print("checkSimpleStrategy:-",val)#for testing purpose
    global gridButtons,trackGridPressed
    
    key = 'nothing match' #key is by default 'nothing match' for computer's move
    
    #all condition of winning and blocking for computer is programmed below. It will first check own 
    #winning combination and then oponent's position to block it.
    if val in gridButtons['grid1'].config('text'): #condition to check grid 1,2,3  
        print("grid1")#for testing
        if val in gridButtons['grid2'].config('text'):
            if(trackGridPressed['grid3'] == False): 
                key='grid3'
        elif val in gridButtons['grid4'].config('text'): #condition to check grid 1,4,7
            if(trackGridPressed['grid7'] == False):
                key='grid7'
        elif val in gridButtons['grid5'].config('text'): #condition to check grid 1,5,9
            if(trackGridPressed['grid9'] == False):
                key='grid9'
        elif val in gridButtons['grid3'].config('text'): #condition to check grid 1,3,2
            if(trackGridPressed['grid2'] == False):
                key='grid2'
        elif val in gridButtons['grid7'].config('text'): #condition to check grid 1,7,4
            if(trackGridPressed['grid4'] == False):
                key='grid4'
        elif val in gridButtons['grid9'].config('text'): #condition to check grid 1,9,5
            if(trackGridPressed['grid5'] == False):
                key='grid5'
    elif val in gridButtons['grid2'].config('text'): #condition to check grid 2,3,1
        print("grid2") #for testing
        if val in gridButtons['grid3'].config('text'):
            if(trackGridPressed['grid1'] == False):
                key='grid1'
        elif val in gridButtons['grid5'].config('text'): #condition to check grid 2,5,8
            if(trackGridPressed['grid8'] == False):
                key='grid8'
        elif val in gridButtons['grid8'].config('text'): #condition to check grid 2,8,5
            if(trackGridPressed['grid5'] == False):
                key='grid5'
                   
    elif val in gridButtons['grid3'].config('text'): #condition to check grid 3,6,9
        print("grid3")
        if val in gridButtons['grid6'].config('text'):
            if(trackGridPressed['grid9'] == False):
                key='grid9'
        elif val in gridButtons['grid5'].config('text'): #condition to check grid 3,5,7
            if(trackGridPressed['grid7'] == False):
                key='grid7'
        elif val in gridButtons['grid7'].config('text'): #condition to check grid 3,7,5
            if(trackGridPressed['grid5'] == False):
                key='grid5'
        elif val in gridButtons['grid9'].config('text'): #condition to check grid 3,9,6
            if(trackGridPressed['grid6'] == False):
                key='grid6'
    elif val in gridButtons['grid4'].config('text'): #condition to check grid 4,5,6
        print("grid4")
        if val in gridButtons['grid5'].config('text'):
            if(trackGridPressed['grid6'] == False):
                key='grid6'
        elif val in gridButtons['grid6'].config('text'): #condition to check grid 4,6,5
            if(trackGridPressed['grid5'] == False):
                key='grid5'
        elif val in gridButtons['grid7'].config('text'): #condition to check grid 4,7,1
            if(trackGridPressed['grid1'] == False):
                key='grid1'

    elif val in gridButtons['grid5'].config('text'): #condition to check grid 5,6,4
        print("grid5")
        if val in gridButtons['grid6'].config('text'):
            if(trackGridPressed['grid4'] == False):
                key='grid4'
        elif val in gridButtons['grid7'].config('text'): #condition to check grid 5,7,3
            if(trackGridPressed['grid3'] == False):
                key='grid3'
        elif val in gridButtons['grid8'].config('text'): #condition to check grid 5,8,2
            if(trackGridPressed['grid2'] == False):
                key='grid2'
    elif val in gridButtons['grid6'].config('text'): #condition to check grid 6,9,3
        print("grid6")
        if val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid3'] == False):
                key='grid3'
    elif val in gridButtons['grid7'].config('text'): #condition to check grid 7,8,9
        print("grid7") 
        if val in gridButtons['grid8'].config('text'):
            if(trackGridPressed['grid9'] == False):
                key='grid9'
    elif val in gridButtons['grid8'].config('text'): #condition to check grid 8,9,7
        print("grid8")
        if val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid7'] == False):
                key='grid7'
    return key #return the grid according to condition for computer's move
    
#function 'checkAdvanceStrategy'; parameter val('o' and 'x' according to selector)
def checkAdvanceStrategy(val):
    print("checkAdvanceStrategy:-",val)#for testing purpose
    global gridButtons,trackGridPressed
    
    key = 'nothing match' #default value for key
    #it will check each and every possible combination for winning and blocking both.
    #if grid1 and 2 is block it will check grid 3 if it is also blocked it will check grid 1, 4 to 
    #set a move on grid 7 and so on.
    if val in gridButtons['grid1'].config('text'):
        if val in gridButtons['grid2'].config('text'):
            if(trackGridPressed['grid3'] == False):
                key='grid3' #retrun 'grid3' if only 1 & 2 is blocked.
            elif val in gridButtons['grid4'].config('text'):
                if(trackGridPressed['grid7'] == False):
                    key='grid7' #return 'grid7' if 1,2,3,4 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,4,5 is blocked
                    elif val in gridButtons['grid3'].config('text'):
                        if(trackGridPressed['grid2'] == False):
                            key='grid2' #return 'grid2'if 1,3,4,5,7,9 is blocked
                        elif val in gridButtons['grid7'].config('text'):
                            if(trackGridPressed['grid4'] == False):
                                key='grid4' #return 'grid4' if 1,2,3,5,7,9 is blocked
                            elif val in gridButtons['grid9'].config('text'):
                                if(trackGridPressed['grid5'] == False):
                                    key='grid5' #return 'grid5' if 1,2,3,4,7,9 is blocked.
                                
        elif val in gridButtons['grid4'].config('text'):
            if(trackGridPressed['grid7'] == False):
                key='grid7' #retun 'grid7' if 1 & 4 is blocked
            elif val in gridButtons['grid2'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 1,2,4,7 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,4,5,7 is blocked
                    elif val in gridButtons['grid3'].config('text'):
                        if(trackGridPressed['grid2'] == False):
                            key='grid2' #return 'grid2' if 1,3,4,5,7,9 is blocked
                        elif val in gridButtons['grid7'].config('text'):
                            if(trackGridPressed['grid4'] == False):
                                key='grid4' #return 'grid4' if 1,2,3,5,7,9 is blocked
                            elif val in gridButtons['grid9'].config('text'):
                                if(trackGridPressed['grid5'] == False):
                                    key='grid5' #return 'grid5' if 1,2,3,7,9 is blocked
        elif val in gridButtons['grid5'].config('text'):
            if(trackGridPressed['grid9'] == False):
                key='grid9' #return 'grid9' if 1 & 5 is blocked
            elif val in gridButtons['grid2'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 1,2,5,9 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,5 is blocked
                    elif val in gridButtons['grid4'].config('text'):
                        if(trackGridPressed['grid7'] == False):
                            key='grid7' #return 'grid7' if 1,2,3,4,5,9 is blocked
                        elif val in gridButtons['grid7'].config('text'):
                            if(trackGridPressed['grid4'] == False):
                                key='grid4' #return 'grid4' if 1,2,3,5,7,9 is blocked
                            elif val in gridButtons['grid9'].config('text'):
                                if(trackGridPressed['grid5'] == False):
                                    key='grid5' #return 'grid5' if 1,2,3,4,7,9
        elif val in gridButtons['grid3'].config('text'):
            if(trackGridPressed['grid2'] == False):
                key='grid2' #return 'grid2' if 1 & 3 is blocked
            elif val in gridButtons['grid2'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 1,2 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,5 is blocked
                    elif val in gridButtons['grid4'].config('text'):
                        if(trackGridPressed['grid7'] == False):
                            key='grid7' #return 'grid7' if 1,2,3,4,5,9 is blocked
                        elif val in gridButtons['grid7'].config('text'):
                            if(trackGridPressed['grid4'] == False):
                                key='grid4' #return 'grid4' if 1,2,3,5,7,9 is blocked
                            elif val in gridButtons['grid9'].config('text'):
                                if(trackGridPressed['grid5'] == False):
                                    key='grid5' #return 'grid5' if 1,2,3,4,7,9 is blocked
        elif val in gridButtons['grid7'].config('text'):
            if(trackGridPressed['grid4'] == False):
                key='grid4' #return 'grid4' if 1 & 7 is blocked
            elif val in gridButtons['grid2'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 1,2,4,7 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,4,5,7 is blocked
                    elif val in gridButtons['grid4'].config('text'):
                        if(trackGridPressed['grid7'] == False):
                            key='grid7' #return 'grid7' if 1,2,3,4,5,9 is blocked
                        elif val in gridButtons['grid3'].config('text'):
                            if(trackGridPressed['grid2'] == False):
                                key='grid2' #return 'grid2' if 1,2,4,5,7,9 is blocked
                            elif val in gridButtons['grid9'].config('text'):
                                if(trackGridPressed['grid5'] == False):
                                    key='grid5' #return 'grid5' if 1,2,3,4,7,9 is blocked
        elif val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid5'] == False):
                key='grid5' #return 'grid5' if 1 & 9 is blocked
            elif val in gridButtons['grid2'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 1,2,5,9 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid9'] == False):
                        key='grid9' #return 'grid9' if 1,2,3,5 is blocked
                    elif val in gridButtons['grid4'].config('text'):
                        if(trackGridPressed['grid7'] == False):
                            key='grid7' #return 'grid7' if 1,2,3,4,5,9 is blocked
                        elif val in gridButtons['grid7'].config('text'):
                            if(trackGridPressed['grid4'] == False):
                                key='grid4' #return 'grid4' if 1,2,3,5,7,9 is blocked
                            elif val in gridButtons['grid3'].config('text'):
                                if(trackGridPressed['grid2'] == False):
                                    key='grid2' #return 'grid2' if 1,3,4,5,7,9 is blocked
    elif val in gridButtons['grid2'].config('text'):
        print("grid2")
        if val in gridButtons['grid3'].config('text'):
            if(trackGridPressed['grid1'] == False):
                key='grid1' #return 'grid1' if 2 & 3 is blocked
            elif val in gridButtons['grid5'].config('text'):
                if(trackGridPressed['grid8'] == False):
                    key='grid8' #return 'grid8' if 1,2,3,5 is blocked
                elif val in gridButtons['grid8'].config('text'):
                    if(trackGridPressed['grid5'] == False):
                        key='grid5'  #return 'grid5' if 1,2,3,8 is blocked   
        elif val in gridButtons['grid5'].config('text'):
            if(trackGridPressed['grid8'] == False):
                key='grid8' #return 'grid8' if 2 & 5 is blocked
            elif val in gridButtons['grid3'].config('text'):
                if(trackGridPressed['grid1'] == False):
                    key='grid1' #return 'grid1' if 2,3,5,8 is blocked
                elif val in gridButtons['grid8'].config('text'):
                    if(trackGridPressed['grid5'] == False):
                        key='grid5' #return 'grid5' if 1,2,3,8 is blocked
        elif val in gridButtons['grid8'].config('text'):
            if(trackGridPressed['grid5'] == False):
                key='grid5' #return 'grid5' if 2 & 8 is blocked
            elif val in gridButtons['grid3'].config('text'):
                if(trackGridPressed['grid1'] == False):
                    key='grid1' #return 'grid1' if 2,3,5,8 is blocked
            elif val in gridButtons['grid5'].config('text'):
                if(trackGridPressed['grid8'] == False):
                    key='grid8' #return 'grid8' if 1,2,3,5 is blocked
                   
    elif val in gridButtons['grid3'].config('text'):
        print("grid3")
        if val in gridButtons['grid6'].config('text'):
            if(trackGridPressed['grid9'] == False):
                key='grid9' #return 'grid9' if 3 & 6 is blocked
            elif val in gridButtons['grid5'].config('text'):
                if(trackGridPressed['grid7'] == False):
                    key='grid7' #return 'grid7' if 3,5,6,9 is blocked
                elif val in gridButtons['grid7'].config('text'):
                    if(trackGridPressed['grid5'] == False):
                        key='grid5' #return 'grid5' if 3,6,7,9 is blocked
                    elif val in gridButtons['grid9'].config('text'):
                        if(trackGridPressed['grid6'] == False):
                            key='grid6' #return 'grid6' if 3,5,6,7,9 is blocked
        elif val in gridButtons['grid5'].config('text'):
            if(trackGridPressed['grid7'] == False):
                key='grid7' #return 'grid7' if 3 & 5 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid9'] == False):
                    key='grid9' #return 'grid9' if 3,5,6,7 is blocked
                elif val in gridButtons['grid7'].config('text'):
                    if(trackGridPressed['grid5'] == False):
                        key='grid5' #return 'grid5' if 3,6,7,9 is blocked
                    elif val in gridButtons['grid9'].config('text'):
                        if(trackGridPressed['grid6'] == False):
                            key='grid6' #return 'grid6' if 3,5,7,9 is blocked
        elif val in gridButtons['grid7'].config('text'):
            if(trackGridPressed['grid5'] == False):
                key='grid5' #return 'grid5' 3 & 7 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid9'] == False):
                    key='grid9' #return 'grid9' if 3,5,6,7 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid7'] == False):
                        key='grid7' #return 'grid7' if 3,5,6,9 is blocked
                    elif val in gridButtons['grid9'].config('text'):
                        if(trackGridPressed['grid6'] == False):
                            key='grid6' #return 'grid6' if 3,5,7,9 is blocked
        elif val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid6'] == False):
                key='grid6' #return 'grid9' if 3 & 9 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid9'] == False):
                    key='grid9' #return 'grid9' if 3 & 6 is blocked
                elif val in gridButtons['grid7'].config('text'):
                    if(trackGridPressed['grid5'] == False):
                        key='grid5' #return 'grid5' if 3,6,7,9 is blocked
                    elif val in gridButtons['grid5'].config('text'):
                        if(trackGridPressed['grid7'] == False):
                            key='grid7' #return 'grid7' if 3,5,6,9 is blocked
    elif val in gridButtons['grid4'].config('text'):
        print("grid4")
        if val in gridButtons['grid5'].config('text'):
            if(trackGridPressed['grid6'] == False):
                key='grid6' #return 'grid6' if 4 & 5 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid5'] == False):
                    key='grid5' #return 'grid5' if 4 & 6 is blocked
                elif val in gridButtons['grid7'].config('text'):
                    if(trackGridPressed['grid1'] == False):
                        key='grid1' #return 'grid1' if 4,5,6,7 is blocked
        elif val in gridButtons['grid6'].config('text'):
            if(trackGridPressed['grid5'] == False):
                key='grid5' #return 'grid5' if 4 & 6 is blocked
            elif val in gridButtons['grid5'].config('text'):
                if(trackGridPressed['grid6'] == False):
                    key='grid6' #return 'grid6' if 4 & 5 is blocked
                elif val in gridButtons['grid7'].config('text'):
                    if(trackGridPressed['grid1'] == False):
                        key='grid1' #return 'grid1' if 4,5,6,7 is blocked
        elif val in gridButtons['grid7'].config('text'):
            if(trackGridPressed['grid1'] == False):
                key='grid1' #return 'grid1' if 4 & 7 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid5'] == False):
                    key='grid5' #return 'grid5' if 1,4,6,7 is blocked
                elif val in gridButtons['grid5'].config('text'):
                    if(trackGridPressed['grid6'] == False):
                        key='grid1' #return 'grid1' if 4,5,6,7 is blocked

    elif val in gridButtons['grid5'].config('text'):
        print("grid5")
        if val in gridButtons['grid6'].config('text'):
            if(trackGridPressed['grid4'] == False):
                key='grid4' #return 'grid4' if 5 & 6 is blocked
            elif val in gridButtons['grid7'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 4,5,6,7 is blocked
                elif val in gridButtons['grid8'].config('text'):
                    if(trackGridPressed['grid2'] == False):
                        key='grid2' #return 'grid2' if 3,4,5,6,7,8 is blocked
        elif val in gridButtons['grid7'].config('text'):
            if(trackGridPressed['grid3'] == False):
                key='grid3' #return 'grid3' if 5 & 7 is blocked
            elif val in gridButtons['grid6'].config('text'):
                if(trackGridPressed['grid4'] == False):
                    key='grid4' #return 'grid4' if 3,5,6,7 is blocked
                elif val in gridButtons['grid8'].config('text'):
                    if(trackGridPressed['grid2'] == False):
                        key='grid2' #return 'grid2' if 3,4,5,6,7,8 is blocked
        elif val in gridButtons['grid8'].config('text'):
            if(trackGridPressed['grid2'] == False):
                key='grid2' #return 'grid2' if 5 & 8 is blocked
            elif val in gridButtons['grid7'].config('text'):
                if(trackGridPressed['grid3'] == False):
                    key='grid3' #return 'grid3' if 2,5,7,8
                elif val in gridButtons['grid6'].config('text'):
                    if(trackGridPressed['grid4'] == False):
                        key='grid4' #return 'grid4' if 2,3,5,6,7,8
    elif val in gridButtons['grid6'].config('text'):
        print("grid6")
        if val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid3'] == False):
                key='grid3' #return 'grid3' if 6 & 9 is blocked;other possibilities is stated earlier
    elif val in gridButtons['grid7'].config('text'):
        print("grid7")
        if val in gridButtons['grid8'].config('text'):
            if(trackGridPressed['grid9'] == False):
                key='grid9' #return 'grid9' if 7 & 8 is blocked;other possibilities is stated earlier
    elif val in gridButtons['grid8'].config('text'):
        print("grid8")
        if val in gridButtons['grid9'].config('text'):
            if(trackGridPressed['grid7'] == False):
                key='grid7' #return 'grid9' if 8 & 9 is blocked;other possibilities is stated earlier
    return key
    
                 
def userWinConfig():
    global selector,gridButtons
    if selector == 1: #winning condition for the player with image option cross 'X'
        if 'x' in gridButtons['grid1'].config('text'): #checking grid 1,2,3
            if 'x' in gridButtons['grid2'].config('text'):
                if 'x' in gridButtons['grid3'].config('text'):
                    return True
            if 'x' in gridButtons['grid4'].config('text'): #checking grid 1,4,7
                if 'x' in gridButtons['grid7'].config('text'):
                    return True
            if 'x' in gridButtons['grid5'].config('text'): #checking 1,5,9
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
        if 'x' in gridButtons['grid3'].config('text'): #checking 3,6,9
            if 'x' in gridButtons['grid6'].config('text'):
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
            if 'x' in gridButtons['grid5'].config('text'): #checking 3,5,7
                if 'x' in gridButtons['grid7'].config('text'):
                    return True
        if 'x' in gridButtons['grid7'].config('text'): #checking 7,8,9
            if 'x' in gridButtons['grid8'].config('text'):
                if 'x' in gridButtons['grid9'].config('text'):
                    return True
        if 'x' in gridButtons['grid2'].config('text'): #checking 2,5,8
            if 'x' in gridButtons['grid5'].config('text'):
                if 'x' in gridButtons['grid8'].config('text'):
                    return True
        if 'x' in gridButtons['grid4'].config('text'): #checking 4,5,6
            if 'x' in gridButtons['grid5'].config('text'):
                if 'x' in gridButtons['grid6'].config('text'):
                    return True
#showing all winning combination for player with 'o' image option.
    elif selector == 0:
        if 'o' in gridButtons['grid1'].config('text'): #checking 1,2,3
            if 'o' in gridButtons['grid2'].config('text'):
                if 'o' in gridButtons['grid3'].config('text'):
                    return True
            if 'o' in gridButtons['grid4'].config('text'): #checking 1,4,7
                if 'o' in gridButtons['grid7'].config('text'):
                    return True
            if 'o' in gridButtons['grid5'].config('text'): #checking 1,5,9
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
        if 'o' in gridButtons['grid3'].config('text'): #checking 3,6,9
            if 'o' in gridButtons['grid6'].config('text'):
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
            if 'o' in gridButtons['grid5'].config('text'): #checking 3,5,7
                if 'o' in gridButtons['grid7'].config('text'):
                    return True
        if 'o' in gridButtons['grid7'].config('text'): #checking 7,8,9
            if 'o' in gridButtons['grid8'].config('text'):
                if 'o' in gridButtons['grid9'].config('text'):
                    return True
        if 'o' in gridButtons['grid2'].config('text'): #checking 2,5,8
            if 'o' in gridButtons['grid5'].config('text'):
                if 'o' in gridButtons['grid8'].config('text'):
                    return True
        if 'o' in gridButtons['grid4'].config('text'): #checking 4,5,6
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
        
        playerTitle["title"].destroy() #destroy older player title while reseeeting
        
        for key in gridButtons: #for loop on dictionary gridButton.
            gridButtons[key].config(state = NORMAL, image = icons['default'], text = '')#resetting
            trackGridPressed[key]=False #update trackGridPressed

#function 'newGame'            
def newGame(window,resetNewGame):
    #resetNewGame.destroy()
    resetGridButtonState() #calling this function to reset gridbutton
    #update player and computer's score to 0
    player.get('player1')['score'] = 0 
    score = Label(window, text = 'Score: {}'.format(player.get('player1')['score']))
    score.grid(row = 5, column = 0)
    player.get('player2')['score'] = 0
    score = Label(window, text = 'Score: {}'.format(player.get('player2')['score']))
    score.grid(row = 5, column = 2) 

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
    
    helpmenu = Menu(menu,tearoff=False)#create helpmenu object with menu object with tearoff=False
    menu.add_cascade(label="Help", menu=helpmenu)#add label 'Help' to window menu and assign the helpmenu object
    helpmenu.add_command(label="About...", command=About)#add label 'About' to helpmenu and bind with method 'About'

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