from setup import *

'''

    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.

'''

def main(canvasWidth, canvasHeight, clock):
	canvas = pg.display.set_mode((canvasWidth, canvasHeight))

	background = pg.image.load("Assets/bg.png")

	while True:
		for event in pg.event.get():
			#Enter will exit the test
			if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
				pg.quit()
				done = True
			elif event.type == pg.QUIT:
				pg.quit()
				done = True


		canvas.blit(background, (0,0))
		clock.tick(60)
		pg.display.update()

if __name__ == '__main__':

	pg.init()

	canvasWidth, canvasHeight, clock = setup()

	main(canvasWidth, canvasHeight, clock)