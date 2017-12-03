import graphics as gs
import pygame as pg
import time
WINH = 600
WINW = 600

class grid:


	def __init__(self,grid,path,visited):
		pg.init()
		self.grid = grid
		self.screen = pg.display.set_mode((WINW,WINH))
		self.done = False
		self.path = path
		self.visited = visited
		self.screen.fill([255,255,255])
		n_rows = len(self.grid)
		n_cols = len(self.grid[0])
		while not self.done:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.done = True
			#self.drawGrid()
			sq_size = WINH/len(grid)
			for i in range(n_rows):
				for j in range(n_cols):
					if(grid[i][j]==0):
						pg.draw.rect(self.screen,(0,0,0),pg.Rect(i*sq_size,j*sq_size,sq_size,sq_size),1)
					else:
						pg.draw.rect(self.screen,(255,255,255),pg.Rect(i*sq_size,j*sq_size,sq_size,sq_size),1)
			for i in range(n_rows):
				for j in range(n_cols):

					
					if((j,i) in path):
						pg.draw.rect(self.screen,(255,0,0),pg.Rect(i*sq_size,j*sq_size,sq_size,sq_size),1)
					if((j,i) in visited):
						pg.draw.rect(self.screen,(0,0,255),pg.Rect(i*sq_size,j*sq_size,sq_size,sq_size),1)
				
					#time.sleep(0.00000005)
			pg.display.flip()			
					

        
			#pg.display.flip()

	def drawGrid(self):
		n_rows = len(self.grid)
		n_cols = len(self.grid[0])
		
		pg.draw.rect(self.screen,(0,128,255),pg.Rect(30,30,60,60))

def generateGrid(rows,cols):
	grid = []
	for i in range(0,rows):
		grid.append([])
		for j in range(0,cols):
			grid[i].append(0)

	return grid

# def main():
# 	gr = generateGrid(512,512)
# 	grid_ = grid(gr)
# 	#grid_.draw()

# if __name__ == '__main__':
# 	main()
