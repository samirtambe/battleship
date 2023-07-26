from random import randint
import os
import time
import sys

class cpuplayer:
    #coordinate for each ship
    shiplocations = []

    #coordinates that have been tried against the oponent
    previouslytried = []
    #ships
    #size
    #guess

    def __init__(self, size, ships):
        self.size = size
        self.ships = ships

        #Create Fleet
        cnt = self.ships
        while cnt > 0:

            # Generate random coordinates for the ships
            r = randint(0,self.size -1)
            c = randint(0,self.size -1)

            #if coordinate set is not selected, then add to our list
            if (r,c) not in self.shiplocations:
                
                self.shiplocations.append((r,c))
                cnt -= 1
            else:
                continue
        #print(f"CPU {self.shiplocations} - ADD 1 to each value")
        
    def aim(self):
        #print(f"DEBUG: {self.previouslytried=}")
        while True:
            #generate random coordinates to aim
            randomrow = randint(0, self.size - 1)
            randomcol = randint(0, self.size - 1)

            #don't aim at the same location more than once
            if (randomrow,randomcol) not in self.previouslytried:
                print('PC Aims:', randomrow + 1, ',', randomcol + 1)
                self.previouslytried.append((randomrow,randomcol))
                self.guess = (randomrow,randomcol)
                break
            else:
                #if for this iteration the coordinates were already in 
                #ship locations list, then try again
                continue

    def hit_target(self, targetlocations):
        #did i get what i was aiming for
        if self.guess in targetlocations: 
            print(f"DIRECT HIT!!!")
            return True
        else: 
            return False

class humanplayer:
    square = '~~~~'
    missedsymbol = '....'
    shipsymbol = 'SHIP'
    hitsymbol = '####'
    shiplocations = []
    #ships
    #size
    #guess

    def __init__(self, size, ships):
        self.size = size
        self.ships = ships
        self.area = [[self.square for col in range(0, self.size)] for row in range(0, self.size)]

    #createfleet
        cnt = self.ships
        while cnt > 0:
            # generate random coordinates
            r = randint(0,self.size -1)
            c = randint(0,self.size -1)

            #only add to our list if it has not been used
            if (r,c) not in self.shiplocations:
                
                self.shiplocations.append((r,c))
                cnt -= 1
            else:
                continue

    #place ships on user board
        for row,col in self.shiplocations:
            self.area[row][col] = self.shipsymbol
    
    #update play area to indicate a hit
    def indicatehit(self, aim):
        self.area[aim[0]][aim[1]] = self.hitsymbol

    #update play area to indicate a miss
    def indicatemiss(self,aim):
        self.area[aim[0]][aim[1]] = self.missedsymbol
    
    #show the board
    def displayboard(self):
        for nm,row in enumerate(self.area):
            for col in row:
                print(col, end ='  ')
            print()
        print()

    #did i get what i was aiming for
    def hit_target(self, targetlocations):
        if self.guess in targetlocations: 
            print(f"DIRECT HIT!!!")
            return True
        else: 
            return False

    #determine if user coordinates are correctly entered
    def parse_user_input(self):

        strui = input("Enter (Row,Col): ")

        if (len(strui) < 1):
            return [-1, -1]
        
        elif strui in ('q', 'quit', 'quit()', 'exit'):
            print('Exiting...')
            quit()
        
        try:# split on comma, and save key value pair after 
            # subtracting 1 and converting them to INTEGER (area starts from zero)
            ucoordstrlst = strui.split(',')
            prow = int(ucoordstrlst[0]) - 1
            pcol = int(ucoordstrlst[1]) - 1
        except:
            clearscreen(0)
            print("Unable to process input. Try again...")
            # MUST return value to check for errors, if any go to next iteration in loop and re-enter
            return (-1, -1)
        
        if (prow >= self.size) or (pcol >= self.size) or (prow < 0) or (pcol < 0): 
            clearscreen(0)
            print("Coordinates out of bounds - Try again...")
            # MUST return value to check for errors, if any go to next iteration in loop and re-enter
            return (-1, -1)

        # MUST return value to check for errors, if any go to next iteration in loop and re-enter
        return (prow, pcol) 


def process_user_arguments():
    
    vdict = dict()

    for argument in sys.argv:
        
        # skip the file name
        if argument.endswith('.py'):
            continue
        
        # if argument starts with size= or ships=
        elif argument.startswith('size=') or argument.startswith('ships='):
            try:
                # split argument on = symbol , assign element of list to varuables, convert 
                # 2nd element to an INTEGER and add to the dictionary
                pair = argument.split('=')
                key = pair[0]
                value = int(pair[1])
                vdict[key] = value
            except:
                print(f"Trouble splitting or converting {argument}. Exiting...")
                quit()
        else:
            print(f"Invalid {argument=}. Exiting...")
            quit()

    return vdict

def clearscreen(duration):
    time.sleep(duration)
    os.system('cls')

users_turn = True
size = 4
ships = 1

commandline_args = sys.argv

if len(commandline_args) > 1:
    params = process_user_arguments()
    if 'size' in params:
        size = params['size']
    if 'ships' in params:
        ships = params['ships']

cpuships = ships
humanships = ships

me = humanplayer(size,ships)

oponent = cpuplayer(size, ships)

while (humanships > 0) and (cpuships > 0):
    
    if users_turn is True:

        me.displayboard()

        # MUST return value to check for errors, if any go to next iteration in loop and re-enter
        me.guess = me.parse_user_input() # sets humanplayer.guess

        if me.guess == (-1, -1): continue
        
        if me.hit_target(oponent.shiplocations) is True:
            cpuships -= 1
            print(f"User HIT PC's Battleship! {cpuships=}")
        else:
            print("User Missed!\n")

        users_turn = False
        clearscreen(2)
    else:
        me.displayboard()

        oponent.aim() # sets cpuplayer.guess field
        
        if oponent.hit_target(me.shiplocations) is True:
            me.indicatehit(oponent.guess)
            humanships -= 1
            print(f"PC HIT User Battleship! {humanships=}")    

        else: 
            me.indicatemiss(oponent.guess)
            print("PC Missed!  Now User's turn!\n")
        
        clearscreen(3)
        users_turn = True