from copy import deepcopy
from uuid import uuid4

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Host:
	def __init__(self):
		pass
		
	def Handle(self, request):
		assert type(request)==dict
		action = request.get('Action', 'UnknownAction')
		ret = getattr(self, action)(request)
		return ret
	
	def NewParticipant(self, request):
		ret = {
			'ParticipantToken'	:	uuid4().hex,
		}
		
		return ret
	
	def CheckWaitingStatus(self, request):
		ret = {
			'Matched'	:	1,
			'GameId'	:	uuid4().hex,
		}
		return ret
	
	def GetGameState(self, request):
		token = request['ParticipantToken']
		game,role = self.participantToGameRole[token]
		return game.GetStateForRole(role)
	
	def PerformGameAction(self, request):
		token = request['ParticipantToken']
		game,role = self.participantToGameRole[token]
		action = request['GameAction']
		accepted = game.PerformAction(role, action)
		return {
			'Accepted': 1
		}
		
	def UnknownAction(self, request):
		return {'Processed':0}