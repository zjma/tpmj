import random
from copy import deepcopy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def Check3X(tgids):
    if len(tgids)==0: return True
    if len(tgids)%3!=0: return False
    tgid = min(tgids)
    tgid0Count = len([None for x in tgids if x==tgid])
    if tgid in range(7) or tgid in range(9,16) or tgid in range(18,25):
        tgid1Count = len([None for x in tgids if x==tgid+1])
        tgid2Count = len([None for x in tgids if x==tgid+2])
        if tgid1Count>=1 and tgid2Count>=1:
            tmpTgids = list(tgids)
            tmpTgids.remove(tgid)
            tmpTgids.remove(tgid+1)
            tmpTgids.remove(tgid+2)
            if Check3X(tmpTgids): return True
    if tgid0Count>=3:
        tmpTgids = list(tgids)
        tmpTgids.remove(tgid)
        tmpTgids.remove(tgid)
        tmpTgids.remove(tgid)
        if Check3X(tmpTgids): return True
    return False

def Check3Xn2(tgids):
    if len(tgids)%3!=2: return False
    tg2c = [0 for _ in range(34)]
    for tgid in tgids: tg2c[tgid]+=1
    for tgid in range(34):
        if tg2c[tgid]>=2:
            tmpTgids = list(tgids)
            tmpTgids.remove(tgid)
            tmpTgids.remove(tgid)
            if Check3X(tmpTgids): return True
    return False

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
        if not self._ensureForwardCursorValid(): return None
        i,j = self._forwardCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
        return result
    def drawFromBack(self):
        if len(self)==0: return None
        if not self._ensureBackwardCursorValid(): return None
        i,j = self._backwordCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
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
                self._getAreaViewBySeatID(0,role),
                self._getAreaViewBySeatID(1,role),
                self._getAreaViewBySeatID(2,role),
                self._getAreaViewBySeatID(3,role),
            ],
            'State' : self._state,
        }

    def _getMountainViewBySeatID(self, seatID, role):
        if role==-1 or self._state['Main'] in ('PlayerXWon','Finished'):
            return [({'IsValueVisible':True,'Value':tid} if tid!=None else None) for tid in self._mountain.getTilesBySeatID(seatID)]
        return [({'IsValueVisible':False} if tid!=None else None) for tid in self._mountain.getTilesBySeatID(seatID)]

    def _getOldHandView(self, seatID, role):
        if role==-1 or seatID==self._getSeatIDByRole(role) or self._state['Main'] in ('PlayerXWon','Finished'):
            return [{'IsValueVisible':True,'Value':tid} for tid in self._oldHand[seatID]]
        return [{'IsValueVisible':False} for tid in self._oldHand[seatID]]

    def _getNewHandView(self, seatID, role):
        if role==-1 or seatID==self._getSeatIDByRole(role) or self._state['Main'] in ('PlayerXWon','Finished'):
            return [{'IsValueVisible':True,'Value':tid} for tid in self._newHand[seatID]]
        return [{'IsValueVisible':False} for tid in self._newHand[seatID]]

    def _getAreaViewBySeatID(self, seatID, role):
        '''
        Get what it looks like at seatID area from role's view.
        '''
        return {
            'River'     : [{'IsValueVisible':True,'Value':tid} for tid in self._river[seatID]],
            'Mountain'  : self._getMountainViewBySeatID(seatID, role),
            'OldHand'   : self._getOldHandView(seatID, role),
            'NewHand'   : self._getNewHandView(seatID, role),
            'BuiltSets' : [s.toSetView() for s in self._builtSets[seatID]],
        }
    def performAction(self, role, action):
        '''
        @return True if the action was accepted, or False otherwise.
        '''
        logger.info(f'OldState={self._state}')
        mainState = self._state.get('Main',None)
        try:
            if action==None: return False
            if mainState == 'PlayerXHandleDraw':
                if role==self._state.get('X',None):
                    seatID = self._getSeatIDByRole(role)
                    actionType = action.get('Type',None)
                    if actionType=='DiscardFromHand':
                        fromOldHand = action.get('FromOldHand', False)
                        idx = action.get('Index',999)
                        if idx>=0 and fromOldHand and idx<len(self._oldHand[seatID]) or not fromOldHand and idx<len(self._newHand[seatID]):
                            self._discardFromHandToRiver(seatID,fromOldHand,idx)
                            self._organizeHand(seatID)
                            self._state = {'Main':'PlayerXToRespondToDiscard','X':1-role}
                            return True
                    if actionType=='Win':
                        tgids = [tid//4 for tid in (self._oldHand[seatID] + self._newHand[seatID])]
                        if not Check3Xn2(tgids): return False
                        self._state = {'Main':'PlayerXWon','X':role}
                        return True

            elif mainState == 'PlayerXToRespondToDiscard':
                if role==self._state.get('X',None):
                    seatID = self._getSeatIDByRole(role)
                    oppoRole = 1-role
                    oppoSeatID = self._getSeatIDByRole(oppoRole)
                    actionType = action.get('Type',None)
                    if actionType=='Pass':
                        if len(self._mountain)>=1:
                            self._drawTile(self._getSeatIDByRole(role))
                            self._state = {'Main':'PlayerXHandleDraw','X':role}
                        else:
                            self._state = {'Main':'Finished'}
                        return True
                    elif actionType=='Pon':
                        if len(self._oldHand[seatID])<2: return False
                        if len(self._river[oppoSeatID])<1: return False
                        if len(self._builtSets[seatID])>=4: return False
                        tid0 = self._river[oppoSeatID][-1]
                        tgid = tid0 // 4
                        candidates = [tile for tile in self._oldHand[seatID] if tile//4==tgid]
                        if len(candidates)<2: return False
                        tid1 = candidates[0]
                        tid2 = candidates[1]
                        self._buildSet(seatID,[tid0,tid1,tid2])
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                        return True
                    elif actionType=='Chi':
                        chiMode = action.get('ChiMode', None)
                        if len(self._oldHand[seatID])<2: return False
                        if len(self._river[oppoSeatID])<1: return False
                        if len(self._builtSets[seatID])>=4: return False
                        tid0 = self._river[oppoSeatID][-1]
                        tgid = tid0 // 4
                        if chiMode=='_YZ':
                            if tgid in range(0,7) or tgid in range(9,16) or tgid in range(18,25):
                                tiles_1 = [tid for tid in self._oldHand[seatID] if tid//4==tgid+1]
                                tiles_2 = [tid for tid in self._oldHand[seatID] if tid//4==tgid+2]
                                if len(tiles_1)==0 or len(tiles_2)==0: return False
                                self._buildSet(seatID,[tid0,tiles_1[0],tiles_2[0]])
                                self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                                return True
                            else:
                                return False
                        elif chiMode=='X_Z':
                            if tgid in range(1,8) or tgid in range(10,17) or tgid in range(19,26):
                                tilesm1 = [tid for tid in self._oldHand[seatID] if tid//4==tgid-1]
                                tilesp1 = [tid for tid in self._oldHand[seatID] if tid//4==tgid+1]
                                if len(tilesm1)==0 or len(tilesp1)==0: return False
                                self._buildSet(seatID,[tilesm1[0],tid0,tilesp1[0]])
                                self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                                return True
                            else:
                                return False
                        elif chiMode=='XY_':
                            if tgid in range(2,9) or tgid in range(11,18) or tgid in range(20,27):
                                tilesm1 = [tid for tid in self._oldHand[seatID] if tid//4==tgid-1]
                                tilesm2 = [tid for tid in self._oldHand[seatID] if tid//4==tgid-2]
                                if len(tilesm1)==0 or len(tilesm2)==0: return False
                                self._buildSet(seatID,[tilesm2[0],tilesm1[0],tid0])
                                self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif actionType=='Win':
                        if len(self._river[oppoSeatID])==0: return False
                        tgids = [tid//4 for tid in (self._oldHand[seatID] + [self._river[oppoSeatID][-1]])]
                        if not Check3Xn2(tgids): return False
                        self._state = {'Main':'PlayerXWon','X':role}
                        return True
            return False
        finally:
            logger.info(f'NewState={self._state}')
    def _buildSet(self, builderSeatID, tiles):
        for tile in tiles:
            self._removeTile(tile)
        self._builtSets[builderSeatID].append(Set(tiles))
    def _removeTile(self, tid):
        '''
        Remove a given tile from whatever hand/river it is in currently.
        '''
        for seatID in range(4):
            self._removeIfExist(self._oldHand[seatID],tid)
            self._removeIfExist(self._newHand[seatID],tid)
            self._removeIfExist(self._river[seatID],tid)
    def _removeIfExist(self, lst, val):
        if val in lst: lst.remove(val)
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
    def finished(self):
        return self._state['Main'] in ('PlayerXWon','Finished')
