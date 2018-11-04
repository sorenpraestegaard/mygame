import pygame

class Level():
	def __init__(self, in_tile = 2):
		self.tiles = [[0 for i in range(0,5)] for j in range(0,5)]
		self.tiles[0][in_tile] = 1
		self.images = []
		self.images.append(pygame.transform.scale(pygame.image.load("grass.png").convert(), (50,50)))
		self.images.append(pygame.transform.scale(pygame.image.load("trees.png").convert(), (50,50)))

	def get_tile_image(self,x,y):
		return self.images[self.tiles[x][y]]