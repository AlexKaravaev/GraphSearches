import math
import sys

#Heuristic function (Manhattan distance)
def h(cur_coord,goal_coord):
	return abs(cur_coord[0]-goal_coord[1]) + abs(cur_coord[1]-goal_coord[1]) 

#function that returns node with minimal f 
def minNodeFromSet(o_set,parent_set):
	minimal = 1000
	for node in o_set:
		g[node] = len(parent_set)
		h[node] = h(node)
		f[node] = h[node] + g[node]
		if(f[node] <= minimal):
			minimal = f[node]
			min_node = node
	return node

def getnearby(node):
	return ( (node[0]+1,node[1]) , (node[0]-1,node[1]) , (node[0],node[1]+1) , (node[0],node[1]-1) )

def inGrid(node,grid):
	return node[1] < len(grid) and node[1] >= 0 and node[0] < len(grid[0]) and node[0] >= 0 

#Main function
def search(grid,start,goal):
	U = []					#initializing closed set
	Q = []					#initializing open set	
	g = {}					#g will be dictionary with keys=node and values dist from start to this node
	f = {}					#same with g dict
	parent = {}				#our root dict.key = parent;value=child
	Q.append(start)
	g[start] = 0
	f[start] = g[start] + h(start,goal)
	while(len(Q) != 0):
		#current = minNodeFromSet(Q,parent)
		minimal = 1000
		for node in Q:
			g[node] = len(parent)
			f[node] = h(node,goal) + g[node]
			if(f[node] <= minimal):
				minimal = f[node]
				min_node = node
		current = min_node		
		if(current == goal):
			return parent
			

		Q.remove(current)
		U.append(current)
		nearby = getnearby(current)
		for node in nearby:
			if(inGrid(node,grid)):
				tent_score = g[current] + h(current,node)

				if( (node in U ) and tent_score >= g[node]):
					continue

				if( (node not in U) or tent_score < g[node]):
					parent[node] = current
					g[node] = tent_score
					f[node] = g[node] + h(node,goal)

					if(node not in Q):
						Q.append(node)

	return False

def main():
	grid = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]
	]
	path = search(grid,(0,0),(6,7))
	display_path(path,grid)


def display_path(path,grid):
	for i in range(0,len(grid)):
		for j in range(0,len(grid[0])):
			if((j,i) not in path):
				sys.stdout.write("0 ")
			else:
				sys.stdout.write("I ")
		sys.stdout.write("\n")

if __name__ == '__main__':
	main()


