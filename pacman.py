############################################################
# This function just creates a 5 by 5 grid and returns it
############################################################
def createGrid():
    grid = [
        ['1','0','0','0','0'],
        ['0','0','0','0','0'],
        ['0','0','0','0','0'],
        ['0','0','0','0','0'],
        ['0','0','0','0','0']
    ]
    return grid
############################################################
# This function returns position of pacman
############################################################
def pacmanPosition(pacmanDirection, pacmanRow, pacmanColumn):
    print("Pacman is at (" + str(pacmanRow) + (",") + str(pacmanColumn) + ") direction is " + pacmanDirection + " !")
    
#####################################################################################
# This function checks if user entered a valid value in PLACE positon within 5x5 grid
#####################################################################################
def validatePlace(row, column):
    if row >= 0 and row < 5 and column >= 0 and column < 5:
       return True
    return False
#################################################################
# This function checks if user entered a valid direction in PLACE
#################################################################
def validateDirection(direction):
    if direction =="NORTH" or direction =="EAST" or direction =="SOUTH" or direction =="WEST":
         return True
    return False

#####################################################################
# This function to move of pacman on when user wants to. The function
# moves the pacman according to direction one step
#####################################################################
def move(direction, row, column):
    if direction == "NORTH" and ((column + 1) < 5) :
        column += 1
        return direction, row, column
    if direction == "SOUTH" and ( ( column - 1 ) >= 0 ):
        column -= 1
        return direction, row, column
    if direction == "WEST" and ( ( row - 1 ) >= 0 ):
        row -= 1
        return direction, row, column
    if direction == "EAST" and ( ( row + 1 ) < 5 ):
        row += 1
        return direction, row, column
#####################################################################
# This function to move of pacman to left
#####################################################################    
def left(direction):
    if direction == "NORTH":
        direction = "WEST"
        return direction
    if direction == "WEST":
        direction = "SOUTH"
        return direction
    if direction == "SOUTH":
        direction = "EAST"
        return direction
    if direction == "EAST":
        direction = "NORTH"
        return direction
#####################################################################
# This function to move of pacman to right
#####################################################################    
def right(direction):
    if direction == "NORTH":
        direction = "EAST"
        return direction
    if direction == "EAST":
        direction = "SOUTH"
        return direction
    if direction == "SOUTH":
        direction = "WEST"
        return direction
    if direction == "WEST":
        direction = "NORTH"
        return direction



if __name__ == '__main__':
    pacmanRow = 0
    pacmanColumn = 0
    pacmanDirection = "NORTH"

    row = 0
    column = 0
    direction = ""
    
    grid = createGrid()
    pacmanPosition(pacmanDirection, pacmanRow, pacmanColumn)

    while True:
     place = input("Enter PLACE : ")
     place = place.split()
     row = int(place[0])
     column = int(place[1])
     direction = str(place[2])
     if ((validatePlace(row, column)) & (validateDirection(direction.upper()))):
      break
     else:
         print("Invalid PLACE arguments")
         continue

    #This while loop will keep on taking input of MOVE, LEFT or RIGHT if REPORT is entered the loop terminates
    while True:
        operation = str(input())
        if operation == "MOVE":
            direction, row, column = move(direction, row, column)
            pacmanDirection, pacmanRow, pacmanColumn = direction, row, column
            continue
        if operation == "LEFT":
            direction = left(pacmanDirection)
            pacmanDirection = direction
            continue
        if operation == "RIGHT":
            pacmanDirection = right(pacmanDirection)
            continue
        if operation == "REPORT":
            break
        else:
            print("Invalid Input")
            continue
    pacmanPosition(pacmanDirection, pacmanRow, pacmanColumn)