from copy import deepcopy
from uuid import uuid4
from queue import deque
import game2
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Host:
	def __init__(self):
		self._waitingPlayersPerGameType = {}
		self._gidToGameStateMap = {}
		self._playerToGidAndRoleMap = {}
		pass

	def handle(self, request):
		assert type(request)==dict
		action = request.get('Action', 'UnknownAction')
		actionHandlerName = action[:1].lower() + action[1:]
		logger.info(actionHandlerName)
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
		playerCount = 2
		queue = self._waitingPlayersPerGameType[gameType]

		if (len(queue) < playerCount):
			return

		state = game2.newGameState()
		gid = uuid4().hex
		self._gidToGameStateMap[gid] = state

		for i in range(2):
			playerToken = queue.popleft()
			logging.debug(f"Adding {playerToken} into a new game.")
			self._playerToGidAndRoleMap[playerToken] = (gid, i)

	def checkWaitingStatus(self, request):
		playerToken = request.get('PlayerToken', None)
		ret = {
			'Matched' : playerToken in self._playerToGidAndRoleMap,
		}
		return ret

	def getGameState(self, request):
		playerToken = request.get('PlayerToken', None)
		if playerToken not in self._playerToGidAndRoleMap:
			return {}
		gid,role = self._playerToGidAndRoleMap[playerToken]
		gameState = self._gidToGameStateMap[gid]
		return game2.getGameStateView(gameState, role)

	def getGameState2(self, request):
		gid = request.get('GameID', None)
		role = request.get('RoleID', None)
		gameState = self._gidToGameStateMap.get(gid, None)
		return game2.getGameStateView2(gameState, role)
		
	def performGameAction(self, request):
		logger.debug(request)
		playerToken = request.get('PlayerToken', None)
		if playerToken not in self._playerToGidAndRoleMap:
			return {}
		gid,role = self._playerToGidAndRoleMap[playerToken]
		gameState = self._gidToGameStateMap[gid]
		payload = request.get('Payload',None)
		accepted,newState = game2.tryPerformAction(gameState,role,payload)
		ret = {
			'Accepted': accepted
		}
		self._gidToGameStateMap[gid] = newState
		return ret

	def getObservableGame(self, request):
		return {'GameID' : 'a1e9e3bf-8d2a-4602-ab6b-29b017d98d15'}

	def unknownAction(self, request):
		return {'Processed':0}
