from tkinter import *
import human, computer

# This function used to open a window in center postion of system
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Radio button to choose human or computer
def sel(root,selectOption):
    label = Label(root)
    label.pack()
    root.destroy()# To destroy old window
    nameEntryFrame(selectOption.get()) # open new window calling nameEntryFrame

# function to draw the main window
def mainframe():
    root = Tk()

    root.minsize(width=480, height=150) # setting minimum window size and max window size same to avoid resize
    root.maxsize(width=480, height=150)
    # setting the title of root;creating the label with text message,selecting the font size font type background and message color.
    root.title('Tic Tac Toe')
    label = Label(root,text = 'Welcome to Tic Tac Toe!', font = ('Comic Sans MS',30),bg = 'Green', fg = 'blue')
    label.pack()

    selectOption = StringVar() # creating a variable 'selectOption'
    selectOption.set("human") # by default setting radio button to human
    # creating Radiobutton 'R1' and 'R2' with two option according to human and computer respectively.
    # the values will be assigned to 'stringVar()'.
    R1 = Radiobutton(root, text="Play with Human", variable=selectOption, value="human",)
    R1.pack( anchor = W ) # display to west side of frame
    R2 = Radiobutton(root, text="Play with Computer", variable=selectOption, value="computer")
    R2.pack( anchor = W ) # display to west side of frame
    b=Button(root,text="Start Game",command=lambda: sel(root,selectOption)) # on clicked Start Button call "sel" function pass parameter root and selectOption
    b.pack()

    center(root) # Call center function to open window in center position
    root.mainloop()

# function 'nameEntryFrame' to enter players names.It will open another window.

def nameEntryFrame(val):
    root = Tk()
    root.minsize(width=350, height=150) # setting minimun and maximum height and width of this window.
    root.maxsize(width=350, height=150)
    # creating another frame with background color gray.the height and width ia being set padding  from x and y coord 10 px
    centerFrame = Frame(root, bg='gray', width=330, height=130, padx=10, pady=10)

    root.title("Tic Tac Toe") # setting the title of this window.
    # creating first Label with text message. position and size was set by 'grid()'
    L0 = Label(centerFrame,text="Please enter player(s) name below:-")
    L0.grid(row=1,column=2,columnspan=8,rowspan=3)
    # creating 2nd Label with text message.position and size is set by 'grid()'
    L1 = Label(centerFrame, text="Player 1 Name: ")
    L1.grid(row=4,column=2)
    E1 = Entry(centerFrame, bd =5) # Input box for player 1 name
    E1.grid(row=4,column=3,columnspan=4) # position and size of this input box  is set by 'grid()'
    # creating 3rd Label with text message.
    L2 = Label(centerFrame, text="Player 2 Name: ")
    E2 = Entry(centerFrame, bd =5)# Input box for player 2 name

    if(val == "human"):# Only display E2 and L2 when human option choosen,in case of computer playing it will be invalid.
        L2.grid(row=5,column=2) # position and size of this input box
        E2.grid(row=5,column=3,columnspan=4) # position and size of this input box is set by 'grid()'

    # call startGame function with current tk() object , option value, Input elements as parameters on click of button "Start Game Now!"
    b = Button(centerFrame, text="Start Game Now!", command=lambda: startGame(root, val, E1.get(), E2.get()))
    b.grid(row=7, column=3, rowspan=3, columnspan=2) # position and size of this button  is set by 'grid()'
    centerFrame.grid(row=2,column=2, sticky="nsew") # Display the frame
    center(root) # calling function 'center'
    root.mainloop()

# function 'startGame' with parameter 'root','val','player1','player2'
def startGame(root,val,player1,player2):
    root.destroy() # to destroy old window
    if(val == "human"): # checking 'val' with 'human' to call function 'frame' from human module.
        human.frame(player1,player2)
    elif(val == "computer"): # checking 'val' with 'computer' to call function 'frame' from computer module
        computer.frame(player1,"Computer")
