from copy import deepcopy
from uuid import uuid4
from queue import deque
from game import Game

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Host:
	def __init__(self):
		self._waitingPlayersPerGameType = {}
		self._activeGames = []
		self._playerToGameAndRoleMap = {}
		pass
		
	def handle(self, request):
		assert type(request)==dict
		action = request.get('Action', 'UnknownAction')
		actionHandlerName = action[:1].lower() + action[1:]
		ret = getattr(self, actionHandlerName)(request)
		return ret
	
	def newPlayer(self, request):
		newPlayerToken = uuid4().hex
		ret = {
			'PlayerToken'	:	newPlayerToken,
		}
		
		gameType = request.get('GameType', 'tp')
		# Only two players is supported. Change this once more types are
		# implemented.
		gameType = 'tp'
		self._waitingPlayersPerGameType.setdefault(gameType, deque()).append(
				newPlayerToken)
		self._tryCreateGame(gameType)
		
		return ret
	
	def _tryCreateGame(self, gameType):
		playerCount = Game.getPlayerCount(gameType)
		queue = self._waitingPlayersPerGameType[gameType]
		
		if (len(queue) < playerCount):
			return
			
		newGame = Game(gameType)
		self._activeGames.append(newGame)
		for i in range(newGame.playerCount):
			# TODO(zjma): make this a class.
			playerToken = queue.popleft()
			logging.debug(f"Adding {playerToken} into a new game.")
			self._playerToGameAndRoleMap[playerToken] = (newGame, i)
	
	def checkWaitingStatus(self, request):
		playerToken = request.get('PlayerToken', None)
		logger.debug(request)
		logger.debug(self._playerToGameAndRoleMap)
		ret = {
			'Matched' : playerToken in self._playerToGameAndRoleMap,
		}
		return ret
	
	def getGameState(self, request):
		playerToken = request.get('PlayerToken', None)
		if playerToken not in self._playerToGameAndRoleMap:
			return {}
		game,role = self._playerToGameAndRoleMap[playerToken]
		return transform(game.getStateForRole(role))
	
	def performGameAction(self, request):
		playerToken = request.get('PlayerToken', None)
		if playerToken not in self._playerToGameAndRoleMap:
			return {}
		game,role = self._playerToGameAndRoleMap[playerToken]
		action = request.get('GameAction', None)
		accepted = game.performAction(role, action)
		ret = {
			'Accepted': accepted
		}
		return ret
		
	def unknownAction(self, request):
		return {'Processed':0}