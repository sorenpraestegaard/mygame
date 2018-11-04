class Level():
	def __init__(self, in_tile = 2):
		self.tiles = [[0 for i in range(0,5)] for j in range(0,5)]
		self.tiles[0][in_tile] = 1
		self.images = []
		self.images.append(pygame.image.load("grass.png").convert())

	def get_tile_image(x,y):
		return self.image[self.tiles[x][y]]