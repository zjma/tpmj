from enum import Enum
from random import shuffle

class Game:
	@staticmethod
	def getPlayerCount(gameType):
		if gameType == 'tp':
			return 2
		raise Exception('NotImplemented')
		
	def __init__(self, gameType):
		if gameType != 'tp':
			raise Exception("Not implemented")
		playerCount = Game.getPlayerCount(gameType)
		self.playerCount = playerCount
		self._mountain = Mountain()
		self._river = River(playerCount)
		self._players = [Player() for _ in range(playerCount)]
		
		# Initialize hands
		for player in self._players:
			player.drawInitialHand(self._mountain)

	def performAction(self, role, action):
		raise Exception("Not implemented")
	
	def getStateForRole(self, role):
		pass
	
class Player:
	def __init__(self):
		self._hand = []
		self._builtSets = []
		self._draw = None
	
	def drawInitialHand(self, mountain):
		for _ in range(13):
			self._hand.append(mountain.pop())
	
	def draw(self, mountain):
		self._draw = mountain.pop()
	
	def discard(self, river, tile):
		assert self._draw != None
		if self._draw != tile:
			i = self._hand.index(tile)
			assert i >= 0
			self._draw, self._hand[i] = self._hand[i], self._draw
		
		river.push(self._draw)
		self._draw = None

class TileType(Enum):
	Man = 1
	Sou = 2
	Pin = 3
	East = 4
	South = 5
	West = 6
	North = 7
	White = 8
	Green = 9
	Red = 10
	
class Tile:
	def __init__(self, type, value, index):
		self.type = type
		self.value = value
		self.index = index
		
def _genall():
	ret = []
	for type in (TileType.Man, TileType.Sou, TileType.Pin):
		for val in range(1,10):
			for index in range(4):
				ret.append(Tile(type, val, index))
	
	honorTypes = [
		TileType.East,
		TileType.South,
		TileType.West,
		TileType.North,
		TileType.White,
		TileType.Green,
		TileType.Red,
	]
	
	for type in honorTypes:
		for index in range(4):
			ret.append(Tile(type, 1, index))
	return ret
	
AllTiles = _genall()

class Mountain:
	def __init__(self):
		self.tiles = list(AllTiles)
		shuffle(self.tiles)
		self.current = 0
	
	def pop(self):
		if self.current == len(self.tiles):
			raise Exception("Baaai")
		self.current += 1
		return self.tiles[self.current-1]

class River:
	def __init__(self, playerCount):
		self._tiles = [[] for _ in range(playerCount)]
	
	def push(self, tile):
		self._tiles.append(tile)

