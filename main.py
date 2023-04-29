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

    blockSize = int(canvas.get_width()/10)

    cellList = []

    for xStart in range(0,canvas.get_width(), blockSize):
        for yStart in range(0, canvas.get_height(), blockSize):
            cellList.append(Cell(xStart, yStart, blockSize, False))

    while(not done):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                done = True
            elif pg.mouse.get_pressed()[0]:
                coords = pg.mouse.get_pos()
                xStart = coords[0]//blockSize * blockSize
                yStart = coords[1]//blockSize * blockSize

                #cellListIndex = [index for (index, cell) in enumerate(cellList) if (cell.xStart == xStart and cell.yStart = yStart)]
                for index, cell in enumerate(cellList):
                    if cell.xStart == xStart and cell.yStart == yStart:
                        cellList[index].isAlive = True
                        print(index)
                        break

                for pixelX in range(xStart, xStart+blockSize):
                    for pixelY in range(yStart, yStart+blockSize):
                        canvas.set_at((pixelX,pixelY), (0,0,0))

            pg.display.update()

    return cellList

def displayCells(canvas, cellList):
    print('Updating cells\n')
    for cell in cellList:
        if cell.isAlive:
            for pixelX in range(cell.xStart, cell.xStart+cell.size):
                for pixelY in range(cell.yStart, cell.yStart+cell.size):
                    canvas.set_at((pixelX, pixelY), (0, 0, 0))
    pg.display.update()


def main():
    canvas, clock, fps = setup()

    print('Starting simulation\n')

    done = False

    firstRun = True

    while(not done):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            else:
                #only initialize the cells after we first drew all the background shit
                if firstRun:
                    print('initializing background\n')
                    initializeBackground(canvas)
                    
                displayGrid(canvas)

                if firstRun:
                    print('initializing Cells')
                    cellList = initializeCells(canvas)

                displayCells(canvas, cellList)

                clock.tick(fps)

                firstRun = False
            
                

if __name__ == '__main__':
    main()
