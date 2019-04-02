# TicTacToe
## Set Up:
- Software used: Python 3.6 available from pydev.org
- IDE: Eclipse -Version: Oxygen.1a Release (4.7.1a)
- DataBase: Sqlite3
## **Project Description**

Team project python developing a tic-tac-toe game with python tkinter. In this game we have created both option for computer and human player.To start a game we need to run game.py module.In drawFrame.py module we have generated a small window with tictactoe welcome message and playing option for human and computer with Tkinter label , radio button, button etc. After selecting of any of this option a next frame will be opened with player's name options.In human playing option there are two label, grid for player one and player two. For computer playing option there is one label, grid for player one. After each selection old windows will be destroyed.

According to the selction human.py or computer.py module will be called. In this sections a new window will be created with 9 grids. grids default image is selected in white(which is uploaded as (default.png / default.gif). 

In human.py module players will press the grids with 'x' or 'o' icons(cross.png ,circle.png is uploaded) for playing. A dictionary will track the grids is pressed or not. default value is false. Selection of icons will be random. Players' names and score will be displayed in bottom of this window (left hand and right hand). A menu button is created to start from begining , restart the game and exit. Score database will be displayed after clicking scores in help options. To check users win option a function userWinConfig'()' is used. It will check all possible options for winning combination starting from (1,2,3),(1,4,7),(1,5,9)and so on. Based on this it will select winner and update score. The main idea of this function is taken from:- https://github.com/rdespoiu/tkinter-TicTacToe.

In computer.py module there will be a human player and computer player. The idea of window, menu, grids, frames is taken from human.py.For building computer playing strategy we have implemented rules strategy. Initially computer will choice grids randomly. If human player's score is greater than two it will call function rulestrategy. In rule strategy based on the score it will call checkSimpleStrategy() and checkAdvanceStrategy(). In simple strategy computer will block the human player for a single time. In advanced strategy computer will check all possible nested way to block user.If the human score is greater than 5 advanced stategy will be called. Computer will check its winning combination first and if find any it will press the grid other wise it will block user. Function userWinConfig'()' is used to verify the winning combination for human player and computer.

Module 'userDataBase.py' is created to generate a small table of score with player name , id , score , date time. 'Sqlite3' is used for this program. this module is imported in human.py and computer.py to update score according to id. For different player id will be auto incremented and generate automatically.

## NOTE: 
All image files (default.png,default.gif,cross.png,circle.png) should be in same location with the all .py files otherwise it will throw an exception.

##### Screen 1:-
<img width="364" alt="tic1" src="https://user-images.githubusercontent.com/31170781/33223547-7a47ab72-d12e-11e7-867d-e9429d5dc244.PNG">

##### Screen 2:-
<img width="275" alt="tic2" src="https://user-images.githubusercontent.com/31170781/33223548-7a5472b2-d12e-11e7-9b3d-17b11bff9185.PNG">

##### Screen 3:-
<img width="278" alt="tic3" src="https://user-images.githubusercontent.com/31170781/33223549-7a5fdc4c-d12e-11e7-8769-ca5a7b979fe9.PNG">

##### Screen 4:-
<img width="349" alt="tic4" src="https://user-images.githubusercontent.com/31170781/33223550-7a6c189a-d12e-11e7-9b99-5753817b1fe9.PNG">

##### Screen 5:-

<img width="559" alt="tic5" src="https://user-images.githubusercontent.com/31170781/33223551-7a792422-d12e-11e7-817b-1eff525cffb2.png">

##### Screen 6:-

<img width="344" alt="tic6" src="https://user-images.githubusercontent.com/31170781/33223552-7a8587a8-d12e-11e7-8675-ce4db53f2165.PNG">
