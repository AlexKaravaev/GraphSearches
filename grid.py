import graphics as gs
WINH = 600
WINW = 600

class grid:

	def __init__(self,grid):
		self.grid = grid
		self.win = gs.GraphWin("win",WINH,WINW)
		
	
	def makeRect(self,corner, width, height):
	    '''Return a new Rectangle given one corner Point and the dimensions.'''
	    corner2 = corner
	    corner2.move(width, height)
	    return Rectangle(corner, corner2)

	def clear(self):
		for item in self.win.items[:] :
			item.undraw()
		self.win.update()

	def updategrid(self,new_grid):
		self.grid = new_grid

	def draw():
		self
