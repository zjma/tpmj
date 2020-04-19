from copy import deepcopy
from uuid import uuid4
from threading import Lock
from queue import deque
from game2 import GameState
import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Host:
	def __init__(self):
		self._waitingPlayersPerGameType = {}
		self._gidToGameStateMap = {}
		self._playerToGidAndRoleMap = {}
		self._waitingPlayers = []
		self._lock = Lock()

		# Have a game auto-craeted for various purpose.
		gid = uuid4().hex
		self._gidToGameStateMap[gid] = GameState('fakep0', 'fakep1')
		self._playerToGidAndRoleMap['fakep0'] = (gid,0)
		self._playerToGidAndRoleMap['fakep1'] = (gid,1)
	def handle(self, request):
		with self._lock:
			assert type(request)==dict
			action = request.get('Action', 'UnknownAction')
			actionHandlerName = action[:1].lower() + action[1:]
			ret = getattr(self, actionHandlerName)(request)
			return ret

	def requestMatch(self, request):
		playerName = request.get('PlayerName',None)
		if not playerName: return {'Accepted':False}
		if playerName in self._playerToGidAndRoleMap:
			gid,role = self._playerToGidAndRoleMap[playerName]
			return {
				'GameID': gid,
				'Role'	: role,
			}
		if playerName not in self._waitingPlayers:
			self._waitingPlayers.append(playerName)
		if len(self._waitingPlayers)>=2:
			gid = uuid4().hex
			random.shuffle(self._waitingPlayers)
			player0 = self._waitingPlayers[0]
			player1 = self._waitingPlayers[1]
			self._gidToGameStateMap[gid] = GameState(player0, player1)
			logger.info(f'New game: {self._waitingPlayers[0]} vs {self._waitingPlayers[1]}')
			self._playerToGidAndRoleMap[player0] = (gid,0)
			self._playerToGidAndRoleMap[player1] = (gid,1)
			self._waitingPlayers = self._waitingPlayers[2:]
		return {'Accepted':True}

	def getGameState(self, request):
		gid = request.get('GameID', None)
		role = request.get('RoleID', None)
		if gid not in self._gidToGameStateMap: return {'Accepted':False}
		gameState = self._gidToGameStateMap[gid]
		result = gameState.getStateView(role)
		if gameState.finished():
			for player in self._getPlayersByGameID(gid):
				del self._playerToGidAndRoleMap[player]
		return result

	def performGameAction(self, request):
		gameID = request.get('GameID', None)
		role = request.get('RoleID', None)
		payload = request.get('Payload',None)
		gameState = self._gidToGameStateMap.get(gameID, None)
		accepted = False if gameState==None else gameState.performAction(role,payload)
		ret = {
			'Accepted': accepted
		}
		if gameState.finished():
			for player in self._getPlayersByGameID(gameID):
				del self._playerToGidAndRoleMap[player]
		return ret

	def getGameList(self, request):
		return {
			'AllGames' : [{'GameID':gid,'Players':self._getPlayersByGameID(gid)} for gid in self._gidToGameStateMap.keys()],
		}

	def editGame(self, request):
		gameID = request.get('GameID', None)
		gameState = self._gidToGameStateMap.get(gameID, None)
		accepted = False if gameState==None else gameState.edit(request)
		return {'Accepted' : accepted}

	def unknownAction(self, request):
		return {'Processed':0}

	def _getPlayersByGameID(self, gameID):
		result = []
		for k,v in self._playerToGidAndRoleMap.items():
			if v[0]==gameID:
				result.append(k)
		return result
