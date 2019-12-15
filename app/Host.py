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
	
	def UnknownAction(self, request):
		return {'Processed':0}