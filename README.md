# BattleShip

## Overview
A command prompt battleship game.  User can specify the number of ships and the board size.  You play against the PC.

By Samir Tambe

License: MIT License

## How to Run
### On Windows
In the command prompt, type `py BattleShip.py` OR `python BattleShip.py` and press ENTER

### Mac OS X or linux
In the terminal window type `python BattleShip.py` OR `python3 BattleShip.py` and press RETURN or ENTER.

There is also the option to run this script as an executable where you can change the permissions of the the
`BattleShip.py` file.

## How to play
This is a simplified version of battleship so one whole ship is on a coordinate pair (ROW, COLUMN).  If a coordinate
pair is specified and a ship is at that coordinate pair, then the ship is hit and sinks.

Enter the coordinates as ROW,COLUMN.  If you hit a ship on the PC's board (not visible) then it will indicate a hit.

If the PC hits one of your ships, it will indicate it on your board as you can see your own board.

You can stick to the defaults or you can change the size of the board and/or the number of ships on the board.