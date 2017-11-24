#this is using to run the game by importing 'drawframe' module.
import drawframe
from userDataBase import createDbAndTable
class ticTacToe:
    def __init__(self):
        createDbAndTable()
        drawframe.mainframe() #calling mainframe() to create first window.
           
ticTacToe()
