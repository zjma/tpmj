import random
from copy import deepcopy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def isValidRole(obj):
    return type(obj)==int and obj in (-1,0,1)

def isValidTile(obj):
    return type(obj)==int and obj>=0 and obj<136

def isValidTileView(obj):
    return type(obj)==dict and \
            type(obj.get('Covered', None))==bool and \
            (obj['Covered'] or isValidTile(obj.get('Tile',None)))

def isValidMountainView(obj):
    return type(obj)==list and \
            len(obj)==64 and \
            all((item==None or isValidTileView(item)) for item in obj)

def isValidHand(obj):
    return type(obj)==list and \
            all(isValidTileView(item) for item in obj)

def faceOf(tile):
    if not isValidTile(tile): raise ValueError(f'tile={tile}')
    if tile < 0 or tile > 136: assert False
    if tile < 36: return {'Type':'Character','Value':tile//4+1}
    if tile < 72: return {'Type':'Bamboo','Value':(tile-36)//4+1}
    if tile < 108: return {'Type':'Dot','Value':(tile-72)//4+1}
    if tile < 112: return {'Type':'East'}
    if tile < 116: return {'Type':'South'}
    if tile < 120: return {'Type':'West'}
    if tile < 124: return {'Type':'North'}
    if tile < 128: return {'Type':'White'}
    if tile < 132: return {'Type':'Green'}
    return {'Type':'Red'}

def isValidTripletInstance(obj):
    if type(obj)!='list': return False
    if len(obj)!=3: return False
    if not all(isValidTileView(tile) for tile in obj): return False
    faces = [faceOf(tile) for tile in obj]
    if faces[0]==faces[1] and faces[0]==faces[2]: return True
    return False

def isValidSequenceInstance(obj):
    if type(obj)!='list': return False
    if len(obj)!=3: return False
    if not all(isValidTileView(tile) for tile in obj): return False
    faces = [faceOf(tile) for tile in obj]
    if not all(face['Type'] in ('Character','Bamboo','Dot') for face in faces):
        return False
    sorted_faces = sorted(faces, key=lambda face:face['Value'])
    if sorted_faces[0]['Value']+1!=sorted_faces[1]['Value']: return False
    if sorted_faces[1]['Value']+1!=sorted_faces[2]['Value']: return False
    return True

def isValidBuiltSet(obj):
    if type(obj)!=dict: return False
    typ = obj.get('Type',None)
    val = obj.get('Value',None)
    if not isValidSetType(typ): return False
    if typ=='Triplet' and not isValidTripletInstance(val): return False
    if typ=='Sequence' and not isValidSequenceInstance(val): return False
    if typ=='Quad' and not isValidQuadInstance(val): return False
    return True

def isValidBuiltSetList(obj):
    return type(obj)==list and \
            all(isValidBuiltSet(item) for item in obj)
def isValidPlayerStateView(obj):
    return type(obj)==dict and \
            isValidHand(obj.get('OldHand', None)) and \
            isValidHand(obj.get('NewHand', None)) and \
            isValidBuiltSetList(obj.get('BuiltSets', None)) and \
            isValidDiscarded(obj.get('Discarded', None))

def isValidGameStateView(obj):
    return type(obj)==dict and \
            isValidRole(obj.get('Role',None)) and \
            isValidMountainView(obj.get('MountainView', None)) and \
            type(obj.get('PlayerStates',None))==list and \
            all(isValidPlayerStateView(v) for v in obj['PlayerStates']) and \
            isValidStateHint(obj.get('StateHint', None))


def remainingDrawCount(mountain):
    return len([x for x in mountain if x!=None])

def _draw(mountain):
    if remainingDrawCount(mountain)==0:
        raise Exception('Drawing from an empty mountain')
    sel = min([(idx,val) for idx,val in enumerate(mountain) if val!=None])
    new_mountain = deepcopy(mountain)
    new_mountain[sel[0]] = None
    draw = sel[1]
    return new_mountain,draw

def getGameStateView(gameState, role):
    if role in (0,1):
        return {
            'Role'          :   role,
            'MountainCount' :   remainingDrawCount(gameState['Mountain']),
            'MyState'       :   gameState['PlayerStates'][role],
            'StateHint'     :   gameState['StateHint'],
        }

    assert False

def getTileView(tid, isValueVisible):
    return {
        'IsValueVisible'    : isValueVisible,
        'Value'             : tid,
    }

def getPlayerIdBySeat(seat):
    '''
    Player 0 and player 1 sit face to face.
    '''
    if seat == 0: return 0
    if seat == 2: return 1
    return None

def getRiverView(gameState, seat):
    assert seat in range(4)
    pid = getPlayerIdBySeat(seat)
    if pid==None: return []
    return [getTileView(tid, True) for tid in gameState['Rivers'][pid]]

def getPlayerAreaView(gameState, seat, viewer):
    '''
    Viewer looking at stuff for a given seat. What does it look like?
    '''
    return {
        'River'     : [
            {
                'IsValueVisible'  : True,
                'Value'           : random.randint(0,135),
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 7,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 11,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 22,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 33,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 44,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 55,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 66,
            },
            {
                'IsValueVisible'  : True,
                'Value'           : 77,
            },
        ],
        'Mountain'  : [
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
            {'IsValueVisible' : False},
        ],
        'OldHand'   : [
            {'IsValueVisible' : True, 'Value' : 10},
            {'IsValueVisible' : True, 'Value' : 20},
            {'IsValueVisible' : True, 'Value' : 30},
            {'IsValueVisible' : True, 'Value' : 40},
            {'IsValueVisible' : True, 'Value' : 50},
            {'IsValueVisible' : True, 'Value' : 60},
            {'IsValueVisible' : True, 'Value' : 70},
            {'IsValueVisible' : True, 'Value' : 80},
            {'IsValueVisible' : True, 'Value' : 90},
            {'IsValueVisible' : True, 'Value' : 100},
            {'IsValueVisible' : True, 'Value' : 110},
            {'IsValueVisible' : True, 'Value' : 120},
            {'IsValueVisible' : True, 'Value' : 130},
        ],
        'NewHand'   : [
            {'IsValueVisible' : True, 'Value' : 47},
        ],
        'BuiltSets' : [
            {
                'TileViews' : [
                    {'IsValueVisible':True, 'Value':60, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':61,},
                    {'IsValueVisible':True, 'Value':62,},
                ],
            },
            {
                'TileViews' : [
                    {'IsValueVisible':True, 'Value':60,},
                    {'IsValueVisible':True, 'Value':61, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':62, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':63,},
                ],
            },
            {
                'TileViews' : [
                    {'IsValueVisible':True, 'Value':60,},
                    {'IsValueVisible':True, 'Value':61, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':62, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':63,},
                ],
            },
            {
                'TileViews' : [
                    {'IsValueVisible':True, 'Value':60,},
                    {'IsValueVisible':True, 'Value':61, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':62, 'Rotated':True},
                    {'IsValueVisible':True, 'Value':63,},
                ],
            },
        ],
    }

def getGameStateView2(gameState, role):
    return {
        'AreaViews' : [getPlayerAreaView(gameState, seat, role) for seat in range(4)],
    }

def getActionOptions(gameStateView):
    if gameStateView['StateHint']['Finished']: return []
    if gameStateView['Role']==0:
        if gameStateView['StateHint']['Type']=='P0ToHandleDraw':
            return [{'Type':'DiscardDraw'}]
        return []
    if gameStateView['Role']==1:
        if gameStateView['StateHint']['Type']=='P1ToHandleDraw':
            return [{'Type':'DiscardDraw'}]
        return []
    return []

def tryPerformAction(state, role, action):
    if state['StateHint']['Finished']: return False,state
    if state['StateHint']['Type']=='P0ToHandleDraw':
        if role!=0: return False,state
        if action['Type']=='DiscardDraw':
            newState = deepcopy(state)
            newState['PlayerStates'][0]['Draw'] = None
            if remainingDrawCount(newState['Mountain'])==0:
                newState['StateHint']={'Finished':True}
            else:
                newState['Mountain'],newState['PlayerStates'][1]['Draw'] = _draw(state['Mountain'])
                newState['StateHint']['Type']='P1ToHandleDraw'
            return True,newState
        return False,state
    if state['StateHint']['Type']=='P1ToHandleDraw':
        if role!=1: return False,state
        if action['Type']=='DiscardDraw':
            newState = deepcopy(state)
            newState['PlayerStates'][1]['Draw'] = None
            if remainingDrawCount(newState['Mountain'])==0:
                newState['StateHint']={'Finished':True}
            else:
                newState['Mountain'],newState['PlayerStates'][0]['Draw'] = _draw(state['Mountain'])
                newState['StateHint']['Type']='P0ToHandleDraw'
            return True,newState
        return False,state
    assert False

class Mountain:
    def __init__(self):
        tiles = list(range(36,72)) + list(range(108,136))
        random.shuffle(tiles)
        self._tiles = [
            [None]*6+tiles[:32],
            [None for _ in range(38)],
            [None]*6+tiles[32:],
            [None for _ in range(38)],
        ]
        i0 = random.randint(0,3)
        j0 = random.randint(0,37)
        self._forwardCursor = (i0,j0)
        self._backwordCursor = self._prevCursor(i0,j0)
    def _ensureForwardCursorValid(self):
        attemptCount=0
        while attemptCount<999:
            i,j = self._forwardCursor
            if self._tiles[i][j]!=None: break
            self._forwardCursor = self._nextCursor(i,j)
            attemptCount+=1
        return attemptCount<999
    def _ensureBackwardCursorValid(self):
        attemptCount=0
        while attemptCount<999:
            i,j = self._backwordCursor
            if self._tiles[i][j]!=None: break
            self._backwordCursor = self._prevCursor(i,j)
            attemptCount+=1
        return attemptCount<999
    def draw(self):
        if len(self)==0: return None
        assert self._ensureForwardCursorValid()
        i,j = self._forwardCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
        assert self._ensureForwardCursorValid()
        return result
    def drawFromBack(self):
        if len(self)==0: return None
        assert self._ensureBackwardCursorValid()
        i,j = self._backwordCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
        assert self._ensureBackwardCursorValid()
        return result
    def __len__(self):
        return len([x for x in (self._tiles[0]+self._tiles[2]) if x!=None])
    def getTilesBySeatID(self, seatID):
        return self._tiles[seatID]
    def _nextCursor(self, i, j):
        if j==37: return (i-1)%4,0
        return i,j+1
    def _prevCursor(self, i, j):
        if j==0: return (i+1)%4,37
        return i,j-1
class Set:
    def __init__(self, tiles):
        self._tiles = tiles
    def toSetView(self):
        return {
            'TileViews' : [{'IsValueVisible':True,'Value':tid} for tid in sorted(self._tiles)],
        }

class GameState:
    def __init__(self):
        self._river = [
            [],
            [],
            [],
            [],
        ]
        self._mountain = Mountain()
        self._oldHand = [[],[],[],[]]
        self._newHand = [[],[],[],[]]
        for i in range(13):
            self._oldHand[0].append(self._mountain.draw())
            self._oldHand[2].append(self._mountain.draw())
        self._oldHand[0].sort()
        self._oldHand[2].sort()
        self._newHand[0].append(self._mountain.draw())
        self._builtSets = [[],[],[],[]]
        self._state = {
            'Main'  : 'PlayerXHandleDraw',
            'X'     : 0,
        }
    def getStateView(self, role):
        return {
            'AreaViews' : [
                self._getAreaViewBySeatID(0),
                self._getAreaViewBySeatID(1),
                self._getAreaViewBySeatID(2),
                self._getAreaViewBySeatID(3),
            ],
            'State' : self._state,
        }
    def _getAreaViewBySeatID(self, seatID):
        return {
            'River'     : [{'IsValueVisible':True,'Value':tid} for tid in self._river[seatID]],
            'Mountain'  : [({'IsValueVisible':True,'Value':tid} if tid!=None else None) for tid in self._mountain.getTilesBySeatID(seatID)],
            'OldHand'   : [{'IsValueVisible':True,'Value':tid} for tid in self._oldHand[seatID]],
            'NewHand'   : [{'IsValueVisible':True,'Value':tid} for tid in self._newHand[seatID]],
            'BuiltSets' : [s.toSetView() for s in self._builtSets[seatID]],
        }
    def performAction(self, role, action):
        '''
        @return True if the action was accepted, or False otherwise.
        '''
        if self._state.get('Main',None) == 'PlayerXHandleDraw':
            if role==self._state.get('X',None):
                seatID = self._getSeatIDByRole(role)
                if action.get('Type',None)=='DiscardFromHand':
                    fromOldHand = action.get('FromOldHand', False)
                    idx = action.get('Index',999)
                    if idx>=0 and fromOldHand and idx<len(self._oldHand[seatID]) or not fromOldHand and idx<len(self._newHand[seatID]):
                        self._discardFromHandToRiver(seatID,fromOldHand,idx)
                        self._organizeHand(seatID)
                        if len(self._mountain)>=1:
                            nextRole = 1-role
                            self._drawTile(self._getSeatIDByRole(nextRole))
                            self._state['X'] = nextRole
                        else:
                            self._state = 'Finished'
                        return True
        return False
    def _discardFromHandToRiver(self, seatID, fromOldHand, idx):
        assert seatID in [0,1,2,3]
        if fromOldHand:
            assert idx in range(len(self._oldHand[seatID]))
            tid = self._oldHand[seatID][idx]
            self._oldHand[seatID] = self._oldHand[seatID][:idx]+self._oldHand[seatID][idx+1:]
        else:
            assert idx in range(len(self._newHand[seatID]))
            tid = self._newHand[seatID][idx]
            self._newHand[seatID] = self._newHand[seatID][:idx]+self._newHand[seatID][idx+1:]
        self._river[seatID].append(tid)

    def _organizeHand(self, seatID):
        assert seatID in [0,1,2,3]
        self._oldHand[seatID] = sorted(self._oldHand[seatID]+self._newHand[seatID])
        self._newHand[seatID] = []
    def _drawTile(self, seatID):
        assert seatID in [0,1,2,3]
        tid = self._mountain.draw()
        assert tid!=None
        self._newHand[seatID].append(tid)
    def _getSeatIDByRole(self, role):
        if role==0: return 0
        if role==1: return 2
        return None
