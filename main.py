from setup import *
import random
from cell import *

'''

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.
'''

#make a grid over the background and display it to the screen
def displayGrid(canvas):
    for pixelX in range(canvas.get_width()):
        for pixelY in range(canvas.get_height()):
            if pixelX % (canvas.get_width()/10) == 0 or pixelY % (canvas.get_height()/10) == 0:
                canvas.set_at((pixelX, pixelY), (0,0,0))

    pg.display.update()

#sets all the pixels to white
def initializeBackground(canvas):
    for pixelX in range(canvas.get_width()):
        for pixelY in range(canvas.get_height()):
            canvas.set_at((pixelX, pixelY), (255,255,255))

def initializeCells(canvas):
    done = False

    #each cell is a square
    cellSize = int(canvas.get_width()/10)

    #list of cell objects which store the state (isAlive) as well as sizes and coordinate stuff
    cellList = []

    #add all the cells to the list starting as dead cells
    for xStart in range(0,canvas.get_width(), cellSize):
        for yStart in range(0, canvas.get_height(), cellSize):
            cellList.append(Cell(xStart, yStart, cellSize, False))

    while(not done):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True
            #if we clicked mouse button 1...
            elif pg.mouse.get_pressed()[0]:
                coords = pg.mouse.get_pos()

                #find the starting x and y coords of the cell we clicked on
                xStart = coords[0]//cellSize * cellSize
                yStart = coords[1]//cellSize * cellSize

                #check the above starting coords against the coords in our cell list to find the index of the corresponding cell in our cell list
                #set the status of the cell to alive
                #there can be only one cell in our list with those coords
                for index, cell in enumerate(cellList):
                    if cell.xStart == xStart and cell.yStart == yStart:
                        cellList[index].isAlive = True
                        print(index)
                        break

                #make that cell black
                for pixelX in range(xStart, xStart+cellSize):
                    for pixelY in range(yStart, yStart+cellSize):
                        canvas.set_at((pixelX,pixelY), (0,0,0))

            pg.display.update()

    return cellList

#draw cell to the screen according to it's size and state
def displayCells(canvas, cellList):
    print('Displaying cells\n')
    for cell in cellList:
        if cell.isAlive:
            for pixelX in range(cell.xStart, cell.xStart+cell.size):
                for pixelY in range(cell.yStart, cell.yStart+cell.size):
                    canvas.set_at((pixelX, pixelY), (0, 0, 0))
    pg.display.update()

#apply the rules of the game to the cells
def updateCells(canvas, cellList):

    print('Updating cells\n')

    return cellList

def main():
    canvas, clock, fps = setup()

    print('Starting simulation\n')

    done = False

    firstRun = True

    while(not done):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_q:
                done=True
            else:
                #set all the pixels to white on the first loop
                if firstRun:
                    print('initializing background\n')
                    initializeBackground(canvas)
                    
                #make a grid over the background and display it to the screen
                displayGrid(canvas)

                if firstRun:
                    print('initializing Cells')
                    #allow user to set the starting cells
                    cellList = initializeCells(canvas)

                #apply the rules of the game to the cells
                cellList = updateCells(canvas, cellList)

                #draw cells to the screen according to it's size and state
                displayCells(canvas, cellList)

                clock.tick(fps)

                firstRun = False
            
                

if __name__ == '__main__':
    main()
