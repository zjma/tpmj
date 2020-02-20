import logging
from pprint import pformat,pprint
import time
import json
import requests
import game2
import sys

class Client:
    def __init__(self, endpoint, username):
        self._endpoint = endpoint
        self._username = username

    def run(self):
        self._checkin()
        self._waitgamestart()
        self._play()

    def _checkin(self):
        name = self._username if self._username else input('Name?')
        params = {
            'Action'    :   'NewPlayer',
            'Credential':   name,
        }
        response = self._request(params)
        self._token = response.get('PlayerToken', None)
        assert type(self._token)==str

    def _waitgamestart(self):
        print('Waiting for opponents...')

        params = {
            'Action'        :   'CheckWaitingStatus',
            'PlayerToken'   :   self._token,
        }

        while True:
            response = self._request(params)
            if response.get('Matched', None) == True: break
            time.sleep(1.0)

        pprint('Opponent matched. Starting the game...')

    def _play(self):
        state_params = {
            'Action':'GetGameState',
            'PlayerToken':self._token,
        }

        while True:
            gameStateView = self._request(state_params)
            actions = game2.getActionOptions(gameStateView)
            if actions:
                action = self._chooseAction(gameStateView, actions)
                response = self._requestAction(action)
                assert response.get('Accepted', None)==True
            else:
                pprint(gameStateView)
                sys.stdout.flush()
                if gameStateView['StateHint']['Finished']: break
                time.sleep(1.0)

    def _request(self, params):
        response = requests.post(self._endpoint, json=params)
        ret = json.loads(response.text)
        logging.debug(ret)
        return ret

    def _chooseAction(self, gameStateView, actions):
        print(pformat(gameStateView))
        print(f'Choosing {actions[0]}...')
        sys.stdout.flush()
        # input('Continue?')
        return actions[0]

    def _requestAction(self, action):
        params = {
            'Action'        :   'PerformGameAction',
            'PlayerToken'   :   self._token,
            'Payload'       :   action,
        }
        return self._request(params)
