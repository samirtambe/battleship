# BattleShip
A command prompt battleship game.

By Samir Tambe

License: MIT License

## How to Run
### Windows
In the command prompt, type `py BattleShip.py` OR `python BattleShip.py` and press ENTER

### Mac OS X or Linux
In the terminal window type `python BattleShip.py` OR `python3 BattleShip.py` and press RETURN or ENTER.

There is also the option to run this script as an executable where you can change the permissions of the the
`BattleShip.py` file.

## How to play
This is a simplified version of battleship so one whole ship is on a coordinate pair (ROW, COLUMN).  If a coordinate
pair is specified and a ship is at that coordinate pair, then the ship is hit and sinks.

Enter the coordinates as ROW,COLUMN.  If you hit a ship on the PC's board (not visible) then it will indicate a hit.

If the PC hits one of your ships, it will indicate it on your board as you can see your own board.

You can stick to the defaults or you can change the size of the board and/or the number of ships on the board.

## Alter Parameters
The default board size is 4 x 4 with 1 ship.  The board size will always be a rectangle.

Changes apply to both user and PC.

To change the board size and number here are some examples of how to perform this:

`py BattleShip.py size=9 ships=17` : Board size changes to 9 rows & 9 columns with 17 ships
`py BattleShip.py  ships=5` : Keep default board size of 4 rows & 4 colmns, but the number of ships changes to 5
`py BattleShip.py size=11` : Keep default 1 ship, but board size changes to 11 rows and 11 columns
