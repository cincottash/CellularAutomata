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

def drawCells(canvas, cellList):
    for x in range(len(cellList[0])):
        for y in range(len(cellList[1])):
            if cellList[x][y].state == 'Alive':
                color = (0, 0, 0)
            else:
                color = (255, 255 ,255)

            for x2 in range(cellList[x][y].size):
                for y2 in range(cellList[x][y].size):
                    canvas.set_at((cellList[x][y].x * cellList[x][y].size + x2, cellList[x][y].y * cellList[x][y].size + y2), color)

def update(cellList):

    tempCellList = cellList
    #Any live cell with two or three live neighbours survives.
    for x in range(len(cellList[0])):
        for y in range(len(cellList[1])):
            aliveNeighbors = 0
            if cellList[x][y].state == 'Alive':
                #LMFAO THERE HAS GOT TO BE A BETTER WAY TO DO THIS L0L I AM SO FUCKING STUPID
                try:
                    #Check West
                    if cellList[x-1][y].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                    pass

                try:
                    #check East
                    if cellList[x+1][y].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                    pass
                try:
                    #Check North
                    if cellList[x][y-1].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                    pass
                try:
                    #Check South
                    if cellList[x][y+1].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                    pass
                try:
                    #Check North West
                    if cellList[x-1][y-1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                    pass
                try:
                    #Check North East
                    if cellList[x+1][y-1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                    pass
                try:
                    #Check South West
                    if cellList[x-1][y+1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                    pass
                try:
                    #Check South East
                    if cellList[x+1][y+1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                    pass
                    
                if aliveNeighbors == 2 or aliveNeighbors == 3:
                    tempCellList[x][y].state = 'Alive'
                else:
                    tempCellList[x][y].state = 'Dead'
            
            #Any dead cell with 3 live neighbors becomes a dead cell 
            else:
                try:
                    #check all 8 neighbors state
                    #Check West
                    if cellList[x-1][y].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                        pass
                try:
                    #check East
                    if cellList[x+1][y].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                        pass
                try:
                    #Check North
                    if cellList[x][y-1].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                        pass
                try:
                    #Check South
                    if cellList[x][y+1].state == 'Alive':
                        aliveNeighbors += 1
                except IndexError:
                        pass
                try:
                    #Check North West
                    if cellList[x-1][y-1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                        pass
                try:
                    #Check North East
                    if cellList[x+1][y-1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                        pass
                try:
                    #Check South West
                    if cellList[x-1][y+1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                        pass
                try:
                    #Check South East
                    if cellList[x+1][y+1].state == 'Alive':
                        aliveNeighbors +=1
                except IndexError:
                        pass

                if aliveNeighbors == 3:
                    tempCellList[x][y].state = 'Alive'
                else:
                    tempCellList[x][y].state = 'Dead'

    cellList = tempCellList

    return tempCellList


def selectStartingSquares(canvas, cellList):
    done = False
    while(not done):
        drawCells(canvas, cellList)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                print('Clicked: {}\n'.format(pg.mouse.get_pos()))
                
                posx = pg.mouse.get_pos()[0]
                posy = pg.mouse.get_pos()[1]

                posx = int(posx/10)
                posy = int(posy/10)

                print(posx, posy)

                #Invert the state of the squares we click on
                if cellList[posx][posy].state == 'Alive':
                    cellList[posx][posy].state = 'Dead'
                else:
                    cellList[posx][posy].state = 'Alive'


            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True
    
    return cellList

def populateCanvas(canvas, background):

    #we're gunna make a 2d list where the positions of the cell objects (x, y) 
    #are the same as the indicies in the list 
    cellList = [[None for _ in range (100)] for _ in range(100)]


    #Initially make them all dead
    for x in range(100):
        for y in range(100):
            cellList[x][y] = Cell(x, y, 'Dead')

    return cellList


def main():
    canvas, background, clock, fps = setup()

    print('Populating canvas\n')

    cellList = populateCanvas(canvas, background)

    print('Finished populating canvas\n')

    print('Select starting squares by clicking, press enter to begin simulatio\n')

    cellList = selectStartingSquares(canvas, cellList)

    print('Starting simulation\n')

    done = False

    while(not done):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True
            elif event.type == pg.QUIT:
                done = True
            else:

                print('Blitting background\n')

                canvas.blit(background, (0,0))

                print('Drawing cells\n')

                drawCells(canvas, cellList)

                print('Updating cells\n')

                cellList = update(cellList)

                print('Displaying update\n')

                pg.display.update()
                
                clock.tick(fps)
                

if __name__ == '__main__':
    main()
